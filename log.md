# 📜 Log

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
