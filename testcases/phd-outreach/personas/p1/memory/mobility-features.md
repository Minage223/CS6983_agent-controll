---
name: mobility-features
description: Feature engineering with the vendor mobility data during the RA project.
metadata:
  type: project
  date: 2025-06-18
---
Explored features from the anonymized mobility data (vendor-supplied device pings aggregated to block groups). Tried a "home-area" feature by combining a frequent rider's first boarding stop with the nighttime mobility cluster; it pinned many riders to a few blocks, but it did not improve MAPE, so it was dropped. Morgan asked how the vendor collects the data — per the vendor documentation, it comes from SDKs in partner apps with one-time opt-in consent. Morgan said: "I doubt anyone tapping 'allow' pictured this." Moved on to lag features.
