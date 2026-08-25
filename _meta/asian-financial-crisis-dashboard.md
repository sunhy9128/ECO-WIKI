---
type: meta
title: "亚洲金融危机立体分析图谱"
updated: 2026-08-17
tags:
  - meta
  - dashboard
  - 亚洲金融危机
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
  - "[[concepts/1997亚洲金融危机]]"
---

# 亚洲金融危机立体分析图谱

> 动态 dashboard：以 [[concepts/1997亚洲金融危机]] 为核心 hub，从**事件战役层 → 国家应对层 → 机制工具层 → 人物机构层 → 研究问答层 → 源素材层**六个维度聚合全库相关页面。数据实时来自 vault，页面更新即自动反映。

## ① 事件与战役层（危机谱系全景）

1992 英镑 → 1994 墨西哥 → 1997 亚洲 → 1998 香港/俄罗斯/LTCM → 2022 斯里兰卡：同一套"货币危机谱系"的历次爆发与传导（[[concepts/美元潮汐历史案例]]）。

```dataview
TABLE WITHOUT ID
  file.link AS "事件/战役",
  status AS "状态",
  file.mtime AS "更新"
WHERE file.name IN ["1992欧洲货币危机", "1997亚洲金融危机", "1998香港金融保卫战", "1998 俄罗斯卢布危机", "1994 龙舌兰危机", "2022 斯里兰卡违约", "1998年LTCM危机", "1998香港金融保卫战 × 扩表与缩表"]
SORT file.name ASC
```

## ② 国家应对层（各国/地区应对矩阵）

马来西亚（管制买时间）、韩国（改革换信誉）、香港（储备换防御）、印尼（没选边）——三元悖论三种选边 + 失败样本（[[questions/马来西亚vs韩国vs香港应对1998金融危机]]）。

```dataview
TABLE WITHOUT ID
  file.link AS "页面",
  status AS "状态",
  file.mtime AS "更新"
WHERE file.name IN ["马来西亚模式", "马来西亚vs印尼应对1998金融危机", "马来西亚vs韩国vs香港应对1998金融危机", "韩国历史股灾谱系", "韩国综合指数(KOSPI)", "韩国央行(BOK)", "韩国金融监督院(FSS)", "港元", "联系汇率制度", "香港金管局", "2026-07-21-韩国股灾简史"]
SORT file.name ASC
```

## ③ 机制与工具层（危机机制/政策工具）

资本管制、央行入市、固定/浮动汇率、最后贷款人——理解"为什么这些国家用这些工具"的理论底座（[[concepts/资本管制]]、[[concepts/央行入市干预]]）。

```dataview
TABLE WITHOUT ID
  file.link AS "概念/机制",
  status AS "状态",
  file.mtime AS "更新"
WHERE file.name IN ["资本管制", "央行入市干预", "三元悖论", "汇率制度", "最后贷款人", "外汇储备", "亚洲金融危机传导机制", "蒙代尔-弗莱明模型", "汇率超调模型", "汇率传导机制", "中央银行外汇干预", "美元潮汐", "美元周期", "银行挤兑", "存款保险"]
SORT file.name ASC
```

## ④ 人物与机构层（投机者/央行/国际组织）

索罗斯"三战三例"的主角与对手盘：1992 英格兰银行 → 1997 亚洲央行 → 1998 香港金管局（[[concepts/1992欧洲货币危机]] §九）。

```dataview
TABLE WITHOUT ID
  file.link AS "人物/机构",
  status AS "状态",
  file.mtime AS "更新"
WHERE file.name IN ["索罗斯", "英格兰银行", "香港金管局", "IMF", "世界银行", "GIC", "鲁迪格·多恩布什", "朱镕基"]
SORT file.name ASC
```

## ⑤ 研究问答层（库内深度问答）

```dataview
TABLE WITHOUT ID
  file.link AS "问答/研究",
  status AS "状态",
  file.mtime AS "更新"
WHERE file.name IN ["为什么索罗斯做空英镑而非法郎", "索罗斯做空英镑的金融工具拆解", "美元收割全球的机制是什么", "研究：美元如何收割新兴市场", "新兴市场为避免被美国薅羊毛采取了哪些措施"]
SORT file.name ASC
```

## ⑥ 源素材层（原始素材/时间线）

```dataview
TABLE WITHOUT ID
  file.link AS "源素材",
  status AS "状态",
  file.mtime AS "更新"
WHERE file.name IN ["2019-11-25-香港金融保卫战-巫师财经", "2026-07-21-韩国股灾简史", "2025-02-04-中国粮食金融保卫战-巫师财经", "2026-08-03-美日联手干预日元-环球时报", "2026-08-04-干预汇市美日联手救日元-北京商报"]
SORT file.name ASC
```

## 使用说明

- 本图谱为**动态查询**：页面新增/更新/加标签后自动反映，无需手动维护
- 六个视图对应分析框架：**事件（发生了什么）→ 国家（谁怎么应对）→ 机制（为什么有效/无效）→ 主体（谁在博弈）→ 问答（沉淀结论）→ 源素材（一手资料）**
- 扩展图谱：在任一视图的 `IN [...]` 列表中加入新页面名即可

## 相关

- [[index]] — 全库目录
- [[log]] — 变更日志
- [[concepts/1997亚洲金融危机]] — 图谱核心 hub
- [[questions/马来西亚vs印尼应对1998金融危机]] / [[questions/马来西亚vs韩国vs香港应对1998金融危机]] — 国家应对结论层
