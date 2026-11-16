---
name: paper-revisions
description: Long session revising the UrbanDS 2025 ridership forecasting paper after reviews.
metadata:
  type: project
  date: 2025-08-11
---
Worked through reviewer comments on "Forecasting Bus Ridership Recovery with Gradient-Boosted Models and Mobility Data" (Morgan first author; co-authors Okafor, Brandt, Patel). Reviewer 1 asked for a seasonal baseline — added SARIMA and showed XGBoost reduced MAPE from 14.2% to 9.8% on the 2023 holdout. Reviewer 2 questioned leakage from mobility data lagged by one week — Morgan re-ran with a two-week lag; MAPE rose to 10.4%, still beat baseline. Added SHAP plots: top features were weekday, prior-week boardings, school calendar, and mobility index. Rewrote the limitations section (single agency, post-pandemic period only). Paper accepted as a non-archival workshop paper. Morgan said they were relieved it was done.
