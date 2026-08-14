#!/usr/bin/env python3
"""Apply approved mechanical wiki-lint fixes (2026-08-14).
1. Strip nested/double-bracket wikilink malformations.
2. Fix redirect stub bodies to match their redirects_to target.
3. Bump address-counter.txt to max assigned address.
4. Add missing `status` to synthesis/安倍经济学的政治属性评价.md.
"""
from pathlib import Path

ROOT = Path("/Users/mac/Documents/金融WIKI")

# (relative_path, old, new) — exact replacements, verified against files
FIXES = [
    # ---- nested-bracket malformations ----
    ("journal/digest-2026-08-06.md",
     "[[concepts/[[保交楼]]]]", "[[concepts/保交楼]]"),
    ("synthesis/扩表与缩表 × 财政货币化.md",
     "[[扩表与缩表 × [[中国央行]]]]", "[[扩表与缩表 × 中国央行]]"),
    ("synthesis/美联储 × 欧元区主权债务危机.md",
     "[[美联储 × [[IMF]]]]", "[[美联储 × IMF]]"),
    ("synthesis/扩表与缩表 × 央行入市干预.md",
     "[[[[美联储]] × 扩表与缩表]]", "[[美联储 × 扩表与缩表]]"),
    ("synthesis/欧盟 × 贸易战.md",
     "[[[[欧盟要与中国打贸易战]]？]]", "[[欧盟要与中国打贸易战？]]"),
    ("entities/美以伊战争.md",
     "[[2026-04-15-[[2026年1-3月中国外贸数据]]]]", "[[2026年1-3月中国外贸数据]]"),
    ("entities/韩国央行(BOK).md",
     "（[[[[央行]]]]）", "（[[央行]]）"),
    ("entities/意大利.md",
     "**来源文件**：[sources/[[[[欧盟要与中国打贸易战？]]]]]", "**来源文件**：[[欧盟要与中国打贸易战？]]"),
    ("concepts/粮食危机.md",
     "wiki/sources/[[2026-04-15-[[2026年1-3月中国外贸数据]]]].md", "[[2026年1-3月中国外贸数据]]"),
    ("concepts/冲销式干预.md",
     "[[sources/2026-06-02-[[2026-06-02-冲销式干预]]|冲销式干预]]", "[[sources/2026-06-02-冲销式干预|冲销式干预]]"),
    ("concepts/1970年代滞胀.md",
     "[[[[美联储独立性]]]]", "[[美联储独立性]]"),
    ("concepts/流动性风险.md",
     "[[美联储]] [[[[2023年SVB危机]]]]", "[[美联储]] [[2023年SVB危机]]"),
    ("concepts/美元霸权.md",
     "### 2.3 [[2026-06-02-[[石油美元体系]]]]", "### 2.3 [[2026-06-02-石油美元体系]]"),
    ("concepts/财政货币化.md",
     "[[questions/[[什么是财政货币化]]|财政货币化（问答）]]", "[[questions/什么是财政货币化|财政货币化（问答）]]"),
    ("concepts/实际利率框架.md",
     "[[[[1970年代滞胀]]]]", "[[1970年代滞胀]]"),
    ("concepts/广场协议.md",
     "[[[[1970年代滞胀]]]]", "[[1970年代滞胀]]"),
    ("sources/美联储中央央行流动性互换-Fed官网.md",
     "[[[中央银行]] Liquidity Swaps]", "[[中央银行]] Liquidity Swaps]"),
    ("sources/2026-03-24-中东局势对全球金融市场影响.md",
     "原 [[[中东局势对全球金融市场的影响]]]", "原 [[中东局势对全球金融市场的影响]]"),
    # ---- redirect stub bodies pointing at wrong name variant ----
    ("concepts/2008金融危机.md",
     "This page has been merged into [[2008 全球金融危机]].", "This page has been merged into [[2008全球金融危机]]."),
    ("entities/ECB.md",
     "This page has been merged into [[欧洲央行（ECB）]].", "This page has been merged into [[欧洲央行]]."),
    ("entities/ESM.md",
     "This page has been merged into [[欧洲稳定机制（ESM）]].", "This page has been merged into [[欧洲稳定机制]]."),
    ("entities/港股 vs 美股 vs A股.md",
     "This page has been merged into [[港股 vs 美股 vs A 股]].", "This page has been merged into [[港股vs美股vsA股]]."),
    ("entities/港股-vs-美股-vs-A股.md",
     "This page has been merged into [[港股 vs 美股 vs A 股]].", "This page has been merged into [[港股vs美股vsA股]]."),
    # ---- missing status field ----
    ("synthesis/安倍经济学的政治属性评价.md",
     "__ADD_STATUS__", "__ADD_STATUS__"),
]

def _add_status(text, rel):
    """Insert `status: developing` into frontmatter if absent (after lifecycle_changed line)."""
    import re
    m = re.search(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None, "no frontmatter"
    fm = m.group(1)
    if re.search(r"^status:", fm, re.M):
        return None, "status already present"
    if re.search(r"^lifecycle_changed:", fm, re.M):
        fm2 = re.sub(r"^(lifecycle_changed:[^\n]*)$", r"\1\nstatus: developing", fm, count=1, flags=re.M)
    else:
        fm2 = fm + "\nstatus: developing"
    return text[:m.start(1)] + fm2 + text[m.end(1):], None

applied, failed = [], []
for rel, old, new in FIXES:
    p = ROOT / rel
    if not p.exists():
        failed.append((rel, "FILE MISSING"))
        continue
    text = p.read_text(encoding="utf-8")
    if old == "__ADD_STATUS__":
        out, err = _add_status(text, rel)
        if err:
            failed.append((rel, err))
            continue
        p.write_text(out, encoding="utf-8")
        applied.append((rel, "added 'status: developing'"))
        continue
    if old not in text:
        failed.append((rel, f"OLD NOT FOUND: {old[:60]!r}"))
        continue
    cnt = text.count(old)
    text = text.replace(old, new)
    p.write_text(text, encoding="utf-8")
    applied.append((rel, f"{cnt}x '{old[:50]}' -> '{new[:50]}'"))

# address counter: peek -> max assigned
counter = ROOT / ".vault-meta" / "address-counter.txt"
try:
    cur = int(counter.read_text().strip())
    import json, re
    stats = json.loads((ROOT / ".vault-meta" / "lint-stats.json").read_text(encoding="utf-8"))
    maxn = 0
    for r in stats["records"]:
        m = re.match(r"^c-(\d{6})$", r.get("address", ""))
        if m:
            maxn = max(maxn, int(m.group(1)))
    if maxn > cur:
        counter.write_text(str(maxn) + "\n", encoding="utf-8")
        applied.append(("address-counter.txt", f"{cur} -> {maxn}"))
    else:
        failed.append(("address-counter.txt", f"no drift (peek={cur}, max={maxn})"))
except Exception as e:
    failed.append(("address-counter.txt", str(e)))

print("=== APPLIED ===")
for a in applied:
    print(" ", a[0], "|", a[1])
print(f"\n=== FAILED ({len(failed)}) ===")
for f in failed:
    print(" ", f[0], "|", f[1])
