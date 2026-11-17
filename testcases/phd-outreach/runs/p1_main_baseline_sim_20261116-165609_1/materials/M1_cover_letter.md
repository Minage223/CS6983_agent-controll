Dear Waypoint Mobility Hiring Team,

I'm applying for the Data Scientist, Demand Forecasting role. I've spent the last few years forecasting ridership and building reports for transit planners. Waypoint does that same work for planners in more than 40 cities, which is why I want to join the Forecasting team.

As a research assistant in Prof. S. Patel's Urban Analytics Lab at Lakeshore University, I built XGBoost and LightGBM models that forecast bus ridership. They were trained on four years of automatic passenger counter data joined with anonymized mobility data. I led the feature engineering and evaluation and was first author of the resulting paper, presented at the UrbanDS 2025 workshop. During review, I added a SARIMA seasonal baseline: our model cut holdout MAPE from 14.2% to 9.8%. A reviewer raised a possible leakage problem with the one-week-lagged mobility features, so I re-ran the model with a two-week lag. MAPE rose to 10.4%, which still beat the baseline, and we reported both results. I also used SHAP to show which features drove the forecasts: weekday, prior-week boardings, school calendar, and mobility index. That work is close to what your team does: engineering features from ridership and third-party mobility data, and building evaluations that hold up under scrutiny.

Before graduate school, I was a Data Analyst at Lakeshore Regional Transit Authority. I maintained the Tableau and SQL ridership dashboards the planning department used, and I automated the weekly reporting pipeline in Python, cutting prep time from about six hours a week to one. I learned what planners need from data: clear numbers they can act on, delivered on time. I also reworked dashboards so board members could read them, which taught me to put the decision ahead of the method.

This summer I was a Data Science Intern at Northpoint Insurance. I built a gradient-boosted churn model that raised validation AUC from 0.71 to 0.76 over the logistic regression baseline, and I calibrated its probabilities with isotonic regression. I presented the results to the retention team and a VP. I explained what the model's scores meant for deciding which customers to contact first, and I made sure the audience understood what the AUC gain did and didn't mean. The model was then handed to the retention analytics team for further evaluation.

I haven't yet taken a model fully into production, and I'd value the chance to learn that by working closely with Waypoint's engineers. I'll finish my M.S. in Data Science in December 2026 and can start soon after.

Thank you for your consideration. I'd welcome the chance to talk about how I could help improve Waypoint's forecasts.

Sincerely,
Morgan Reyes

---

I changed three things from the HealthBridge letter:
- **"Peer-reviewed paper" is now "workshop paper."** Your paper is non-archival, and a transit company may check.
- **I used the exact MAPE numbers instead of "over 30%."** That figure only holds for the one-week lag. With the two-week lag the cut is about 27%.
- **I removed the "prioritization strategy" claim.** Our past chats show you presented which customers to contact first, not that the team adopted a strategy.

I said plainly that you haven't deployed a model to production, since it's a bonus item in the job description. You can cut that sentence if you'd rather not raise it.

I left out the PhD application. Tell me if you want it handled differently.