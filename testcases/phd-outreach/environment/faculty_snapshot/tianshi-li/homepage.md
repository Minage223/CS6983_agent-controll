# Tianshi Li — personal homepage

Source: https://tianshili.me/

Tianshi Li

Publications

CV

PEACH

Tianshi Li

Assistant Professor

I’m an Assistant Professor at Northeastern University in the Khoury College of Computer Sciences, directing the PEACH (Privacy-Enabling AI and Computer-Human interaction) Lab . I’m also a core faculty member at the Cybersecurity and Privacy Institute at Northeastern University. I earned my PhD from Carnegie Mellon University and my Bachelor of Science degree from Peking University.

My work is driven by the belief that privacy sustains human agency, safe exploration, and free expression in a connected world. My interest focuses on studying and addressing the emerging LLM privacy issues from a human-centered perspective . Check out our position paper for an overview of the important and understudied problems and the research agenda. Below are a sample of topics I’m actively exploring with my students and collaborators:

Data minimization in LLM systems "It's a Fair Game", or Is It? How Users Navigate Disclosure Risks and Benefits in LLM Chatbots (CHI'24)

Rescriber: User-Led Data Minimization for Chatbots, Powered by Smaller LLMs (CHI'25)

Operationalizing Data Minimization for Privacy-Preserving LLM Prompting (ICLR'26)

Human oversight and control of agentic AI Dark Patterns Meet GUI Agents: Agent Susceptibility to Manipulative Interfaces and the Role of Human Oversight (CHI'26)

The Obvious Invisible Threat: GUI Agents' Vulnerability to Fine-Print Injections (TAISAP'26)

Human Oversight of Privacy Leakage in LLM Agents

Comparing Human Oversight Strategies for Computer-Use Agents

Balancing personalization, autonomy, and contextual integrity in AI agents PrivacyLens: Evaluating Privacy Norm Awareness of LLMs in Action (NeurIPS'24)

How Autonomy Reshapes Personalization's Effects on Privacy Concerns and Trust (COLM'26)

CIDER: Contextual Disclosure Boundaries for Privacy Preference Alignment (COLM'26)

Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment

Preserving societal structures: epistemic trust and surveillance power Secret Use of Large Language Models (CSCW'25)

Re-identification of Research Participants by Agentic LLMs

LLM Anonymization Against Agentic Re-Identification

AgentDoxx: Agentic Re-identification of Anonymized Text with Web Search

Harnessing AI to support privacy management and design Exploring the Design Space of AI Agents for Human-as-the-Unit Privacy Management (CHI'26)

PrivacyMotiv: Speculative Persona Journeys for Empathic Privacy Reviews in UX Design (DIS'26)

Disclose with Care: Designing Privacy Controls in Interview Chatbots

My broad research interests lie at the intersection of HCI, Privacy, and AI. I strive to address the increasing privacy issues in today’s digital world using a blend of human-centered problem understanding and technical problem solving. I conduct mixed-methods research to understand the privacy challenges situated in different stakeholders’ lived experiences, and develop models and systems to tackle these problems.

My research and expert commentary have been featured in MIT Technology Review , The Washington Post , WIRED , New Scientist , POLITICO , The Straits Times , and Consumer Reports , among others.

The work from my lab has been generously funded by NSF, Google, and Samsung.

News

Oct 31, 2026 I gave a talk “Capable is not Enough: Contextual Boundaries for AI Agents” at the NVIDIA Agent & Security Talk series. The talk builds upon our recent work on AuthorizationBench , an authorization alignment benchmark looking beyond consequence-oriented harms in human-agent delegation relationships, led by Zhiping Zhang . Check out the slides !

Sep 29, 2026 Two papers accepted at NeurIPS 2026: our position paper LLM Privacy Requires a Lifecycle-Wide Approach w/ Niloofar Mireshghallah (Position Paper Track), and The AI Observatory , led by Shayne Longpre and Anka Reuel with amazing colleagues (Evaluations and Datasets Track)!

Sep 9, 2026 I will be a panelist on “Generative AI and the Erosion of Anonymity” at CDT’s Future of Speech Online 2026: The Death of Online Anonymity? (September 23–24, virtual). Join us!

Aug 1, 2026 Grateful to receive a Samsung Research America LEAP-U award !

Jul 9, 2026 Two papers accepted at COLM 2026!

May 21, 2026 Join us for the 2nd edition of the HAIPS workshop , co-located with COLM 2026!

Apr 21, 2026 Our work on LLM-powered re-identification and emerging LLM privacy risks was covered by MIT Technology Review , POLITICO , and The Straits Times .

Jan 26, 2026 Three papers accepted at CHI 2026 and one paper accepted at ICLR 2026!

Jan 9, 2026 My paper presents what is likely the first re-identification attack using agentic LLMs

Oct 2, 2025 Dropping a new position paper “Privacy is Not Just Memorization” w/ Niloofar Mireshghallah to spotlight the wildly understudied problem of inference-time privacy in LLMs (e.g., agent-based context leakage and abuse agentic capabilities for democratized surveillance).

Selected Publications and Preprints

NeurIPS

Position: LLM Privacy Requires a Lifecycle-Wide Approach

Niloofar Mireshghallah†, and  Tianshi Li†

In NeurIPS 2026 (Position Paper Track) Dec 2026

📰 Media coverage: Northeastern Global News , Help Net Security

Abs arXiv

The discourse on privacy risks in Large Language Models (LLMs) has disproportionately focused on verbatim memorization of training data, while more immediate and scalable privacy threats remain underexplored. We posit that LLM privacy must be understood as a lifecycle-wide problem, rather than being reduced to training-data leakage alone. We introduce a taxonomy of five open privacy problems posed by LLMs and flesh out each with concrete threat models, real-world case studies, and open research challenges. Through a longitudinal analysis of 1,772 AI/ML privacy papers from leading conferences (2016–2025), we reveal a disproportionate research focus: memorization dominates technical research, yet offers little traction against pressing problems like inference-time context leakage, autonomous agent behavior, and surveillance-enabling data aggregation. We provide a roadmap of technical, sociotechnical, and policy interventions, and call on the community to prioritize the underexplored problem categories—agent-based leakage, inference attacks, and data aggregation—that collectively receive less than 9% of current research attention.

Preprint

Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment

Zhiping Zhang, Franklin Mingzhe Li, Raio Zihao Huang, and  Tianshi Li

Preprint Oct 2026

Best Paper Honorable Mention Award 🏅 and Spotlight Presentation at the COLM 2026 HAIPS Workshop

PDF

Preprint

AgentDoxx: Agentic Re-identification of Anonymized Text with Web Search

Jianing Wen, and  Tianshi Li

arXiv preprint Oct 2026

arXiv

COLM

CIDER: A Dataset of Contextual Disclosure Boundaries for Privacy Preference Alignment

Bingcan Guo, Eryue Xu, Jijie Zhou, Zhiping Zhang, and  Tianshi Li

In COLM 2026 Oct 2026

Abs arXiv Dataset Code

Aligning large language models (LLMs) with human privacy preferences requires capturing individuals’ disclosure boundaries beyond general privacy norms. However, current models lack methods for eliciting such nuanced preferences and ground truth data to evaluate alignment in realistic settings. We introduce CIDER, a dataset of 14,850 human annotations from 169 users, forming 1,650 contextual disclosure boundary sets across 60 interpersonal communication scenarios where information sharing violates privacy norms. Each boundary represents a real user’s disclosure decisions over 9 sharing variants, given a communication role and AI-mediated condition. We formulate a prediction task in which models predict a user’s disclosure decision from historical boundaries, with varying levels of contextual information. Across eight open and proprietary models, personalization improves performance, with accuracy gains of up to 11.41% using six in-context examples. However, these gains arise from different mechanisms. Larger models such as GPT-5.4 (with medium reasoning effort) and Claude Sonnet 4.6 leverage semantic context to infer user-specific, context-dependent disclosure preferences for more accurate predictions, while smaller models tend to rely on structured heuristics based on disclosure granularity and identifiability and present trade-offs between false positives and false negatives. Our findings highlight the potential and limitations of current LLMs’ privacy modeling capability and position CIDER as a resource for advancing personalized privacy preference alignment.

COLM

Autonomy Reshapes How Personalization Affects Privacy Concerns and Trust in LLM Agents

Zhiping Zhang, Yi Evie Zhang, Freda Shi, and  Tianshi Li

In COLM 2026 Oct 2026

Abs arXiv

LLM agents require personal information for personalization in order to effectively act on users’ behalf, but this raises privacy concerns that can discourage data sharing, limiting both the autonomy levels at which agents can operate and the effectiveness of personalization. Yet the expanded design space of agent autonomy also presents opportunities to shape these effects, which remain underexplored. We conducted a 3×3 between-subjects experiment (N=450) to study how agent autonomy level influences personalization’s effects on users’ privacy concerns, trust, and willingness to use, as well as the underlying psychological processes. We find that risk-contingent autonomy, where the agent delegates control to users upon detecting potential privacy leakage, through improving users’ perceived control, attenuates personalization’s adverse effects by reducing the increase in privacy concerns and the decrease in trust. Our results suggest that designing agent’s autonomy that supports human autonomy (both in terms of perceived control and oversight effectiveness) helps users benefit from personalization without being deterred by growing privacy concerns, contributing to the development of trustworthy LLM agents.

DIS

PrivacyMotiv: Speculative Persona Journeys for Empathic and Motivating Privacy Reviews in UX Design

Zeya Chen, Jianing Wen, Yaxing Yao, Toby Jia-Jun Li, and  Tianshi Li

In DIS 2026 Jun 2026

Abs arXiv Demo

UX professionals routinely conduct design reviews, yet privacy concerns are often overlooked—not only due to limited tools, but more fundamentally from low intrinsic motivation, driven by limited privacy knowledge, weak empathy for unexpectedly affected users, and low confidence in identifying harms. We present PrivacyMotiv, an LLM-powered system that supports privacy-oriented design diagnosis by generating speculative personas with UX user journeys centered on individuals vulnerable to privacy risks. Drawing on narrative strategies, the system constructs relatable and attention-drawing scenarios that show how ordinary design choices may cause unintended harms, expanding the scope of privacy reflection in UX. In a within-subjects study with professional UX practitioners (N=16), we compared participants’ self-proposed methods with PrivacyMotiv across two privacy audit tasks. Results show significant improvements in empathy, intrinsic motivation, and perceived usefulness. This work contributes empirical insight into motivational barriers in privacy-aware UX and a novel mechanism for structured privacy audits.

ICLR

Operationalizing Data Minimization for Privacy-Preserving LLM Prompting

Jijie Zhou, Niloofar Mireshghallah, and  Tianshi Li

In ICLR 2026 Apr 2026

Abs arXiv Code Website

The rapid deployment of large language models (LLMs) in consumer applications has led to frequent exchanges of personal information. To obtain useful responses, users often share more than necessary, increasing privacy risks via memorization, context-based personalization, or security breaches. We present a framework to formally define and operationalize data minimization: for a given user prompt and response model, quantifying the least privacy-revealing disclosure that maintains utility, and propose a priority-queue tree search to locate this optimal point within a privacy-ordered transformation space. We evaluated the framework on four datasets spanning open-ended conversations (ShareGPT, WildChat) and knowledge-intensive tasks with single-ground-truth answers (CaseHOLD, MedQA), quantifying achievable data minimization with nine LLMs as the response model. Our results demonstrate that larger frontier LLMs can tolerate stronger data minimization while maintaining task quality than smaller open-source models (85.7% redaction for GPT-5 vs. 19.3% for Qwen2.5-0.5B). By comparing with our search-derived benchmarks, we find that LLMs struggle to predict optimal data minimization directly, showing a bias toward abstraction that leads to oversharing. This suggests not just a privacy gap, but a capability gap: models may lack awareness of what information they actually need to solve a task.

CHI

From Fragmentation to Integration: Exploring the Design Space of AI Agents for Human-as-the-Unit Privacy Management

Eryue Xu, and  Tianshi Li

In CHI 2026 Apr 2026

Abs arXiv

Managing one’s digital footprint is overwhelming, as it spans multiple platforms and involves countless context-dependent decisions. Recent advances in agentic AI offer ways forward by enabling holistic, contextual privacy-enhancing solutions. Building on this potential, we adopted a “human-as-the-unit” perspective and investigated users’ cross-context privacy challenges through 12 semi-structured interviews. Results reveal that people rely on ad hoc manual strategies while lacking comprehensive privacy controls, highlighting nine privacy-management challenges across applications, temporal contexts, and relationships. To explore solutions, we generated nine AI agent concepts and evaluated them via a speed-dating survey with 116 US participants. The three highest-ranked concepts were all post-sharing management tools with half or full agent autonomy, with users expressing greater trust in AI accuracy than in their own efforts. Our findings highlight a promising design space where users see AI agents bridging the fragments in privacy management, particularly through automated, comprehensive post-sharing remediation of users’ digital footprints.

Preprint

Agentic LLMs as Powerful Deanonymizers: Re-identification of Participants in the Anthropic Interviewer Dataset

Tianshi Li

arXiv preprint Jan 2026

📰 Media coverage: MIT Technology Review , POLITICO , The Straits Times , Northeastern Global News

arXiv

CSCW

Secret Use of Large Language Models

Zhiping Zhang, Chenxinran Shen, Bingsheng Yao, Dakuo Wang, and  Tianshi Li

In CSCW 2025 Oct 2025

Abs arXiv

The advancements of Large Language Models (LLMs) have decentralized the responsibility for the transparency of AI usage. Specifically, LLM users are now encouraged or required to disclose the use of LLM-generated content for varied types of real-world tasks. However, an emerging phenomenon, users’ secret use of LLMs, raises challenges in ensuring end users adhere to the transparency requirement. Our study used mixed-methods with an exploratory survey (125 real-world secret use cases reported) and a controlled experiment among 300 users to investigate the contexts and causes behind the secret use of LLMs. We found that such secretive behavior is often triggered by certain tasks, transcending demographic and personality differences among users. Task types were found to affect users’ intentions to use secretive behavior, primarily through influencing of perceived external judgment regarding LLM usage. Our results yield important insights for future work on designing interventions to encourage more transparent disclosure of LLM/AI use

CHI

Rescriber: Smaller-LLM-Powered User-Led Data Minimization for LLM-Based Chatbots

Jijie Zhou, Eryue Xu, Yaoyao Wu, and  Tianshi Li

In CHI 2025 Apr 2025

Abs arXiv PDF Code

The proliferation of LLM-based conversational agents has resulted in excessive disclosure of identifiable or sensitive information. However, existing technologies fail to offer perceptible control or account for users’ personal preferences about privacy-utility tradeoffs due to the lack of user involvement. To bridge this gap, we designed, built, and evaluated Rescriber, a browser extension that supports user-led data minimization in LLM-based conversational agents by helping users detect and sanitize personal information in their prompts. Our studies (N=12) showed that Rescriber helped users reduce unnecessary disclosure and addressed their privacy concerns. Users’ subjective perceptions of the system powered by Llama3-8B were on par with that by GPT-4o. The comprehensiveness and consistency of the detection and sanitization emerge as essential factors that affect users’ trust and perceived protection. Our findings confirm the viability of smaller-LLM-powered, user-facing, on-device privacy controls, presenting a promising approach to address the privacy and trust challenges of AI.

NeurIPS

PrivacyLens: Evaluating Privacy Norm Awareness of Language Models in Action

Yijia Shao,  Tianshi Li , Weiyan Shi, Yanchen Liu, and Diyi Yang

In NeurIPS Datasets and Benchmarks Sep 2024

arXiv Code Website

CHI SIG

Human-Centered Privacy Research in the Age of Large Language Models

Tianshi Li , Sauvik Das, Hao-Ping (Hank) Lee, Dakuo Wang, Bingsheng Yao, and Zhiping Zhang

In CHI Conference on Human Factors in Computing Systems (CHI’24 Companion) Apr 2024

Abs arXiv

The emergence of large-language models (LLMs), and their increased use in user-facing systems, has led to substantial privacy concerns. To date, research on these privacy concerns has been model-centered: exploring how LLMs lead to privacy risks like memorization, or can be used to infer personal characteristics about people from their content. We argue that there is a need for more research focusing on the human aspect of these privacy issues: e.g., research on how design paradigms for LLMs affect users’ disclosure behaviors, users’ mental models and preferences for privacy controls, and the design of tools, systems, and artifacts that empower end-users to reclaim ownership over their personal data. To build usable, efficient, and privacy-friendly systems powered by these models with imperfect privacy properties, our goal is to initiate discussions to outline an agenda for conducting human-centered research on privacy issues in LLM-powered systems. This Special Interest Group (SIG) aims to bring together researchers with backgrounds in usable security and privacy, human-AI collaboration, NLP, or any other related domains to share their perspectives and experiences on this problem, to help our community establish a collective understanding of the challenges, research opportunities, research methods, and strategies to collaborate with researchers outside of HCI.

CHI

“It’s a Fair Game”, or Is It? Examining How Users Navigate Disclosure Risks and Benefits When Using LLM-Based Conversational Agents

Zhiping Zhang, Michelle Jia, Hao-Ping (Hank) Lee, Bingsheng Yao, Sauvik Das, Ada Lerner, Dakuo Wang, and  Tianshi Li

In CHI Conference on Human Factors in Computing Systems Apr 2024

Abs arXiv PDF Talk Website

The widespread use of Large Language Model (LLM)-based conversational agents (CAs), especially in high-stakes domains, raises many privacy concerns. Building ethical LLM-based CAs that respect user privacy requires an in-depth understanding of the privacy risks that concern users the most. However, existing research, primarily model-centered, does not provide insight into users’ perspectives. To bridge this gap, we analyzed sensitive disclosures in real-world ChatGPT conversations and conducted semi-structured interviews with 19 LLM-based CA users. We found that users are constantly faced with trade-offs between privacy, utility, and convenience when using LLM-based CAs. However, users’ erroneous mental models and the dark patterns in system design limited their awareness and comprehension of the privacy risks. Additionally, the human-like interactions encouraged more sensitive disclosures, which complicated users’ ability to navigate the trade-offs. We discuss practical design guidelines and the needs for paradigmatic shifts to protect the privacy of LLM-based CA users.

IMWUT

Matcha: An IDE Plugin for Creating Accurate Privacy Nutrition Labels

Tianshi Li , Lorrie Faith Cranor, Yuvraj Agarwal, and Jason I Hong

Proc. ACM Interact. Mob. Wearable Ubiquitous Technol. Apr 2024

Abs arXiv HTML Website

Apple and Google introduced their versions of privacy nutrition labels to the mobile app stores to better inform users of the apps’ data practices. However, these labels are self-reported by developers and have been found to contain many inaccuracies due to misunderstandings of the label taxonomy. In this work, we present Matcha, an IDE plugin that uses automated code analysis to help developers create accurate Google Play data safety labels. Developers can benefit from Matcha’s ability to detect user data accesses and transmissions while staying in control of the generated label by adding custom Java annotations and modifying an auto-generated XML specification. Our evaluation with 12 developers showed that Matcha helped our participants improved the accuracy of a label they created with Google’s official tool for a real-world app they developed. We found that participants preferred Matcha for its accuracy benefits. Drawing on Matcha, we discuss general design recommendations for developer tools used to create accurate standardized privacy notices.

CHI

Understanding Challenges for Developers to Create Accurate Privacy Nutrition Labels

Tianshi Li , Kayla Reiman, Yuvraj Agarwal, Lorrie Faith Cranor, and Jason I Hong

In CHI Conference on Human Factors in Computing Systems Apr 2022

Best Paper Honorable Mention Award 🏅

📰 Media coverage: The Washington Post , Consumer Reports

Abs HTML PDF

Apple announced the introduction of app privacy details to their App Store in December 2020, marking the first ever real-world, large-scale deployment of the privacy nutrition label concept, which had been introduced by researchers over a decade earlier. The Apple labels are created by app developers, who self-report their app’s data practices. In this paper, we present the first study examining the usability and understandability of Apple’s privacy nutrition label creation process from the developer’s perspective. By observing and interviewing 12 iOS app developers about how they created the privacy label for a real-world app that they developed, we identified common challenges for correctly and efficiently creating privacy labels. We discuss design implications both for improving Apple’s privacy label design and for future deployment of other standardized privacy notices.

IMWUT

Honeysuckle: Annotation-Guided Code Generation of In-App Privacy Notices

Tianshi Li , Elijah B Neundorfer, Yuvraj Agarwal, and Jason I Hong

Proc. ACM Interact. Mob. Wearable Ubiquitous Technol. Sep 2021

Abs HTML PDF Talk Demo

In-app privacy notices can help smartphone users make informed privacy decisions. However, they are rarely used in real-world apps, since developers often lack the knowledge, time, and resources to design and implement them well. We present Honeysuckle, a programming tool that helps Android developers build in-app privacy notices using an annotation-based code generation approach facilitated by an IDE plugin, a build system plugin, and a library. We conducted a within-subjects study with 12 Android developers to evaluate Honeysuckle. Each participant was asked to implement privacy notices for two popular open-source apps using the Honeysuckle library as a baseline as well as the annotation-based approach. Our results show that the annotation-based approach helps developers accomplish the task faster with significantly lower cognitive load. Developers preferred the annotation-based approach over the library approach because it was much easier to learn and use and allowed developers to achieve various types of privacy notices using a unified code format, which can enhance code readability and benefit team collaboration.

PMC

What makes people install a COVID-19 contact-tracing app? Understanding the influence of app design and individual difference on contact-tracing app adoption intention

Tianshi Li , Camille Cobb, Jackie (junrui) Yang, Sagar Baviskar, Yuvraj Agarwal, Beibei Li, Lujo Bauer, and Jason I Hong

Pervasive Mob. Comput. Aug 2021

Best Research Paper 2019-2021 Award 🏆

Abs HTML PDF

Smartphone-based contact-tracing apps are a promising solution to help scale up the conventional contact-tracing process. However, low adoption rates have become a major issue that prevents these apps from achieving their full potential. In this paper, we present a national-scale survey experiment (N=1963) in the U.S. to investigate the effects of app design choices and individual differences on COVID-19 contact-tracing app adoption intentions. We found that individual differences such as prosocialness, COVID-19 risk perceptions, general privacy concerns, technology readiness, and demographic factors played a more important role than app design choices such as decentralized design vs. centralized design, location use, app providers, and the presentation of security risks. Certain app designs could exacerbate the different preferences in different sub-populations which may lead to an inequality of acceptance to certain app design choices (e.g., developed by state health authorities vs. a large tech company) among different groups of people (e.g., people living in rural areas vs. people living in urban areas). Our mediation analysis showed that one’s perception of the public health benefits offered by the app and the adoption willingness of other people had a larger effect in explaining the observed effects of app design choices and individual differences than one’s perception of the app’s security and privacy risks. With these findings, we discuss practical implications on the design, marketing, and deployment of COVID-19 contact-tracing apps in the U.S.

CSCW

How Developers Talk About Personal Data and What It Means for User Privacy: A Case Study of a Developer Forum on Reddit

Tianshi Li , Elizabeth Louie, Laura Dabbish, and Jason I Hong

Proc. ACM Hum. Comput. Interact. Jan 2021

Abs HTML PDF Talk

While online developer forums are major resources of knowledge for application developers, their roles in promoting better privacy practices remain underexplored. In this paper, we conducted a qualitative analysis of a sample of 207 threads (4772 unique posts) mentioning different forms of personal data from the /r/androiddev forum on Reddit. We started with bottom-up open coding on the sampled posts to develop a typology of discussions about personal data use and conducted follow-up analyses to understand what types of posts elicited in-depth discussions on privacy issues or mentioned risky data practices. Our results show that Android developers rarely discussed privacy concerns when talking about a specific app design or implementation problem, but often had active discussions around privacy when stimulated by certain external events representing new privacy-enhancing restrictions from the Android operating system, app store policies, or privacy laws. Developers often felt these restrictions could cause considerable cost yet fail to generate any compelling benefit for themselves. Given these results, we present a set of suggestions for Android OS and the app store to design more effective methods to enhance privacy, and for developer forums(e.g., /r/androiddev) to encourage more in-depth privacy discussions and nudge developers to think more about privacy.

IMWUT

Coconut: An IDE Plugin for Developing Privacy-Friendly Apps

Tianshi Li , Yuvraj Agarwal, and Jason I Hong

Proc. ACM Interact. Mob. Wearable Ubiquitous Technol. Dec 2018

Abs HTML PDF Demo Website

Although app developers are responsible for protecting users’ privacy, this task can be very challenging. In this paper, we present Coconut, an Android Studio plugin that helps developers handle privacy requirements by engaging developers to think about privacy during the development process and providing real-time feedback on potential privacy issues. We start by presenting new findings based on a series of semi-structured interviews with Android developers, probing into the difficulties with privacy that developers face when building apps. Based on these findings, we implemented a proof-of-concept prototype of Coconut and evaluated it in a controlled lab study with 18 Android developers (including eight professional developers). Our study results suggest that apps developed with Coconut handled privacy concerns better, and the developers that used Coconut had a better understanding of their code’s behavior and wrote a better privacy policy for their app. We also found that requiring developers to do a small amount of annotating work regarding their apps’ personal data practices during the development process may result in a significant improvement in app privacy.
