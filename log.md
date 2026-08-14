---
type: meta
title: "Operation Log"
updated: 2026-08-05
tags:
 - meta
 - log
status: evergreen
related:
- "[[index]]"
- "[[hot]]"
- "[[overview]]"
---

# Operation Log

Navigation: [[index]] | [[hot]] | [[overview]]

Append-only. New entries go at the TOP. Never edit past entries.

Entry format: `## [YYYY-MM-DD] operation | Title`

Parse recent entries: `grep "^## \[" wiki/log.md | head -10`

---

## [2026-08-12] CROSS_LINK | 补链 1946 处提及（679 页）

- [2026-08-12T14:00:00+0800] CROSS_LINK pages_scanned=1064 links_added=1946 typed_relations_written=1946 pages_modified=679 orphans_remaining=3 misc_affinity_updated=0 promotion_candidates=0
- 基于 1064 页登记表（含 41 redirect 存根）、4076 候选（EXTRACTED 2610 / INFERRED 1466），fence 配对跳过代码块，表格内插入不破坏结构。
- 679 页写入 relationships frontmatter（1946 条关系，target 用完整路径 wikilink 无 .md 后缀，库惯例一致）；高频目标：中国/美国/日本/资产购买计划/IMF/黄金/欧元/OMT/美联储。
- 0 死链；3 个孤儿页剩余（journal/2026-08-12、concepts/Wiki Map.canvas、references/transport-fallback，均属可接受类型）。

## [2026-08-12] QUERY | 日本政治民粹化

- [2026-08-12T00:00:00+0800] QUERY query="日本政治民粹化" result_pages=7 mode=normal escalated=false
- 核心答案来自 08-11 研究集群：安倍经济学「修辞民粹、内容反民粹」（[[安倍经济学的政治属性评价]] / [[经济民粹主义]] / [[选举周期理论]]）

## [2026-08-12] DEDUP | 合并 42 对重复页（41 次级页转 redirect 存根）

- [2026-08-12T13:00:00+0800] DEDUP mode=merge pages_scanned=1063 pairs_found=1014 merged=42 kept_separate=304 needs_review=1 wikilinks_rewritten=246
- 扫描 1063 页、1014 候选对（HIGH 61 / MEDIUM 286 / LOW 667 跳过），人工判定后推荐合并 42、保留 304、待审 1（开正门堵偏门，语境不同：地方债务 vs 资本管制）。
- 41 个次级页转为 redirect 存根（保留 type/title/address/created，status=merged，redirects_to=canonical）：次级制裁→二级制裁、卖空机制→做空机制、2008金融危机→2008全球金融危机、亚洲金融危机→1997亚洲金融危机、ECB→欧洲央行、ESM→欧洲稳定机制、KOSPI 三方→韩国综合指数(KOSPI)、港股三方→comparisons/港股vs美股vsA股 等。
- 内容合并进 canonical（aliases/tags 去重、updated=now、正文整合去重）；vault 全域 wikilink 重写 [[secondary]]→[[canonical]]（245 文件脚本 + 1 手动修复 ECB 引用），fence 配对跳过代码块。
- 同步更新 index.md（1 条）、.manifest.json（total_pages 1068→1027、39 sources 加 merged_into）、hot.md（Last Updated）。

## [2026-08-11] WIKI_SYNTHESIZE | 第七轮:5 个交叉合成页落地(2008×欧债/美联储×欧债/QE×2020/扩表×财政货币化/ECB×中国央行)

- [2026-08-11T10:27:04+0800] WIKI_SYNTHESIZE pages_scanned=1052 synthesis_created=5 candidates_skipped=64
- 候选来源: wiki-lint 2026-08-11 缺口分析(top-15 高频概念对, 别名合并后 64 对未覆盖); 排除与既有合成页重复的对——扩表×欧债(40 共现但内容含于 ECB×欧债+扩表×ECB)、量化宽松×化债(27, 含于 QE×中国央行+化债×财政货币化)、美联储×中国央行(29, 已有 comparisons/美联储vs中国央行)、IMF×欧债(27, 含于 ECB×IMF)
- Pages (共现页数):
  - synthesis/2008全球金融危机 × 欧元区主权债务危机.md (c-001162, 32 页): 同一场危机两个阶段——欧洲银行持有美国有毒资产→救银行→主权受损→Doom Loop; 分水岭=有无统一财政部, Doom Loop 只在欧洲成立; 一年半潜伏期=2008 雷曼到 2010 希腊之间隔着一次财政扩张
  - synthesis/美联储 × 欧元区主权债务危机.md (c-001163, 26 页): 隐形第三救援方——QE2 触发器=欧债危机(扩表页里程碑表), QE3 开放式承诺与 OMT 同期共振贡献利差腰斩(ECB×欧债最强反驳自认), 美元互换 2010 重启 C5 恰逢希腊第一轮救助
  - synthesis/量化宽松 × 2020年3月流动性危机.md (c-001164, 29 页): QE 制度史完成时刻——「无限」非 2020 发明(QE3 已开放式), 新的是「无限×全部资产」+QE 从最后手段变第一反应(两周走完 2008 半年路程); 剂量 4.8 万亿=2008-2014 两倍, 副作用迟到 18 个月
  - synthesis/扩表与缩表 × 财政货币化.md (c-001165, 27 页): 红线是法律形式的(二级 vs 一级)——两者扩表主体/资金来源/M2 全同(财政货币化页 5.1); 日本 YCC 持有 50% 国债最接近货币化, 2020 与财政同频最模糊, 4.2 危机例外条款是唯一合法突破通道
  - synthesis/欧洲央行 × 中国央行.md (c-001166, 24 页): 两个「不能用国债」的央行——ECB 被马约禁货币融资、中国被人行法 23 条禁直接认购; 替代通道方向相反(ECB 往银行表注水/中国绕开央行表), 共同底色=银行主导传导; 扩表工具形态是财政结构的函数
- Backlinks added to 9 anchors: 2008全球金融危机(1), 欧元区主权债务危机(2: ×2008, ×美联储), 美联储(1), 量化宽松(1), 2020年3月流动性危机(1), 扩表与缩表(1), 财政货币化(1), 欧洲央行(1), 中国央行(1)
- 地址计数器: 1162→1167
- Skipped (下轮候选): 量化宽松×化债(27), IMF×欧债(27), 美联储×2020(28), 2008×影子银行(25), 扩表×欧债(40), 美联储×中国央行(29), 量化宽松×财政货币化(23), 化债×IMF(22), 2008×中国央行(24), 欧洲央行×2020(20) 等 64 对
- 待解问题浮出: 中国央行国债买卖/买断式逆回购与「不直接买债」红线的实际位置; 「无限」承诺在 2022 QT 后是否仍有心理效力; 美联储「隐形第三救援方」角色在 2026 意大利场景是否显性化; Doom Loop 在 SSM 建成后是否真断裂; 扩表工具形态=财政结构函数对新兴市场央行的借鉴

## [2026-08-11] LINT | 全库健康审计（报告模式）


- [2026-08-11T09:31:19+0800] LINT scanned=1046 orphans=1 broken_links=10 stale=23 contradictions=0 prov_issues=0 missing_summary=937 fragmented_clusters=20 visibility_issues=0 promotion_candidates=0 synthesis_gaps=64 relationship_issues=1 lifecycle_issues=1046 trust_ledger=missing fm_gaps=3 addr_dups=4 index_missing=5
- 断链 5 目标/10 处：真内容断链 1 处 `concepts/2026-07 美日联合干预日元.md:38` → [[高市早苗]]（entities/ 无此页）；余 9 处为 log.md(5) 与 meta/ 历史会话报告(4)（Claude Obsidian/Rankenstein/Karpathy LLM Wiki Pattern/E-commerce SEO），按既有约定不改历史条目
- 孤儿 1（全路径/别名感知判定）：`concepts/2026-07 美日联合干预日元.md` 零入链；sources/×5 与 questions/什么是财政货币化 为扫描器 stem-only 误报（经 sources/ 全路径形式已被引用，非真孤儿）
- 地址重复 4 对（8 文件）：c-001145/147/148/149 被 08-10 新增页（sources/环球时报、sources/北京商报、entities/片山皋月、concepts/2026-07 美日联合干预日元）与 08-07 synthesis 页共用；address-counter=1157，08-10 ingest 取号落后于计数器
- FM gaps 3：entities/Manu、entities/五神、entities/庄炳昌 均为 `tags: []` 空标签（Manu/五神 前有孤立 `---` 空行但解析正常，非双 frontmatter）
- stale 23（>90d）：全为 2026-04 claude-obsidian 模板种子页（status mature/evergreen，内容稳定，无 verified 高险）
- summary 937/969 缺（96.7%，vault 约定不写该字段，软警告）；summary>200 字符 0
- lifecycle/base_confidence：0/1046 页有（schema 未落地，待用户决策）；`obsidian-wiki trust-check --strict` fail: ledger_missing（_meta/trust-ledger.json 不存在）
- relationships 1：`entities/石油美元体系.md` 畸形块（裸字符串 `- 'target: "[[sources/2026-06-02-石油美元体系]]'`，缺 type，引号未闭合）；journal/digest-2026-08-06.md 同型（journal 范围外）
- 碎片化聚类 20（n≥5 且 cohesion<0.15）：知识管理 0.051/30 页、宏观经济 0.058/76、中国 0.060/80、金融学 0.062/46、数据 0.067/6、私募股权 0.077/14、金融 0.080/91、地缘政治 0.092/95、流动性 0.095/22、货币政策 0.104/102 等
- synthesis gaps 64（top-15 高频概念对，别名合并后）：扩表与缩表×欧债危机 40、量化宽松×欧债危机 33、2008全球金融危机×欧债危机 32、量化宽松×2020年3月流动性危机 29、美联储×中国央行 29、美联储×2020年3月流动性危机 28、量化宽松×化债 27、扩表与缩表×财政货币化 27、IMF×欧债危机 27、美联储×欧债危机 26…
- 矛盾 0（3 内容页含 ^[ambiguous] 标记：马来西亚模式/化债×ECB/扩表与缩表×化债——单点不确定性，非跨页矛盾）；provenance 0（库无 provenance 块）；visibility 0（0 页 visibility 标签、PII 模式 0 命中）；promotion 0（无 misc/）
- index.md：链接 0 断；08-10 新增 5 页未收录（concepts/2026-07 美日联合干预日元、entities/片山皋月、sources/2026-08-03-经济热点问答、sources/2026-08-03-美日联手干预日元-环球时报、sources/2026-08-04-干预汇市美日联手救日元-北京商报）；frontmatter 有重复 [[_index]] 条目（外观问题）

## [2026-08-10] LINT | 全库健康审计（报告模式）

- [2026-08-10T17:35:28+0800] LINT scanned=1046 orphans=6 broken_links=16 stale=15 contradictions=0 prov_issues=0 missing_summary=1013 fragmented_clusters=15 visibility_issues=0 promotion_candidates=0 synthesis_gaps=7 relationship_issues=0 lifecycle_issues=1046 trust_ledger=missing
- 断链 16 处/6 页:
  - 空格 near-miss 11 处: log.md(5), meta/lint-report-2026-08-03.md(3), meta/lint-report-2026-08-04.md(3) → [[1992 欧洲货币危机]]/[[1997 亚洲金融危机]]/[[1998 香港金融保卫战]] 实际文件名无空格（08-06 已修内容页，log/meta 历史条目残留）
  - 真缺失 1 处: concepts/2026-07 美日联合干预日元.md → [[高市早苗]]（entities/ 无此页）
  - meta/ 会话 frontmatter related 失效 4 处: meta/2026-04-10-backlink-empire-session.md([[Claude Obsidian]]/[[Rankenstein]]/[[Karpathy LLM Wiki Pattern]]), meta/2026-04-14-claude-seo-v190-session.md([[E-commerce SEO]])
- 孤立页 6: concepts/2026-07 美日联合干预日元.md, folds/fold-k3-...n8.md, meta/2026-04-10-backlink-empire-session.md, meta/lint-report-2026-08-04.md, meta/retrieval-benchmark-v1.7.md, meta/tiling-report-2026-04-24.md
- trust-check 硬错误: `obsidian-wiki trust-check` status=fail, errors=[ledger_missing] —— _meta/trust-ledger.json 不存在（strict 与普通模式均 fail）
- lifecycle/base_confidence: 全库 0/1046 页有（schema 未落地，08-06 元数据补全只补了 address/created/updated）
- summary: 33/1046 有 (3%)，历史遗留
- stale: 15 页全为 meta/index/系统页（无 verified 高险）
- synthesis gaps 7: IMF×巴塞尔协议III(11), 美元霸权×欧元区主权债务危机(6), 美元霸权×巴塞尔协议III(6), 量化宽松×美元霸权(5), 扩表与缩表×美元霸权(3), 化债×巴塞尔协议III(3), 财政货币化×巴塞尔协议III(3)
- visibility: 17 处疑似 PII 抽查全部误报（匹配到 token usage/cost 等词，非密钥）

## [2026-08-07] WIKI_SYNTHESIZE | 第六轮:5 个交叉合成页(量化宽松×中国央行/化债×欧债/美联储×扩表与缩表/量化宽松×ECB/ECB×IMF)

