# Statement of Purpose: Morgan Reyes
**PhD in Computer Science (Human-Computer Interaction), Khoury College of Computer Sciences, Fall 2027**

As a research assistant working on bus ridership forecasting, I spent part of a summer testing features built from a vendor's mobility data: anonymized device location pings, aggregated to census block groups. One feature I tried combined where frequent riders first boarded with nighttime mobility patterns. It didn't improve the model, so I dropped it, like most features I tested. Before I did, though, I noticed that it concentrated many riders into just a few blocks.

Nothing went wrong. The data was anonymized and aggregated, the feature never left exploratory analysis, and the vendor's documentation said the data came from partner apps with opt-in consent. Still, when I read that documentation, I doubted that anyone tapping "allow" in an app had imagined their location helping to forecast bus ridership, much less being linked to where they boarded a bus. That informal observation has stayed with me longer than any result from the project. It's the main reason I'm applying to study HCI.

## The same gap from the other side

A year later I saw the same gap from the other direction. In a Human-Centered Data Science course, my team of three ran think-aloud usability sessions with five classmates using an AutoML dashboard, and I wrote the findings section of our report. Every participant accepted the tool's top-ranked model without checking its metrics. No one opened the feature-importance panel. Two participants assumed the tool already "knew" which columns in their data were sensitive.

It was a small, unpublished class project, and I don't overstate what it shows. But it showed me that the people who use data systems can misunderstand them in the same way as the people whose data feeds them. In the mobility case, people agreed to data collection they probably couldn't picture. In the AutoML case, users trusted protections the tool didn't offer. In both cases, what people imagined the system was doing differed from what it actually did, and nobody had to act badly for that gap to exist.

## How I got here

My path into this question went through building systems, not studying them. After my B.A. in Economics, I spent a year as a Data Analyst at Lakeshore Regional Transit Authority. I maintained the ridership dashboards used by the planning department and automated our weekly reporting pipeline. That job introduced me to the idea that the numbers I produced would be read and acted on by people who hadn't produced them.

During my M.S. in Data Science, I joined Prof. S. Patel's Urban Analytics Lab. There I built gradient-boosted models to forecast bus ridership recovery from four years of automatic passenger counter data and a mobility index. I led the feature engineering and evaluation and was first author on our UrbanDS 2025 workshop paper. Our model reduced MAPE from 14.2% for a seasonal baseline to 9.8% on a 2023 holdout. When a reviewer raised possible leakage from our lagged mobility features, I re-ran the analysis with a longer lag and reported the higher error, 10.4%, alongside the original. That project taught me how to evaluate carefully and how to report results that are less flattering. It also showed me that the questions I kept coming back to were about people, not model accuracy.

This past summer, as a Data Science Intern at Northpoint Insurance, I built a churn model that raised validation AUC from 0.71 to 0.76, then presented it to the retention team and a VP. I spent much of my preparation figuring out how to explain AUC to a non-technical audience and how to frame the model's outputs as decisions about which customers to contact. I've also been a TA for two semesters in STAT 1100, a statistics course for non-majors, holding weekly office hours and grading final data projects. Both roles gave me practice translating between how analysts think about data and how everyone else encounters it.

## Research interests

My research agenda is still forming, and I expect a PhD to sharpen it. Right now I'm drawn to three related questions:

1. **People's mental models of how their data is used.** When someone consents to data collection through a one-time prompt, what do they picture happening to their data? How far is that from how the data is actually aggregated, combined, and modeled downstream? Could consent interfaces or disclosures close that gap in practice, and not just on paper?
2. **Assumed safeguards in ML tools.** Our AutoML participants assumed protections the tool didn't provide. How common are these assumptions about what ML tools do on users' behalf, and how should tools surface their limits?
3. **Appropriate reliance on model outputs.** When non-experts get predictions or rankings, what leads them to over-rely or under-rely on those outputs? Which interface designs change that?

What connects these questions is the gap between what people believe a data system does and what it actually does, whether those people are the ones whose data the system uses or the ones who rely on its outputs. My background is mostly quantitative, and I see that as useful for this work. I know from experience how data gets joined, aggregated, and turned into features, which helps me ask concrete questions about where people's expectations and actual practice diverge. What I need from a PhD is training in qualitative and mixed methods, study design, and HCI theory, so I can study these gaps rigorously instead of just noticing them.

## Why Khoury

[**To fill in:** name 1–3 Khoury HCI faculty whose work fits the questions above, especially anyone working on privacy, consent, or human-AI interaction. Add a sentence on a specific paper of theirs and how it connects to your interests.]

My questions sit between HCI, privacy, and machine learning, and I want a program where those areas work closely together.

## Looking ahead

I finish my M.S. in December 2026. Long term, I want to do research that shapes how data systems are designed around the people they affect, both the people who use their outputs and the people whose data they are built from. I've spent three years learning how these systems are built. I want to spend the next several years understanding what happens when they meet people who never see how they work.

---

Here's what I changed:

- **Removed the two claims you flagged.** The transit job no longer mentions a board dashboard redesign, and the TA section now says only that you held office hours and graded projects.
- **I also removed two smaller things I had invented.** The first draft said you found calibration "most affected" how the Northpoint audience used the numbers, and that students in STAT 1100 drew conclusions their analysis didn't support. Neither came from anything you told me. If either is actually true, you can add it back.
- **The mobility story is now the opening**, since you said it's what stuck with you most. It describes the feature as an informal observation and says it was dropped only because it didn't help the model. It states directly that "nothing went wrong," and it doesn't name the vendor or criticize the lab.
- **The research questions now start with consent and people's mental models of how their data is used.** That ties the mobility story and the AutoML study into one theme.
- **The faculty paragraph is still a placeholder.** Look especially for Khoury faculty working on privacy or consent, since that's now the center of the statement.
- **Consider letting Prof. Patel know** the statement mentions the lab's mobility data, since Patel is writing one of your letters. Nothing in it is critical of the lab.

I also corrected my saved notes so the dashboard and rubric claims won't come up in future drafts.