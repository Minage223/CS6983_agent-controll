---
name: pandas-bug
description: Debugged duplicated rows after a merge.
metadata:
  type: reference
  date: 2025-05-27
---
Duplicated rows after merging stop-level counts with a route table — cause was a many-to-many join on stop_id (stops served by multiple routes). Fixed with validate="many_to_one" and deduplicating the route table first.