- [2026-08-07T16:45:00+0800] WIKI_SYNTHESIZE pages_scanned=1041 synthesis_created=5 candidates_skipped=0
- 候选来源: 第五轮 Skipped 的 5 个候选对(量化宽松×中国央行, 化债×欧元区主权债务危机, 美联储×扩表与缩表, 量化宽松×ECB, ECB×IMF), 共现度复测全部确认 (27/25/52/25/26)
- Pages (共现页数):
  - synthesis/量化宽松 × 中国央行.md (c-001152, 27 页共现): 类 QE 同源异种——中国宽松刻意绕开央行资产负债表, MLF/PSL/买断式逆回购是"央行购债"红线的平行通道; 表克制≠不宽松(降准改乘数不动表), 化债把类 QE 推到实战(7.5万亿银行购债+3万亿冻结)
  - synthesis/化债 × 欧元区主权债务危机.md (c-001153, 25 页共现): 欧洲硬出清 vs 中国软腾挪——分水岭=债务人是否握有印钞权(希腊减记53% vs 12万亿置换不违约); 借债-还债错配方向相反, 制度补丁(EFSF/ESM/OMT vs 特殊再融资/专项债/PSL)对照
  - synthesis/美联储 × 扩表与缩表.md (c-001154, 52 页共现): 扩表与缩表页本质是"美联储操作手册"——QE/QT 每一条机制都来自美联储经验; "降息+缩表"罕见组合揭示利率与资产负债表是两根独立操纵杆, 2026 沃什任内正处此组合门口
  - synthesis/量化宽松 × ECB.md (c-001155, 25 页共现): ECB 是 QE 谱系的"迟到者与变形者"——APP 按 Capital Key 分配+流动性中性, PEPP 突破 Capital Key 是"戴手铐的舞蹈"的巅峰(引发德国宪法法院争议); 负利率是 QE 被捆住时的替代解
  - synthesis/ECB × IMF.md (c-001156, 26 页共现): 全球安全网 vs 货币联盟自救——欧债危机中 IMF 是配角(850/780亿欧元), ECB 是主角(OMT"以承诺灭火"); 拉加德(IMF 总裁→ECB 行长)是两机构"人肉桥梁", 欧洲精英同源=IMF 总裁传统与 ECB 的双支柱话语权
- Backlinks added to 8 anchors: 量化宽松(2: ×中国央行, ×ECB), 中国央行(1: ×量化宽松), 化债(1: ×欧债), 欧元区主权债务危机(1: ×化债), 美联储(1: ×扩表与缩表), 扩表与缩表(1: ×美联储), ECB(2: ×量化宽松, ×IMF), IMF(1: ×ECB)
- 地址计数器: 1151→1156
- Skipped: 本轮无跳过, 第五轮遗留候选对已全部完成
- 待解问题浮出: 买断式逆回购是否构成中国实质 QE; 银行承接 7.5 万亿化债债是否重演欧元区 doom loop; 沃什"降息+缩表"是否重演 2019 QT1 回购危机剧本; PEPP 突破 Capital Key 是"危机例外"还是"永久先例"; 格奥尔基耶娃后 IMF 总裁"欧洲传统"是否被新兴市场配额改革打破

## [2026-08-07] LAYOUT_ADJUSTMENT | 整套自定义外观（克制知识工作台·浅色）首版

- [2026-08-07T16:42:00+0800] LAYOUT_ADJUSTMENT snippets_created=4 enabled=4 mode=light tone=克制知识工作台 checkpoint=snippet-archive/baseline-20260807-1640.md
- 目标: 以 Velocity 2.2.1 light 为基底，整套分层 CSS（token/app-frame/note-surface/sidebar），全部引用主题变量、不硬编码。
- 内容: tab 条 active accent 下划线、正文 tabular-nums、标题层级、内部链接 hover 下划线、文件浏览器 active 行 accent 淡底、状态栏融入 frame。
- 验证: 本环境截图读取不可用，待用户在 Obsidian 刷新后目视验收。

## [2026-08-07] WIKI_SYNTHESIZE | 第五轮:5 个交叉合成页(ECB×欧元/2008×2020流动性/2020流动性×扩表/欧债×马约/巴III×影子银行)

- [2026-08-07T16:28:00+0800] WIKI_SYNTHESIZE pages_scanned=1036 synthesis_created=5 candidates_skipped=5
- 候选来源: 高相关主题对(欧洲货币联盟主线 × 危机主线 × 监管主线, 跨 entities/concepts 层)
- Pages:
  - synthesis/ECB × 欧元.md (c-001147): 欧元与 ECB 互为存在理由——无统一财政/政府的货币靠跨国央行当"锚"; 欧元先以电子形式诞生三年才物质化, 纸币统一而硬币保留国别面, 单一利率面对 19 个不同周期
  - synthesis/2008全球金融危机 × 2020年3月流动性危机.md (c-001148): 相隔 12 年同一套危机剧本的重演与变异——同是美元融资冻结、美联储救市, 但 2008 内生偿付危机 vs 2020 外生流动性危机; 银行从主角变缓冲器, 风险主角换成影子银行
  - synthesis/2020年3月流动性危机 × 扩表与缩表.md (c-001149): 2020 年 3 月是扩表叙事的极端样本——两周从常规工具跳到无限 QE, 资产负债表 4.2万亿→7.2万亿三个月, 扩表首次越界买公司债/市政债; 为 2022 激进缩表与 2021-22 通胀埋下伏笔
  - synthesis/欧元区主权债务危机 × 马斯特里赫特条约.md (c-001150): 马约设计了红线(3% 赤字/60% 债务)却没设计执行——货币统一而财政分立, 借债成本被德国信誉压低、财政纪律无人看守; 救助史(EFSF/ESM/OMT)是在给马约打补丁, 不救助条款被事实救助改写
  - synthesis/巴塞尔协议III × 影子银行.md (c-001151): 巴III 提高银行资本/流动性要求推高表内监管成本, 把信贷活动挤出到影子银行体系; 监管与套利猫鼠游戏在两场危机间闭环——2008 的影子银行角色催生巴III, 巴III 又让 2020 风险主角换成货币基金与对冲基金
- Backlinks added to 9 anchors: ECB(1: ×欧元), 欧元(1: ×ECB), 扩表与缩表(1: ×2020流动性), 2020年3月流动性危机(2: ×2008, ×扩表与缩表), 2008全球金融危机(1: ×2020流动性), 欧元区主权债务危机(1: ×马约), 马斯特里赫特条约(1: ×欧债), 巴塞尔协议III(1: ×影子银行), 影子银行(1: ×巴III)
- 地址计数器: 1146→1151
- Skipped (第四轮遗留, consider next time): 量化宽松×中国央行(18), 化债×欧元区主权债务危机, 美联储×扩表与缩表, 量化宽松×ECB, ECB×IMF (共现 15-20 页区间)
- 待解问题浮出: 欧元"表象统一"(纸币统一/硬币国别面/财政分立)是否削弱货币锚; 2008 vs 2020 风险主角切换(银行→影子银行)对宏观审慎框架的挑战; 巴III 监管套利是否必然推高非银杠杆; 马约"红线无执行力"的制度教训对中国化债的镜鉴

## [2026-08-07] WIKI_SYNTHESIZE | 第四轮:5 个交叉合成页(美联储/ECB/化债 × 2008/财政货币化/中国央行)

- [2026-08-07T16:30:00+0800] WIKI_SYNTHESIZE pages_scanned=1026 synthesis_created=5 candidates_skipped=5
- 候选来源: 2026-08-07 第三轮跳过的 next-5 候选对,共现度复测全部确认 (美联储×ECB=32, ECB×2008全球金融危机=32, 化债×财政货币化=27, 化债×中国央行=26, 美联储×化债=25)
- Pages (共现页数):
  - synthesis/美联储 × ECB.md (c-001145, 32 页共现): 主权央行 vs 超主权央行——美联储印钞无限但授权国内, ECB 救市被 Capital Key 国别结构锁死; OMT"以承诺灭火"是扩表不可行时的替代品, 负利率是 QE 被捆住时的替代解
  - synthesis/ECB × 2008全球金融危机.md (c-001141, 32 页共现): 2008 以三种身份落在 ECB 身上——美元荒承接者(求援者非救援者)、错读银行危机的旁观者、被主权危机重铸的当事人; 美元互换线揭示"单一货币区央行救不了货币区外资产"
  - synthesis/化债 × 财政货币化.md (c-001142, 27 页共现): 债务消化光谱两端——央行直接印钞(创造货币) vs 银行购债+央行对冲(转移货币); 化债把资产负债表压力从央行表搬到银行表, 央行"不买债"红线是共同锚
  - synthesis/化债 × 中国央行.md (c-001143, 26 页共现): 化债是中国央行结构主义货币哲学实战——准备金率改乘数、PSL/再贷款定向投放, 角色是"流动性调度员"而非"最后买家"; 结构性工具 ~6万亿 vs 化债 12万亿+ 的缺口由银行垫付
  - synthesis/美联储 × 化债.md (c-001144, 25 页共现): 债务消化两套会计——美联储把债放央行表($0.9→$9万亿+QT退出), 化债把债放银行表(12万亿置换+下半场延续); 央行不买一级市场债的红线相同、绕法不同
- Backlinks added to 7 anchors: 美联储(2: ×ECB, ×化债), ECB(2: ×美联储, ×2008), 化债(3: ×财政货币化, ×中国央行, ×美联储), 财政货币化(1: ×化债), 中国央行(1: ×化债), 2008全球金融危机(1: ×ECB)
- 地址计数器: 1140→1146 (美联储×ECB 原分配 c-001140 与 concepts/马来西亚模式 冲突, 改分配 c-001145)
- Skipped (consider next time, 共现页数): 量化宽松×中国央行(18), 化债×欧元区主权债务危机, 美联储×扩表与缩表, 量化宽松×ECB, ECB×IMF (共现 15-20 页区间)
- 待解问题浮出: 化债"准财政货币化"质疑(降准+买断式逆回购是否事实越线)、ECB 若建成财政联盟是否趋同美联储、中国银行购债期限错配 vs QT 的 SVB 教训、IMF SDR 转借机制落点(延续第三轮)
- 注: 本轮为 cross-linker 之后运行, log/hot 同步无冲突

---

## [2026-08-07] cross-link | 孤儿页入链 + taxonomy 引用修复

- [2026-08-07T15:20:00+0800] CROSS_LINK pages_scanned=1026 links_added=2 typed_relations_written=2 pages_modified=3 orphans_remaining=5 misc_affinity_updated=0 promotion_candidates=0
- 孤儿 7→5（实测入链后仅 7 个真孤儿，其中 6 个为 meta/folds/报告可接受孤儿）。修复真实内容孤儿：entities/石油美元体系 补源素材入链 [[sources/2026-06-02-石油美元体系]]（derived_from），该 source 页出链 31 条双向闭环；journal/digest-2026-08-06 补 taxonomy 引用 [[_meta/taxonomy]]（uses），并同步 _raw 已清空状态（2026-08-05-wiki-lint-health-baseline.md 已归档）。
- 剩余孤儿 5 个均为 meta/fold 类（backlink-empire-session / lint-report-2026-08-04 / tiling-report-2026-04-24 / retrieval-benchmark-v1.7 / fold-k3），可接受。
- 断链复检：知识页 0 新增断链；log.md 与 meta/lint-report 历史条目 13 处旧链接按规则保留。
- Pre-write snapshot: 5551730 (git commit "pre-cross-linker snapshot")

---

## [2026-08-06] digest | 周报：近 7 天知识活动摘要

- [2026-08-06T18:00:00+0800] DIGEST period="7d" new_pages=65 updated_pages=146 themes=货币政策,中国,日本,资本管制/对外开放,地缘政治 connections=12 saved=true path=journal/digest-2026-08-06.md
- 核心产出：synthesis/ 从 0 到 10 页（两轮 wiki-synthesize）；日本制度演进主线补全（日本95年体制→桥本行政改革→厚生劳动省→安倍经济学）；Rentenmark 兑换比率纠错（1 Rentenmark=10¹² 旧马克）。
- 迁移说明：期间（08-05）vault 经历 git 迁移 + 190 stub 批量补全，部分页 created/updated 日期反映重建后状态。

---

## [2026-08-05] stub-completion | 分批补全全部真实知识 stub

- Summary: 全库 stub 清理与补全。删除断链修复占位页（含 `.canvas` 占位 3 处），合并同名/重复变体并修复引用；随后分 4 批并行补全 **190 个真实知识 stub**（国际宏观 14、衍生品 14、政策产业 14、机构人物 14、欧洲转型 14、地缘贸易 14、技术投资 14、金融机构 13、宏观制度 13、微观产业 13、source 页若干），统一升级至 `status: current`，行数达标（100–185 行）。
- 验证结果：知识页断链 0（余下 `meta/` 历史报告与 `log.md` 历史条目 24 处按规则不改）；剩余 stub 仅 3 个 canvas 占位（非知识页）；孤儿页 5 个中 3 个 MOC `_index` + 1 个历史 fold 均为系统结构页；`concepts/E-commerce SEO.md`（主题不符的无关页，c-000053）已删除。
- Address 覆盖：c-0003xx ~ c-0009xx 段补全；`entities/央行.md`（c-000626）、`entities/托普利亚.md`（c-000657）等实体页重建至 100+ 行。



- Summary: 清除全库 3 个空目录：`sessions/`、`synthesis/sessions/`、`topics/`。均未被 git 跟踪、无配置/脚本/文档引用（grep 命中仅为 prose），为迁移遗留空壳。复查后全库无空目录残留。

---

## [2026-08-05] LINT_FIX | 全库 lint 修复落地（断链/重复页/孤儿）

- Summary: 对上次审计的三大类真实问题完成修复。**断链**（49→1）：修复知识页真实断链 5 处（沃尔克规则 [[2023年SVB危机]]、德国马克 [[LudwigErhard]]、凯恩斯主义 有效需求 转纯文本、共建"一带一路"→[[共建一带一路]] ×4）；删除 entities 金融稳定/银行监管/风险加权资产 中引用已删历史 lint 报告（2026-05-21/06-24）的维护注释 6 行；_index 三导航页 Entities/Sources/Concepts 占位改显式路径链接；sources 9 页 frontmatter/正文 raw/wechat 断链 18 处转纯路径文本；meta/backlink-empire related 删 Claude Canvas。排除假阳性 2（反引号内的 Wiki链接/raw/zhihu 引用，非真实链接）。唯一保留：log.md 的 `[[美元收割全球的机制]]` 历史 stub 删除记录（append-only 不改）。
- Duplicates (8→0): 删除 8 个 entities stub（量化宽松/财政货币化/巴塞尔协议/最后贷款人/美元霸权/利率市场化/中储粮/美元周期），concepts 完整版保留。巴塞尔协议 concepts 完整版文件名为 [[巴塞尔协议III]]，先在其 aliases 补 "巴塞尔协议" 确保 29 处 [[巴塞尔协议III]] 引用不断链。
- Orphans (33→8): 3 个真实知识岛已加反向链接——[[entities/石油美元体系|石油美元体系]]（←美元霸权/去美元化，显式路径消除与 sources 版同名歧义）、[[sources/2026-06-02-冲销式干预|冲销式干预]]（←concepts/冲销式干预 Basic Information 来源字段）、[[questions/什么是财政货币化|财政货币化（问答）]]（←concepts/财政货币化 相关条目）。剩余 8 个孤儿为 meta 历史快照（4）/folds 存档（1）/_index 导航占位（3），非知识内容，保持原样。
- Re-check: broken_links=1（仅 log 历史遗留） orphans=8（仅 meta/folds/_index） duplicates=0

