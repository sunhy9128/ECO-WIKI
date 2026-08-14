#!/usr/bin/env python3
"""Apply the crosslink-fragmented plan (2026-08-14).
- Inline-link first natural unlinked mention of each name.
- Append related_to relationships entries (dedup against existing targets).
- Bump `updated:` to 2026-08-14 on modified pages.
"""
import json, re
from pathlib import Path

ROOT = Path("/Users/mac/Documents/金融WIKI")
TODAY = "2026-08-14"

plan = json.loads((ROOT / ".vault-meta" / "crosslink-plan.json").read_text(encoding="utf-8"))
by_src = {}
for p in plan:
    by_src.setdefault(p["src"], []).append(p)

def insert_first(body, name, tgt_no_ext):
    """Return (new_body, inserted_bool). Link the first occurrence of `name`
    that is not inside an existing [[...]] span or markdown link [t](url).
    Never drops trailing text."""
    PROTECT = re.compile(r"\[\[[^\]]*?\]\]|\[[^\]\n]*\]\([^)\n]*\)")
    out = []
    pos = 0
    done = False
    for m in PROTECT.finditer(body):
        out.append(body[pos:m.start()])
        out.append(m.group(0))
        pos = m.end()
        if not done:
            seg = out[-2]  # the non-link chunk just emitted
            idx = seg.find(name)
            if idx >= 0:
                out[-2] = seg[:idx] + f"[[{tgt_no_ext}|{name}]]" + seg[idx + len(name):]
                done = True
    seg = body[pos:]
    if not done:
        idx = seg.find(name)
        if idx >= 0:
            out.append(seg[:idx] + f"[[{tgt_no_ext}|{name}]]" + seg[idx + len(name):])
            done = True
        else:
            out.append(seg)
    else:
        out.append(seg)
    return "".join(out), done

def add_relationships(fm_text, targets):
    rel_lines = ["relationships:"]
    for t in targets:
        rel_lines.append(f'  - target: "[[{t}]]"')
        rel_lines.append("    type: related_to")
    block = "\n".join(rel_lines)
    m = re.search(r"^relationships:\s*(.*)$", fm_text, re.M)
    if m:
        tail = m.group(1).strip()
        if tail in ("[]", '""', "''", ""):
            return fm_text[:m.start()] + block + fm_text[m.end():]
        rest = fm_text[m.end():]
        nxt = re.search(r"\n[a-zA-Z_][a-zA-Z0-9_]*:", rest)
        block_end = m.end() + nxt.start() if nxt else len(fm_text.rstrip("\n"))
        return fm_text[:block_end] + "\n" + "\n".join(rel_lines[1:]) + fm_text[block_end:]
    anchor = None
    for key in ("aliases:", "tags:", "status:", "category:"):
        am = re.search(rf"^{re.escape(key)}.*(?:\n(?:\s+-[^\n]*))*", fm_text, re.M)
        if am:
            anchor = am.end()
            break
    if anchor is None:
        anchor = len(fm_text.rstrip("\n"))
    return fm_text[:anchor] + "\n" + block + fm_text[anchor:]

stats = {"pages": 0, "links": 0, "rel": 0, "bumped": 0, "failed": []}

for src, items in by_src.items():
    p = ROOT / src
    text = p.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        stats["failed"].append((src, "no frontmatter"))
        continue
    fm, body = m.group(1), text[m.end():]
    inserted_targets = []
    for item in items:
        name, tgt = item["name"], item["tgt"]
        if len(inserted_targets) >= 3:
            break
        tgt_no_ext = tgt[:-3] if tgt.endswith(".md") else tgt
        body, ok = insert_first(body, name, tgt_no_ext)
        if ok:
            inserted_targets.append(tgt_no_ext)
    if not inserted_targets:
        stats["failed"].append((src, "no insertable mention"))
        continue
    # dedup relationships targets already present in fm
    existing = set(re.findall(r'target:\s*"\[\[([^\]]+)\]\]"', fm))
    new_targets = [t for t in inserted_targets if t not in existing]
    fm2 = add_relationships(fm, new_targets) if new_targets else fm
    # bump updated
    fm2 = re.sub(r"^updated:.*$", f"updated: {TODAY}", fm2, count=1, flags=re.M)
    p.write_text(f"---\n{fm2}\n---\n{body}", encoding="utf-8")
    stats["pages"] += 1
    stats["links"] += len(inserted_targets)
    stats["rel"] += len(new_targets)
    stats["bumped"] += 1

print(json.dumps(stats, ensure_ascii=False, indent=1))
print("\n=== FAILED ===")
for f in stats["failed"][:20]:
    print("  ", f)
