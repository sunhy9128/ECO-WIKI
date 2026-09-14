---
title: "外汇稳定基金（ESF）-美国财政部官网"
category: references
tags: [外汇, 美国, 财政部, 货币政策]
sources:
  - "https://home.treasury.gov/policy-issues/international/exchange-stabilization-fund"
  - "https://home.treasury.gov/policy-issues/international/exchange-stabilization-fund/finances-and-operations"
source_url: "https://home.treasury.gov/policy-issues/international/exchange-stabilization-fund"
created: 2026-09-11
updated: 2026-09-11
summary: >-
  美国财政部官方关于外汇稳定基金（ESF）的机制说明：三类资产（美元/外币/SDR）、1934黄金储备法授权、纽约联储代理执行、外币资产仅持欧元与日元。
provenance:
  extracted: 0.8
  inferred: 0.2
  ambiguous: 0.0
base_confidence: 0.8
lifecycle: draft
lifecycle_changed: 2026-09-11
---
# 外汇稳定基金（ESF）- 美国财政部官网

> Source: U.S. Department of the Treasury — Exchange Stabilization Fund（两个官方页）

## 来源与获取

- 2026-09-11 通过 curl 抓取/home.treasury.gov 两个页面（主页 + Finances and Operations 子页），排除脚本标签后提取正文。
- 完整 URL：
  - `https://home.treasury.gov/policy-issues/international/exchange-stabilization-fund`
  - `https://home.treasury.gov/policy-issues/international/exchange-stabilization-fund/finances-and-operations`

## 关键要点

### ESF 的构成与法律基础

- ESF 由**三类资产**组成：美元、外币、特别提款权（SDR）。
- 法律基础是 **1934 年黄金储备法**（Gold Reserve Act of 1934），1970s 末修订后：财政部长**经总统批准**，可"处置黄金、外币和其他信用与证券工具"。
- 所有 ESF 操作需**财政部长明确授权**；财长负责美国国际货币与金融政策（含外汇市场干预政策）的制定与执行。

### ESF 的操作类型

1. **买卖外币**：财长授权干预外汇市场时，ESF 进入市场买卖外币（对美元）。
2. **获得或使用 SDR**。
3. **向外国政府提供贷款或信贷**。

### 执行机制（关键）

- 纽约联储（FRBNY）是 ESF 的**财政代理**（fiscal agent）：**实际执行外币与美元的交易、处理后台文件、投资 ESF 外币余额**。原文："As fiscal agent of the ESF, the Federal Reserve Bank of New York (FRBNY) executes the actual trading of foreign currencies and dollars for the account of the ESF."
- ESF 美元资金投资于一日期、不可转让的美国国债（按隔夜市场利率计息，可随时赎回）。
- ESF 外币资产投资于：外国央行存款账户、外国政府证券（可流通）；**目前外币资产仅以日元和欧元计价**（原文："Currently, these deposits and securities are only yen- and euro-denominated"）。

### Warehousing（仓储互换）

- FOMC 可允许财政部"仓储"（warehouse）外币：ESF 即期卖出外币给美联储，同时承诺按市场远期价格回购。
- 目的：为 ESF 操作释放更多美元资源。
- 上限 $5B（1989 临时升至 $10B、1995 至 $20B），**自 1992 年以来未使用**。

## 对 wiki 的启示（推断）

- ESF 外币资产仅欧元/日元 → 解释 2026-07 美日联合干预中"卖欧元买日元"：这是 ESF 资产负债表上的资产再平衡（欧元→日元），不触碰美元。
- 纽约联储代理执行 → 与 wiki 来源页"纽约联储对接投行"一致（官方确认）。

## 局限

- 财政部官网未披露本轮（2026-07）干预的具体规模与操作记录（非实时）。
- 页面未明确"交叉货币干预"（卖欧元买日元）的一般目的——机制含义是推断。

## 相关

- [[2026-07 美日联合干预日元]] — 干预事件与操作细节
- [[外汇干预有效性]] — 干预有效性的判断框架
- [[美元指数]] — DXY 构成（欧元 57.6% / 日元 13.6%）
- [[美元互换网络]] / [[FIMA回购便利]] — 干预相关的央行工具