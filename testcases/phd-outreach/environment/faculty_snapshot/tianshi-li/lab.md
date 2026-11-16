# PEACH Lab

Source: https://peach.codes/

PEACH Lab

Home

-->

People

Research area

-->

Publication

News

-->

We are PEACH ( P rivacy- E nabling A I and C omputer- H uman Interaction) Lab at the Northeastern University .

We are a group of researchers passionate about exploring the intersection of HCI, AI, and privacy.

We believe that addressing privacy issues raised by AI requires not only model-centered approaches—approaches that improve the models—but also human-centered approaches—approaches that empower people.

-->

Our work has been supported by the following funding agencies: National Science Foundation, Google, and CMU CyLab.

-->

We are PEACH ( P rivacy- E nabling

A I and C omputer-

H uman Interaction) Lab at the

Northeastern University

.

We are a group of researchers passionate about

exploring the intersection of HCI, AI, and privacy

.

We believe that addressing privacy issues raised by AI requires not only model-centered approaches—approaches that improve the models—but also human-centered approaches—approaches that empower people.

-->

News

Two papers accepted at NeurIPS 2026

Sep 29, 2026

We have two papers accepted at NeurIPS 2026: a position paper on why LLM privacy requires a lifecycle-wide approach, and The AI Observatory in the Evaluations and Datasets Track! Congrats to Arya, and huge thanks to our amazing collaborators Niloofar Mireshghallah, Shayne Longpre, Anka Reuel, and the whole AI Observatory team!

Two papers accepted at COLM 2026

Jul 9, 2026

We have two papers accepted at COLM 2026! One paper shows that an LLM agent's autonomy level reshapes how personalization affects privacy concerns and trust. Our second paper introduces CIDER, a dataset of people's contextual disclosure boundaries for aligning LLMs with individual privacy preferences. Congrats to Arya, Gloria, Yolanda, and Gigi, and thanks to our collaborators Yi Evie Zhang and Freda Shi!

> View All

-->

Research

Position: LLM Privacy Requires a Lifecycle-Wide Approach

Niloofar Mireshghallah † , Tianshi Li †

NeurIPS 2026 (Position Paper Track)

The discourse on privacy risks in Large Language Models (LLMs) has disproportionately focused on verbatim memorization of training data, while a constellation of more immediate and scalable privacy threats remain underexplored. This position paper argues that the privacy landscape of LLM systems extends far beyond training data extraction, encompassing risks from data collection practices, inference-time context leakage, autonomous agent capabilities, and the democratization of surveillance through deep inference attacks. We present a comprehensive taxonomy of privacy risks across the LLM lifecycle -- from data collection through deployment -- and demonstrate through case studies how current privacy frameworks fail to address these multifaceted threats. Through a longitudinal analysis of 1,322 AI/ML privacy papers published at leading conferences over the past decade (2016--2025), we reveal that while memorization receives outsized attention in technical research, the most pressing privacy harms lie elsewhere, where current technical approaches offer little traction and viable paths forward remain unclear. We call for a fundamental shift in how the research community approaches LLM privacy, moving beyond the narrow focus of current technical solutions and embracing interdisciplinary approaches that address the sociotechnical nature of these emerging threats.

arXiv

-->

Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment

Zhiping Zhang, Franklin Mingzhe Li, Raio Zihao Huang, Tianshi Li

Preprint

When an LLM agent acts on behalf of a user, it is expected to act within the authorization scope the user grants. Existing agent evaluations largely measure task completion or harmful consequences and can therefore overlook actions that violate this delegation without producing conventional safety or privacy harms. We introduce AuthorizationBench, a benchmark of authorization alignment grounded in documented real-world cases. Each task is specified by an authorization contract that separates the principal's instruction, completion criteria, and out-of-authorization actions. A scalable construction pipeline produces 286 executable tasks spanning situational triggers, the presence or absence of direct harmful consequences, and ten application domains. We execute every task with four models at two reasoning-effort settings across three agent harnesses in an authorization-aware sandbox that keeps authorized and out-of-authorization paths executable and observable, yielding 6,864 trajectories. Agents act out of authorization in 19.2% of trajectories, with rates ranging from 10.5% to 26.6% across the 24 configurations. Task completion does not imply authorization. Increasing reasoning effort leaves the aggregate rate nearly unchanged (19.3% at low effort versus 19.1% at high effort), with effects varying across models. On controlled pairs, agents act out of authorization at similar rates with (17.9%) and without (20.8%) direct harmful consequences, and more often under benign pressures than malicious injections (23.5% versus 17.6%, p = 0.002). Our results show that task capability, additional reasoning, and consequence-oriented safety evaluation do not by themselves ensure authorization alignment, motivating it as a distinct target for agent evaluation and development. Moreover, agents that consult the principal before completing a task exhibit lower rates of out-of-authorization behavior (14.0% versus 21.6%, p

