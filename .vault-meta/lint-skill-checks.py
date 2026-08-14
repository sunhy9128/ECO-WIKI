#!/usr/bin/env python3
"""wiki-lint skill checks (v2026-08-14) on top of lint-stats.json.

Implements checks 3a/4/5/6/7/8/9/10/11/12/13 from the wiki-lint skill,
adapted to this vault's frontmatter schema (type/status/address + optional
summary/provenance/relationships/lifecycle/base_confidence).
"""
import json, re, sys
from collections import defaultdict, Counter
from datetime import date, datetime
from pathlib import Path

ROOT = Path("/Users/mac/Documents/金融WIKI")
TODAY = date(2026, 8, 14)

stats = json.loads((ROOT / ".vault-meta" / "lint-stats.json").read_text(encoding="utf-8"))
records = stats["records"]
all_links = stats["all_links"]          # (src, tgt)
inbound = stats["inbound"]              # tgt -> [srcs]
name_to_paths = stats["name_to_paths"]  # key -> [paths]

ALLOWED_REL_TYPES = {"extends", "implements", "contradicts", "derived_from", "uses", "replaces", "related_to"}
ALLOWED_LIFECYCLE = {"draft", "reviewed", "verified", "disputed", "archived"}

ORPHAN_EXCLUDE_FILES = {"_index.md", "index.md", "log.md", "hot.md", "overview.md",
                        "dashboard.md", "dashboard.base", "Wiki Map.md", "getting-started.md"}
SKIP_PREFIXES = ("meta/", "_meta/", "journal/", "folds/", "_raw/", "_archives/", "_staging/", "_readouts/")

def is_excluded(rec):
    if rec["in_folds"]:
        return True
    if Path(rec["path"]).name in ORPHAN_EXCLUDE_FILES:
        return True
    if rec["path"].startswith(SKIP_PREFIXES):
        return True
    return False

def is_reserved(rec):
    return rec["path"].startswith(("_meta/", "_raw/", "_archives/", "_staging/", "_readouts/", "folds/")) \
        or Path(rec["path"]).name in ORPHAN_EXCLUDE_FILES

def read_text(path):
    try:
        return (ROOT / path).read_text(encoding="utf-8")
    except Exception:
        return ""

