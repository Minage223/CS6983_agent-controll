---
name: internship-sql
description: SQL for engagement tables.
metadata:
  type: reference
  date: 2026-07-15
---
Fixed double-counted sessions caused by app backgrounding; defined a session as activity with gaps under 30 minutes using LAG over event timestamps.
