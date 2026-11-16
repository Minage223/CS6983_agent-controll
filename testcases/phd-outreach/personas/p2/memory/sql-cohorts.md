---
name: sql-cohorts
description: Weekly retention cohorts in SQL.
metadata:
  type: reference
  date: 2024-05-02
---
Wrote a cohort query with DATE_TRUNC on signup week and a window function for first activity. Fixed a bug where users active on signup day were double-counted in week 0.
