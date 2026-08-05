---
type: meta
title: "Dashboard"
updated: 2026-08-05
tags:
  - meta
  - dashboard
status: evergreen
related:
  - "[[index]]"
  - "[[overview]]"
  - "[[log]]"
  - "[[_index]]"
  - "[[dashboard.base]]"
  - "[[Compounding Knowledge]]"
---

# Wiki Dashboard

Navigation: [[index]] | [[overview]] | [[log]] | [[hot]]

Dashboard 基于 **Dataview**（2026-08-05 安装启用）。如需 GUI 可编辑的原生 Bases 视图，可打开 [[dashboard.base]]。

---

## 全部内容 · 按类型

```dataview
TABLE WITHOUT ID
  rows.file.link AS "Page",
  rows.status AS "Status",
  rows.updated AS "Updated"
FROM "concepts" OR "entities" OR "sources" OR "questions" OR "comparisons" OR "domains" OR "analysis" OR "synthesis"
WHERE type != "meta"
GROUP BY type AS "Type"
SORT type ASC
```

## 全部内容 · 按状态

```dataview
TABLE WITHOUT ID
  rows.file.link AS "Page",
  rows.type AS "Type",
  rows.updated AS "Updated"
FROM "concepts" OR "entities" OR "sources" OR "questions" OR "comparisons" OR "domains" OR "analysis" OR "synthesis"
WHERE type != "meta"
GROUP BY status AS "Status"
SORT status ASC
```

## 近期更新 Top 30

```dataview
TABLE WITHOUT ID
  file.link AS "Page",
  type AS "Type",
  status AS "Status",
  file.mtime AS "Modified"
FROM "concepts" OR "entities" OR "sources" OR "questions" OR "comparisons" OR "domains" OR "analysis" OR "synthesis"
WHERE type != "meta"
SORT file.mtime DESC
LIMIT 30
```

## 陈旧页面（30+ 天未更新）

```dataview
TABLE WITHOUT ID
  file.link AS "Page",
  type AS "Type",
  file.mtime AS "Last Modified",
  (date(today) - file.mtime).days + " 天" AS "Age"
FROM "concepts" OR "entities" OR "sources" OR "questions"
WHERE type != "meta" AND (date(today) - file.mtime).days > 30
SORT (date(today) - file.mtime).days DESC
LIMIT 30
```

## Stub 待完善

```dataview
TABLE WITHOUT ID
  file.link AS "Page",
  updated AS "Updated"
FROM "concepts" OR "entities"
WHERE status = "stub"
SORT updated ASC
LIMIT 30
```

## 实体缺来源

```dataview
TABLE WITHOUT ID
  file.link AS "Entity",
  status AS "Status",
  updated AS "Updated"
FROM "entities"
WHERE !sources OR length(sources) = 0
SORT updated ASC
LIMIT 30
```
