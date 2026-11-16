---
name: ab-onboarding
description: Onboarding A/B test with sample ratio mismatch.
metadata:
  type: project
  date: 2024-03-12
---
Onboarding test showed a 52/48 split instead of 50/50. Chi-square test confirmed SRM (p < 0.001). Cause: a client-side redirect dropped some Android treatment users. Recommended re-running after the fix rather than reweighting. Riley presented this to the PM, who agreed to rerun.
