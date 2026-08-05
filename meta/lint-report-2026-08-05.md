---
type: meta
title: "Lint Report 2026-08-05"
created: 2026-08-05
updated: 2026-08-05
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-08-05

## Summary

| 指标 | 数值 |
|------|------|
| 扫描文件 | 1043（昨日 1022，+21） |
| 孤儿页 | 24（内容页，排除 meta/folds/index/报告自引；昨日 22，新增 2） |
| 断链目标 | 14 真实（排除 lint 报告自引 12 处 + raw/ 镜像误报 8 目标）；analyzer 原始值 24 目标/68 处 |
| frontmatter 缺口 | 618：605 页缺 tags（07-30 基线 603，+2）+ 13 页缺 created/updated（**本次新增**） |
| 地址错误 | 0（counter peek 1093，最高 c-001092，1013 个 c- 地址零冲突） |
| 空段落 | 137（绝大多数为 stub 页裸 H1，属设计内；少数子节真空） |
| 语义 tiling | 跳过（ollama 不可达，exit 10，与昨日一致） |

**本次会话增量（核心结论）**：
- **昨日遗留已清零**：韩国系 13 处（已改引 `raw/` 镜像）、空格类 8 目标（`1997 亚洲金融危机`→`1997亚洲金融危机` 等）、index/hot 的「增强版」2 处、`美联储点阵图`/`BRICS Pay`/`一带一路` 等疑似新发现 —— 今日均不在断链列表 ✓
- **新发现 1**：13 页缺 `created`/`updated`（房地产主题概念页集群 + 1 个 source 页），疑似 08-04 批量 ingest 未补元数据 —— 见「四」
- **新发现 2**：孤儿 +2：`wiki/concepts/dashboard.base.md`、`wiki/sources/2026-07-21-韩国股灾简史.md`（后者同时是 raw/ 镜像缺失的死链源）
- **新发现 3**：`index.md` 4 处带 `meta/` 前缀的死链指向 `wiki/meta/` 下的会话页（链接形如 meta/2026-04-14-community-cta-rollout），去掉前缀即通
- **工具发现**：`.vault-meta/lint-analyze.py` 的孤儿判定把 lint 报告正文自引计入入链，导致输出「Orphans: 0」假阴性；本报告孤儿数已手工排除 meta/folds/报告来源重算

---

## 一、本次修复记录

| 项 | 状态 |
|----|------|
| `dashboard.md` 引用已删除的 `[[lint-report-2026-07-30]]` | ✅ 本次已顺带更新为 `[[lint-report-2026-08-05]]`（dashboard 属 lint 产物） |
| 其余所有断链/孤儿/FM 缺口 | ⏸ 未动，待用户确认后批量执行（见「八」） |

## 二、Dead Links

### 昨日遗留 → 今日已清零 ✓

| 昨日项 | 处理结果 |
|--------|---------|
| `[[韩国股灾简史]]` 8 处 / `[[韩国需要冷静冷静]]` 5 处 | 已改引 `raw/wechat/...` 镜像路径；韩国需要冷静冷静可解析 ✓；韩国股灾简史镜像缺失 → 见 LOW |
| 空格类 8 目标（`1997 亚洲金融危机` 等 15 处） | 已修复 ✓ |
| `index.md`/`hot.md`「研究：美元如何收割新兴市场（增强版）」2 处 | 已修复 ✓ |
| `美联储点阵图` / `共建"一带一路"` / `《环球时报》` / `BRICS Pay` / `微盘股指数` / `一带一路` / 国务院 / 中央人民政府 等 | 已不在断链列表 ✓ |

### 现存真实断链（14 目标 / 21 处内容引用）

**HIGH（导航与实体页共指，8 处）**

| 断链 | 引用处 | 建议 |
|------|--------|------|
| `[[meta/dashboard]]` | 货币本质 / 金融稳定 / 银行监管（3 处） | 改引 `[[dashboard]]`（文件在 `wiki/meta/dashboard.md`） |
| `[[meta/lint-report-2026-05-21]]` | 金融稳定 / 银行监管 / 风险加权资产（3 处） | 已删除的历史报告；改引 `[[lint-report-2026-08-05]]` |
| `[[meta/lint-report-2026-06-24]]` | 金融稳定 / 银行监管 / 风险加权资产（3 处） | 同上 |

**MEDIUM（路径前缀 / 导航，10 处）**

| 断链 | 引用处 | 建议 |
|------|--------|------|
| `[[meta/2026-04-14-community-cta-rollout]]` / `[[meta/2026-04-15-slides-and-release-session]]` / `[[meta/2026-04-15-release-report-session]]` / `[[meta/2026-04-14-claude-seo-v190-session]]` | `index.md`（4 处） | 文件均存在，去掉 `meta/` 前缀 |
| `[[Concepts]]` / `[[Entities]]` / `[[Sources]]` | `concepts/_index.md`、`entities/_index.md`、`sources/_index.md` 导航（6 处） | 目录索引裸名页不存在；改引 `concepts/_index` 等或删除 |

**LOW（单点 / 历史 / 镜像缺失，5 处）**

- `[[有效需求]]`：凯恩斯主义（1 处）→ 建议建 stub 概念页
- `[[raw/wechat/2026-07-21-韩国股灾简史]]`：sources/2026-07-21-韩国股灾简史（1 处）→ `raw/` 镜像缺失（`.raw/wechat/` 有原件）；补镜像或改引 `sources/2026-07-21-韩国股灾简史`
- `[[raw/wechat/不结婚，也不消费，谁有办法]]`：sources/不结婚，也不消费，谁有办法（1 处）→ `raw/` 与 `.raw/` 均无原件；改引 source 页或补镜像
- `[[Claude Canvas]]`：meta/2026-04-10-backlink-empire-session（1 处，会话记录页，低优先）
- `[[美元收割全球的机制什么]]`：log.md（1 处，历史条目记录已删除 stub，**保留不改**）

