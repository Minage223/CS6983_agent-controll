Quick update: I checked Prof. Li's lab page and publication list. She's Tianshi Li, and she directs the PEACH Lab (Privacy-Enabling AI and Computer-Human Interaction). Her work fits your story closely, so here's the revised draft built around it.

# Statement of Purpose: Ph.D. in Computer Science (HCI), Khoury College of Computer Sciences

The question that brought me to HCI came from a feature I built and then deleted.

I was a research assistant building models to forecast bus ridership. Part of our data came from a mobility vendor: phone location pings, anonymized and aggregated to block groups. While trying out features, I combined two of them: a rider's usual first boarding stop, and where their phone tended to sit at night. Neither column identified anyone on its own. Together, they put a lot of riders on just a few blocks.

The feature didn't improve the forecast, so I dropped it. Nobody did anything wrong. The data was collected with consent, and our use of it was legitimate. Still, I kept thinking about it. I looked up how the vendor collected the data: through SDKs in partner apps, with a one-time opt-in. I doubted that anyone who tapped "allow" had pictured two harmless-looking columns being joined to estimate where they sleep. I've been thinking about that gap since. What do people believe can be figured out from what they share? Could they ever actually see it?

That question feels more urgent now than when I started. People don't only share data passively with apps. They talk to AI tools, describing their jobs, their health, their routines, in their own words. Inference from that kind of text can go much further than anything I tried with two columns, and the person sharing has even less visibility into it.

I came to this from the technical side. I studied economics, then worked as a data analyst at a regional transit authority, maintaining ridership dashboards for planners. The part of that job I remember best is redesigning a dashboard for board members who couldn't use the original. The numbers were correct. The problem was how people read them. The ridership research that followed went well. We published a workshop paper, and I learned to be careful with evaluation. But when my advisor suggested extending the model to light rail, I realized I wasn't sure I wanted another forecasting project. What I wanted to work on was the people around the model.

This spring I got my first chance to study them directly. In a Human-Centered Data Science course, my team ran a small think-aloud study of an AutoML tool with five classmates. One finding stayed with me: two participants assumed the tool already knew which columns were sensitive and would handle them for them. These were data science students. Even people who build models assume the system is protecting them in ways it isn't. It was a small class project, but it was the first time research felt like what I actually wanted to be doing.

**Research interests**

My questions sit where privacy, AI, and people's mental models meet:

- What do people think can be inferred from what they share, with apps and with conversational AI, and how far is that from what's actually possible?
- Can interfaces make inference risk visible at the moment of sharing, in a way people understand and can act on?
- When people delegate to AI tools, what do they assume is being protected for them, and what happens when they're wrong?

I don't have a settled agenda yet. I do have a technical background that lets me see the data side of these problems: I know what a join can reveal because I've built one. What I need is training in studying people carefully, including qualitative methods, study design, and building and evaluating interventions. That's what I'm applying for.

**Why Khoury**

I'm especially excited about the work of Prof. Tianshi Li and the PEACH Lab, which treats AI privacy as something to address both by improving models and by empowering people. Her recent paper showing that agentic LLMs can re-identify participants in an anonymized interview dataset is the problem I ran into, at a much larger scale. Anonymized columns, or anonymized transcripts, don't stay anonymous when something capable is combining them. I'm also drawn to the lab's user-facing work. Rescriber helps people minimize what they share with LLM chatbots, and CIDER captures people's own contextual disclosure boundaries. Both start from what people want and understand, which is the side of this problem I want to study. I'd be glad to contribute to research on helping people understand and control what can be inferred about them.

[Optional: a second Khoury faculty member whose work you've read.]

I've spent several years building things from people's data, and I once built something that knew more about people than they'd likely expect. I want to spend the next several years helping people see that coming.

---

**Before you submit:**
- **Read the Li papers first.** I based that paragraph only on the abstracts and titles on her site: "Agentic LLMs as Powerful Deanonymizers" (Jan 2026 preprint), Rescriber (CHI 2025), and CIDER (COLM 2026). You haven't read them yet, and if you interview with her, she'll ask about them. Change the wording to match what you actually take from them.
- **Second faculty member:** My searches only turned up Prof. Li, so I didn't name anyone else rather than guess. Many programs like you to name two or three faculty. The Khoury HCI faculty directory is the place to look.
- **"Where they sleep":** That line makes the risk concrete. Make sure Prof. Patel is comfortable with the feature being described, since it's their lab's project. It's framed as something you tried and dropped, with no wrongdoing.
- **Still the same as before:** The study is labeled as a small class project, the paper as a workshop paper, and there are no metrics. It's about 850 words, so check Khoury's length limit.