---
title: "金融WIKI 健康审计基线 2026-08-05"
category: skills
tags:
  - 维护
  - 知识库
  - 审计
  - 结构
summary: "全库 1000 页 lint 审计结果：孤儿清零、6 真实断链、lifecycle/base_confidence schema 全库未采用、synthesis 层空缺。"
tier: supporting
related: []
extends: null
contradicts: null
superseded_by: null
capture_source: claude-session
project: "金融WIKI"
base_confidence: 0.9
lifecycle: draft
lifecycle_changed: 2026-08-05
provenance:
  extracted: 0.9
  inferred: 0.1
sources:
  - "金融WIKI lint session (2026-08-05)"
---

## 全库扫描基线（2026-08-05）

扫描 1000 个内容页 / 11658 条 wikilink（排除 _archives、_raw、.obsidian）。结果：

- **孤儿页：0**（昨日 24 → 清零，git bc808dc 修复）
- **真实断链：6 目标**：`How does the LLM Wiki pattern work?`(hot.md)、`Claude Obsidian`/`Rankenstein`/`Karpathy LLM Wiki Pattern`(meta 会话页)、`dashboard.base`(meta/dashboard.md，Bases 配置无 .md 后缀，疑误报)、`raw/zhihu/日元保卫战…`(sources/2026-05-13，raw/ 镜像整体缺失)
- **frontmatter 缺口 615**：599 缺 tags（570 为 `tags: []` 空列表，存量 backlog）；13 缺 created/updated（房地产主题集群 12 概念页 + 1 source 页）；1 缺 type
- **stale >90 天：25 页**，全为 4 月迁入的 LLM-Wiki/SEO 生态说明页，非金融内容
- **summary 缺失：963/1000**（新字段存量未回填，软警告）

## 结构性发现

**1. lifecycle/base_confidence schema 全库 0/1000 采用**。vault 用的是旧 schema（`type` + `status` + `address`），与技能 Rule 12 强制 schema 完全不兼容——这是 schema 迁移决策，非逐页修补问题。

**2. synthesis/ 目录为空（仅 .gitkeep），但扫出 79 对高共现概念对**。top：扩表与缩表×化债(42 页)、扩表与缩表×2008全球金融危机(39)、量化宽松×扩表与缩表(38)、化债×财政货币化(23)。建议运行 /wiki-synthesize。

**3. index.md 声明 "Total pages: 58" 严重过时**，实际 1000 页，index 是策展子集（130 链接）。

## 工具注意

- 旧 `.vault-meta/lint-scan.py`/`lint-analyze.py` 硬编码迁移前路径 `金融知识库/wiki`，对扁平结构已失效；本次用临时脚本重写（/tmp/lint-wiki-2026-08-05.py）
- lint 报告自引会污染断链/孤儿统计，须排除 `meta/lint-report*` 来源
- git 中有 186 个文件未提交（+15899/−2389），为 bc808dc(14:22) 之后的批量 stub→current 扩写（mtime 14:27–15:07）
