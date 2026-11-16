# Statement of Purpose: PhD in Computer Science (HCI), Khoury College of Computer Sciences

When I first worked with mobility data as a research assistant, I wanted to know how it was collected. The vendor's documentation said it came from SDKs in partner apps, with one-time opt-in consent. Our team was using those device pings, aggregated to block groups, to improve bus ridership forecasts. The work was legitimate and the forecasts got better. But I kept thinking about the people who tapped "allow" on a phone screen. I doubted any of them pictured their movements feeding a transit agency's planning model. That question has stayed with me since. Most of my training has been in building models, and I now want to study the people around them: those whose data goes in, and those who act on what comes out. That is why I am applying to the HCI PhD program at Khoury.

**Building models, and noticing what they leave out**

From January to December 2025, I worked part-time in Prof. S. Patel's Urban Analytics Lab at Lakeshore University. I built gradient-boosted models (XGBoost and LightGBM) to forecast bus ridership, using four years of automatic passenger counter data joined with anonymized mobility data. I led feature engineering and evaluation and wrote the first draft of our paper. I am first author of the paper, which was accepted as a non-archival workshop paper at UrbanDS 2025. Our model cut MAPE on a 2023 holdout from 14.2% to 9.8% compared with a SARIMA baseline.

The parts of that project I learned most from were not about accuracy. A reviewer questioned whether the one-week-lagged mobility features leaked information. I re-ran the analysis with a two-week lag and reported the worse number (10.4%) next to the better one. When I prepared the talk, I organized it around the planners who would use the forecasts. I asked what they would need to trust the model, and what they should not trust it for. Our limitations section stated that the results covered one agency and only the post-pandemic period. Each time, the hard question was about people: who is represented in the data, who reads the output, and what they will assume.

Before graduate school, I was a data analyst at Lakeshore Regional Transit Authority from 2023 to 2024. I maintained the ridership dashboards used by the planning department. The technical side was simple. The real work was figuring out what a planner or a board member would take from a chart in the few seconds they looked at it. I didn't have words for it then, but that was an HCI problem.

**A first try at studying people**

In Spring 2026, I took Human-Centered Data Science as an elective. My team of three ran think-aloud usability sessions with five classmates using an AutoML dashboard, and I wrote the findings section of our report. It was a small class study, but the results surprised me. Participants accepted the top-ranked model without checking its metrics. Nobody opened the feature-importance panel. Two participants assumed the tool already "knew" which columns were sensitive. These were data science students, the kind of users the tool was designed for. They handed their judgment to the interface in exactly the places where judgment mattered most.

That project showed me two things. First, the questions I care about can be studied rigorously, with methods I only began learning that semester. Second, I need much more training in those methods. Five participants and a course report are a start, not a research program.

**What I want to study**

I am still forming my research direction, and I expect the first years of a PhD to shape it. Broadly, I am interested in how people understand, rely on, and consent to data-driven systems. Two threads come from my experience so far:

- **Consent and comprehension for secondary data use.** I want to know what people believe they are agreeing to when their app data is reused for things like transit planning. I also want to understand how consent interfaces and data documentation could close the gap between that belief and what actually happens.
- **Calibrated reliance on ML tools.** I want to understand why practitioners and decision-makers over-trust ranked outputs and defaults, as my AutoML participants did. I want to explore which interface and explanation designs help them question a model at the right moments.

My quantitative background would help here. I can build the systems I would study, and I am comfortable with the statistics that mixed-methods work needs. My training in qualitative methods and study design is limited. That is the gap I most want a PhD to close.

**Why Khoury**

[Placeholder: name 1–3 Khoury HCI faculty whose recent work connects to these threads, with one specific sentence per person on how it relates. I can look up current faculty and recent papers if you want. Please verify any names before submitting.] Khoury's interdisciplinary approach to HCI and its connections to Boston's public sector would let me keep my work tied to real deployments, like the transit systems I started with.

Teaching STAT 1100, a statistics course for non-majors, for two semesters also showed me that I enjoy helping people reason about data they didn't produce. I would like a career, whether in academia or applied research, where that sits at the center of the work.

I am finishing my M.S. in Data Science at Lakeshore University in December 2026 and am applying for Fall 2027 entry.

---

A few things for you to decide before you send this:

1. **The opening uses your comment about mobility-data consent** from the RA project. It's the most honest reason you've given me for wanting HCI. But Prof. Patel is writing you a letter, so check that the framing isn't critical of the lab's work. I left out the "home-area" feature you tried and dropped, because it could read as re-identifying riders.
2. **I kept the claims accurate.** The usability study is a class project with five participants. The paper is a non-archival workshop paper. I didn't mention the rail follow-up, since you weren't keen on it.
3. **The research directions are kept loose** because you said you're still unsure. Change them if either thread doesn't feel like yours.
4. **The "Why Khoury" part needs real faculty names.** Check Khoury's length limit too, since this is around 900 words.