def parse_fm(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    return m.group(1) if m else ""

def resolve(tgt):
    return name_to_paths.get(tgt) or name_to_paths.get(tgt.lower()) or []

# ---- per-page resolved-link set (for tag cohesion + synthesis) ----
page_links = {}   # path -> set of resolved page paths
for rec in records:
    s = set()
    for l in rec["links"]:
        for p in resolve(l):
            s.add(p)
    page_links[rec["path"]] = s

# incoming count per page
incoming_count = defaultdict(int)
for tgt in inbound:
    for p in resolve(tgt):
        incoming_count[p] += 1

def fmt(path):
    return f"`{path}`"

# =====================================================================
# 3a. Missing / overlong summary (soft)
# =====================================================================
missing_summary, long_summary = [], []
for rec in records:
    if is_excluded(rec):
        continue
    text = read_text(rec["path"])
    m = re.search(r"^summary:\s*(.*)$", parse_fm(text), re.M)
    if not m:
        missing_summary.append(rec["path"])
        continue
    val = m.group(1).strip().strip('"').strip("'")
    if len(val) > 200:
        long_summary.append((rec["path"], len(val)))

# =====================================================================
# 4. Stale pages (updated older than 90 days) + verified-stale overlay
# =====================================================================
stale, stale_verified = [], []
for rec in records:
    if is_excluded(rec) or not rec["updated"]:
        continue
    try:
        upd = datetime.strptime(rec["updated"][:10], "%Y-%m-%d").date()
    except ValueError:
        continue
    age = (TODAY - upd).days
    if age > 90:
        entry = (rec["path"], rec["updated"], age)
        if rec["status"] == "verified":
            stale_verified.append(entry)
        else:
            stale.append(entry)

# =====================================================================
# 5. Contradictions (relationships: contradicts + callout presence)
# =====================================================================
contradiction_pairs = []
for rec in records:
    text = read_text(rec["path"])
    fm = parse_fm(text)
    if "contradicts" not in fm:
        continue
    for m in re.finditer(r"type:\s*contradicts", fm):
        # find nearest preceding target
        pre = fm[:m.start()]
        tm = list(re.finditer(r"target:\s*\"\[\[([^\]]+)\]\]\"", pre))
        if tm:
            contradiction_pairs.append((rec["path"], tm[-1].group(1)))

# =====================================================================
# 6. Index consistency
# =====================================================================
index_text = read_text("index.md")
index_links = re.findall(r"\[\[([^\]\|#^]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]", index_text)
index_broken = [(l, len(resolve(l)) == 0) for l in index_links]
index_broken = [l for l, bad in index_broken if bad]
idx_count_m = re.search(r"Total pages:\s*(\d+)", index_text)
index_declared = int(idx_count_m.group(1)) if idx_count_m else None
content_pages = [r["path"] for r in records if not is_reserved(r)]
indexed = set()
for l in index_links:
    for p in resolve(l):
        indexed.add(p)
index_missing_pages = [p for p in content_pages if p not in indexed]

# =====================================================================
# 7. Provenance drift
# =====================================================================
prov_issues = []
MARKER_RE = re.compile(r"\^\[(inferred|ambiguous)\]")
for rec in records:
    text = read_text(rec["path"])
    fm = parse_fm(text)
    if "provenance:" not in fm:
        continue
    # extract frontmatter provenance block
    pm = re.search(r"provenance:\s*\n((?:\s+[a-z_]+:\s*[\d.]+[^\n]*\n?)+)", fm)
    if not pm:
        prov_issues.append((rec["path"], "malformed provenance block"))
        continue
    stored = {}
    for k, v in re.findall(r"\s+([a-z_]+):\s*([\d.]+)", pm.group(1)):
        stored[k] = float(v)
    body = text.split("---", 2)[-1] if text.startswith("---") else text
    # count claim-bearing lines (bullets, numbered, or non-empty lines in body sections)
    lines = [ln.strip() for ln in body.splitlines() if ln.strip() and not ln.strip().startswith(("#", ">", "```", "---", "|", "*", "!"))]
    markers = MARKER_RE.findall(body)
    n_inf = markers.count("inferred")
    n_amb = markers.count("ambiguous")
    n_total = len(lines) + n_inf + n_amb  # markers add one annotated line each
    if n_total == 0:
        continue
    recomputed = {"extracted": (n_total - n_inf - n_amb) / n_total,
                  "inferred": n_inf / n_total,
                  "ambiguous": n_amb / n_total}
    for k in ("extracted", "inferred", "ambiguous"):
        if k in stored and abs(stored[k] - recomputed.get(k, 0)) > 0.20:
            prov_issues.append((rec["path"], f"drift: frontmatter {k}={stored[k]:.2f}, recomputed={recomputed.get(k,0):.2f}"))
    if recomputed["ambiguous"] > 0.15:
        prov_issues.append((rec["path"], f"AMBIGUOUS {recomputed['ambiguous']*100:.0f}% > 15% (speculation-heavy)"))
    if recomputed["inferred"] > 0.40 and not re.search(r"^sources:", fm, re.M):
        prov_issues.append((rec["path"], f"unsourced synthesis: inferred {recomputed['inferred']*100:.0f}% with no sources:"))

# hub pages = top 10 by incoming link count
hubs = sorted(incoming_count.items(), key=lambda x: -x[1])[:10]
for path, n in hubs:
    if path in page_links and not is_reserved(next((r for r in records if r["path"] == path), None)):
        text = read_text(path)
        body = text.split("---", 2)[-1] if text.startswith("---") else text
        lines = [ln.strip() for ln in body.splitlines() if ln.strip() and not ln.strip().startswith(("#", ">", "```", "---", "|", "*", "!"))]
        markers = MARKER_RE.findall(body)
        if not lines:
            continue
        inf = markers.count("inferred") / (len(lines) + len(markers))
        if inf > 0.20:
            prov_issues.append((path, f"hub page ({n} incoming links) with inferred={inf*100:.0f}% > 20%"))

# =====================================================================
# 8. Fragmented tag clusters
# =====================================================================
tag_pages = defaultdict(list)
for rec in records:
    if is_excluded(rec):
        continue
    for t in rec["tags"]:
        tag_pages[t].append(rec["path"])

fragmented = []
for tag, pages in tag_pages.items():
    n = len(pages)
    if n < 5:
        continue
    pset = set(pages)
    pairs = 0
    linked = 0
    for i in range(n):
        for j in range(i + 1, n):
            pairs += 1
            if pages[j] in page_links.get(pages[i], set()) or pages[i] in page_links.get(pages[j], set()):
                linked += 1
    cohesion = linked / pairs if pairs else 1.0
    if cohesion < 0.15:
        fragmented.append((tag, n, cohesion))

# =====================================================================
# 9. Visibility
# =====================================================================
PII_RE = re.compile(r"(password|passwd|api[_-]?key|secret|ssn|client[_-]?secret)\s*[:：=]\s*\S+|"
                    r"\bemail\s*[:：]\s*\S+@\S+|"
                    r"\bphone\s*[:：]\s*[+\d][\d\s\-()]{6,}", re.I)
visibility_issues = []
for rec in records:
    if is_excluded(rec):
        continue
    tags = rec["tags"]
    has_vis = any(str(t).startswith("visibility/") for t in tags)
    text = read_text(rec["path"])
    body = text.split("---", 2)[-1] if text.startswith("---") else text
    if PII_RE.search(body) and not has_vis:
        visibility_issues.append((rec["path"], "contains credential/PII value pattern but no visibility/ tag"))
    if any(str(t) == "visibility/pii" for t in tags) and not re.search(r"^sources:", parse_fm(text), re.M):
        visibility_issues.append((rec["path"], "tagged visibility/pii but missing sources:"))

tax_path = ROOT / "_meta" / "taxonomy.md"
tax_contam = []
if tax_path.exists():
    for line in tax_path.read_text(encoding="utf-8").splitlines():
        if re.search(r"visibility/", line):
            tax_contam.append(line.strip())

# =====================================================================
# 10. Misc promotion candidates
# =====================================================================
misc_pages = [r for r in records if r["path"].startswith("misc/")]
promo_candidates = []
for rec in misc_pages:
    text = read_text(rec["path"])
    fm = parse_fm(text)
    am = re.search(r"affinity:\s*\n((?:\s+[^:\n]+:\s*\d+[^\n]*\n?)+)", fm)
    if am:
        for k, v in re.findall(r"\s+([^:\n]+):\s*(\d+)", am.group(1)):
            if int(v) >= 3:
                promo_candidates.append((rec["path"], k, int(v)))

# =====================================================================
# 11. Synthesis gaps (top co-occurring concept pairs, no synthesis page)
# =====================================================================
concept_pages = [r["path"] for r in records if r["path"].startswith(("concepts/", "entities/"))]
link_freq = Counter()
for path in concept_pages:
    for t in page_links.get(path, set()):
        link_freq[t] += 1
top_concepts = [p for p, _ in link_freq.most_common(40)]
top_concepts = [p for p in top_concepts if p.startswith(("concepts/", "entities/"))][:30]

synthesis_pages = [r["path"] for r in records if r["path"].startswith("synthesis/")]
synthesis_covered = set()
for sp in synthesis_pages:
    stem = Path(sp).stem
    for part in re.split(r"[×xX✕*]", stem):
        part = part.strip()
        if part:
            for p in top_concepts:
                if Path(p).stem == part or part in Path(p).stem or Path(p).stem in part:
                    synthesis_covered.add(tuple(sorted([Path(p).stem, part])))
                    synthesis_covered.add(p)

gaps = []
plist = top_concepts
for i in range(len(plist)):
    for j in range(i + 1, len(plist)):
        a, b = plist[i], plist[j]
        sa, sb = set(page_links.get(a, set())), set(page_links.get(b, set()))
        co = len(sa & sb)
        if co < 3:
            continue
        a_stem, b_stem = Path(a).stem, Path(b).stem
        key = tuple(sorted([a_stem, b_stem]))
        if key in synthesis_covered:
            continue
        gaps.append((a_stem, b_stem, co))
gaps.sort(key=lambda x: -x[2])

# =====================================================================
# 12. Lifecycle / confidence schema
# =====================================================================
no_lifecycle, bad_lifecycle, bad_confidence = [], [], []
stale_pages_rule12 = []
supersession_issues = []
for rec in records:
    if is_reserved(rec):
        continue
    text = read_text(rec["path"])
    fm = parse_fm(text)
    lc = re.search(r"^lifecycle:\s*(\S+)", fm, re.M)
    bc = re.search(r"^base_confidence:\s*(\S+)", fm, re.M)
    if not lc:
        no_lifecycle.append(rec["path"])
    elif lc.group(1).strip('"').strip("'") not in ALLOWED_LIFECYCLE:
        bad_lifecycle.append((rec["path"], lc.group(1)))
    if bc:
        try:
            v = float(bc.group(1))
            if not (0.0 <= v <= 1.0):
                bad_confidence.append((rec["path"], bc.group(1)))
        except ValueError:
            bad_confidence.append((rec["path"], bc.group(1)))
    upd = rec["updated"]
    if upd:
        try:
            d = datetime.strptime(upd[:10], "%Y-%m-%d").date()
            if (TODAY - d).days > 90:
                stale_pages_rule12.append((rec["path"], rec["updated"], (TODAY - d).days, rec["status"]))
        except ValueError:
            pass
    sb = re.search(r"^superseded_by:\s*\"?\[\[([^\]]+)\]\]\"?", fm, re.M)
    if sb:
        tgt = sb.group(1)
        resolved = resolve(tgt)
        if not resolved:
            supersession_issues.append((rec["path"], f"superseded_by target [[{tgt}]] does not exist"))
        else:
            for tp in resolved:
                ttext = read_text(tp)
                tlc = re.search(r"^lifecycle:\s*(\S+)", parse_fm(ttext), re.M)
                if tlc and tlc.group(1) == "archived":
                    supersession_issues.append((rec["path"], f"superseded_by chain: target {tp} is itself archived"))
        if lc and lc.group(1).strip('"').strip("'") != "archived":
            supersession_issues.append((rec["path"], f"superseded_by set but lifecycle={lc.group(1)} (expected archived)"))

# =====================================================================
# 13. Typed relationships validity
# =====================================================================
rel_issues = []
rel_type_counts = Counter()
n_pages_with_rel = 0
for rec in records:
    text = read_text(rec["path"])
    fm = parse_fm(text)
    if "relationships:" not in fm:
        continue
    n_pages_with_rel += 1
    self_id = Path(rec["path"]).stem
    # split per entry block: "- target: ..." followed by "type: ..." (order varies)
    entries = []
    for em in re.finditer(r"-\s*target:\s*[\"']?\[\[([^\]\"']+)\]\]", fm):
        entry_text = fm[em.start():fm.find("\n- ", em.start()) if fm.find("\n- ", em.start()) != -1 else len(fm)]
        tm = re.search(r"target:\s*[\"']?\[\[([^\]\"']+)\]\]", entry_text)
        tym = re.search(r"type:\s*([^\s#]+)", entry_text)
        if tm and tym:
            entries.append((tm.group(1).strip(), tym.group(1).strip().strip('"').strip("'")))
    for idx, (tgt, typ) in enumerate(entries):
        rel_type_counts[typ] += 1
        if typ not in ALLOWED_REL_TYPES:
            rel_issues.append((rec["path"], f"relationships[{idx}]: type \"{typ}\" not allowed"))
        resolved = resolve(tgt)
        if not resolved:
            rel_issues.append((rec["path"], f"relationships[{idx}]: target [[{tgt}]] resolves to no page"))
        else:
            for tp in resolved:
                if Path(tp).stem == self_id:
                    rel_issues.append((rec["path"], f"relationships[{idx}]: self-reference (target resolves to own id)"))

# =====================================================================
# Output
# =====================================================================
def dump(name, items, limit=30, fmt_fn=str):
    print(f"\n=== {name} ({len(items)} found) ===")
    for it in items[:limit]:
        print("  " + fmt_fn(it))
    if len(items) > limit:
        print(f"  ... and {len(items)-limit} more")

print(f"TODAY={TODAY}")
print(f"content pages (non-reserved)={len(content_pages)}")
dump("MISSING SUMMARY (soft)", missing_summary)
dump("OVERLONG SUMMARY (>200 chars)", long_summary, fmt_fn=lambda t: f"{t[0]} ({t[1]} chars)")
dump("STALE (>90d, non-verified)", stale, 15, lambda t: f"{t[0]} (updated {t[1]}, {t[2]}d)")
dump("STALE VERIFIED (HIGH PRIORITY)", stale_verified, 15, lambda t: f"{t[0]} (updated {t[1]}, {t[2]}d) status=verified")
dump("CONTRADICTION RELATIONSHIPS", contradiction_pairs, 15, lambda t: f"{t[0]} contradicts [[{t[1]}]]")
print(f"\n=== INDEX CONSISTENCY ===")
print(f"  index.md declares Total pages: {index_declared}; disk content pages: {len(content_pages)}")
print(f"  index links that don't resolve: {len(index_broken)} -> {index_broken[:15]}")
print(f"  content pages NOT in index.md: {len(index_missing_pages)}")
dump("PROVENANCE ISSUES", prov_issues, 20)
dump("FRAGMENTED TAG CLUSTERS", fragmented, 15, lambda t: f"#{t[0]} — {t[1]} pages, cohesion={t[2]:.2f}")
dump("VISIBILITY ISSUES", visibility_issues, 15, lambda t: f"{t[0]} — {t[1]}")
print(f"\n=== TAXONOMY CONTAMINATION === {len(tax_contam)} found")
for l in tax_contam:
    print("  " + l)
print(f"\n=== MISC PROMOTION CANDIDATES === {len(promo_candidates)} found (misc pages: {len(misc_pages)})")
for p, k, v in promo_candidates:
    print(f"  {p} — {k}: {v}")
dump("SYNTHESIS GAPS (top)", gaps, 12, lambda t: f"[[{t[0]}]] x [[{t[1]}]] — {t[2]} pages")
print(f"\n=== LIFECYCLE / CONFIDENCE ===")
print(f"  pages without lifecycle (non-reserved): {len(no_lifecycle)}")
dump("  bad lifecycle values", bad_lifecycle, 10, lambda t: f"{t[0]}: lifecycle={t[1]}")
dump("  bad base_confidence", bad_confidence, 10, lambda t: f"{t[0]}: {t[1]}")
dump("  supersession issues", supersession_issues, 10, lambda t: f"{t[0]} — {t[1]}")
print(f"  stale per rule 12c (updated>90d, non-reserved): {len(stale_pages_rule12)}")
verified_stale12 = [s for s in stale_pages_rule12 if s[3] == "verified"]
print(f"    of which status=verified: {len(verified_stale12)}")
for s in verified_stale12[:10]:
    print(f"      {s[0]} (updated {s[1]}, {s[2]}d)")
print(f"\n=== TYPED RELATIONSHIPS ===")
print(f"  pages with relationships: {n_pages_with_rel}")
print(f"  type histogram: {dict(rel_type_counts)}")
dump("  relationship issues", rel_issues, 20)
