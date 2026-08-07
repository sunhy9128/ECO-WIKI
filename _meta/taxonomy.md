---
type: meta
title: "Tag Taxonomy"
created: 2026-08-06
updated: 2026-08-06
tags: [meta, taxonomy]
status: current
---

# Tag Taxonomy — 标签受控词表

> 本文件是标签体系的**唯一事实来源**。打标签、审计、规范化前必须先读本文件。
> 由 2026-08-06 全库标签审计归纳得出(986 页 / 856 个去重标签 / 590 个单次标签)。

## 规则 Rules

1. **每页最多 5 个标签**。超过 5 个时裁剪:优先保留 Domain 标签,移除 type 与次要标签。
2. **Type 不进 tags**。分类由 frontmatter `type:` 字段承担(concept/entity/source/synthesis/comparison/question/domain)。tags 中出现的 type 类标签(`concept`/`entity`/`term`/`event`/`person`/`source`/`index`/`question`/`meta`/`synthesis`/`stub`)属于迁移遗留,应移除,见 Migration Guide。
3. **一个概念只保留一个 canonical**。别名列于下节 Aliases 映射,不并存。检索时别名应归并到 canonical。
4. **中文优先**。Domain 标签以中文为主;国际通用金融缩写(`QE`/`YCC`/`QQE`/`CPI`/`ECB`/`IMF`/`ESG`/`KOSPI`/`NISA`/`DXY`/`COFER`/`PSL`)无自然中文简写,保留原文。
5. **优先 broad,避免专属**。标签描述主题领域而非单一事件。页面专属词(机构名/人名/产品名)仅在跨页复用时才成标签。
6. **`visibility/` 为系统保留组**:不计数、不受别名约束、不与 Domain 混用。当前库内零使用(无敏感内容)。

## Canonical Tags(Domain)

### 货币政策与央行
- 货币政策 (alias: monetary-policy, monetary, monetary-mechanics)
- 央行 (alias: central-bank)
- 美联储 (alias: fed)
- 量化宽松 (alias: QE, quantitative-easing)
- 量化紧缩 (alias: QT)
- 扩表缩表 (alias: balance-sheet)
- QQE
- YCC
- 负利率
- 利率
- 加息
- 降息
- 利率走廊

### 国际金融与货币体系
- 美元 (alias: dollar)
- 汇率 (alias: exchange-rate, fx)
- 美元周期 (alias: dollar-cycle, dollar-tide)
- 货币体系 (alias: monetary-system)
- 布雷顿森林 (alias: bretton-woods)
- 储备货币 (alias: reserve-currency)
- 资本管制 (alias: capital-controls, capital-control, capital-account)
- 人民币国际化
- 特里芬难题
- SDR
- 石油美元 (alias: petrodollar)
- 原罪
- 过度特权
- 货币错配 (alias: currency-mismatch)

### 金融市场与工具
- 衍生品 (alias: derivatives)
- 期权 (alias: options)
- 期货 (alias: futures)
- 套期保值 (alias: hedging, hedge)
- 轧空 (alias: short-squeeze, short-selling)
- 回购 (alias: repo, money-market)
- 市场机制 (alias: market-mechanics, market-mechanism, market-structure)
- 股票市场 (alias: stock-market, stock-index, equity)
- 债券市场 (alias: bond-market, treasury)
- 资产定价
- 风险管理 (alias: risk-management)

### 银行与监管
- 银行 (alias: banking, investment-bank, bank)
- 监管 (alias: regulation, banking-regulation, post-crisis)
- 巴塞尔协议 (alias: basel-iii)
- 资本充足 (alias: capital-requirement, leverage-ratio)
- 流动性 (alias: liquidity)
- 影子银行 (alias: shadow-banking)
- 系统性风险 (alias: systemic-risk)
- 金融危机 (alias: financial-crisis, crisis, banking-crisis)
- 金融稳定 (alias: financial-stability)
- 保险 (alias: insurance)

### 宏观与地缘
- 宏观经济 (alias: macroeconomics, macro, economy)
- 通胀 (alias: inflation, CPI)
- 财政政策 (alias: fiscal-policy)
- 地缘政治 (alias: geopolitics)
- 制裁 (alias: sanctions, financial-sanctions)
- 能源 (alias: energy)
- 军工
- 贸易 (alias: trade)
- 全球化

### 中国
- 中国 (alias: china)
- 房地产
- 房价
- 化债
- 城投 (alias: local-government)
- 财税改革
- 国企改革 (alias: soe-reform)
- 金融改革
- A股 (alias: a股)
- QF制度
- 对外开放
- 香港 (alias: hong-kong)
- 央企 (alias: central-enterprise)
- 收入分配
- 新质生产力

### 日本
- 日本 (alias: japan)
- 安倍经济学 (alias: Abenomics)
- 泡沫经济
- 广场协议
- 日元套利交易 (alias: carry-trade)
- 失落的三十年

### 欧洲
- 欧元区 (alias: eurozone, european-union)
- 欧债危机
- ECB
- 欧洲货币体系 (alias: european-monetary-system, ems)
- 德国

### 美国与其他地区
- 美国 (alias: usa)
- 韩国 (alias: korea)
- 新兴市场 (alias: emerging-markets)
- 新加坡 (alias: singapore)
- KOSPI (alias: kospi)
- 亚洲 (alias: asia)
- 亚洲金融危机

### 投资与机构
- 主权基金 (alias: swf, sovereign-wealth)
- 对冲基金 (alias: hedge-fund)
- 私募股权 (alias: private-equity)
- 动态对冲 (alias: dynamic-hedging)
- 资本回报 (alias: capital-return)
- ESG

