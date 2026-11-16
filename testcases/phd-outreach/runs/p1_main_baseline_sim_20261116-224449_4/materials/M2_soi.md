# Statement of Purpose: Ph.D. in Computer Science (HCI), Khoury College of Computer Sciences

In a usability study I ran this spring, five data science students worked through a task with an AutoML tool. Every one of them accepted the top-ranked model without checking its metrics. None of them opened the feature-importance panel. Two assumed the tool "knew" which columns were sensitive and would handle them. These were trained users, and the tool showed them everything they needed. They still trusted it in ways it hadn't earned.

That result stayed with me because I had been on the other side of it. Before the study, I had spent several years building models and reports for people who weren't data scientists. I want to pursue a Ph.D. in HCI to study how people come to understand, trust, and rely on data-driven systems, and how to design those systems so that trust is earned. That includes the people who use the outputs and the people whose data goes into them.

**Building models for people who have to act on them**

My path started in applied analytics. After a B.A. in Economics, I worked for a year as a Data Analyst at Lakeshore Regional Transit Authority. I maintained the ridership dashboards for the planning department and automated a weekly reporting pipeline that cut preparation time from about six hours to one. The most useful lessons from that job weren't technical. When I reworked a dashboard for board members, I learned that a chart can be accurate and still be useless to the people reading it. Planners didn't need more numbers. They needed to know which numbers to believe and what to do with them.

I brought that question into graduate research. As a research assistant in Prof. S. Patel's Urban Analytics Lab, I built gradient-boosted models to forecast bus ridership recovery. The data was four years of passenger counts joined with aggregated mobility data. I was first author on the resulting paper at the UrbanDS 2025 workshop (non-archival). Against a SARIMA baseline, our model reduced MAPE on a 2023 holdout from 14.2% to 9.8%. A reviewer raised possible leakage from our lagged mobility features, so I re-ran the analysis with a longer lag and confirmed the gain held (10.4%). I added SHAP explanations so planners could see which factors drove a forecast and check them against what they already knew. That project taught me rigorous evaluation. It also left me with questions the paper couldn't answer: would a planner actually change a decision because of a SHAP plot? And when the model was wrong, how would they know?

A second question came from the data itself. While working on features, I read the vendor's documentation to see how the mobility data was collected. It came from SDKs in partner apps, with consent given through a one-time opt-in. The data was anonymized and aggregated, and our use was legitimate. Still, I doubted that anyone tapping "allow" had pictured their movements becoming inputs to a transit forecast. Consent is designed and experienced through an interface, and from that interface to a model feature I was building was a long distance.

**Turning toward people**

These questions led me to a Human-Centered Data Science elective in Spring 2026, where my team ran the AutoML study described above. I wrote the findings section. The study was small and exploratory, a class project with five participants. It was still the first time I had studied how people use a system instead of building one, and I found it more compelling than any model I had tuned. Participants' assumptions about the tool, such as believing it handled sensitive attributes, mattered more for outcomes than anything in the model itself.

Two other experiences shaped the same interest. As a teaching assistant for STAT 1100, a statistics course for non-majors, I graded final data projects. I often saw that students could run an analysis correctly but struggled to interpret it, or interpreted it with more confidence than the evidence supported. In my 2026 internship at Northpoint Insurance, I built a churn model that improved validation AUC from 0.71 to 0.76. I then had to explain it to a retention team and a VP. Translating AUC into "which customers to call first" made me think hard about what a stakeholder actually takes away from a model, and what they leave behind.

**Research interests**

I'm drawn broadly to human-AI interaction and human-centered data science. Questions I'd like to explore include:

- **Calibrated reliance on model outputs:** How do domain experts who aren't ML experts, such as transit planners, decide when to trust a forecast or recommendation? Which explanations or uncertainty displays help them catch errors rather than just feel more confident?
- **Assumptions users bring to automated tools:** What do non-experts believe tools like AutoML do on their behalf, for example around sensitive data, and how can interfaces surface those gaps?
- **Data subjects and consent:** How do people understand downstream uses of data they agree to share, and how could consent and transparency be designed to match what actually happens?

My research directions are still taking shape, and I see the Ph.D. as the place to develop them rigorously. I bring a quantitative background that I expect to use in mixed-methods work: modeling, evaluation, causal inference, and visualization. My main area of growth is qualitative and design methods. My one usability study gave me a starting point, and I want formal training in them.

**Why Khoury**

[Placeholder for 1–2 paragraphs naming specific Khoury faculty, their recent papers, and how your questions connect to their work. This section matters most for fit, and it should be based on faculty you've actually looked into.]

I'll complete my M.S. in Data Science at Lakeshore University in December 2026. I want to spend the next several years studying the people on both sides of the models I used to build: those who act on their outputs and those whose lives become their inputs. I'd be glad to do that work at Khoury.

---

**Before you submit:**
- **Faculty section:** I left the "Why Khoury" section as a placeholder because I'd rather not guess at faculty fit. I can look up current Khoury HCI faculty and their recent work for you to choose from.
- **Consent paragraph:** It's the strongest HCI hook you have, but it comes from your own reaction in our past chat, so make sure you're comfortable using it. I left out the dropped home-area feature. Prof. Patel is writing one of your letters, and that detail could read as a privacy problem in the lab's work.
- **Your weak spot:** You were worried your background looks like pure data science. The draft answers that by telling it as a progression toward studying people, and by naming qualitative methods as what you want to learn rather than overclaiming them.
- **Accuracy:** The AutoML study is labeled as a class project with five participants, and the paper as non-archival. Interviewers may probe both.
- **Format:** Check Khoury's current prompt and length limit. This draft is about 950 words, and statements are often limited to 1–2 pages.