-->

AgentDoxx: Agentic Re-identification of Anonymized Text with Web Search

Jianing Wen, Tianshi Li

Preprint

As Large Language Models (LLMs) gain tool use capabilities such as web search, they can retrieve and cross-reference public information, creating privacy risks beyond memorization. One manifestation is re-identification: linking an anonymized interview transcript to a named individual. Yet without ground-truth identities, the coverage of such attacks and the protection offered by a defense cannot be reliably measured. We introduce AgentDoxx, an evaluation suite of 822 synthetic interview transcripts grounded in public information about real individuals with known identities. We evaluate fifteen configurations of open-weight and proprietary models, isolating the effect of web search, and analyze their search trajectories to distinguish retrieval-driven from parametric identifications. Ground-truth identities reveal that re-identification risk is distributed across an agent's execution: retrieval and parametric recall both contribute, with open-weight models identifying 15-28% of transcripts without search; identification succeeds in over 88% of cases once the target appears in a retrieved result; entity masking leaves at least one attacker successful on 85.3% of a stratified sample; and privacy instructions suppress naming but not retrieval, with configurations scoring 0% accuracy yet retrieving the subject in up to 62% of transcripts. We further show that observed attack trajectories can provide supervision for localizing identifying spans, offering a path toward attack-informed anonymization.

arXiv

-->

Autonomy Reshapes How Personalization Affects Privacy Concerns and Trust in LLM Agents

Zhiping Zhang, Yi Evie Zhang, Freda Shi, Tianshi Li

COLM 2026

LLM agents require personal information for personalization in order to effectively act on users' behalf, but this raises privacy concerns that can discourage data sharing, limiting both the autonomy levels at which agents can operate and the effectiveness of personalization. Yet the expanded design space of agent autonomy also presents opportunities to shape these effects, which remain underexplored. We conducted a 3×3 between-subjects experiment (N=450) to study how agent autonomy level influences personalization's effects on users' privacy concerns, trust, and willingness to use, as well as the underlying psychological processes. We find that risk-contingent autonomy, where the agent delegates control back to users upon detecting potential privacy leakage, improves users' perceived control. This in turn attenuates personalization's adverse effects: privacy concerns rise less and trust declines less. Our results suggest that designing agent's autonomy that supports human autonomy (both perceived control and oversight effectiveness) helps users benefit from personalization without being deterred by growing privacy concerns. This positions aligning decision authority between users and agents (autonomy alignment) as an important opportunity and challenge for trustworthy human-agent interaction.

arXiv

-->

> View All

People

Tianshi Li

Principal Investigator

Zhiping (Arya) Zhang

Ph.D. Student

Jianing Wen

Ph.D. Student

Ziwen (Aaron) Li

Ph.D. Student

Raio Huang

Ph.D. Student

Zeya Chen

PhD Collaborator

Eryue (Yolanda) Xu

PhD Collaborator

Alumni

Bingcan (Gloria) Guo

Former Intern

Next Position: PhD Student @ UCLA

William Namgyal

Former Intern

Next Position: Undergrad @ UC Berkeley, then CEO of Luel

Yaoyao Wu

Former Intern

Next Position at Apple

Our work has been supported by the following funding agencies: National Science Foundation, Google, Samsung, and CMU CyLab.

-->

-->

PEACH Lab @ Khoury College of Computer Sciences, Northeastern University

Boston, MA 02115, United States

-->