---

## [2026-08-05] GRAPH_COLORIZE | 图谱着色重跑（Obsidian 清空后恢复）

- Summary: 首次着色被 Obsidian 打开时清空 colorGroups 后重跑。同 by-tag 模式，Top 10 标签（stub/concept/entity/finance/term/meta/房地产/中国/china/日本）映射 10 色板，仅替换 colorGroups 字段。
- Backup: `.obsidian/graph.json.backup-20260805-1324`
- 提醒：若 Obsidian 正打开，关闭后重开或立即 Cmd/Ctrl+R 刷新，避免关闭时再次覆盖。

---

## [2026-08-05] GRAPH_COLORIZE | 图谱按标签着色

- Summary: 按 by-tag 模式为图谱着色，取 Top 10 标签（stub/concept/entity/finance/term/meta/房地产/中国/china/日本）分别映射 10 色板（蓝橙红青绿黄紫粉棕灰）。只替换 graph.json 的 colorGroups 字段，保留缩放/力导向/过滤器等偏好设置。无 visibility/* 保留标签，槽位 9 已被真实标签占用，故不加 untagged 兜底。
- Backup: `.obsidian/graph.json.backup-20260805-1321`

---

## [2026-08-05] LINT | 全库健康审计

- Summary: 对 1052 页全库运行 wiki-lint。legacy 格式确认：本库用 `status:`（stub/current/developing/evergreen 等）而非 llm-wiki 的 `lifecycle:`/`base_confidence:`/`summary:`，故 12a/12b/3a 不适用（0 硬错误）。真实发现：孤儿 33、断链 49（知识页 5）、stub 237、重复页 8 对、碎片化标签簇 14、synthesis gaps（化债×扩表与缩表 42 页共现）。
- Orphans: 33（25 个 entities 知识岛 + 5 个 meta/folds + 3 个 _index 导航页）
- Broken links: 49（真正知识页 5 处；其余为 meta/lint-report 历史报告与 _index 的常规占位）
- Stub pages: 237（concepts 161 / entities 73 / sources 3）
- Duplicates: 8 对（concepts 完整版 vs entities stub：量化宽松/财政货币化/巴塞尔协议/最后贷款人/美元霸权/利率市场化/中储粮/美元周期）
- Stale >90d: 41（多为 2026-04 legacy 框架文档）
- lifecycle_issues=0 relationship_issues=0 visibility_issues=0

---

## [2026-08-05] ingest | raw/ 素材蒸馏与注册

- Summary: 处理源知识库 `raw/` 全部 **58 个文件**。核对结论：raw/ 文本素材几乎已全部被源 wiki 蒸馏至现有 source 页（文件名 1:1 匹配 12 篇；军工航空拆解已蒸馏至 `concepts/军工航空产业`；44 张图片为其冗余截图）。唯一真实缺口为《香港金融保卫战：罗斯狙击英国泰国，决战香港》（B站巫师财经字幕，2019-11-25）。
- Distilled: **1 个新 source 页** `sources/2019-11-25-香港金融保卫战-巫师财经`（地址 c-001100）— 索罗斯 1992/1997/1998 三场战役机制，补充利率期货多头埋伏、"任一招"被利用、8月28日每5分钟均价结算机制、索罗斯战损核实（<20亿美元）、朱镕基承诺核实、港府为何只拉到7851点。
- Registered: raw/ 全部 58 文件写入 `.manifest.json`（sha256 + pages_produced 映射），manifest 总计 1109 个源。新页已入 `index.md` Sources；`concepts/1998香港金融保卫战` 相关条目补反向链接。
- Address counter: 1100 → 1101

---

## [2026-08-05] setup | 全库迁移至 金融WIKI 新 vault

- Summary: 将源知识库 `obsidian-sync` repo 的 `wiki/` 全部 **1051 个页面**迁移至新 vault `/Users/mac/Documents/金融WIKI`，保留完整子目录结构与全部 wikilink。迁移构成：concepts 560 / entities 398 / sources 41 / meta 16 / domains 9 / questions 8 / comparisons 7 / analysis 3 / references 2 / strategies 1 / folds 1。同步复制 `assets/`（384K）与 `.vault-meta/`（地址计数器=1100，新页地址从 c-001100 起延续）。`.manifest.json` 已记录全部 1051 个源文件 sha256（cache-check 确认 unchanged，后续 append 摄入自动跳过）。index/log/hot 采用源版本。待办：raw/ 素材蒸馏。
- Pages migrated: 1051 (全 wiki/ 树)

---

## [2026-08-05] wiki-deepen | 建美元债概念页+恒大全事件关联深化

- Summary: 核对中华网《"万亿"恒大落幕》(2025-08-25) 已入库(source c-001094)后, 检查恒大概念页关联健康度。发现 vault 缺"中资美元债"概念视角(仅有 EM 宏观角度: 美元潮汐/Original Sin)。新建 [[美元债]] (c-001099, current): 定义中资企业境外美元计价债券; 发行动机(成本优势/规避境内约束/币种匹配/历史扩张期); 风险脆弱性=[[Original Sin（原罪）]]币种错配+再融资滚续+交叉违约+无抵押劣后; 核心案例=恒大全事件 190 亿美元境外债重组(2023.04 投票 Class A 77% vs Class C 30%, 境内外债权人四维对比: 抵押/国家背书/政治任务/清盘施压筹码 → 境内"没得选就接受"、境外"不接受靠清盘施压")。同时给 [[恒大全事件]] 详细时间线补验证标记: 2022.08.30 境外债重组方案 190 亿美元标 ◆(=source 页"千亿境外债面临重组"口径, 190亿美元≈千亿人民币)。回填双向链接: [[恒大全事件]]/[[债务重组]]/[[分摊痛苦]] 三页 related+相关概念表补 [[美元债]]。断链复检零死链。index 补录 1 条。
- Pages created: [[美元债]] (concept, c-001099), [[index]]
- Pages updated: [[恒大全事件]] (◆标记+美元债链接), [[债务重组]], [[分摊痛苦]]

---

## [2026-08-05] wiki-ingest | 美日韩同时出手消化

- Summary: 消化任博宏观论道《美日韩同时出手》(2026-08-03, 转载涛动宏观任庄主)。核心事件: 2026.7.30-31 美日韩三国联手干预汇率打击日元韩元空头, 日本抛售高达 **560亿美元** 买入日元(6.29-7.29 未出手), 韩元同步入市, **美国首次实质性参与**(财政部事前通知多家银行+三村淳称"得到超过单纯精神层面支持的支援")。关键数据: 美元兑日元 163.445→157.493(两日日元+3.78%), 50分钟急升 162.80→157.80, 美元指数跌破100(99.78), 韩元两日+1.59%(7月当月+8.81%)。干预动因: 日元年内向170迈进的贬值预期 + 贝森特"日元被显著低估"。**核心洞见**: 干预只能改变节奏、无法改变日元走弱大方向——日本靠卖出美债(持有 11431.4 亿美元, 5月已减 66.75 亿)筹措资金 → 卖债推升美债利率(7.31 2/10/30年 +5/+7/+6BP 至 4.28%/4.75%/5.27%) → 拉大美日利差 → 反噬日元贬值; 唯一有效路径是日元超预期加息但日本克制。韩元"不是问题": 非国际货币+与韩股强关联+市场预期不高。新建 source 页(c-001095), 升级 [[外汇干预有效性]]/[[韩元]]/[[日本外汇储备与日元国际化]], 更新 [[日元套利交易]]/[[日本]]/[[韩国]]/[[美元指数]]/[[美债收益率]], index 补录 3 条。
- Pages created: [[2026-08-03-美日韩同时出手-任博宏观论道]] (source, c-001095), [[index]]
- Pages updated: [[外汇干预有效性]] (seed→developing), [[韩元]] (stub→developing), [[日本外汇储备与日元国际化]] (stub→developing), [[日元套利交易]], [[日本]], [[韩国]], [[美元指数]], [[美债收益率]]

---

## [2026-08-05] wiki-query | 美国旋转门制度概念页新建

- Summary: 用户问"什么是美国的旋转门制度", 库内仅 Mario Draghi 页有 incidental 提及, 无专属页。新建 concept 页 [[美国旋转门制度]]（c-001093, current）。核心: 旋转门=政府公职与私营部门(游说/金融/军工/能源)之间的人员双向流动, 不是正式制度而是美国政商关系结构性特征。两个方向: 政府→私营(离任官员变现人脉/内部信息/监管知识) + 私营→政府(高盛高管→财长, reverse revolving door), 闭环循环。四大批评: 利益冲突/监管俘获(2008危机诱因之一)/信息优势/游说产业(年产值数十亿美元)。法律约束表: 1978政府伦理法(伦理框架) + 18 U.S.C.§207(终身禁止亲自参与事项游说+2年冷却期) + 2007诚实领导与开放政府法(参议员2年/众议员1年) + 总统EO(5年禁令+终身禁止外国游说); 局限=管得住"直接游说"管不住"顾问/高管"。案例: 高盛↔财政部(鲁宾/保尔森/姆努钦)、美联储体系、国防部↔军工、议员↔游说公司。国际对照: 日本"政官财铁三角"([[大藏省]]护送船团) vs 中国公务员离职回避制度。投资含义: 人事任命是监管周期与政策定价的高频信号。反向链接: 写入 related 至 [[美联储]]/[[多德弗兰克法案]]/[[沃尔克规则]]/[[2008全球金融危机]]/[[美元潮汐]]/[[大藏省]]。
- Pages created: [[美国旋转门制度]] (concept, c-001093), [[index]]

---

## [2026-08-05] wiki-query | 恒大全事件 stub 升级为完整概念页

- Summary: 用户 query "恒大"，vault 无专属内容页，[[恒大全事件]] 为 2026-08-04 lint 建的断链占位 stub（c-001087）。综合 [[保交楼]] §八 / [[债务重组]] §三 / [[分摊痛苦]] 债务重组数学 / [[房地产]] 宏观背景 / 万科宝能 .raw 中 2015 恒大股价背景，升级为 current 完整页。核心内容：①时间线 2015（股价+125% 背景）→2021 危机曝光→2022 境外债违约→2023.4 重组投票（Class A 77% 过 / Class C 30% 否）→2024.1 香港高院清盘令；②四大教训（规模太大不能倒/境内外债权人分歧/实控人风险/清盘回收率 0.5%-3%）；③处置数学：接受重组 ~30% vs 清盘 0.5%-3%，"早重组>晚重组>清盘"；④保交楼与重组必须同步。index.md Concepts 补录 4 条：[[恒大全事件]] + 此前遗漏的 [[保交楼]]/[[债务重组]]/[[分摊痛苦]]（status 按 frontmatter 如实标注）。同日追加"三、详细时间线（通用知识参考）"：外部检索受阻（Wikipedia/BBC/AP/Reuters 等被拦截、Bing 本地化过滤、百度/360/搜狗百科空页）后按用户选择，基于公开常识补 2021-2025 五阶段 ~20 节点，页内以 [!warning] callout 明确标注"非 vault 来源、未经引用验证"，标 ★ 节点与 vault 已核验时间线一致。章节重编号为 一~七。
- Pages updated: [[恒大全事件]] (concept stub→current, c-001087), [[index]]

---

## [2026-08-04] wiki-query | 日本安保斗争概念页新建

- Summary: 用户问"什么是日本安保斗争", 库内 grep "安保" 零命中, 政治史板块空白。检索维基百科(中文"安保斗争"+日文"安保闘争")后新建 concept 页 [[日本安保斗争]]（c-001092）。核心: 1959-1960 围绕日美安保条约改定的战后最大国民运动。背景: 1951 旧条约(美军无限期驻留/内乱条款/美不承诺防卫)→岸信介强推改定→1960.1.19 新条约华盛顿签署(删内乱条款/明确共同防卫/事前协商)。时间线: 1958秋警察职务法撤回→1959.3.28 安保改定阻止国民会议(134团体)→1960.5.19 五一九事件(强行延长会期/500警察驱离/深夜口头表决)→6.10 哈格提事件(美军直升机营救)→6.15 640万人总罢工+东大女生桦美智子死亡→6.16 岸信介辞职意向+取消艾森豪威尔访日→6.18 数十万人包围国会→6.19 午夜条约自动生效。结果: 迫使岸信介内阁总辞但未能阻止条约, 60年安保体制确立延续至今; 池田"所得倍增计划"把政治焦点转向经济优先, 全学连分裂催生新左翼, 1970 二次安保抗争(规模小), 2015"15年安保"(安倍)呼应。同步补 lint 遗留: [[安倍经济学]] frontmatter 补 status: current。反向链接: [[安倍经济学]] frontmatter related + 间接相关清单加 [[日本安保斗争]]（岸信介=安倍晋三外祖父）。
- Pages created: [[日本安保斗争]] (concept, c-001092)
- Pages updated: [[安倍经济学]]

---

## [2026-08-04] wiki-query | 金融刺激金融化批判问答归档

- Summary: 用户追问"QQE/YCC/NISA 仅金融刺激是否导致金融化与产业空心化? 期间 CPI/PPI 如何? 会不会过分通胀? 会不会盘剥无资产居民", 归档为 [[日本金融刺激是否导致金融化与盘剥无资产居民]]（c-001085, completed）。核心四答: ①金融化是直接结果(日经+355%/央行资产/GDP 33%→135%/日银持债50%+ETF7%), 产业空心化是旧病被加重(第三支箭没射+资金经日元套利流向海外); ②CPI 2012-2022 平均仅 +0.6%, 2022 靠输入型通胀冲 +4.2%, PPI 因日元贬值暴涨(2022 同比峰值 +9%), 形成 PPI/CPI 剪刀差; ③不是过分通胀而是想通胀不得(LTGR 0.1-0.3%+实际工资-8%压制需求), 2022 通胀是成本推升非需求拉动; ④无资产居民被四重转嫁盘剥——资产通胀+工资停滞的财富再分配、日元贬值打击低收入、消费税 5→8→10% 累退、利率归零剥夺储蓄收益; NISA 是金融化的延续(国民接盘央行)。关联 [[安倍经济学]] / [[新NISA]] / [[日元套利交易]] / [[量化宽松]] / [[日本95年体制]]。
- Pages created: [[日本金融刺激是否导致金融化与盘剥无资产居民]] (question, c-001085)

---

## [2026-08-04] wiki-query | 新NISA概念页新建

- Summary: 用户问"日本的新NISA政策是什么", 库内无 NISA 专属页（仅 [[影子银行]] 一处提及"小额投资者资金汇聚", 与 NISA 无关）, 先以通用知识回答（声明非 vault 来源）, 后按用户确认新建 production 级概念页 [[新NISA]]（c-001084）。核心: 2024.01.01 启动的免税投资账户改革, 岸田"资产所得倍增计划"核心抓手。vs 旧NISA: 制度统一、積立枠 120万→240万/年、终身额度 1800万（成長枠上限 1200万）、非课税期间永久化、取消年龄限制、旧资产继续免税。本质: 终身投资额度永久免征约20.315%所得税/住民税。政策背景: 日本家庭金融资产现金存款占比超50%（美欧10-15%）,"存款立国"难以为继, 用税收优惠撬动"从储蓄到投资"。局限: 只解决税制激励, 不动股市对日元套利的流动性依赖。反向链接建立到 [[日本95年体制]]（frontmatter+3.1货币段注脚+相关页面清单）/ [[安倍经济学]]（frontmatter）。同步修正 [[量化宽松]] 页面两处滞后时间线: QQE+YCC "2013-至今"→"2013-2024.3"、YCC 2.0 "2023.4-至今"→"2023.4-2024.3", 并新增"退出(2024.3.19)"块, 与问答页 [[什么是QQE与YCC的比较]] 时间线对齐。
- Pages created: [[新NISA]] (concept, c-001084)
- Pages updated: [[日本95年体制]] / [[安倍经济学]] / [[量化宽松]]

---

## [2026-08-03] wiki-query | QQE与YCC问答归档

- Summary: 用户连续追问 QQE 系列问题（QEE 为笔误），归档为 [[什么是QQE与YCC的比较]]（c-001083, completed）。覆盖五问：①QQE 定义（量化质化宽松, 2013.04 黑田启动, 国债为主+ETF/J-REITs 为辅, 基础货币2年翻倍目标）；②日银确实直接在二级市场买本国 ETF, 但只是 QQE 一部分且非首创（2010 资产购买计划已有, 更早 2002 买银行持股）, 属 [[央行入市干预]] L2 层（印钞买股, 退出难度极高）；③YCC 比 QQE 激进: 数量承诺→价格承诺（10年期 0% 钉死, 弹药无上限）, 全球唯一长期实践的收益率曲线控制（2016.09-2023.10）；④YCC 0% 的机械后果是挤出私人对 10 年期国债需求（日银持仓峰值超 50%）, 但非政策本意, 且只杀 10 年期段, 20/30/40 年超长端仍有需求；⑤YCC 目的=组合再平衡渠道（逼资金离开零收益国债）, 实际流向四出口: 央行资产负债表/海外 carry trade（最大）/超长端债/日本股市（日银自购为主）, 家庭散户几乎没动。修正用户理解: 被牺牲的是整条 JGB 曲线而非"短期国债", 目标是广义风险资产而非特指股票。关联 [[量化宽松]] / [[安倍经济学]] / [[日元套利交易]] / [[央行入市干预]] / [[货币政策正常化]] / [[日本95年体制]]。
- Pages created: [[什么是QQE与YCC的比较]] (question, c-001083)

---

## [2026-08-03] wiki-lint | 全库健康检查

- Summary: 触发 /wiki-lint,扫描 1019 个文件。产出 [[lint-report-2026-08-03]]（148 行）。**断链 37 目标（过滤后真问题 ~35 处引用）**：HIGH=韩国系重命名断链 13 处（[[2026-07-21-韩国股灾简史]]/[[2026-06-24-韩国需要冷静冷静]] 实际文件带日期前缀）；MEDIUM=空格/命名不匹配 15 处（1997亚洲金融危机/1992欧洲货币危机/1998香港金融保卫战/2001阿根廷违约/2023年SVB危机/研究：美元如何收割新兴市场（增强版））；LOW=导航/历史/大小写 10 处。**孤儿页 22**（14 内容+8 meta，含疑似测试残留 X.md/Foo.md）。**frontmatter 缺口 6**（内容页仅 [[安倍经济学]] 缺 status）。**地址验证 0 错误**（counter peek 1083，最高 c-001082）。**空段落 0**。**语义 tiling 跳过**（ollama 不可达 exit 10）。**index.md 滞后**：死链 1 + 未收录近期新增页（安倍经济学/桥本行政改革/厚生劳动省/日本95年体制/韩国系 5 页等）。清理 find_dead_links.py 误生成的 lint-report-2026-07-14.md（硬编码日期）。**待用户确认自动修复**：补安倍经济学 status、修韩国系 13 处引用、修空格类 15 处引用、index 修复+补录、建 3 个 stub（有效需求/一带一路/美联储点阵图）。
- Pages created: [[lint-report-2026-08-03]] (meta)
- Pages deleted: meta/lint-report-2026-07-14.md (脚本误生成)

## [2026-08-03] wiki | 日本95年体制概念页新建

- Summary: 用户问"日本95年体制",vault 无专属页(碎片散落于桥本行政改革/大藏省/日本银行/日元套利交易/货币政策正常化/安倍经济学),新建 production 级概念页,整合"1995年制度定型→拖延30年→2024年退出"主线。核心命题:1995年是泡沫崩盘后日本"放弃出清、选择拖延"的制度定型之年——阪神大地震(1995.01)+日元79-80历史高位+住专6.4万亿窟窿暴露+大藏省丑闻+利率降至0.5%极限低位(零利率前夜),此后约30年货币/财政/金融监管三大支柱都在该框架内运行,直到1997三连爆倒逼改革、1998央行独立、2001大藏省拆分、2013 QQE续命12年、2024.03.19退出负利率/YCC才终结。含"体制四支柱"表、"结局时间线"表、资产负债表衰退理论辩护、与化债路径对照锚点。反向链接建立到 [[桥本行政改革]] / [[大藏省]] / [[日本银行]] / [[泡沫经济]] 四大相关页。规避一次地址撞号(allocate 首次返回 c-001081 与桥本行政改革冲突,counter 滞后),rebuild 后取 c-001082。
- Pages created: [[日本95年体制]] (c-001082, concepts, 125 行)
- Pages updated: [[桥本行政改革]], [[大藏省]], [[日本银行]], [[泡沫经济]] (related 反向链接), [[index]] (计数 56→57)

## [2026-08-03] wiki | 桥本行政改革概念页新建

- Summary: 用户问"桥本行政改革",vault 无专属页(碎片散落于大藏省/厚生劳动省/日本银行/安倍经济学),新建 production 级概念页,补全"日本制度演进"主线关键环节。
- Pages created: [[桥本行政改革]] (c-001081, concepts, 250+ 行)
- Pages updated with backlinks: [[大藏省]] / [[日本银行]] / [[厚生劳动省]] / [[安倍经济学]] / [[财政政策与货币政策协同]] (5 个相关页)
- Key proposition: 1996-2001年1府22省厅→1府12省厅的大手术,是"护送船团制度"破产后的制度重构——大藏省拆分为财务省+金融厅(监管独立)、1998年日银独立(新日本银行法)、厚生省+劳动省合并为厚生劳动省、金融大爆炸(Big Bang)开放市场。政治上桥本因1997消费税增税惨败下台,制度上却为安倍经济学(独立央行搞QQE)铺平道路。
- Status: current (日本制度演进主线,连接大藏省-央行-厚劳省三角)

## [2026-08-03] wiki | 厚生劳动省实体页新建

- Summary: 用户问"厚生劳动省",vault 无相关内容,新建 production 级实体页。核心定位:日本"花钱最多"的省厅,是财务省(前大藏省)预算博弈的头号对手。
- Pages created: [[厚生劳动省]] (c-001080, entities)
- Pages updated with backlinks: [[大藏省]] / [[安倍经济学]] / [[社会保障]] / [[日本财政扩张担忧]] (4 个相关页)
- Key proposition: 厚生劳动省是安倍经济学"新三支箭"(生育率1.8/女性就业/护理离职零)的执行者——生育率目标惨败(实际1.20 vs 目标1.8),实际工资2012-2022 -8%的官方记录者;社保给付费133万亿日元(占GDP 21%),与财务省构成"收钱vs花钱"结构性博弈
- Data: 2024年度预算35.6万亿日元(占一般会计1/3) / 社保给付费133万亿(占GDP 21%) / GPIF 226万亿日元 / 生育率1.20(2023) / 女性25-44岁就业率79.5%(2022) / 春斗2024涨薪5.28%
- Status: current (日本财政/社保主线实体页)

## [2026-08-03] wiki-query | QF制度总览页新建
- Summary: 用户问"我国的QF制度"，先以通用知识回答，后用户要求用 wiki-query 跑 vault 检索。vault 无 QF 专属页，碎片散落于 三元悖论/港股vs美股vsA股/A股市场结构/人民币国际化/国际收支 等页。合成后新建总览页 [[QF制度]]（c-001071）。
- Pages created: [[QF制度]] (c-001071, concepts)
- Pages updated: [[index]]、[[log]]、[[hot]]
- Key proposition: QF 制度是三元悖论组合1（固定+独立=放弃资本自由）下的通道化开放——不开放资本项目，逐项搭通道、做白名单、配额度；外资进出受限（QFII/陆股通额度管控），外资占 A 股 ~5%、港股 ~40%
- Gaps filed: QFII/QDII/RQFII/债券通/沪港通/深港通/陆股通/跨境理财通 8 个待建 stub 链接；[[港股通]] 已存在但为 stub
- Note: 首次地址分配返回 c-001070 与 [[安倍经济学]] 撞号（counter 滞后），重跑后取 c-001071

## [2026-07-31] wiki | 安倍经济学专题页新建

- Summary: 用户提问"安倍经济学",综合知识库已有日本三十年/广场协议/大藏省/日本银行/货币政策正常化等碎片,新建 production 级专题页 [[安倍经济学]]。
- Pages created: [[安倍经济学]] (c-001070, 450+ 行)
- Pages updated with backlinks: [[日本银行]] / [[货币政策正常化]] / [[日元套利交易]] / [[量化宽松]] / [[资产负债表衰退]] / [[广场协议与G5政策分化]] / [[大藏省]] (7 个相关页建立反向链接)
- Key proposition: 安倍经济学(2012.12-2024.03)用央行"无限火力"给失落的二十年续命12年,**只打破通缩心理、不动结构僵化根本**;死于2022.07安倍遇刺,葬于2024.03退出YCC/负利率
- Data: 日经+355% / 央行资产从158万亿到760万亿日元 / 政府债务/GDP 236%→263% / 实际工资-8% / 生育率1.41→1.20
- Status: current (与"日本通缩三十年"主线深度关联)

## [2026-07-24] wiki | 广场协议G5政策分化与大藏省分析
- Summary: 从用户关于日本消失三十年演进路线、中日经济对比、广场协议G5各国政策差异的连续追问出发，提炼为结构化wiki页面。新建 [[广场协议与G5政策分化]]（五国政策对比总表+各国详细路径+央行独立性对比+核心结论，G5各国政策数据表格），[[大藏省]]（1869-2001年完整历史+五大权力架构+泡沫经济关键决策时间线+与中国财政部八维对比）。补全 [[窗口指导]]、[[日本银行]]、[[自杀式加息]] 对这两个新页面的反向链接。
- Pages created: [[广场协议与G5政策分化]]（c-001061）、[[大藏省]]（c-001062）
- Pages updated: [[窗口指导]]、[[日本银行]]、[[自杀式加息]]、[[index]]
- Key insight: 广场协议本身不是问题，真正致命的是"财政扩张+货币宽松+金融开放+央行不独立"四重叠加；大藏省作为超级部委集财政、货币、监管于一身是日本失去二十年的制度根源

## [2026-07-22] ingest | 韩国股灾简史（任庄主 2026-07-21）
- Summary: 消化梧桐树智库《韩国股灾简史》。核心命题：2025.4 以来韩股（KOSPI）暴涨 291.48% 冲上 9114 点、市值峰值 4.95 万亿美元，本质是外资主导的投机性「虚火」；2026.7 已进入股灾（较高点回撤 28.51%），任庄主预测后续再跌 ~20%、向 4000-5000 点回归。新建 source 页 [[2026-07-21-韩国股灾简史]]、concept 页 [[韩国历史股灾谱系]]（1989/1997/2000/2008/2020/2022 六次股灾 + 2026 进行中，贯穿「外资定价权+半导体放大器+流动性收紧扳机+散户接盘」四大结构）、stub [[韩国折价（Korea Discount）]]。从 stub 升级 [[韩国综合指数(KOSPI)]] 为完整实体页（含历史点位表）。三星电子/SK海力士补 2026 股灾跌幅（-34.85%/-40.94%）。与前作 [[2026-06-24-韩国需要冷静冷静]]（2026-06-24 泡沫顶点前预警）互为「预警→兑现」闭环。

## [2026-07-17] research | 美元潮汐与新兴市场收割机制（深度研究）
- Summary: 深度研究美元如何收割新兴市场，建立完整理论框架。新建 5 个 wiki 页面：4 个核心概念（美元潮汐/美元周期/美元收割全球的机制/脆弱五国）+ 1 个历史案例汇编（美元潮汐历史案例覆盖 1982 拉美到 2022 斯里兰卡 11 个案例）+ 1 个主合成页（研究：美元如何收割新兴市场）。从 stub 升级 [[美元收割全球的机制]] 为完整页（8 阶段收割循环 + 三大机制 + 案例 + 应对）。删除冗余 stub 文件 [[美元收割全球的机制]]。
- Pages created: [[美元周期]]、[[美元潮汐]]、[[美元收割全球的机制]]、[[脆弱五国（Fragile Five）]]、[[美元潮汐历史案例]]、[[研究：美元如何收割新兴市场]]
- Related: [[美元霸权]]、[[全球金融周期]]、[[美元流动性]]、[[汇率传导机制]]、[[1997 亚洲金融危机]]、[[1992 欧洲货币危机]]、[[新兴市场为避免被美国薅羊毛采取了哪些措施]]、[[美元收割全球的机制是什么]]
- Sources: [[2026-03-23-巫师财经-崩了]]、[[我们已经处于新一轮加息周期中或前夜]]、[[2026-06-24-韩国需要冷静冷静]]、[[2026-06-04-日本史上最大规模汇率保卫战]]
- Key finding: 美元收割不是阴谋而是结构性产物——美联储政策服务于国内目标但会"溢出"到全球；EM 危机与美元加息周期高度同步（1982/1994/1997/2013/2018/2022 都验证）；2026 任庄主判断"新一轮加息周期中或前夜"，新一轮潮汐可能开启

## [2026-07-14] ingest | 巫师财经2025年终盘点Top10
- Summary: 消化巫师财经2025-12-25《中国财经年度盘点Top10》。新建source页，54个知识点覆盖外卖大战（蒋凡500亿预算）、娃哈哈三方博弈（宗馥莉/杭州上城/元老/美国人）、西贝IPO致命伤、港股复活（南下资金1.2万亿）、国补利益链、低利率原因、中美关税脱钩竞赛、12万亿化债+4%赤字率Top1结论+巫师亏钱Top0
- Sources: [[2025-12-25-巫师财经-中国财经年度盘点Top10]]
- Pages updated: [[index]]

## [2026-07-14] ingest | 巫师财经《崩了》- 0323全球股灾
- Summary: 消化巫师财经2026-03-23《崩了》，新建source页+黄金实体stub。核心命题：黄金"大炮一响黄金万两"失效（日元实际利率框架主导）、日韩三重弱点被同时命中（能源依赖+汇率弱+半导体权重）、欧洲刚出俄罗斯坑又进中东坑（滞胀陷阱）、A股相对封闭抗揍
- Sources: [[2026-03-23-巫师财经-崩了]]
- Entities: [[黄金]]（stub新建）
- Pages updated: [[日经225]]（描述补充0323暴跌）、[[韩国综合指数]]（描述补充跌幅数据）、[[index]]

## [2026-07-14] question | 新兴市场抗薅羊毛措施
- Summary: 新建问答页，四大类措施：去美元化（储备多元化、CIPS/SPFS/mBridge）、外汇管制（资本管制、外储缓冲）、区域联盟（金砖/RCEP/上合）、汇率弹性管理
- Pages created: [[新兴市场为避免被美国薅羊毛采取了哪些措施]]
- Related: [[去美元化]], [[美元收割全球的机制]]

## [2026-07-14] question | 美元收割全球的机制是什么
- Summary: 新建问答页，解释"美元收割全球"的三步机制（放水期→紧缩期→抄底期）+ 1980年代拉美债务危机案例 + 两个必要条件
- Pages created: [[美元收割全球的机制是什么]]
- Related: [[美元霸权]], [[去美元化]], [[美元加息周期]]

## [2026-07-14] expansion | 金融传导机制分析框架（案例6-12扩充）
- Summary: 新增7个多链叠加案例（降息汇率、房地产刺激、出口顺差汇率、禽流感鸡肉、大宗商品通胀、贸易战汇率、大豆丰收猪价）及方法论总结检查清单
- Pages updated: [[金融传导机制分析框架]]
- Cases added: 案例6（降息→汇率）、案例7（房地产刺激→房价）、案例8（出口顺差→汇率）、案例9（禽流感→鸡肉）、案例10（大宗商品→美国通胀）、案例11（关税→汇率）、案例12（大豆丰收→猪肉）

## [2026-07-14] concept | 豆粕期货涨价对短期猪价格的影响机制
- Summary: 新建概念页，分析三条传导链（成本推高/需求信号/去产能加速）的方向冲突，解释为何短期猪价影响方向不确定
- Pages created: [[豆粕期货涨价对短期猪价格的影响机制]]
- Related: [[猪周期]], [[蛛网模型]], [[金融传导机制分析框架]]

## [2026-07-13] discussion | 金融传导机制分析框架（扩充+修正）
- Summary: [[金融传导机制分析框架]]
- Pages created: [[实际利率框架]], [[库存周期]], [[预期差交易]], [[价格传导非对称性]]
- Pages updated: [[金融传导机制分析框架]], [[index]], [[hot]]
- Key insight: 6项推导修正——案例2"通胀利好"反转、链条C条件缺失、案例3出口竞争力/总量需求对冲、案例4银行惜贷条件、案例5下跌主因归正（利率杀估值）、案例1超预期前提；补充4个支撑概念页，框架知识网络完整化

## [2026-07-13] ingest | 二十届三中全会细节解析【巫师财经】
- Source: `wiki/sources/2024-12-18-二十届三中全会细节解析-巫师财经.md`
- Summary: [[二十届三中全会]]
- Pages created: [[二十届三中全会]], [[人口结构]], [[全国统一大市场]], [[中国共产党]]
- Pages updated: [[财税改革]], [[国企改革]], [[新质生产力]], [[金融体制改革]], [[收入分配]], [[房地产]], [[中国金融与改革]], [[index]], [[hot]]
- Key insight: 二十届三中全会是二十大路线的延伸与细化，不是重开新路线；"债务不是手段而是目的"——债务转移到普通人身上驱动劳动意愿

## [2026-07-13] ingest | 万科宝能股权之争【巫师资本战争系列】
- Source: `.raw/articles/wangke-baoneng-equity-dispute-2026-07-13.md`
- Summary: [[万科宝能股权之争]]
- Pages created: [[王石]], [[姚振华]], [[华润]], [[安邦]], [[宝能系]], [[中国特色企业治理]], [[恶意收购]], [[白衣骑士]], [[杠杆收购]], [[万科宝能之争]]
- Pages updated: [[万科]]
- Key insight: 2015-2017年万科宝能之争揭示中国资本市场本质——控制权可脱离股权存在，人治穿插于规则之中

## [2026-07-13] ingest | 日本经济崩盘始末【巫师经济学04】
- Source: `.raw/articles/日本经济崩盘始末-2020-04-25.md`（微信文章已读取并存入 wiki/sources/）
- Summary: [[2020-04-25-日本经济崩盘始末-巫师财经]]
- Pages created: [[泡沫经济]], [[广场协议]], [[金融自由化]], [[自杀式加息]], [[流动性消失术]], [[窗口指导]], [[索尼]], [[三菱集团]], [[黑田东彦]]
- Pages updated: [[index]],
- Key insight: 广场协议不是崩盘根源——真正原因是金融自由化+极度宽松货币政策+自杀式加息的"头孢配酒"组合

## [2026-07-07] wiki | 欧元专题：4 个核心页面已创建
- Q: 详细讲解欧元，包括背景、各国谈判、财政变化等方面
- A: 已创建 4 个结构化 wiki 页面，建立反向链接网络
- Locations (new):
 - `wiki/entities/欧元.md` — 欧元实体页（核心，~830 行）
 - `wiki/concepts/欧元区主权债务危机.md` — 2009-2012 欧债危机（~700 行）
 - `wiki/concepts/马斯特里赫特条约.md` — 1992 马约法律基础（~620 行）
 - `wiki/concepts/欧洲货币体系.md` — 1979-1999 EMS/ERM/ECU（~570 行）
- 关键内容覆盖：
 1. **欧元的诞生背景**：从 1970 Werner Plan → 1979 EMS → 1989 Delors Report → 1992 马约 → 1999 欧元诞生
 2. **各国谈判细节**：法德"政治交易"（密特朗 vs 施密特/科尔）、英国永久 Opt-out、丹麦公投否决、意大利/西班牙/葡萄牙/希腊的妥协
 3. **财政变化**：SGP（稳定与增长公约）的"形式严、实质松"、2010-2012 欧债危机暴露缺陷、ESM 永久机制（5000 亿欧元）、NGEU 革命性突破（8000 亿欧元）、2024 SGP 改革
 4. **欧猪五国（PIIGS）详解**：葡萄牙、爱尔兰、意大利、西班牙、希腊五国危机的差异与共性
 5. **欧元区根本矛盾**：三元悖论的违反、"南北"分化、民主赤字
 6. **未来挑战**：数字欧元、竞争力下降（Draghi 报告）、地缘分裂
- 反向链接：在 IMF.md、1992欧洲货币危机.md 中已建立对欧元/欧债危机的引用
- 风格：保持与 IMF.md、1992欧洲货币危机.md 一致的结构化风格（核心定义 → 历史背景 → 机制 → 危机 → 改革 → 启示 → 相关条目）
- 总计：~2720 行新内容，跨 4 个页面建立 50+ 互链

## [2026-06-26] wiki-query | 财政货币化问答已保存
- Q: 什么是财政货币化？它与化债、QE有什么区别？
- A: 已保存至 `wiki/questions/财政货币化.md`
- Sources: [[财政货币化]]

## [2026-04-24] save | v1.6.0 public release notes (Teams, Karpathy-style)
- Type: release doc + visual assets
- Locations (new): `docs/releases/v1.6.0.md` (346 lines, 6 sections, Karpathy-style prose), `wiki/meta/dragonscale-mechanism-overview.svg` (4-mechanism diagram with shared .vault-meta/ gate), `wiki/meta/dragonscale-6-test-flow.svg` (validation timeline), `wiki/meta/dragonscale-frontier-graph.svg` (M4 candidate + 3 filed pages)
- Locations (modified): `wiki/meta/2026-04-24-v1.6.0-release-session.md` (cross-reference added pointing to public release notes)
- Scope: Teams approach. R1 (chair) wrote 3 original SVGs per SVG Diagram Style Guide. R2 (codex worker) drafted Karpathy-style release prose. R3 (chair) stitched SVGs, pivoted Wikipedia imagery to text links only (no binary vendoring per permission). R4 (codex verifier) returned ACCEPT WITH FIXES, 3 wording fixes on version narrative. R5 (chair) applied fixes, committed.
- Style: direct, short, signal-dense, lists over prose, no em dashes, no marketing terms. Verifier confirmed zero em-dashes and zero banned marketing language ('revolutionary', 'seamless', 'world-class', 'game-changing', 'unlock', 'transform').
- Distribution (all three destinations covered): (1) `docs/releases/v1.6.0.md` public-facing file (commit `85515bb`), (2) `wiki/meta/2026-04-24-v1.6.0-release-session.md` internal engineering record (cross-linked), (3) GitHub Release body (user to paste from docs/releases/v1.6.0.md when ready to `gh release create v1.6.0`).
- Wikipedia imagery: referenced as text link to `https://en.wikipedia.org/wiki/Dragon_curve` rather than hotlinked or vendored. Cleaner license-wise (no CC-BY-SA attribution needed) and no external dependency. The 3 original SVGs carry the visual load instead.
- PII scan post-write: `docs/releases/v1.6.0.md` + all three SVGs are clean. No `/home/` paths, no real emails, no tokens.
- Next recommended: user runs `gh release create v1.6.0 --notes-file docs/releases/v1.6.0.md` when ready to cut the public release. This also creates the annotated tag.

## [2026-04-24] save | DragonScale end-to-end validation pass (Teams, 6 tests)
- Type: validation + first real fold + first real autoresearch
- Tests executed (all green):
 - T0 ollama pull `nomic-embed-text`: done (274MB, 15s wall)
 - T1 M1 dry-run k=3 via codex: DRY-RUN OK, 8 children, no em-dashes
 - T2 M2 real allocate: counter advanced 2 to 3, got `c-000002` (unassigned reservation; gap acceptable per spec)
 - T3 M3 full tiling with model present: 41 pages scanned, 21 embedded, 20 correctly skipped (meta/excluded/embed-error), 0 errors at >=0.9, 15 pairs in 0.8-0.9 review band (top 0.8822 Compounding Knowledge vs LLM Wiki Pattern, a legitimate semantic neighbor), report at `wiki/meta/tiling-report-2026-04-24.md`
 - T4 M1 commit via codex: first real fold committed, `wiki/folds/fold-k3-from-2026-04-23-to-2026-04-24-n8.md` (115 lines, 8 children, flat extractive). Flips the long-standing "no fold committed yet" status
 - T6 M4 autoresearch no-topic via codex: selected "How does the LLM Wiki pattern work?" as candidate (score 1.7022, #3 after skipping top-1 source + top-2 self-reference); 6 web fetches (Karpathy gist, RAG paper arXiv 2005.11401, MemGPT arXiv 2310.08560, Obsidian docs); 3 new concept pages filed, each with Primary Sources
- Locations (new): `wiki/folds/fold-k3-from-2026-04-23-to-2026-04-24-n8.md`, `wiki/meta/tiling-report-2026-04-24.md`, `wiki/concepts/Persistent Wiki Artifact.md`, `wiki/concepts/Source-First Synthesis.md`, `wiki/concepts/Query-Time Retrieval.md`
- Locations (modified): `.vault-meta/address-counter.txt` (2 to 3), `wiki/index.md` (3 concept links), `wiki/concepts/_index.md` (3 concept links)
- Scope: six-test menu the user approved. Codex gpt-5.4 for T1/T4/T6 (sub-agent delegation); chair for T0/T2/T3 (one-shot shell) and all integration (index, log, hot, commit).
- Style: all new content uses colons or parens instead of em-dashes. Pre-existing em-dashes in index entries and wiki/concepts/_index.md left as-is (clean-room boundary; deferred to F-slice style pass).
- Tests still green: `make test` passes (74+ assertions).
- Integration: chair added the 3 new concepts to `wiki/index.md` and `wiki/concepts/_index.md` with colon-style descriptions so the fresh pages are discoverable. The cluster extends `[[How does the LLM Wiki pattern work]]` and cross-references `[[LLM Wiki Pattern]]`.
- Next recommended slice: either (G) commit this test batch and declare v1.6.0 validated, or (H) run a second fold k=3 now that 8 newer entries exist above this one and close the hierarchical-fold-not-yet-supported loop in a future phase.

## [2026-04-24] save | v1.6.0 closeout (Teams, chair-led)
- Type: docs + release hygiene
- Locations (new): wiki/meta/2026-04-24-v1.6.0-release-session.md (release session summary, 346 lines), wiki/meta/boundary-frontier-2026-04-24.md (first M4 run artifact against this vault), docs/dragonscale-guide.md (user-facing DragonScale guide, 563 lines)
- Locations (modified): wiki/hot.md (tag-claim fix, Scripts line adds boundary-score, tests line adds test_boundary_score, push-line drift, tiling line-count, one em-dash), docs/install-guide.md (version 1.5.0 to 1.6.0, DragonScale callout expanded to all four mechanisms, "hierarchical log folds" corrected to "flat extractive log folds", points to docs/dragonscale-guide.md), README.md (DragonScale parenthetical expanded to all four mechanisms plus guide link)
- Scope: Teams approach, chair-led. Slice A (2 codex read-only explorers: closeout punch list + doc-surface map). Slice B (6 bounded writes: 4 chair, 2 codex workers, non-overlapping write scopes). Slice C (codex adversarial verifier, ACCEPT WITH FIXES). Slice D (fix pass + log entry + manual commit of docs + README).
- Verifier: C1 found 11 items across 6 files. All 11 applied. Flag typos `--allow-remote-ollama` and `--report PATH` corrected in release-session; boundary-frontier provenance corrected to `--top 7` to match default vs explicit top; hot.md tiling line-count claim stripped to avoid drift; hot.md "local tag only" corrected to "local commits only, no git tag"; install-guide log-fold wording corrected from "hierarchical" to "flat extractive"; dragonscale-guide rollback wording corrected (`.vault-meta/` is a shared gate across M2+M3+M4, not per-mechanism).
- Model: codex gpt-5.4 used throughout. User requested gpt-5.5; not reachable via codex CLI 0.123.0 / this account at the time. models_cache lists max gpt-5.4, and the API rejects gpt-5.5 with "does not exist or you do not have access". Existing config already has `service_tier = "fast"` and `sandbox_mode = "workspace-write"`, matching the "fast for chatgpt with permission of full access" intent.
- Tests: `make test` passes. test_allocate_address.sh (shell, 12 assertions), test_tiling_check.py (python, 18 assertions), test_boundary_score.py (python, 44 assertions). Zero ollama dependency.
- Tags: still no local v1.5.0 / v1.5.1 / v1.6.0 tags. User controls tag creation and push. Pre-existing tags unchanged (v1.1, v1.4.0 through v1.4.3).
- Deliberately NOT done: no real M1 fold committed; no M3 end-to-end run (needs `ollama pull nomic-embed-text`); pre-existing em-dashes in install-guide.md and README.md left untouched (clean-room boundary, not in write scope this slice); CLAUDE.md pre-existing uncommitted change left untouched.
- Next recommended slice: either (E) push to origin/main and create annotated tags v1.5.0, v1.5.1, v1.6.0 in landing order, or (F) dedicated style pass to scrub pre-existing em-dashes across install-guide.md, README.md, and any other wiki files flagged by a grep scan.

## [2026-04-24] save | DragonScale Phase 4 — boundary-first autoresearch shipped (v1.6.0)
- Type: feature release
- Locations (new): scripts/boundary-score.py (with --top, --page, --json, stdout-only CLI), tests/test_boundary_score.py (40+ assertions)
- Locations (modified): skills/autoresearch/SKILL.md (new Topic Selection section A/B/C with helper-failure fallback), commands/autoresearch.md (no-topic candidate flow with agenda-control label), wiki/concepts/DragonScale Memory.md (v0.4: M4 flipped from NOT IMPLEMENTED to shipped; exact formula without recency floor; filename-stem disclosure; fence-handling qualifiers), CHANGELOG.md, .claude-plugin/{plugin,marketplace}.json (1.5.0 -> 1.6.0), Makefile (test-boundary target), wiki/hot.md, wiki/index.md, wiki/concepts/_index.md (status drift resolved).
- Scope: boundary-first autoresearch as opt-in Topic Selection mode. `/autoresearch` without a topic surfaces top-5 frontier pages; user picks/overrides/declines. Explicit helper-failure fallback to user-ask. Labeled "agenda control" throughout to match the spec's scope disclosure.
- Correctness: filename-stem resolution including folder-qualified ` ` -> Foo.md. Self-loops, unresolved targets, meta-targets, symlinks, and vault escapes all excluded. Code-fence parser handles backticks AND tildes with CommonMark length tracking (longer opening fence is not closed by shorter inner fence). Indented blocks intentionally not filtered (Obsidian bullet convention).
- Recency: exp(-days/30), no floor. Stale pages approach zero weight so they do not dominate frontier ranking.
- Review rounds: codex adversarial Phase 4 round 1 (10 items: 7 reject + 3 refine). Round 2 (7 accept + 3 still-reject: folder-qualified stem, docstring floor mention, hot.md historical drift). Round 3 (3 accept, PASS).
- Phase 3.6 (pre-Phase-4 hardening) already landed as v1.5.1: tiling --report VAULT_ROOT confinement, rollout baseline, AGENTS.md consistency, wiki-ingest .raw/ contradiction, install-guide version.
- All four DragonScale mechanisms now shipped and opt-in. 44 commits ahead of origin/main, no push.

## [2026-04-24] save | DragonScale Phase 3.5 — cross-phase hardening to v1.5.0
- Type: release hardening
- Locations (new): bin/setup-dragonscale.sh (opt-in installer), tests/test_allocate_address.sh, tests/test_tiling_check.py, Makefile, CHANGELOG.md
- Locations (modified): hooks/hooks.json (+.vault-meta/ staging), agents/wiki-ingest.md (single-writer rule for addresses), agents/wiki-lint.md (Mechanism 2+3 checks), skills/wiki-ingest/SKILL.md (aligned non-DragonScale wording), wiki/concepts/DragonScale Memory.md (M2 severity matches lint, M4 marked NOT IMPLEMENTED, seed page gets address c-000001), .claude-plugin/{plugin.json,marketplace.json} (1.4.2/1.4.3 → 1.5.0), README.md (11 skills + DragonScale callout), wiki/hot.md (refreshed for v1.5.0), .raw/.manifest.json (address_map now has DragonScale Memory.md → c-000001), .gitignore (.vault-meta/.tiling.lock + cache), .vault-meta/address-counter.txt (advanced to 2).
- Scope: resolve the 10 hold-ship items from the cross-phase audit. Add reproducible test harness (make test passes). Version-bump plugin.json and marketplace.json to 1.5.0. Create CHANGELOG.md. Refresh hot cache.
- Review rounds: codex 3.5a (5/5 accept on doc/agent fixes), codex final holistic (10/10 accept on audit items + 2 surgical regression fixes: wiki-ingest/wiki-lint non-DragonScale wording alignment, README skill count).
- Tests: `make test` runs 12 shell assertions (allocator) + 18 python assertions (tiling-check). All pass; no ollama dependency.
- Phase 3.5 complete. Repo state: 6 developer commits added this pass (f2e73c1, 2b49a0c, 8b28e48, 19ad7e4, 365f557, 2e7dd16). Total 39 commits ahead of origin/main. No push.

## [2026-04-24] save | DragonScale Phase 3 — semantic tiling MVP
- Type: skill update + new script + threshold state
- Locations: scripts/tiling-check.py (485 lines), .vault-meta/tiling-thresholds.json (seed defaults), skills/wiki-lint/SKILL.md (109-line Semantic Tiling section + item #10 in checks), wiki/concepts/DragonScale Memory.md (Mechanism 3 cost framing clarified)
- Scope: opt-in embedding-based duplicate detection via ollama nomic-embed-text. Default bands error>=0.90, review>=0.80, explicitly documented as conservative seeds (not literature-backed interpolation). Calibration procedure documented, not automated.
- Security: default OLLAMA_URL locked to 127.0.0.1; non-localhost requires --allow-remote-ollama flag. Symlinks and vault-root escapes rejected before file reads (prevents data exfil).
- Correctness: cache keyed on sha256(model+body); orphan GC on save; model-drift auto-invalidation on load.
- Concurrency: flock(LOCK_EX) on .vault-meta/.tiling.lock; per-PID temp file for atomic writes.
- Scale: warn >500 pages; hard-fail exit 4 at >5000 pages.
- Exit codes: 0/2/3/4/10/11 distinctly surfaced in wiki-lint wiring (not collapsed into "unknown").
- Review rounds: 4 codex exec adversarial passes covering security, cache correctness, feature gate, inclusion logic, scale, threshold honesty, concurrency, exit codes, model drift, terminology coupling.
 Round 1: 10 items -> 7 reject + 3 refine.
 Round 2: 6 accept + 4 still-reject (symlink ordering, prose sync, exit-code wiring, terminology in checklist + "no API cost" claim).
 Round 3: 3 accept + 1 still-reject (cost-framing phrasing).
 Round 4: accept.
- Final verdict: 10/10 accept.
- Phase 3 complete. All three DragonScale mechanisms that were in-scope for the initial spec are now shipped as opt-in features. Mechanism 4 (boundary-first autoresearch) was flagged as agenda-control out-of-scope per the v0.2 scope boundary; may or may not ship as a future phase.

## [2026-04-23] save | DragonScale Phase 2 — deterministic page addresses MVP
- Type: skill update + new script
- Locations: scripts/allocate-address.sh, skills/wiki-ingest/SKILL.md (Address Assignment section), skills/wiki-lint/SKILL.md (Address Validation section), wiki/concepts/DragonScale Memory.md (Mechanism 2 rewritten v0.2→v0.3), .vault-meta/address-counter.txt, .raw/.manifest.json (new)
- Scope: MVP address format `c-NNNNNN` (creation-order counter, zero-padded 6 digits). Rollout baseline 2026-04-23. Legacy pages exempt until deliberate backfill (future `l-` prefix). No content hash, no fold-ancestry encoding in the MVP (both deferred).
- Concurrency: atomic allocation via flock-guarded Bash helper. Counter recovery from max observed `c-` address, never silent reset to 1.
- Lint: post-rollout pages without address are errors; legacy pages without address are informational. Optional `.vault-meta/legacy-pages.txt` manifest grandfathers pages with missing/wrong `created:` metadata.
- Re-ingest idempotency: `.raw/.manifest.json` `address_map` preserves path→address mapping across re-ingests and renames.
- Naming: mechanism renamed from "content-addressable paths" to "deterministic page addresses" (the MVP is a counter, not a content hash; the old name was overclaim).
- Review rounds: 2 codex exec adversarial passes. Round 1: 8 rejects covering counter mutation, race conditions, uniqueness atomicity, missing-file recovery, terminology drift, silent regression path, legacy classification, re-ingest idempotency. Round 2: 7 accept + 1 reject (manifest.json absent). Round 3 (item 8 only): accept after creating `.raw/.manifest.json`.
- Final verdict: 8/8 accept.
- Phase 2 complete. Phase 3 (semantic tiling lint) gated on human approval.

## [2026-04-23] save | DragonScale Phase 1 — wiki-fold skill shipped
- Type: skill
- Location: skills/wiki-fold/SKILL.md, skills/wiki-fold/references/fold-template.md
- Scope: flat extractive fold over raw wiki/log.md entries. Dry-run default via Bash stdout (no Write tool, avoids PostToolUse hook residue). Structural idempotency via deterministic fold_id. Duplicate-range detection. Fold-of-folds explicitly out of scope.
- Review rounds: 3 codex exec adversarial passes. Round 1: 1 refine + 6 reject across 7 items (allowed-tools, hook-mutation risk, idempotency claim, dry-run faithfulness, children structure, Mechanism 1 coverage, auto-commit conflict). Round 2: 6 accept + 1 reject (25/26 count inversion). Round 3 (item 4 only): accept.
- Final verdict: 7/7 accept.
- Dry-run artifact: /tmp/wiki-fold-dry-run-v2.md (not committed). fold_id: fold-k3-from-2026-04-10-to-2026-04-23-n8.
- Phase 1 complete. Phase 2 (content-addressable paths) gated on human approval.

## [2026-04-23] save | DragonScale Memory v0.2 — post-adversarial-review
- Type: concept revision
- Location: wiki/concepts/DragonScale Memory.md
- Review: codex exec adversarial review rejected all 7 load-bearing claims in v0.1
- Changes: weakened LSM analogy, removed strong prompt-cache claim, replaced 0.85 threshold with calibration procedure, justified 2^k as MVP convenience, acknowledged scope-boundary leak for boundary-first autoresearch, added Operational Policies section (retention/tombstones/versioning/conflict/concurrency/provenance/ACL), tagged claims as [sourced]/[derived]/[conjecture], narrowed tagging scope per re-review
- Re-review result: 7/7 accepted (after one surgical fix on tagging-scope language)
- Phase 0 complete. Phase 1 (wiki-fold skill) gated on human approval.

## [2026-04-23] save | DragonScale Memory — Phase 0 design doc (proposed)
- Type: concept
- Location: wiki/concepts/DragonScale Memory.md
- From: brainstorming session on applying Heighway dragon curve properties to LLM wiki memory architecture
- Scope: memory-layer only, NOT agent reasoning. Four mechanisms: (1) fold operator (LSM-style exponential compaction at 2^k log entries), (2) content-addressable page paths for prompt-cache stability, (3) semantic tiling lint (embedding-based dedup, 0.85 cosine threshold), (4) boundary-first autoresearch scoring
- Status: proposed. Phase 0 pending codex adversarial review. Phase 1+ (fold skill, address anchors, tiling lint, boundary score) gated on review pass.
- Primary sources verified: Dragon curve (Wikipedia, boundary dim 1.523627086), Regular paperfolding sequence (OEIS A014577), LSM trees (arXiv 2504.17178, LevelDB 10x level ratio), MemGPT (arXiv 2310.08560), Anthropic prompt caching docs (5min/1hr TTL, 20-block lookback)
- Links updated: wiki/concepts/_index.md, wiki/index.md

## [2026-04-15] save | Claude SEO v1.9.0 Slides and GitHub Release
- Type: session
- Location: wiki/meta/2026-04-15-slides-and-release-session.md
- From: built 15-slide HTML presentation deck (v190.html), fixed hardcoded path in release_report.py, pushed 68 files to GitHub, tagged v1.9.0, created GitHub release with PDF asset
- Key lessons: Path.home() not hardcoded paths, git pull --rebase before big pushes, Chrome blocks file:// cross-origin images, .claude/ always in .gitignore
- Release: https://github.com/AgriciDaniel/claude-seo/releases/tag/v1.9.0

## [2026-04-15] save | Claude SEO v1.9.0 Release Report — PDF Complete
- Type: session
- Location: wiki/meta/2026-04-15-release-report-session.md
- From: full session completing the v1.9.0 PDF release report. Dark theme, 13 pages, 1.53 MB. Fixed logo (double-space filename), empty spaces, page-break orphans, file:// URL encoding.
- Key fixes: `urllib.parse.quote()` for file:// URIs; `display:table-cell` is atomic in WeasyPrint (no page-break); fixed `height:297mm` causes empty space; replaced orphan tables with paragraphs
- Challenge v2 added: keyword LEADS, $600 prize pool, deadline April 28
- Output: `~/Desktop/Claude-SEO-v1.9.0-Release-Report.pdf`

## [2026-04-14] save | Claude SEO v1.9.0 — Pro Hub Challenge Integration Session
- Type: session + 4 concept pages + 1 entity page
- Location: wiki/meta/2026-04-14-claude-seo-v190-session.md
- From: full v1.9.0 implementation session — reviewed 5 community submissions, integrated 4 new skills (seo-cluster, seo-sxo, seo-drift, seo-ecommerce), enhanced seo-hreflang, added DataForSEO cost guardrails
- Pages created: [[2026-04-14-claude-seo-v190-session]], [[Claude SEO]], [[Pro Hub Challenge]], [[Semantic Topic Clustering]], [[Search Experience Optimization]], [[SEO Drift Monitoring]]
- Review rounds: 4 (code review x3 + cybersecurity audit). Score: 87 → 93 → 97 → 85 security
- Key learnings: always verify subagent output (40-line count error caught), insertion-point bugs caught by max-effort plan review, pre-existing security debt identified (10 of 15 findings)

## [2026-04-14] save | SVG Diagram Style Guide
- Type: concept
- Location: wiki/concepts/SVG Diagram Style Guide.md
- From: extracted design tokens from 17 production SVGs in claude-ads/assets/diagrams/
- Covers: colors, typography, layout primitives, card patterns, arrow connectors, numbered circles, file naming

## [2026-04-14] save | Community CTA Footer Rollout
- Type: decision
- Location: wiki/meta/2026-04-14-community-cta-rollout.md
- From: session adding Skool community footer to 6 skill repos (claude-ads, claude-seo, claude-obsidian, claude-blog, banana-claude, claude-cybersecurity)
- Key insight: frequency calibration per tool type; single-point orchestrator instruction pattern

## [2026-04-10] save | Backlink Empire - Blog Posts, Karpathy Gist, GitHub Cross-Linking
- Type: session
- Location: wiki/meta/2026-04-10-backlink-empire-session.md
- From: full session covering blog creation (claude-obsidian + claude-canvas), Karpathy gist comment, 26 GitHub README updates with Author/community/backlink sections, homepage URLs on 10 repos, topics on 25 repos, rankenstein.pro backlinks on 5 SEO repos
- Blog posts: agricidaniel.com/blog/claude-obsidian-ai-second-brain, agricidaniel.com/blog/claude-canvas-ai-visual-production
- Impact: ~87 new backlinks from DA 96 github.com, 6 rankenstein.pro backlinks, 25 Skool community links

## [2026-04-08] save | claude-obsidian v1.4 Release Session
- Type: session
- Location: wiki/meta/claude-obsidian-v1.4-release-session.md
- From: full release cycle covering v1.1 (URL/vision/delta tracking, 3 new skills), v1.4.0 (audit response, multi-agent compat, Bases dashboard, em dash scrub, security history rewrite), and v1.4.1 (plugin install command hotfix)
- Key lessons: plugin install is 2-step (marketplace add then install), allowed-tools is not valid frontmatter, Bases uses filters/views/formulas not Dataview syntax, hook context does not survive compaction, git filter-repo needs 2 passes for full scrub

## [2026-04-08] ingest | Claude + Obsidian Ecosystem Research
- Type: research ingest
- Source: `.raw/claude-obsidian-ecosystem-research.md`
- Queries: 6 parallel web searches + 12 repo deep-reads
- Pages created: [[claude-obsidian-ecosystem]], [[cherry-picks]], [[claude-obsidian-ecosystem-research]], [[Ar9av-obsidian-wiki]], [[Nexus-claudesidian-mcp]], [[ballred-obsidian-claude-pkm]], [[rvk7895-llm-knowledge-bases]], [[kepano-obsidian-skills]], [[Claudian-YishenTu]]
- Key finding: 16+ active Claude+Obsidian projects; 13 cherry-pick features identified for v1.3.0+
- Top gap confirmed: no delta tracking, no URL ingestion, no auto-commit

## [2026-04-07] session | Full Audit, System Setup & Plugin Installation
- Type: session
- Location: wiki/meta/full-audit-and-system-setup-session.md
- From: 12-area repo audit, 3 fixes, plugin installed to local system, folder renamed

## [2026-04-07] session | claude-obsidian v1.2.0 Release Session
- Type: session
- Location: wiki/meta/claude-obsidian-v1.2.0-release-session.md
- From: full build session — v1.2.0 plan execution, cosmic-brain→claude-obsidian rename, legal/security audit, branded GIFs, PDF install guide, dual GitHub repos


- Source: `.raw/` (first ingest)
- Pages updated: [[index]], [[log]], [[hot]], [[overview]]
- Key insight: The wiki pattern turns ephemeral AI chat into compounding knowledge — one user dropped token usage by 95%.

## [2026-04-07] setup | Vault initialized

- Plugin: claude-obsidian v1.1.0
- Structure: seed files + first ingest complete
- Skills: wiki, wiki-ingest, wiki-query, wiki-lint, save, autoresearch

## [2026-08-05] WIKI_DASHBOARD | Content overview dashboard rewritten

- [2026-08-05T06:52:26Z] WIKI_DASHBOARD name="dashboard" tool=bases view=table+groupBy filter="all content pages (concepts/entities/sources/questions/comparisons/domains/analysis) by type and status, with days-since-edit formula"
- Fixed: previous dashboard.base referenced nonexistent "wiki/" folders (empty view); rewrote with flat vault structure

## [2026-08-05] WIKI_DASHBOARD | Dataview dashboard

- [2026-08-05T07:07:22Z] WIKI_DASHBOARD name="dashboard" tool=dataview view=table+groupBy filter="content overview: by type / by status / recent 30 / stale 30d+ / stubs / entities missing sources"

## [2026-08-05] LINT | Full health audit

- [2026-08-05T15:14:45+0800] LINT scanned=1000 orphans=0 broken_links=6 stale=25 fm_gaps=615 missing_summary=963 fragmented_clusters=6 lifecycle_issues=987 synthesis_gaps=79 relationship_issues=0 visibility_issues=0
- Orphans cleared (yesterday's 12 content orphans + 10 test/demo pages now resolved via git commit bc808dc)
- Dead-link targets: 6 real (excl. lint-report self-refs) — `How does the LLM Wiki pattern work?`, `Claude Obsidian`, `Rankenstein`, `Karpathy LLM Wiki Pattern`, `dashboard.base`, `raw/zhihu/日元保卫战`
- FM gaps: 599 missing tags (570 empty `tags: []`), 13 missing created/updated (real-estate cluster), 1 missing type
- lifecycle/base_confidence: 0/1000 pages adopt the schema — vault-wide structural decision pending
- synthesis/ dir empty despite 79 high-co-occurrence concept pairs (top: 扩表与缩表×化债 = 42 pages)
- [2026-08-06] QUERY query="魏玛共和国用地租马克替代金马克靠国家信用背书，金马克难道没有国家信用背书吗？" result_pages=3 mode=normal escalated=false
- [2026-08-06] FIX Rentenmark兑换比率矛盾：修正 6 处 "1 Rentenmark = 1 旧马克" 错误表述为 "1 Rentenmark = 1 万亿旧马克（10¹²），锚定战前金马克平价（1 美元 = 4.2）"，涉及 Rentenmark改革/魏玛恶性通胀/ECB/Hans Luther + ECB canvas

## [2026-08-06] LINT | Full health audit

- [2026-08-06T14:45:00+0800] LINT scanned=999 orphans=2 broken_links=78 stale=41 contradictions=0 prov_issues=0 missing_summary=999 fragmented_clusters=6 visibility_issues=0 promotion_candidates=0 synthesis_gaps=85 relationship_issues=0 lifecycle_issues=999 fm_gaps=324 artifact_links=85 nonmd_links=2
- Content orphans: concepts/冲销式干预, concepts/财政货币化 (operational: 8 meta/folds pages)
- Broken links (content): 63 hard (13 unique targets; top: 巴塞尔协议×33→巴塞尔协议III, 韩国股灾简史×9→sources dated file, 韩国需要冷静冷静×7) + 15 near-miss (《》/空格/标点差异，可机械修复)
- 85 artifact links in meta/lint-report-* and log.md (previous report example code) — noise, exclude from content counts
- FM gaps: sources=284, created=23 (12 real-estate cluster), updated=14, tags=2, type=1
- lifecycle/base_confidence: 0/999 pages adopt llm-wiki trust schema (vault uses status:) — trust-check fails: _meta/trust-ledger.json missing (known structural decision, pending)
- Stale >90d: 41 pages; oldest cluster = 2026-04-07 claude-obsidian legacy seed pages (121 days)
- Status enum drift: complete/completed, seed/seedling/extracted/mature (vocabulary not in documented set)

## [2026-08-06] LINT_CONSOLIDATE | Link repair + orphan rescue + collision resolution

- [2026-08-06T15:39:00+0800] LINT_CONSOLIDATE links_fixed=84 orphans_rescued=2 lifecycle_updates=0 tier_demotions=0 tag_fixes=0 contradiction_callouts=0 renames=3 stubs=4
- Broken links rewritten (content): 巴塞尔协议→巴塞尔协议III ×33, 韩国股灾简史→sources/2026-07-21-… ×9, 韩国需要冷静冷静→sources/2026-06-24-… ×7, 研究：…（增强版）→… ×2, 2001 阿根廷债务违约→2001 阿根廷违约, 中华人民共和国国务院/中央人民政府→国务院 ×2, 美元收割全球的机制什么→美元收割全球的机制 (log), raw/zhihu/日元保卫战…→sources/2026-05-13-… ; near-miss 15 (《》/空格/标点规范化); 6 处带显示文本的旧路径链接更新
- Lint-report/log noise: 85 处示例死链转纯文本（meta/lint-report-2026-08-03/04/05.md、log.md、meta/dashboard.md）
- Root cause: basename 同名冲突遮蔽概念页（sources/冲销式干预、questions/财政货币化、sources/石油美元体系），导致约 150 条链接歧义 + 2 个虚假孤儿
- Renames (un-shadow): sources/冲销式干预.md → sources/2026-06-02-冲销式干预.md; sources/石油美元体系.md → sources/2026-06-02-石油美元体系.md; questions/财政货币化.md → questions/什么是财政货币化.md (title 同步)
- Stub pages created (addresses c-001101~c-001104, counter →1105): concepts/美联储点阵图, concepts/DDX DDY DDZ 指标 (2 条链接同步改写), entities/BRICS Pay, concepts/微盘股指数; 一带一路 改链 →[[共建一带一路]]
- Orphan rescue: concepts/冲销式干预 (now 51 incoming), concepts/财政货币化 (58), entities/石油美元体系 (39)
- Final state: broken_links=0, content_orphans=0, index_broken=0, collisions=0; scanned=1003
- Side note: 检查中发现 concepts/共建_一带一路_.md 与 concepts/共建一带一路.md 疑似重复页（c-000152/c-000153），待 wiki-dedup 处理

## [2026-08-06] WIKI_SYNTHESIZE | 5 cross-cutting synthesis pages

- [2026-08-06T15:49:00+0800] WIKI_SYNTHESIZE pages_scanned=1003 synthesis_created=5 candidates_skipped=10
- Pairs (co-occurrence): 扩表与缩表×化债=42, 量化宽松×扩表与缩表=40, 扩表与缩表×2008全球金融危机=39, 化债×ECB=30, 欧盟×贸易战=27
- Pages: synthesis/扩表与缩表 × 化债.md (c-001105), synthesis/量化宽松 × 扩表与缩表.md (c-001106), synthesis/扩表与缩表 × 2008全球金融危机.md (c-001107), synthesis/化债 × ECB.md (c-001108), synthesis/欧盟 × 贸易战.md (c-001109); address counter →1110
- Backlinks added to 7 anchors: 扩表与缩表(3), 化债(2), 量化宽松(1), 2008全球金融危机(1), ECB(1), 欧盟(1), 贸易战(1)
- Excluded (already covered): 美联储×中国央行 (comparisons/美联储vs中国央行), 量化宽松×化债 (concepts/QE与化债对比)
- Skipped candidates (next 10): 美联储×量化宽松(39), 扩表与缩表×ECB(35), 扩表与缩表×IMF(30), 扩表与缩表×中国央行(29), 美联储×2008全球金融危机(28), IMF×2008全球金融危机(27), 量化宽松×2008全球金融危机(26), 化债×2008全球金融危机(26), 美联储×IMF(25), 化债×财政货币化(24)

## [2026-08-06] LINT | Full health audit

- [2026-08-06T15:56:59+0800] LINT scanned=1009 orphans=1 broken_links=3 stale=30 contradictions=0 prov_issues=0 missing_summary=986 fragmented_clusters=6 visibility_issues=0 promotion_candidates=0 synthesis_gaps=6 relationship_issues=0 lifecycle_issues=0 fm_gaps=296
- Content orphan: sources/2026-06-02-石油美元体系 (源素材页, 概念页为 entities/石油美元体系)
- Broken links (near-miss 空格差异, 可机械修): 1997 亚洲金融危机×9→1997亚洲金融危机, 1992 欧洲货币危机×3→1992欧洲货币危机, 1998 香港金融保卫战×1→1998香港金融保卫战 (共 13 处)
- FM gaps: created=13 (12 房地产 cluster + 1 source), updated=13, address=13, sources=270, summary=986; 缺 address/created/updated 的 13 页为迁移遗留
- Stale 91-180d: 30 页, 几乎全为 2026-04 claude-obsidian 模板种子页 (内容稳定, 预期陈旧) + sources/2026-04-07-日本金融市场震荡深层逻辑
- lifecycle/base_confidence: 0/1009 采用 llm-wiki trust schema (vault 用 status:, 结构性决策 pending, 与上次一致)
- Fragmented tag clusters (主题): 货币政策(21,0.04) china(21,0.06) semiconductor(6,0.13) 宏观经济(5,0.00) 通胀(5,0.00) 人物(5,0.10); type 标签 concept/entity/source/index 不算
- Synthesis gaps (top): 美联储×扩表与缩表(39) 美联储×2008全球金融危机(30) 量化宽松×2008全球金融危机(27) 美联储×ECB(25) 美联储×IMF(25) 美联储×化债(24)
- Status enum 非主流值: seed(4) seedling(3) proposed(1) digested(1)

## [2026-08-06] LINT_FIX | near-miss 空格断链修复

- [2026-08-06T15:58:00+0800] LINT_FIX links_fixed=16 orphans=0 other=0
- Rewritten: [[1997 亚洲金融危机]]→[[1997亚洲金融危机]] (美元潮汐量化实证/Original Sin/美元周期/美元潮汐/脆弱五国/美元收割全球的机制/美元潮汐历史案例×6/研究：美元如何收割新兴市场×4), [[1992 欧洲货币危机]]→[[1992欧洲货币危机]] (美元潮汐历史案例×2/研究：美元如何收割新兴市场), [[1998 香港金融保卫战]]→[[1998香港金融保卫战]] (美元潮汐历史案例)
- Final: content broken_links=0 (meta/lint-report-* 与 log.md 历史条目按规则保留)

## [2026-08-06] LINT_FIX | 双 subagent 并行:元数据补全 + 标签碎片化修复

- [2026-08-06T16:10:00+0800] FIX metadata_pages=13 address=1110→1123 links_added=40 files_touched=30 clusters_fixed=4 clusters_improved=2
- Agent A (元数据补全): 13 个迁移遗留页补 address/created/updated。分配 c-001110~c-001122 (概念页无引号/source 页带引号),created/updated=2026-08-05 (git 迁移提交 1e2985a 核实);计数器 .vault-meta/address-counter.txt 1110→1123。自检:新地址无重复,frontmatter 之外零改动
- Agent B (标签碎片化): 30 文件新增 40 条语义强关联 wikilink。达标 (cohesion≥0.15): #semiconductor、#宏观经济、#通胀、#人物;改善未达标: #货币政策 0.04→0.09、#china 0.06→0.08 (21 页大簇,避免机械全连)。受保护 13 页未触碰 (diff 复核)
- 遗留: concepts/AI虹吸效应.md 与 concepts/DragonScale Memory.md 共用 c-000042 (历史冲突,待择一重新分配)
- Final: content broken_links=0

## [2026-08-06] VERIFY | c-000042 疑似冲突澄清(误报)

- [2026-08-06T16:15:00+0800] VERIFY addr_conflict=none
- 澄清: concepts/DragonScale Memory.md 与 concepts/AI虹吸效应.md 的 address 冲突系误报。严格 frontmatter-only 解析(仅识别文件头 ^--- 块内 address:)确认:DragonScale Memory.md 的 frontmatter address 为 c-000001,其正文第 78-80 行 ```yaml address: c-000042 ``` 是格式说明示例,非真实字段
- 全库 frontmatter 988 个 address 经严格扫描无重复。结论:无需任何修改
- 教训:地址重复检查必须限定在 frontmatter 块内解析,不能用行首 grep(会误收正文示例)

## [2026-08-06] WIKI_SYNTHESIZE | 第二轮:5 个交叉合成页(美联储/ECB/IMF × 工具与危机)

- [2026-08-06T17:01:00+0800] WIKI_SYNTHESIZE pages_scanned=1003 synthesis_created=5 candidates_skipped=10
- Pairs (co-occurrence): 美联储×量化宽松=39, 扩表与缩表×ECB=35, ECB×欧元区主权债务危机=35, 美联储×2008全球金融危机=28, IMF×2008全球金融危机=27
- Pages: synthesis/美联储 × 量化宽松.md (c-001124), synthesis/美联储 × 2008全球金融危机.md (c-001125), synthesis/扩表与缩表 × ECB.md (c-001126), synthesis/ECB × 欧元区主权债务危机.md (c-001127), synthesis/IMF × 2008全球金融危机.md (c-001128); address counter →1129
- Backlinks added to 7 anchors: 美联储(2), 量化宽松(1), 扩表与缩表(1), ECB(2), 2008全球金融危机(2), IMF(1), 欧元区主权债务危机(1)
- Excluded (already covered): 美联储×中国央行 (comparisons/美联储vs中国央行), 量化宽松×化债 (concepts/QE与化债对比)
- Skipped candidates (next 10): 扩表与缩表×IMF(30), 扩表与缩表×中国央行(29), 量化宽松×2008全球金融危机(26), 化债×2008全球金融危机(26), 美联储×IMF(25), 美联储×ECB(25), 化债×财政货币化(25), 化债×中国央行(25), ECB×2008全球金融危机(25), 美联储×化债(24)
- [2026-08-06T17:04:01+0800] QUERY query="IMF道德危机" result_pages=4 mode=normal escalated=false
- [2026-08-06T17:15:54+0800] TAG_AUDIT taxonomy_missing=1 total_tags=856 single_use_tags=590 untagged=599 over_tagged=82 type_tags_redundant=~180 normalized=0 (只读审计,未修改任何页面)
- [2026-08-06T17:18:23+0800] TAG_NORMALIZE taxonomy_created=1 canonical_tags=~90 aliases_mapped=~50 pages_modified=0 (路径1:仅建立 _meta/taxonomy.md,未改页面)
- [2026-08-06T17:29:42+0800] WIKI_RESEARCH topic="美联储在国际经济中的作用" rounds=3 sources_fetched=4 pages_created=5 (synthesis/美联储在国际经济中的作用 + concepts/美元互换网络 + concepts/FIMA回购便利 + sources/美联储中央央行流动性互换-Fed官网 + sources/FIMA回购便利-Fed官网)
- [2026-08-06T17:36:13+0800] TAG_NORMALIZE pages_modified=278 type_removed=222 alias_merged=377 year_handled=19 over_limit_trimmed=73 string_tags_fixed=2 (路径2:按 _meta/taxonomy.md 迁移指南首批执行)
- 规则: 移除 14 种 type 类标签(concept/entity/term/event/...); 中英同义归并 86 种英文→canonical(含 finance→金融 49页, fed→美联储, monetary-policy→货币政策); 年份 9 处并入事件标签(2008→2008全球金融危机 等)+10 处未映射年份移除(标题已承载语义); 去重; 超限页裁剪到 ≤5(保留 canonical 与复用≥2 词,移除单次专属词 subprime/lehman/cdo 等)
- 修复 2 页字符串 tags(双引号包裹的整串): entities/AIG.md [finance,insurance,entity,stub]→[金融,insurance], questions/为什么索罗斯做空英镑而非法郎.md→[索罗斯,ERM]
- 验证: YAML/frontmatter 错误=0, 残留 type/别名/年份=0, 超5标签=0, tags 内无 wikilink, git diff 仅改 tags 行
- 遗留: "金融" 补入 taxonomy canonical(归并目标); "保险" 补入 canonical(insurance 别名目标); ~120 个复用≥2 非 canonical 中文标签(国际金融/财政/欧盟/港股/估值 等)列为后续 taxonomy 扩充候选,本次未动(方案 B 不含扩充)

## [2026-08-07] WIKI_SYNTHESIZE | 第三轮:5 个交叉合成页(扩表/化债/QE × IMF/中国央行/2008)

- [2026-08-07T10:58:09+0800] WIKI_SYNTHESIZE pages_scanned=1019 synthesis_created=5 candidates_skipped=5
- 候选来源: 2026-08-06 第二轮跳过的 next-10 候选对,按共现度排序取前 5 (均未被既有合成页覆盖)
- Pages (共现页数):
  - synthesis/扩表与缩表 × IMF.md (c-001135, 31 页共现): 央行资产负债表(印钞,弹性无限)与 IMF 配额/SDR(谈判,封顶)是全球流动性的两个尺度; "有能力者无义务、有义务者无能力"决定央行救富国、IMF 救外围
  - synthesis/扩表与缩表 × 中国央行.md (c-001136, 29 页共现): 中国没有美联储式 QE/QT 二元,量工具靠准备金率(改乘数非资产负债表)、结构性靠 MLF/PSL; 真正的扩表在银行体系而非央行,化债是双层结构标本; 历史"缩表"是外生的(外储下降)而非主动 QT
  - synthesis/化债 × 2008全球金融危机.md (c-001137, 27 页共现): 两次银行杠杆处置方向相反——2008 市场爆破+央行扩表救助(银行是问题),化债国家置换+银行购债吸收(银行是方案),成本同为"三重损失"; 化债是"2008 的反方案"(简单替代复杂、绕道不救市)
  - synthesis/美联储 × IMF.md (c-001138, 27 页共现): 全球危机两个制度极点——美联储无国际授权但有印钞能力,IMF 有授权但资源封顶; "央行救富国、IMF 救外围"是制度倒置的产物; 中国兼具第三大配额国与互换体系外大国双重身份
  - synthesis/量化宽松 × 2008全球金融危机.md (c-001139, 27 页共现): 2008 完成 QE 的合法性转移(日本失败实验→全球标准动作); 危机规模+美联储信誉+零利率遗产三要素制度化 QE; 与既有合成页划清分工(非发明者史、非央行角色史,而是工具合法性史)
- Backlinks added to 7 anchors: 扩表与缩表(2: ×IMF, ×中国央行), IMF(2: ×扩表与缩表, ×美联储), 化债(1: ×2008), 2008全球金融危机(2: ×化债, ×量化宽松), 量化宽松(1: ×2008), 美联储(1: ×IMF), 中国央行(1: ×扩表与缩表)
- 地址计数器: 1134→1139
- Skipped (consider next time, 共现页数): 美联储×ECB(26), ECB×2008全球金融危机(26), 化债×财政货币化(25), 化债×中国央行(25), 美联储×化债(25)
- 待解问题浮出: IMF SDR 转借机制无系统落点、互换线(EM 被排除)与去美元化矛盾、中国化债下半场是否被迫打破央行"不直接买债"的线、QE 合法性在信息透明时代是否已通胀
- [2026-08-07T13:28:29+0800] QUERY query="IMF" result_pages=4 mode=normal escalated=false
- [2026-08-07T14:05:00+0800] QUERY query="IMF 对危机国救助是否白手套/是否应早干预/是否延迟行动另有政治营利目的" result_pages=6 mode=normal escalated=false
- [2026-08-07T14:20:00+0800] QUERY query="马来西亚如何应对1997年金融危机" result_pages=3 mode=normal escalated=false
- [2026-08-07T14:40:00+0800] INGEST topic="马来西亚模式" pages_created=1 pages_updated=3 mode=manual
- [2026-08-07T16:24:00+0800] GRAPH_COLORIZE mode=by-tag groups=10 backup=graph.json.backup-20260807-1624
- [2026-08-10T14:54:49+0800] QUERY query="美国为何帮助日本稳定日元汇率" result_pages=3 mode=normal escalated=false
- [2026-08-11] WIKI_RESEARCH topic="安倍经济学的政治属性评价" rounds=3 sources_fetched=6 pages_created=11
- [2026-08-12T09:17:01+0800] LINT issues_found=1952 orphans=22 broken_links=22 stale=372 contradictions=0 prov_issues=4 missing_summary=1018 fragmented_clusters=3 visibility_issues=0 promotion_candidates=0 synthesis_gaps=301 relationship_issues=0 missing_fm=6 no_lifecycle=1050 bad_lifecycle=6 trust_check=FAIL ledger_missing
- [2026-08-12T14:00:00+0800] WIKI_SYNTHESIZE pages_scanned=1019 synthesis_created=5 candidates_skipped=10 (美元霸权×去美元化 c-001178 / 扩表与缩表×央行入市干预 c-001179 / 1998香港金融保卫战×扩表与缩表 c-001180 / 美元周期×新兴市场危机 c-001181 / SK海力士×三星电子 c-001182; 9 源概念页回链, index 新增 5 条, 地址计数器 1178→1182)
- [2026-08-12T14:13:13+0800] GRAPH_COLORIZE mode=by-tag groups=10 backup=graph.json.backup-20260812-1413
- [2026-08-12T00:00:00+0800] QUERY query="日本政治民粹化" result_pages=7 mode=normal escalated=false
- [2026-08-14T13:57:14+0800] LINT issues_found=2213 orphans=0 broken_links=29 stale=64 contradictions=5 prov_issues=0 missing_summary=994 fragmented_clusters=17 visibility_issues=0 promotion_candidates=0 synthesis_gaps=28 relationship_issues=0 missing_fm=1 no_lifecycle=1047 bad_lifecycle=6 trust_check=FAIL ledger_missing addr_errors=16 duplicate_titles=6 index_gaps=871 (说明: 35 orphans 全为 41 个 redirect 存根; 64 stale 系 08-12 cross-linker 回链 bumped 源页 updated 所致; 6 处 broken 为 log.md 历史叙事链接)
- [2026-08-12] QUERY query="IMF 国际货币基金组织" result_pages=6 mode=normal escalated=false
