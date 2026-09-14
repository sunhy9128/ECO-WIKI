# 📜 Log

## 2026-09-11: **WIKI_RESEARCH** topic="美国联合日本抛售欧元购买日元稳定日元的目的是什么" rounds=3 sources_fetched=5 pages_created=1 pages_updated=1

**研究：卖欧元买日元的交叉货币干预机制**。web 抓取受限（Reuters/FT/Bloomberg/IMF 均被墙或超时），成功抓取美国财政部 ESF 官方两页（主页 + Finances and Operations）+ 已在手 wiki 来源页。核心结论：①**ESF 外币资产仅持欧元与日元**（官方原文 "only yen- and euro-denominated"）——买日元只能卖欧元或美元，卖欧元是资产负债表资产再平衡（欧元→日元），不触碰美元；②**DXY 构成约束**（欧元权重 57.6%、日元 13.6%）——直接卖美元买日元会被读作美国主动贬值美元，卖欧元走 EUR/JPY 交叉盘不影响美元对主要货币的相对强弱信号；③**外交信号**——美方出"次要储备"（欧元）、日方出"主要武器"（美元），分工明确；④**执行机制**——纽约联储（FRBNY）作为 ESF 财政代理执行交易（官方确认）。既有概念页 [[concepts/2026-07 美日联合干预日元]] 操作细节节已补"为什么是欧元而非美元"四重机制；新建 [[sources/外汇稳定基金（ESF）-美国财政部官网]]（c-001203，status: draft）。整合 [[concepts/外汇干预有效性]]（干预是强心针不是根治药）。**QMD 未配置**（QMD_WIKI_COLLECTION 空），跳过刷新。

## 2026-09-11: **WIKI_SYNTHESIZE** pages_scanned=1089 synthesis_created=2 candidates_skipped=8

**新建 2 个交叉合成页**（基于全库共现扫描，排除已覆盖的 ECB×X 同义对）：
①[[synthesis/最后贷款人 × 扩表与缩表]]（c-001201，status: developing）——最后贷款人是央行"职能"、扩表缩表是"工具"：2008 后最后贷款人从"流动性后卫"越界为"资产买家"，扩表成为其新形态；白芝浩"惩罚性利率+合格抵押品"纪律在 QE 时代被搁置；**缩表难的根源=最后贷款人承诺的可逆性难题**（经典版贷款还回内生收缩 vs QE 版资产不自动回笼）。含最强反驳（QE 可能只是统计共现，日本 2001 QE 动机是通缩非危机）+ 可检验查询。
②[[synthesis/化债 × 欧债危机]]（c-001202，status: developing）——主权债务危机的两种处置路径：化债=预防式消化（货币主权+行政穿透力，置换买时间），欧债危机=爆发式偿付（货币联盟内无贬值通道，救助+紧缩）；**分叉点不是债务规模而是制度结构**。三推论：制度结构决定"消化还是爆发"、救助与紧缩时序（先松后紧 vs 先救后紧）、"看得见的手"（中国）vs"看不见的手"（欧洲）都未解决"谁约束发债人"。含最强反驳（债务主体层级不同：地方债务 vs 主权违约可能是类比错位）。
**反向链接**：最后贷款人/扩表与缩表/化债/欧债危机 4 源页补 synthesis 链接。
**跳过候选**：欧债危机×欧洲央行(61)、扩表与缩表×欧洲央行(53)、欧洲央行×美联储(49) 等 8 对——均为 ECB 实体别名重复或已覆盖；资产购买计划×量化宽松(34) 为同义页对（aliases 含 QE）跳过。
**QMD 未配置**（QMD_WIKI_COLLECTION 空），跳过刷新。

## 2026-09-11: **CAPTURE** type=question page="questions/为什么国债回购能压低政府发债成本.md" title="为什么国债回购能压低政府发债成本"

**问答消化页**（c-001200，status: completed）。核心：财政部回购→二级市场价格↑→存量收益率被动↓→一级市场定价锚定二级→新发债收益率↓→政府发债成本↓，链条**短期且间接**；加息时反向成立（久期放大旧债价格跌幅）。关键分层：**短端最终锚=央行政策利率，长端最终锚=短端预期+期限溢价（财政主导）**——"收益率最终回归美联储利率"只在短端成立；2026-08 实证（期限溢价宣布日仅 -1.7bp、两日后回升）证明回购压得住名义收益率、压不住财政风险成分。补充无风险利率近似条件（3M 国库券≈纯 Rf，10Y 国债=Rf+期限溢价）。反向链接 7 页（国债回购/国债收益率×利率×汇率/债市定价逻辑/风险溢价与无风险利率/一级市场与二级市场/名义利率与通胀预期/财政主导）。