### 主题横切
- 金融史
- 金融学
- 宏观经济史
- 央行史
- 数据 (alias: statistics, empirical, data)
- 金融 (alias: finance)

### 来源与人物(低优先,仅在跨页复用时使用)
- 巫师财经
- 任庄主
- 索罗斯 (alias: soros, george-soros)

## Aliases 映射(中英同义 → canonical)

| 别名 | → Canonical |
|---|---|
| `monetary-policy` / `monetary` / `monetary-mechanics` | 货币政策 |
| `central-bank` | 央行 |
| `fed` | 美联储 |
| `QE` / `quantitative-easing` | 量化宽松 |
| `QT` | 量化紧缩 |
| `balance-sheet` | 扩表缩表 |
| `dollar` | 美元 |
| `exchange-rate` / `fx` | 汇率 |
| `dollar-cycle` / `dollar-tide` | 美元周期 |
| `monetary-system` | 货币体系 |
| `bretton-woods` | 布雷顿森林 |
| `reserve-currency` | 储备货币 |
| `petrodollar` | 石油美元 |
| `derivatives` | 衍生品 |
| `options` | 期权 |
| `futures` | 期货 |
| `hedging` | 套期保值 |
| `short-squeeze` / `short-selling` | 轧空 |
| `repo` / `money-market` | 回购 |
| `market-mechanics` / `market-mechanism` / `market-structure` | 市场机制 |
| `banking` / `bank` | 银行 |
| `regulation` / `banking-regulation` / `post-crisis` | 监管 |
| `basel-iii` | 巴塞尔协议 |
| `capital-requirement` | 资本充足 |
| `liquidity` | 流动性 |
| `shadow-banking` | 影子银行 |
| `systemic-risk` | 系统性风险 |
| `financial-crisis` / `crisis` / `banking-crisis` | 金融危机 |
| `macroeconomics` / `macro` / `economy` | 宏观经济 |
| `inflation` / `CPI` | 通胀 |
| `fiscal-policy` | 财政政策 |
| `geopolitics` | 地缘政治 |
| `sanctions` / `financial-sanctions` | 制裁 |
| `energy` | 能源 |
| `china` | 中国 |
| `hong-kong` | 香港 |
| `central-enterprise` | 央企 |
| `japan` | 日本 |
| `Abenomics` | 安倍经济学 |
| `carry-trade` | 日元套利交易 |
| `eurozone` / `european-union` | 欧元区 |
| `european-monetary-system` / `ems` | 欧洲货币体系 |
| `usa` | 美国 |
| `korea` | 韩国 |
| `emerging-markets` | 新兴市场 |
| `singapore` | 新加坡 |
| `kospi` | KOSPI |
| `asia` | 亚洲 |
| `swf` / `sovereign-wealth` | 主权基金 |
| `hedge-fund` | 对冲基金 |
| `dynamic-hedging` | 动态对冲 |
| `capital-return` | 资本回报 |
| `statistics` / `empirical` | 数据 |
| `soros` / `george-soros` | 索罗斯 |
| `insurance` | 保险 |
| `finance` | 金融 |

## Migration Guide 迁移指南

> **执行状态**:首批(第 1-3 项)+ 第 4 项超限裁剪已于 2026-08-06 完成——278 页,移除 type 222 页次、中英归并 377 页次、年份 19 页次、超限页 82→0。剩余:第 5 项单次专属标签(非超限页上的 ~590 个,本次未逐页处理)、第三批 type 全聚焦 Domain。

**首批(低风险,机械)✅ 已完成:**

1. **移除 tags 中的 type 类标签**(由 `type:` 字段承担):`concept`、`entity`、`term`、`event`、`person`、`source`、`index`、`question`、`meta`、`synthesis`、`stub`、`method`、`statistics`、`data`。
2. **中英同义归并**:按上表 Aliases 替换为 canonical(如 `finance`→`金融`、`fed`→`美联储`、`monetary-policy`→`货币政策`)。**finance 决策(2026-08-06)**:已并入 `金融`,全库一致;`finance` 与 `金融` 均为 canonical(互为别名)。
3. **纯年份标签并入语义标签或移除**:`2008`→`金融危机`(具体页面并入 `2008全球金融危机` 语义)、`1992`→`1992欧洲货币危机`、`1997`→`亚洲金融危机`、`1998`→`1998香港金融保卫战`、`2020`→`2020年3月流动性危机`、`2021`/`2023`/`2010`/`2012`/`1979`/`1995`/`1999`/`1960`/`1944` 等并入对应事件标签或移除。

**第二批(中风险,需逐页判断):**

4. **超 5 标签裁剪**:82 页超过上限,裁剪规则——保留 2-3 个 Domain + 至多 1 个来源/人物标签 + 至多 1 个横切标签,移除 type 与年份。✅ **已执行(2026-08-06)**:超限页 82→0。
5. **单次专属标签(590 个)**:多数是事件/机构/人名的页面专属词。规则——跨页复用 ≥2 次才保留为标签;否则并入最接近的 canonical,或移除(该信息由页面标题与 wikilink 承担)。**不逐条上表**。⏳ **待执行**:本次仅处理了超限页内的单次词;非超限页上的单次标签仍在,下次审计可批量移除复用<2 者。

**第三批(结构化,待决策):**

6. `type:` 字段 vs tags 的长期关系:当前 524 概念/382 实体等已由 `type:` 承担,建议 tags 完全聚焦 Domain,最终 100% 移除 type 类 tag。

## Reserved System Tags

- `visibility/public` — 显式公开(默认,同无标签)
- `visibility/internal` — 仅团队
- `visibility/pii` — 敏感数据

`visibility/` 标签不计数、不参与 Domain 别名映射、每页至多一个;内容明确公开时省略即可。
