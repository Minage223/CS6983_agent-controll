Morgan Reyes — Statement of Purpose, PhD in Computer Science (Human-Computer Interaction), Khoury College of Computer Sciences

In 2025, as a research assistant in Prof. S. Patel's Urban Analytics Lab at Lakeshore University, I was building features for a bus ridership forecasting model. Our data included an anonymized mobility dataset: device location pings from a vendor, aggregated to census block groups. As an experiment, I tried a "home-area" feature. It linked a frequent rider's first boarding stop of the day to the cluster where their device spent its nights. The feature didn't improve accuracy, so I dropped it. What stayed with me was what it did along the way: for many riders it narrowed "anonymized" data down to a few blocks. I went back to the vendor's documentation to see how the data was collected. It came from software kits built into partner apps, which ask users once for consent. I doubted that anyone who tapped "allow" pictured their data being used the way I had just used it.

I didn't misuse anything. The data was licensed, the feature was dropped, and the paper went forward. But the gap I saw is the problem I want to study in a PhD. Privacy protections usually focus on the moment of consent and on the person giving it. Much of the real risk sits further down the pipeline, with data workers like me who combine datasets, engineer features, and make choices that the original consent never covered. Nobody involved in those choices sees the whole picture: not the user, not the app developer, and not the analyst.

**What I've done so far**

My background is in quantitative modeling. I have a B.A. in Economics and will finish an M.S. in Data Science at Lakeshore University in December 2026. Over the past few years I've worked on how people make sense of data-driven systems, first in applied roles and then in research.

In the Urban Analytics Lab, I led feature engineering and evaluation for gradient-boosted ridership models and was first author of a workshop paper at UrbanDS 2025. During review, a reviewer asked whether the mobility features leaked future information into the model. I re-ran the analysis with a longer lag and reported both results. The accuracy loss was small, but the exercise taught me that a reported number depends on choices readers can't see.

In Spring 2026 I took Human-Centered Data Science, where my team of three ran think-aloud usability sessions with five classmates using an AutoML dashboard. I wrote the findings section. The study was small and a class project, but the patterns were striking. Participants accepted the top-ranked model without checking its metrics. Nobody opened the feature-importance panel. Two participants assumed the tool already "knew" which columns were sensitive. These were trained data science students, and they handed their judgment to the interface at exactly the points where it mattered most. This was my first time studying people instead of models, and it made me want to do it properly, with stronger methods and at a larger scale.

My other roles taught me how hard it is to communicate what models mean. As a Data Analyst at Lakeshore Regional Transit Authority, I maintained ridership dashboards for planners and reworked them so board members could read them. As a Data Science Intern at Northpoint Insurance, I built a churn model and explained it to the retention team and a VP, who needed to know what the scores did and didn't mean. As a TA for an introductory statistics course for non-majors, I wrote the rubric for the final data project. Its hardest criterion to teach was interpretation: saying what an analysis shows and what it doesn't.

**What I want to study**

I want to study how data practitioners understand and act on privacy risks that arise after data has been collected: when they join datasets, engineer features, and build models on data that's labeled "anonymized." My starting questions are:

- What mental models do analysts and data scientists have of "anonymized" or "aggregated" data, and where do those models fail?
- At which points in a typical workflow (joining, feature engineering, choosing a model) could a tool make risks of re-identifying people or inferring things about them visible, without asking practitioners to become privacy experts?
- How do tools like AutoML dashboards and other analysis interfaces shape what practitioners assume has already been handled for them?

I expect to use mixed methods: interviews and observation of practitioners working on real tasks, followed by building and testing tools that fit into their existing workflows. My modeling background means I can build those tools myself and understand the pipelines I'd be studying from the inside.

**Why Khoury**

I'm especially interested in working with Prof. Tianshi Li and the PEACH Lab. Prof. Li's work on developer-facing privacy tools, including Coconut and Matcha, takes the same stance I want to take. It treats the people who build systems as a place to intervene, and it studies what they find hard instead of assuming they don't care. Her recent position paper with Niloofar Mireshghallah argues that data aggregation is among the privacy problems that get the least research attention. That matches what I saw from the practitioner side. Her research on re-identification is also closely related to the risk I ran into with mobility data. I'd be glad to extend that line of work from developers and LLM systems to data scientists and analytics pipelines.

[Add one or two more faculty here whose work you've read and want to name.]

I'm not coming to HCI from a long research record. I'm coming from years inside the kinds of data pipelines HCI researchers study, with a specific question about them that I haven't been able to set aside. I want to spend the next five years learning to answer it rigorously.

---

Before you use this, please check a few things:

1. **I picked the research direction.** Our past chats show you weren't sure of a topic beyond "something with people and AI, not just building models." I built the statement around the mobility consent episode and the AutoML findings, because those are the most HCI-like moments in your record. If that's not the question you actually care about, the whole statement needs a different frame. Tell me and I'll rewrite it.
2. **The opening story is yours to approve.** It's based on your comment that you doubted anyone tapping "allow" pictured this use. I made up the part about the gap staying with you, and Prof. Patel is writing one of your letters. Make sure you're comfortable describing that feature publicly and that the story reflects how you actually felt.
3. **I only checked one faculty member.** I looked up Prof. Li's homepage, and everything I said about her work comes from it. I didn't look at other Khoury HCI faculty, so I left a placeholder. Don't name anyone whose work you haven't read.
4. **I didn't check Khoury's requirements.** Confirm the length limit and any specific prompts on the application portal. This draft is about 900 words.