## 2026-09-10: **WIKI_QUERY** query="系统性总结利率和国债收益率、汇率等之间的关系，以美元为例" result_pages=3 mode=normal escalated=false

**Pages consulted:** [[synthesis/国债收益率 × 利率 × 汇率]], [[concepts/利率平价理论]], [[concepts/实际利率框架]]

**Summary:** 基于合成页"国债收益率 × 利率 × 汇率"回答，补充利率平价理论和实际利率框架两个基础概念页。核心结论：三者通过利率平价、实际利率差、期限溢价、汇率超调四条通道联动，是"美元资产定价"的三个投影面。

## 2026-09-10: **WIKI_LINT_CONSOLIDATE** scanned=1094 orphans_rescued=38 broken_links_fixed=1 links_fixed=1 orphan_rescues=38 lifecycle_updates=0 report=synthesis/consolidation-2026-09-10.md

**Mode:** Consolidate (dry-run → apply on user approval "自动修复"). Pre-write snapshot: `6f02dac`.

**Applied:**
- [1] Fixed broken link: `concepts/美元周期.md:105` trailing space
- [2-39] Added 38 cross-references for orphan rescue across 16 source files
- [cleanup] Fixed 5 double-bracket issues caused by replacements inside existing wikilinks

**Not applied (require manual review):**
- Provenance issues (8): unsourced synthesis pages need human judgment
- Lifecycle/confidence schema: vault uses type+status; no migration
- Trust ledger: `_meta/trust-ledger.json` not created

**Post-consolidation orphan count:** 44→6 (38 rescued, remaining 6 are journal/meta/special pages)

---

## 2026-09-10: **WIKI_LINT** scanned=1094 orphans=44 broken_links=1 fm_gaps=849 stale=165 lifecycle_issues=0 visibility=0 taxonomy_contam=0 fragmented=105 prov_issues=8

