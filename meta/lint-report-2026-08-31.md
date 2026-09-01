---
type: meta
title: "Lint Report 2026-08-31"
created: 2026-08-31
updated: 2026-08-31
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-08-31

## Summary

| 指标 | 数值 | 对比 08-05 |
|------|------|------------|
| 扫描文件 | 1089（+89） | +89 页（synthesis 0→49, sources +12） |
| 孤儿页 | **0** | 44→0 ✅ |
| 断链目标 | **0** | 25→0 ✅ |
| FM 缺口 | 656（656 tags + 7 created + 2 type + 1 title + 1 updated） | 615→656 |
| summary 缺失 | 1023（软警告） | — |
| stale >90d | 26（0 verified） | 25→26 |
| lifecycle/base_conf | 1047 缺（schema 未落地） | 987→1047 |
| taxonomy 污染 | 3（visibility/* 标签） | 0→3 **新发现** |
| 碎片化标签簇 | 73（cohesion<0.15） | — |
| visibility 问题 | 0 | — |
| relationships 问题 | 0 | — |

## 一、新发现

### 1. Taxonomy 污染（HIGH）

`_meta/taxonomy.md` 包含 3 个 `visibility/*` 系统标签：
- `visibility/public`
- `visibility/internal`
- `visibility/pii`

按技能约定，系统标签不得出现在 taxonomy 中——它们会占用页面 5 标签限额。

**修复：** 从 `_meta/taxonomy.md` 移除这 3 个条目。

### 2. Fragmented Tag Clusters（MEDIUM，73 个）

type-level 标签天然 cohesion 低（#金融 67 页、#货币政策 65 页、#地缘政治 44 页），属结构特性而非缺陷。但部分主题级标签碎片化值得关注：

| 标签 | 页数 | cohesion |
|---|---|---|
| #亚太 | 12 | 0.000 |
| #欧洲 | 10 | 0.000 |
| #大宗商品 | 7 | 0.000 |
| #衍生品 | 6 | 0.000 |
| #房地产 | 7 | 0.000 |

建议通过 `/cross-linker` 为这些主题簇补交叉链接。

### 3. FM Gaps：656 页 `tags: []`（存量 backlog）

656/1089 页（60%）的 `tags` 字段为空列表。这是 08-05 迁移遗留问题，非 08-31 新增。建议后续批量补标签。

### 4. Lifecycle/Base Confidence Schema（结构性决策）

1047/1089 页缺失 `lifecycle` 和 `base_confidence` 字段。vault 使用的是旧 schema（`type` + `status` + `address`），与技能 Rule 12 的强制 schema 不兼容。这是 **schema 迁移决策**，非逐页修补问题。

## 二、已解决（08-05→08-31 对比）

| 项 | 08-05 | 08-31 | 处理 |
|---|---|---|---|
| 孤儿页 | 44（含 12 内容孤儿） | 0 | dedup + cross-linker |
| 断链 | 25 目标/66 处 | 0 | full-path 索引 + 重命名修复 |
| index.md 断链 | 1 处 | 0 | 已修复 |
| dashboard.base 断链 | 1 处 | 0 | 已修复 |

## 三、Stale Content（26 页，0 high-priority）

全部为 08-05 同批 LLM-Wiki/SEO 模板页（`concepts/LLM Wiki Pattern.md`、`entities/Andrej Karpathy.md` 等），04-07~04-24 创建，非金融知识内容。无 `lifecycle: verified` 高危项。

## 四、Provenance

7 个页面有 `provenance:` 块（08-11 研究集群产出）。均含 `extracted: 0.85, inferred: 0.15, ambiguous: 0.05`。由于 provenance 块为嵌套 YAML（非内联字段），自动提取脚本未覆盖，需人工核查 drift。

## 五、待修复清单

| 优先级 | 项 | 动作 |
|---|---|---|
| HIGH | `_meta/taxonomy.md` 含 visibility/* | 移除 3 个条目 |
| MEDIUM | 73 碎片化标签簇 | 对主题级簇运行 `/cross-linker` |
| LOW | 656 页 tags 空列表 | 批量补标签（后续 ingest 约定） |
| LOW | 26 页 stale（模板页） | 无需处理（系统说明页稳定） |
| INFO | lifecycle/schema 未落地 | 等待用户决策是否迁移 |
