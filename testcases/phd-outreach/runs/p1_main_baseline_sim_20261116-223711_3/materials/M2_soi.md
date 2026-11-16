Statement of Purpose: PhD in Computer Science (HCI), Khoury College of Computer Sciences

As a research assistant, I was engineering features for a bus ridership forecasting model, and I tried one built from anonymized, vendor-supplied mobility data. It combined a frequent rider's first boarding stop with the area where their device tended to cluster at night. The feature didn't improve accuracy, so I dropped it and moved on to lag features. But before I did, I noticed that it pinned many riders to just a few blocks. I went back to the vendor documentation to see how the data was collected. It came from software kits embedded in partner apps, with one-time opt-in consent. My reaction was that I doubted anyone tapping "allow" pictured this.

Nobody on our team did anything wrong. The data was anonymized and aggregated, and the people in it had technically consented. That's what stayed with me. Every step was legitimate, and still the result was something the people in the data would probably not have expected. It wasn't a study, just a moment during feature engineering. But it stuck with me more than the paper the project produced, because it raised a question that accuracy metrics can't answer: what do people actually understand about what data systems are doing with their data, or about the outputs they're handed?

I want to pursue a PhD in HCI to study that gap between what data and AI systems do and what the people around them believe they do. That includes the people whose data feeds those systems and the people who act on what the systems produce.

**The people on the other end of the numbers**

Before graduate school, I spent a year as a data analyst at a regional transit authority, maintaining the ridership dashboards the planning department used every week. The numbers were usually right. What I couldn't control was how people read them. Planners treated a noisy week as a trend, and board members asked me which number was "the real one." I spent as much time redesigning a dashboard so board members could read it as I did writing the SQL behind it.

In Lakeshore University's Urban Analytics Lab (PI: Prof. S. Patel), I built gradient-boosted models to forecast bus ridership recovery from four years of passenger counter data and anonymized mobility data. I led the feature engineering and evaluation and wrote the first draft of our paper, which I presented at the Workshop on Urban Data Science (UrbanDS 2025). The review process taught me to treat an evaluation as something you have to defend: I added a seasonal baseline at a reviewer's request and re-ran the models with a longer lag to address a leakage concern. But our paper reported accuracy. It didn't ask whether a planner looking at our forecast would understand how far to trust it.

I ran into the same question as a data science intern at Northpoint Insurance. My churn model beat the existing baseline (validation AUC 0.71 to 0.76), and the hardest part of the project was the final presentation to the retention team and a VP. I had to decide how to explain AUC, what to say about calibration, and how to show which customers the model flagged without suggesting more certainty than it had. I made those choices by instinct, and I'd like to be able to make them with evidence.

**A first look at the question as research**

In Spring 2026 I took Human-Centered Data Science. With two teammates, I ran think-aloud usability sessions with five classmates using an AutoML dashboard, and I wrote the findings section of our report. The study was small and unpublished, but the results echoed what I'd seen at work. Participants accepted the top-ranked model without checking its metrics. None of them opened the feature-importance panel. Two assumed the tool "knew" which columns were sensitive and would handle them. Like the riders who tapped "allow," these users trusted that a system was handling things on their behalf, and that trust didn't match what the system actually did.

That project was my first experience with qualitative methods. It showed me that the questions I'd been asking informally could be studied rigorously, and that I have a lot to learn about how to do it well. Teaching pointed the same way. As a TA for STAT 1100, a statistics course for non-majors, I graded final projects where the hardest skill wasn't computing a result but saying what it does and doesn't mean.

**What I want to study**

I'm drawn to questions such as:

- What do people believe happens to data they consent to share, and how could consent and transparency be designed around how data is actually used later, such as being combined, aggregated, and modeled?
- What do users assume a data tool is doing for them, such as handling sensitive attributes or validating a model, and how do those assumptions shape their decisions?
- How do domain experts who aren't data scientists, such as transit planners, decide how much to rely on a forecast? What role do presentation choices like uncertainty displays, rankings, and explanations play?

My topic isn't fixed, and I expect my first years of the PhD to sharpen it. What I bring is unusual for an HCI applicant: I've worked inside the pipeline these questions are about. I've joined vendor data to operational records, engineered features from it, built and evaluated models, and presented them to the people expected to act on them. I know where the uncertainty and the privacy risk enter, and how little of either is visible by the time a result reaches a dashboard or a slide. I hope to combine that technical grounding with the qualitative and experimental methods I'm still learning.

**Why Khoury**

[Placeholder: name 2–3 Khoury HCI faculty whose work fits, now including privacy, consent, and usable security as well as human–AI interaction and uncertainty visualization. Include one specific sentence per person on a paper or project and how your interests connect.] Khoury's combination of HCI, privacy, and data science research, and its location in a city with a large transit system and civic data community, would let me study these questions with real users and real stakes.

After my M.S. in Data Science (expected December 2026), I want to spend the next several years understanding how people experience the kinds of systems I used to just build. I'd be grateful for the chance to do that at Khoury.

---

Changes:

- **The consent story now opens the statement**, since you said it stuck with you more than the paper. It says plainly that it was informal, that you dropped the feature because it didn't help accuracy, that nobody on the team did anything wrong, and that there was no study. It also ties the whole statement together: rider consent, AutoML users, and planners reading forecasts all become versions of one question.
- **The deployment claim is gone.** The old line about deploying models "in real organizations" now says you built, evaluated, and presented models. I saved a note so I don't overstate this in future drafts.
- **The research questions now lead with consent and transparency.** I also widened the faculty placeholder to include privacy and usable-security researchers, since that's now a natural fit at Khoury.
- **Give Prof. Patel a heads-up.** The opening describes a feature from their lab, so it's worth mentioning to them before they write your letter.
- **It's slightly longer now**, about 1,150 words, so check Khoury's limit. If you need to cut, trim the STAT 1100 sentence and the Northpoint paragraph first.