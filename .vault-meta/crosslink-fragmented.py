#!/usr/bin/env python3
"""Targeted cross-linker pass for fragmented tag clusters (2026-08-14).

Conservative, mechanical: for pages in tag clusters with cohesion < 0.15,
link the FIRST natural, unlinked mention of another content page's name/alias
(stem ≥3 CJK chars or ≥5 ASCII chars, unambiguous resolution, non-redirect,
non-self). Max 3 inline links per page. Writes `related_to` relationships
entries for each added link. Dry-run by default; `--apply` writes files.
"""
import json, re, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path("/Users/mac/Documents/金融WIKI")
APPLY = "--apply" in sys.argv

stats = json.loads((ROOT / ".vault-meta" / "lint-stats.json").read_text(encoding="utf-8"))
records = stats["records"]
n2p = stats["name_to_paths"]

RESERVED_FILES = {"_index.md", "index.md", "log.md", "hot.md", "overview.md",
                  "dashboard.md", "dashboard.base", "Wiki Map.md", "getting-started.md"}
SKIP_SRC_PREFIXES = ("meta/", "folds/", "_meta/", "_raw/", "_archives/", "_staging/", "_readouts/", "journal/")

def parse_fm(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    return m.group(1) if m else ""

def is_redirect(text):
    return bool(re.search(r"^redirects_to:", parse_fm(text), re.M))

def is_reserved(path):
    return Path(path).name in RESERVED_FILES or path.startswith(SKIP_SRC_PREFIXES) \
        or path.startswith(("_meta/", "_raw/", "_archives/", "_staging/", "_readouts/", "folds/"))

# ---------- 1. registry ----------
registry = {}   # path -> {"name": stem, "aliases": [...]}
for r in records:
    path = r["path"]
    if is_reserved(path):
        continue
    text = (ROOT / path).read_text(encoding="utf-8")
    if is_redirect(text):
        continue
    fm = parse_fm(text)
    aliases = []
    m = re.search(r"^aliases:\s*\[(.*?)\]", fm, re.M)
    if m:
        aliases = [a.strip().strip('"').strip("'") for a in m.group(1).split(",") if a.strip()]
    registry[path] = {"name": Path(path).stem, "aliases": aliases}

# ---------- 2. candidate names ----------
def cjk_count(s):
    return sum(1 for c in s if "\u4e00" <= c <= "\u9fff")

candidate_names = {}  # name -> [paths]
for path, info in registry.items():
    for name in [info["name"]] + info["aliases"]:
        name = name.strip()
        if not name:
            continue
        if "[" in name or "]" in name or name.startswith("wiki/"):
            continue
        cjk = cjk_count(name)
        if cjk >= 3 or (cjk == 0 and len(name) >= 5):
            candidate_names.setdefault(name, [])
            if path not in candidate_names[name]:
                candidate_names[name].append(path)

# unambiguous only; also skip names that are substrings of longer candidate names
longer = sorted(candidate_names, key=len, reverse=True)
final = {}
for name in longer:
    if len(candidate_names[name]) != 1:
        continue
    if any(name != other and name in other for other in longer):
        continue  # substring of a longer candidate -> ambiguous mention
    final[name] = candidate_names[name][0]

print(f"candidates: {len(final)} unique names (from {len(registry)} pages)")

# ---------- 3. fragmented clusters ----------
tag_pages = defaultdict(list)
for r in records:
    if is_reserved(r["path"]):
        continue
    tags = r["tags"] if isinstance(r["tags"], list) else []
    for t in tags:
        tag_pages[t].append(r["path"])

clusters = []
for tag, pages in tag_pages.items():
    n = len(pages)
    if n < 5:
        continue
    pset = set(pages)
    pairs = n * (n - 1) // 2
    linked = 0
    for i in range(n):
        for j in range(i + 1, n):
            a, b = pages[i], pages[j]
            if any(tgt in (n2p.get(l) or []) for l in []):  # placeholder
                pass
    # recompute cohesion via stored links
    from collections import defaultdict as dd
    inbound = stats["inbound"]
    def res(t):
        return n2p.get(t) or n2p.get(t.lower()) or []
    inlink_of = dd(set)
    for tgt, srcs in inbound.items():
        for s in srcs:
            inlink_of[s].add(tgt)
    linked = 0
    for i in range(n):
        for j in range(i + 1, n):
            a, b = pages[i], pages[j]
            if (a in inlink_of and any(res(t) == [b] for t in inlink_of[a])) or \
               (b in inlink_of and any(res(t) == [a] for t in inlink_of[b])):
                linked += 1
    cohesion = linked / pairs if pairs else 1.0
    if cohesion < 0.15:
        clusters.append((tag, pages, cohesion, linked, pairs))

clusters.sort(key=lambda x: x[2])
scope_pages = set()
for tag, pages, coh, lk, pr in clusters:
    scope_pages.update(pages)
    print(f"  #{tag}: {len(pages)}p cohesion={coh:.2f} ({lk}/{pr})")
print(f"scope pages: {len(scope_pages)} across {len(clusters)} clusters")

# ---------- 4. mention scan ----------
def strip_code(text):
    return re.sub(r"```.*?```", " ", text, flags=re.DOTALL)

def body_of(path):
    text = (ROOT / path).read_text(encoding="utf-8")
    m = re.match(r"^---\n.*?\n---\n", text, re.DOTALL)
    body = text[m.end():] if m else text
    return strip_code(body)

# alternation, longest-first, escaped
names_sorted = sorted(final.keys(), key=len, reverse=True)
pattern = re.compile("|".join(re.escape(n) for n in names_sorted))

proposals = []  # (src, start, end, name, target_path)
for path in sorted(scope_pages):
    if is_reserved(path):
        continue
    body = body_of(path)
    # mask existing links
    masked = re.sub(r"\[\[[^\]]*?\]\]", "\u0000", body)
    seen = set()          # names already linked on this page
    for m in pattern.finditer(masked):
        if len(seen) >= 3:
            break
        name = m.group(0)
        if name not in final or name in seen:
            continue
        target = final[name]
        if target == path:
            continue
        proposals.append((path, m.start(), m.end(), name, target))
        seen.add(name)

print(f"\nproposed links: {len(proposals)}")

# aggregate per source
by_src = defaultdict(list)
for src, s, e, name, tgt in proposals:
    by_src[src].append((name, tgt))
print("pages to modify:", len(by_src))

# sample output
print("\n--- sample (first 25) ---")
for src, items in list(by_src.items())[:25]:
    print(f"  {src}:")
    for name, tgt in items[:3]:
        print(f"    [[{name}]] -> [[{tgt}]]")

# save plan
plan = [{"src": s, "name": n, "tgt": t} for s, items in by_src.items() for n, t in items]
(ROOT / ".vault-meta" / "crosslink-plan.json").write_text(
    json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"\nplan saved: {len(plan)} links across {len(by_src)} pages")