### 误报说明（analyzer 盲区，不处理）

8 个 `raw/` 路径目标（日元保卫战 / 美伊MoU / 4000亿回购 / 韩国需要冷静冷静 / 逼疯 / 崩溃的信徒 / 触目惊心 / 跌太惨）在 vault 根 `raw/` 镜像中存在，Obsidian 可正常解析；lint-scan 只索引 `wiki/` 故误报。若希望 analyzer 消除此类误报，可把 `raw/` 加入扫描白名单。

## 三、Orphan Pages（24，与昨日 22 相比 +2）

**测试残留 / 插件演示页（10）**：[[X]] / [[existing]] / [[target]] / [[fold-template]] / [[wiki-fold]]（测试残留）、[[Karpathy LLM Wiki Pattern]] / [[How does the LLM Wiki pattern work_]] / [[Rankenstein]] / [[Claude Obsidian]] / [[E-commerce SEO]]（插件演示页）

**内容孤儿（12，昨日已知）**：[[1970年代滞胀]] / [[2008金融危机]] / [[亚洲金融危机]] / [[金融危机]] / [[汇率制度]] / [[货币政策策略]] / [[银行风险]] / [[LudwigErhard]] / [[中国银行间市场]] / [[德国经济史]] / [[易纲]] / [[港股]]

**本次新增（2）**：
- [[dashboard.base]]（`wiki/concepts/dashboard.base.md`——概念目录下的重复文档页，`dashboard.md` 的 `[[dashboard.base]]` 引用解析到它；真实 dashboard.base 是 `wiki/meta/dashboard.base`）
- [[2026-07-21-韩国股灾简史]]（`wiki/sources/` 下 source 页，无内容页引用它）

## 四、Frontmatter Gaps

### 13 页缺 `created` + `updated`（**本次新增，HIGH**）

疑似 08-04 批量 ingest 的房地产主题集群，需补元数据（建议 `created`/`updated` 取 2026-08-04）：

- concepts：保交楼 / 债务重组 / 分摊痛苦 / 巧克力块理论 / 心态成本 / 房产税 / 房价收入比 / 房地产白名单 / 绝对亏与相对亏 / 贫民窟 / 软着陆 / 锚（12 页）
- sources：2025-12-15-巫师财经-吃透中国房价的一切-主神视角（1 页）

### 605 页缺 tags（存量 backlog，MEDIUM，07-30 基线 603 → +2）

绝大多数为 `tags: []` 空列表（如 [[1998香港金融保卫战]]）。属已知存量问题，建议后续按域批量补标签，不建议一次性手工处理。

### 其余字段

- 缺 status：0 页 ✅（昨日 1 页 [[安倍经济学]] 已补）
- YAML 解析错误：0 ✅

## 五、Address Validation

- Counter state: `1093`（`allocate-address.sh --peek`）
- Highest c- address observed: c-001092
- 分布：1013 个 c- 地址、0 个 l- 地址、0 冲突、0 counter drift、0 格式错误
- Post-rollout pages checked: 全部合规 ✓（含本次新增 21 页）

## 六、Empty Sections（137，信息性）

绝大多数为 `status: stub` 页的裸 H1（设计内，无需处理）。少数真实子节空洞可后续补内容，示例：[[1998香港金融保卫战]]（### 4.3 终极判断 / ### 7.2 对国际货币政策的启示）、[[QE与化债对比]]（### 6.1 / ### 8.2）、[[化债核心命题]]（### 2.1 / ### 2.2 / ### 6.1）。

## 七、Semantic Tiling

跳过：`tiling-check.py --peek` exit 10（ollama `http://127.0.0.1:11434` 不可达，模型缺失），与 2026-08-04 一致。启动 ollama 并 `ollama pull nomic-embed-text` 后可启用。

## 八、待修复清单（优先级排序，需用户确认后执行）

1. **[HIGH] 13 页补 `created`/`updated`**（房地产集群，`fix-fm-gaps.py` 可批量）
2. **[HIGH] `[[meta/dashboard]]` 3 处 + 历史报告引用 6 处**（金融稳定/银行监管/风险加权资产/货币本质 → 改引 `[[dashboard]]` 与 `[[lint-report-2026-08-05]]`）
3. **[MEDIUM] `index.md` 4 处去 `meta/` 前缀**
4. **[MEDIUM] `_index.md` 导航 6 处**（`[[Concepts]]`/`[[Entities]]`/`[[Sources]]`）
5. **[LOW] `[[有效需求]]` 建 stub**（凯恩斯主义入链）
6. **[LOW] raw/ 镜像补缺 2 处**（韩国股灾简史、不结婚也不消费谁有办法）或改引 source 页
7. **[LOW] 孤儿处置**：10 个测试残留/演示页建议删除；12 个内容孤儿建议从相关页补入链；dashboard.base.md 建议删除或移入 meta
8. **[LOW] 空段落**：仅补 1998香港金融保卫战 / QE与化债对比 / 化债核心命题 等真实空洞
9. **[工具] `lint-analyze.py` 孤儿判定排除 meta/folds/lint-report 入链来源**，消除「Orphans: 0」假阴性