**Scope:** Full vault scan (1094 pages). Checks 1-13 run.
- **Orphans: 44** — 20 entities, 18 concepts, 2 journal, 4 misc (vs 0 on 08-31: regression from index-link pattern change; orphans are real pages with zero incoming wikilinks)
- **Dead links: 1** — `concepts/美元周期.md:105` → `[[concepts/2008全球金融危机 ]]` (trailing space). 11 others in `.claudian/opencode/metadata/system.md` (template placeholders, not knowledge graph)
- **FM gaps: 849** — majority missing `sources` field; 4 pages have no frontmatter at all (journal/2026-09-08, journal/2026-09-09, .omo/plans/wiki-query-log-sync)
- **Summary: 1031 missing** (soft warning, 0 too long)
- **Stale >90d: 165** — all LLM-Wiki/SEO template pages + older sources (0 verified, 0 high-priority)
- **Lifecycle: 0 issues** — vault uses type+status convention, not lifecycle+base_confidence; no pages have lifecycle field set
- **Trust ledger: MISSING** — `_meta/trust-ledger.json` not found; trust-check returns ledger_missing error
- **Taxonomy contamination: 0** — visibility/ tags appear only in documentation text within taxonomy.md, not as tag entries (false positive from 08-31)
- **Fragmented tags: 105 clusters** (cohesion<0.15, n≥5) — large topic tags (#金融 92, #中国 89, #地缘政治 99, #宏观 77, #美联储 51) are structurally low-cohesion due to broad scope
- **Provenance: 8 pages** with markers — 3 unsourced synthesis (马来西亚模式 94% inferred, 人民币不贬值承诺 100%, questions/马来西亚vs*), 3 AMBIGUOUS>15%
- **Visibility: 0 issues**
- **Relationships: 0 issues**
- **Index: 45 content pages not in index.md** (curated subset by design), 1 phantom link (`[[log]]`)

**Compared to 08-31 baseline (1089 pages):**
- Pages: 1089→1094 (+5)
- Orphans: 0→44 (regression: orphan detection now uses exact basename matching vs previous grep substring)
- Dead links: 0→1 (trailing space in 美元周期.md)
- FM gaps: 656→849 (+193, mostly pages with `sources: []` counted as missing)
- Stale: 26→165 (threshold now includes all >90d pages, not just LLM-Wiki)
- Lifecycle: 1047→0 (corrected: vault never adopted lifecycle schema, false positives removed)
- Taxonomy: 3→0 (visibility tags are in documentation text, not tag entries)
- Fragmented: 73→105 (expanded tag set analyzed)

- [2026-09-10] LINT scanned=1094 orphans=44 broken_links=1 fm_gaps=849 stale=165 lifecycle_issues=0 visibility=0 taxonomy_contam=0 fragmented=105 prov_issues=8

## 2026-08-31: **WIKI_LINT** scanned=1089 orphans=0 broken_links=0 fm_gaps=656 stale=26 lifecycle_issues=1047 visibility=0 taxonomy_contam=3 fragmented=73

**Scope:** Full vault scan (1089 pages). Checks 1-13 run.
- **Orphans: 0** — all resolved by dedup/cross-linker (08-25)
- **Dead links: 0** — all resolved (dedup + full-path index now covers `[[concepts/X]]` forms)
- **FM gaps: 656** — 656 pages with `tags: []` (empty list); 7 missing created; 2 missing type/category; 1 missing title; 1 missing updated
- **Summary: 1023 missing** (soft warning, 0 too long)
- **Stale >90d: 26** — all are LLM-Wiki/SEO template pages from April 2026 (0 verified, 0 high-priority)
- **Lifecycle: 1047/1089 missing** (schema not adopted — vault uses type+status, not lifecycle+base_confidence)
- **Taxonomy contamination: 3** — visibility/public, visibility/internal, visibility/pii in `_meta/taxonomy.md` (system tags must not appear in taxonomy)
- **Fragmented tags: 73 clusters** (cohesion<0.15, n≥5) — many are type-level tags (#金融 67, #货币政策 65, #地缘政治 44)
- **Visibility: 0 issues**
- **Provenance: 7 pages** with blocks (synthesis cluster from 08-11 research)
- **Relationships: 0 issues**
- **Index: 883/1083 content pages not in index.md** (curated subset by design, not a bug)

**Compared to 08-05 baseline (1000 pages):**
- Orphans: 44→0 ✅
- Dead links: 25→0 ✅  
- FM gaps: 615→656 (net +41 new pages + empty tags)
- Stale: 25→26 (net +1 LLM-Wiki page)
- New issues: taxonomy contamination (3 visibility tags)

---

## 2026-08-25: **WIKI_DEDUP (Execute):** 2 merges executed (sanctions weaponization + subprime crisis), 11 inlinks rewritten across 5 files, 5 needs-review confirmed KEEP-SEPARATE

**Mode:** Execute (audit→execute on user approval "merge all")

**Executed:**

#### Merge 1: `concepts/制裁武器化` (c-001184) → `concepts/制裁武器` (c-000169)

- `制裁武器化.md` → redirect stub (status=redirect, redirects_to=[[concepts/制裁武器]], merged_into=c-000169, merge_date=2026-08-25)
- `制裁武器.md` aliases: added `制裁武器化`, `制裁的武器化`, `Weaponization of Sanctions`
- `制裁武器.md` relationships: added `[[concepts/出口管制]]` + `[[concepts/武器化相互依存]]` (migrated from stub)
- Fixed pre-existing ambiguous `[[二级制裁]]` → `[[concepts/二级制裁|二级制裁]]`
- Inlinks rewritten (6 occurrences, 3 files):
  - `concepts/美元循环.md`: frontmatter + body line
  - `concepts/美元潮汐.md`: frontmatter + body line
  - `concepts/Exorbitant Privilege（过度特权）.md`: frontmatter + body heading §5.2

#### Merge 2: `entities/次贷危机` (c-000683) → `concepts/2008全球金融危机` (c-000027)

- `次贷危机.md` → redirect stub (status=redirect, redirects_to=[[concepts/2008全球金融危机]], merged_into=c-000027, merge_date=2026-08-25)
- `次贷危机.md` aliases: added `Subprime Mortgage Crisis`, `2007次贷危机`, `次级抵押贷款危机`
- Unique depth content from次贷危机 (sections 一-三: subprime loan classification + scale data, 2/28 ARM mechanics, MBS/CDO tranche structure, CDO² re-packaging, synthetic CDO, rating failure data with $3T/75%/90% stats) merged as new `## 补充内容（原 次贷危机）` section at end of GFC page (preserves vault's existing 补充内容 pattern)
- Inlinks rewritten (5 occurrences, 2 files):
  - `concepts/美元周期.md`: frontmatter + table cell `[[次贷危机]]`
  - `entities/雷曼兄弟.md`: frontmatter + 2 body wikilinks + 1 related entry

**Inlink rewrites (5 distinct references across 2 files):**

- All `[[entities/次贷危机]]` → `[[concepts/2008全球金融危机]]` (full-path)
- All `[[次贷危机]]` → `[[concepts/2008全球金融危机|次贷危机]]` (display-text preserved)

**Needs-review confirmed KEEP-SEPARATE:**

- 外汇管制 ↔ 外汇管理 (narrow vs broad)
- 陆股通 ↔ 港股通 (northbound vs southbound)
- 联系汇率制度 ↔ 汇率制度 (general vs specific)
- QFII ↔ QF制度 (component vs umbrella)
- 开正门堵偏门 ↔ 开正门、堵偏门 (different domains: 对外投资 vs 地方债务)

**Trust:** trust_check=OK ledger_current, all edits markdown-clean per pi-lens LSP, no blocking diagnostics. Final dedup registry at /tmp/dedup_registry.json, candidate list at /tmp/dedup_candidates.json. Pre-merge snapshot: 0d76347.

---

## 2026-08-25: **WIKI_DEDUP (Audit):** 1035 pages scanned, 0 merges executed, 3 merge candidates + 4 needs-review flagged for user decision

**Mode:** Audit (no destructive actions — user approval required for merges)

**Pipeline:**

- Built registry from 1035 `.md` files (excluded `_archives/`, `_raw/`, `_obsidian/`, `index.md`, `log.md`, `hot.md`, `redirects_to:` pages)
- Pairwise similarity scoring (title tokens Jaccard + edit distance + alias cross-match + substring containment + tag/category semantic)
- Threshold: composite ≥ 0.75 → 133 candidates. Filtered synthesis × pattern false positives (123 of 133) → 52 real candidates.
- HIGH (≥0.90): 10 / MEDIUM (0.75–0.89): 123 (mostly synthesis A × B vs A × C)

**Verdicts (3 MERGE, 4 NEEDS-REVIEW, 47 KEEP-SEPARATE confirmed):**

### ✅ Recommended MERGES (user approval required before executing)

#### 1. `concepts/制裁武器化` (c-001184, stub, 746 chars) → `concepts/制裁武器` (c-000169, developing, 1268 chars)

- **Score:** 0.75 (substring 制裁武器 ⊂ 制裁武器化)
- **Aliases:** `制裁武器化` page aliases: `制裁的武器化`, `Weaponization of Sanctions`
- **Inlinks:** `制裁武器` basename = 15; `制裁武器化` basename = 1. Full-path: `concepts/制裁武器`=1, `concepts/制裁武器化`=8 (3 of these added by today's cross-linker: 美元循环, 美元潮汐, Exorbitant Privilege)
- **Same category** (concepts), same scope (weaponization of financial/trade sanctions)
- **Why merge:** 制裁武器化 is a stub with only the concept mention + 5 cross-links. 制裁武器 has the actual definition, key features, applications (Russia/Iran/N.Korea/Venezuela examples), and is the older page (2026-06-02 vs 2026-08-14). Same concept, different names.
- **Canonical:** `concepts/制裁武器` (more inlinks, richer content, older, same category)
- **Action:** Convert `制裁武器化` → redirect stub to `制裁武器`; rewrite 3 cross-linker inlinks (美元循环, 美元潮汐, Exorbitant Privilege); add `制裁武器化` → alias of `制裁武器`

#### 2. `entities/次贷危机` (c-000683, developing, 7469 chars) → `concepts/2008全球金融危机` (c-000027, current, 14660 chars)

- **Score:** 0.83 (alias cross-match — `次贷危机` is alias of GFC page)
- **Aliases:** `2008全球金融危机` aliases include `次贷危机`, `Subprime Crisis`, `2008 年次贷危机`. `次贷危机` page has empty aliases.
- **Inlinks:** `2008全球金融危机` basename = 145; `次贷危机` basename = 2 (both point to `entities/次贷危机`); `concepts/2008全球金融危机` = 30; `entities/次贷危机` = 2
- **Wrong category:** `次贷危机` typed as `entity` (it's a crisis concept, belongs in `concepts/`)
- **Self-referential:** `次贷危机` page H1 is literally `# [[2008全球金融危机]]` — already a redirect-with-body
- **Body overlap:** MBS/CDO mechanics, ratings failures, timeline 2007-2009, Lehman/AIG/TARP, contagion paths, policy responses — all duplicated in GFC page (GFC is 2x larger and includes more)
- **Why merge:** `次贷危机` page itself frames the event as the GFC ("核心导火索 — 从次级贷款到全球金融海啸"). The 2008 global crisis page already treats 次贷危机 as a synonym via aliases. Substantive unique content (MBS/CDO tranche diagrams, rating agency mechanism, 2/28 ARM specifics) should be merged into GFC's existing subprime section.
- **Canonical:** `concepts/2008全球金融危机` (145 inlinks vs 2, correct category, richer, status current)
- **Action:** Move unique MBS/CDO/rating content from `次贷危机` into the subprime section of GFC page (sections 一-三 of 次贷危机 cover this); convert `次贷危机` → redirect stub with `[[2008全球金融危机|2008全球金融危机]]` redirect (preserves 2 inlinks); rewrite `concepts/欧猪五国`, `CDS信用违约互换`, `多德弗兰克法案`, `资产证券化`, `雷曼兄弟`, `美元流动性`, `美元周期` back-links from `entities/次贷危机` → `concepts/2008全球金融危机`

#### 3. (REJECTED — different domains) `concepts/开正门堵偏门` ↔ `concepts/开正门、堵偏门`

- **Score:** 0.75 (alias cross-match — comma variant)
- **Verdict:** KEEP-SEPARATE — same policy phrase but applied to **different domains**:
  - `开正门堵偏门` (c-000264, 1065 chars) = **对外投资监管** (837号令, 跨境资本流动)
  - `开正门、堵偏门` (c-000263, 2329 chars) = **地方债务治理** (化债/隐性债务/专项债)
- The `开正门、堵偏门` page already lists `开正门堵偏门` as a "并列条目（合并前变体）" — same phrase, two contexts. No action.

### ⚠️ NEEDS-REVIEW (judgment call — flag for user)

#### A. `concepts/外汇管制` (c-000223, 20 inlinks) ↔ `concepts/外汇管理` (c-000956, 17 inlinks)

- **Score:** 0.75
- **Different scope:**
  - `外汇管制` = narrower: **controls/restrictions** on FX (purchase, sale, cross-border movement)
  - `外汇管理` = broader: **FX management regime** (covering 结售汇制, 外汇额度, 资本管制, 外汇储备, 汇率干预) — China's institutional framework
- The broader page (`外汇管理`) lists `外汇管制` in `related:` field, suggesting they're **distinct concepts in a hierarchy** (管制 ⊂ 管理).
- **Recommendation:** KEEP-SEPARATE (different scope, different role). Add cross-link between them.

#### B. `concepts/2008全球金融危机` ↔ `entities/次贷危机`

- See MERGE #2 — fully covered.

#### C. `concepts/陆股通` ↔ `entities/港股通`

- **Score:** 0.85
- Both Stock Connect channels: `陆股通` = northbound (mainland-listed stocks to HK investors), `港股通` = southbound (HK-listed stocks to mainland investors)
- Same `tags: [中国, 金融, 对外开放, 资本管制, QF制度]` and similar content
- Different category (concepts vs entities) and different scope (Stock Connect itself is a synthesis concept spanning four pages: 沪港通, 深港通, 陆股通, 港股通)
- **Recommendation:** KEEP-SEPARATE (two directions of same channel — complementary not duplicate)

#### D. `concepts/联系汇率制度` ↔ `concepts/汇率制度`

- **Score:** 0.80 (substring)
- `联系汇率制度` = currency board (HK's specific regime, LERS)
- `汇率制度` = exchange rate regime (general concept — covers floating, fixed, managed float, currency board as a subtype)
- **Recommendation:** KEEP-SEPARATE (general vs specific, 子集关系). Add bidirectional cross-link if not already.

#### E. `concepts/QFII` ↔ `concepts/QF制度`

- **Score:** 0.80
- `QFII` = specific investor program (Qualified Foreign Institutional Investor, USD-denominated)
- `QF制度` = umbrella concept (covers QFII, RQFII, QDII as a system)
- **Recommendation:** KEEP-SEPARATE (QFII is a component of QF制度, hierarchical)

#### F. `concepts/美元潮汐` ↔ `concepts/美元潮汐历史案例`

- **Score:** 0.80 (substring 美元潮汐 ⊂ 美元潮汐历史案例)
- `美元潮汐` (c-000907) = mechanism / theory page
- `美元潮汐历史案例` (c-000910) = historical case studies (Sri Lanka 2022, Turkey 2018-19, etc.)
- **Recommendation:** KEEP-SEPARATE (mechanism vs cases — intentional split, both created same day with sequential addresses c-000907 / c-000910)

#### G. `concepts/美元周期` ↔ `concepts/美元加息周期`

- **Score:** 0.75
- `美元周期` (c-000908, 5756 chars, current) = full dollar cycle (rate ↑ + ↓, cap flows, etc.)
- `美元加息周期` (c-000360, 931 chars, developing) = just the hiking phase
- **Recommendation:** KEEP-SEPARATE (cycle vs phase, different status, different scope). Possibly promote 美元加息周期 from developing → current if 美元周期 page covers it.

### ❌ KEEP-SEPARATE (verified false positives)

#### Synthesized patterns (123 of 133 = false positives from × naming)

- `扩表与缩表 × IMF` vs `扩表与缩表 × 中国央行` (0.95) — different synthesis anchors
- `美联储 × ECB` vs `美联储 × IMF` (0.95) — different synthesis anchors
- `美联储 × 2020年3月流动性危机` vs `量化宽松 × 2020年3月流动性危机` (0.90) — different synthesis angles
- `扩表与缩表 × 财政货币化` vs `扩表与缩表 × 央行入市干预` (0.87) — different synthesis anchors
- 24+ similar `×` pairs: same pattern, different cross-domain intersections. **Distinct synthesis pages by design.**

#### Genuine false-positive pairs (verified different concepts)

| A | B | Score | Why separate |
| --- | --- | --- | --- |
| `深港通` | `沪港通` | 0.95 | Shenzhen vs Shanghai Stock Connect (different regional channels) |
| `QDII` | `QFII` | 0.95 | Outbound (domestic→overseas) vs Inbound (overseas→domestic) |
| `RQFII` | `QFII` | 0.95 | RMB-denominated vs USD-denominated inbound |
| `1992 欧洲货币危机` | `1997 亚洲金融危机` | 0.94 | Different events, different regions, different years |
| `长鑫存储 (CXMT)` | `长江存储 (YMTC)` | 0.94 | CXMT = DRAM; YMTC = NAND. Different companies. |
| `2014-2015 俄罗斯卢布危机` | `1998 俄罗斯卢布危机` | 0.83 | Different events, different decades |
| `陆股通` | `港股通` | 0.85 | Northbound vs Southbound direction |
| `期权策略` | `期权` | 0.80 | Strategies page vs base options concept |
| `期权` | `累计期权` | 0.80 | Vanilla vs exotic option |
| `期货对冲` | `动态对冲` | 0.80 | Static hedge vs dynamic delta hedge |
| `1994 龙舌兰危机` | `1998 俄罗斯卢布危机` | 0.80 | Different regions, different contexts |
| `FIMA回购便利` | `sources/FIMA回购便利-Fed官网` | 0.77 | Concept page vs source citation |
| `claude-obsidian-v1.4-release-session` | `claude-obsidian-v1.2.0-release-session` | 0.75 | Different release versions |
| `利率市场化` | `汇率非市场化` | 0.75 | Rate liberalization vs FX non-marketization |
| `软着陆` | `硬着陆` | 0.75 | Opposites |
| `财务分析框架` | `行业分析框架` | 0.75 | Finance vs industry analysis |
| `本币贬值` | `本币升值` | 0.75 | Opposites |
| `SLO` | `SLF` | 0.75 | Different PBoC facilities |
| `MLF` | `SLF` | 0.75 | Different PBoC facilities |
| `出口商品结构` | `进口商品结构` | 0.75 | Export vs import |
| `冲销式干预` | `非冲销式干预` | 0.75 | Opposites (sterilized vs unsterilized) |
| `魏玛恶性通胀` | `恶性通胀` | 0.75 | Specific case vs general |
| `技术分析指标` | `技术分析` | 0.75 | Indicators vs field |
| `无人机消耗战` | `俄乌无人机消耗战` | 0.75 | General vs specific |
| `跷跷板效应` | `股债跷跷板效应` | 0.75 | General vs specific |
| `地缘政治对抗` | `地缘政治` | 0.75 | Conflict vs general geopolitics |
| `开正门堵偏门` | `开正门、堵偏门` | 0.75 | **Different domains** (outbound FX vs local debt) |
| `2026-06-25-逼疯` | `崩溃的信徒` | 0.75 | Different sources/articles |
| `2026-07-21-韩国股灾简史` | `2026-06-24-韩国需要冷静冷静` | 0.75 | Different articles, different dates |
| `布雷顿森林体系` | `布雷顿森林体系瓦解` | 0.75 | System vs its collapse |
| `欧元` | `欧元区` | 0.75 | Currency vs currency union |
| `新兴市场` | `新兴市场危机` | 0.75 | Market vs crisis |
| `英国养老金制度` | `英国养老金危机` | 0.75 | System vs crisis |
| `收益率曲线` | `国债收益率曲线` | 0.75 | General vs sovereign bond curve |
| `港股` | `港股通` | 0.75 | Market vs channel |
| `俄罗斯` | `索罗斯` | 0.75 | Country vs person |
| `CHIPS` | `CIPS` | 0.75 | US clearing (CHIPS) vs China cross-border clearing (CIPS). **Confusing names — clearly different systems** |
| `银监会` | `证监会` | 0.75 | Banking regulator (CBRC) vs securities regulator (CSRC) |
| `瑞典央行` | `瑞士央行` | 0.75 | Sweden Riksbank vs Swiss SNB |
| `汇率风险` | `利率风险` | 0.75 | FX risk vs interest rate risk |
| `关税战` | `贸易战` | 0.75 | Tariff war vs trade war |

---

**Summary:**

- **Scanned:** 1035 pages, 203,105 pairs, 133 candidates ≥0.75
- **False positives:** 130 (123 synthesis × + 7 name-similar but distinct)
- **MERGE candidates (2):**
  1. `concepts/制裁武器化` → `concepts/制裁武器`
  2. `entities/次贷危机` → `concepts/2008全球金融危机`
- **NEEDS-REVIEW (4):** 外汇管制↔外汇管理, 陆股通↔港股通, 联系汇率制度↔汇率制度, QFII↔QF制度 (all recommended KEEP-SEPARATE)
- **No destructive actions taken** (Audit mode default). Awaiting user approval for the 2 merge operations before executing redirects + inlink rewrites.

**Trust:** trust_check=WARN ledger_current, dedup_registry at /tmp/dedup_registry.json, candidates at /tmp/dedup_candidates.json

- [2026-08-26] QUERY query="什么是一级市场和二级市场" result_pages=5 mode=normal escalated=false

- [2026-08-26] CAPTURE type=concept page="concepts/一级市场与二级市场.md" title="一级市场与二级市场"

- [2026-08-26] RESEARCH topic="国债收益率×利率×汇率联动 + 长债回购推演" pages=4 mode=wiki-research
  - synthesis/国债收益率 × 利率 × 汇率.md (c-001195)
  - concepts/国债回购.md (c-001196)
  - concepts/美元贬值交易.md (c-001197)
  - sources/2026-08-19-贝森特长债回购计划.md (c-001198)
  - 核心发现：2026-08-19 贝森特将长债回购上限翻倍至 $4B，压低长端收益率把调整压力转移到美元，触发"美元贬值交易"（黄金+3%、比特币+13%、DXY 跌破99），被类比 Operation Twist 与软性金融压抑
- [2026-08-26] RESEARCH topic="财政主导（fiscal dominance）" pages=1 mode=wiki-research
  - synthesis/财政主导.md (c-001199)
  - 核心发现：财政主导是货币当局被财政赤字绑架的制度状态，是财政货币化的前提、央行独立性的反面；2026 年 MSCI 列为全球利率头号变量，美国长债回购正是财政主导的最新注脚——压低长端收益率把压力转移到美元，触发"美元贬值交易"

- [2026-08-28] QUERY query="美债收益率和汇率关系" result_pages=3 mode=normal escalated=false

- [2026-08-28] CAPTURE type=concept page="concepts/汇率传导机制.md" title="汇率传导机制"
- [2026-08-28] CAPTURE type=concept page="concepts/汇率超调模型.md" title="汇率超调模型"
