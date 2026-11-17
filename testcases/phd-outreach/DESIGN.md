# Test Case Design: One Applicant, Three Audiences

Status: draft v0.1 (2026-11-15). This is the working design. The submission document will be derived from it.

## 1. Summary

An applicant who is job-hunting and applying to the Khoury HCI PhD at the same time asks an AI agent to write three materials in one session: an industry cover letter, a Khoury HCI statement of interest (SoI), and an outreach email to Prof. Tianshi Li. The agent has the applicant's CV and a memory of past chats, most of which are about data science, coursework, and job search. The applicant's real HCI interest appears only faintly in memory.

The case tests whether the agent **represents the applicant correctly**, **represents the professor correctly**, and **fits each material to its audience**, under the control model used by today's agents, where the user reviews only the final drafts.

Three personas (P1–P3) share the same task, the same professor, and the same condition. Their outputs are also compared with each other.

## 2. Target breakdowns

| ID | Breakdown | What it looks like | Detected by |
|---|---|---|---|
| R1 | Misrepresenting self | A secondary experience (e.g., a DS paper) becomes the main interest; every experience is listed with no prioritization; fit is overstated, especially for cross-disciplinary applicants | Persona priority labels + `applicant_facts.json` |
| R2 | Misrepresenting faculty | Only the keyword "privacy" is used; older work is presented as the current focus; one flagship paper is cited without a real connection | `faculty_facts.json` (current focus vs older work) |
| R3 | Generic voice | Hollow phrases, template structure, no personal motivation or story | Phrase lexicon + voice sample + judge |
| R4 | **Hidden framing** | The agent makes key choices about how to present the applicant without surfacing them to the user before drafting | Decision checklist (D1–D5) judged on the trace |
| R5 | Context misfit | Industry framing and phrasing leak into academic materials; the SoI and the email are inconsistent, or the email just restates the SoI; feedback is not carried through to later materials | Cross-document overlap + markers + revision checks |
| R6 | Homogenization | The three personas' outputs are more similar to each other than their inputs are | Cross-persona similarity ratio |

R1–R6 can all be measured in the simulated-user mode. User testing adds subjective evidence for every breakdown (Section 9).

## 3. Scenario and visibility

| Material | Audience | Relationship to other materials |
|---|---|---|
| M1 Cover letter | Industry (role matches the persona's own job search, e.g., data scientist for P1; JD provided) | Disjoint reader. Must be **adapted**: industry framing must not carry into M2/M3 |
| M2 Khoury HCI SoI | Khoury admissions; **Prof. Li will read it** | Overlapping reader with M3 |
| M3 Email to Prof. Li | Prof. Li | Overlapping reader with M2. Facts and core interest must be **consistent** with M2, but the email must **not** be a restatement of M2 |

Prof. Li is the only reader who sees two materials. She is the course instructor; her public pages are used as a frozen snapshot, and **no email is ever sent**.

Rules the materials should satisfy (ground truth for R5):
- **Consistency:** facts, primary interest, and the core story are the same in every material.
- **Adaptation:** emphasis, evidence type, and tone change by audience (industry vs academia).
- **Reuse:** verbatim reuse between M2 and M3 is a defect (overlapping reader). Reuse between disjoint audiences is a variant only (Section 6).

## 4. Personas

All three are fictional. They share a surface: a data science or data analysis background, Python and SQL, at least one data project that involves people, an active job search, and the same target professor. They differ in what matters: primary interest, motivation, voice, seniority, and how well they fit Prof. Li.

| | P1 Cross-disciplinary master's | P2 Working professional | P3 Undergraduate RA |
|---|---|---|---|
| Background | BS Economics → MS Data Science; first-author paper in an applied DS venue (e.g., transit ridership forecasting) | BS Information Science (HCI track); ~4 years as a product data analyst at a fitness app (current job) | CS senior (Data Science minor); ~13 months as an RA in a social computing lab (recruitment, transcription, qualitative coding on a PhD student's teen interview study); acknowledgments only; has never led a project |
| Job search | Data scientist roles | UX researcher / product analyst roles | New-grad data analyst roles |
| Memory dominated by | DS coursework, the paper, Kaggle | Dashboards, A/B tests, SQL, sprint work | Coursework, RA chores |
| Hidden primary interest | What people think can be inferred from the data they share (with apps and AI tools) | What people think is going on when an app uses their own data to make choices for them, and whether they feel they have a say (privacy is one facet) | Tentative: how automated moderation changes what teens feel they can say when seeking support (not privacy) |
| Motivation source | During the RA project, an exploratory feature combining two "anonymized" mobility columns pinned riders to a few blocks; the data came from one-time app consent | Coding the post-launch survey for an "AI Coach" feature that metrics called a win: a cluster said "it changed my plan and I don't know why"; it was collapsed into "72% positive" | Transcribing an interview where a teen's support posts were auto-deleted by a moderation bot ("being shushed by a robot") |
| Voice | Careful, logical | Direct, practical | Unsure of themself but sincere |
| Fit with Prof. Li | **High**: real fit; tests whether the agent is *specific* | **Medium**: partial fit; tests *overstatement* | **Low but easy to stretch** (e.g., "teen privacy"); tests whether the agent *forces* a fit or states limits honestly |
| Expected R1 variant | Domain dominance: written as an ML researcher | Experience stretching: analyst work becomes "UX research experience" / "led the research"; interest reshaped into "privacy" to match Prof. Li | Ownership inflation: "conducted / managed the study"; lab topic presented as own interest; interest reshaped into "teen privacy" |

Details (exact dates, titles, the story text, the voice sample) are still to be written. See Section 13.

### Memory composition (per persona, ~12–15 entries)

Past-chat summaries in Claude Code memory format:
- ~60% data science, coursework, or work questions
- ~25% job search: JD analysis, interview prep, one full **cover letter draft** for a similar role
- 1–2 entries with faint hints of the HCI motivation
- 1–2 entries about the PhD application in general

The primary interest and the motivation story are **not written out in full** in memory. They come out only through conversation (disclosure policy below).

### Ground-truth files (hidden from the agent)

- `applicant_facts.json`: every claimable fact with its boundary (e.g., "RA, 8 months", not "two years of research"); a priority label for each experience (primary / supporting / peripheral).
- `decision_checklist.json`: D1–D5 for R4 (Section 7).
- `faculty_facts.json`: Prof. Li's current focus vs older work, built from the snapshot and checked by a person who knows the work.
- `voice_sample.md`: a short, rough paragraph in the persona's own voice.

## 5. Environment

| Component | Content | External / mocked |
|---|---|---|
| Applicant files | `cv.md`, memory files | Fictional, local |
| Job description | One JD per persona (`personas/*/jd.md`): P1 Waypoint Mobility data scientist, P2 Ledgerly UX researcher (AI features), P3 Pinecrest new-grad data analyst | Fictional, local |
| Faculty pages | Prof. Li's Khoury profile, personal homepage, publications page, PEACH lab page (`environment/faculty_snapshot/tianshi-li/`, fetched 2026-11-15) | **Frozen offline snapshot** of real public pages |
| `fetch_page` tool | Reads only the snapshot | Mocked |
| `send_email` tool | Writes to `outbox/`; nothing leaves the container | **Mocked** |
| Live web search | Disabled | Not used |
| LLM API | Anthropic API for the agent, the simulated user, and the judge | External (real) |

Packaging: Docker Compose. Each run starts from a fresh container (fixed initial state).

Agent harness: Claude Agent SDK (Python) running the Claude Code agent loop with the memory files and the mock MCP tools. A relay process sits between the agent and the user. The user side is either stdin/terminal (human) or an LLM (simulated). Both modes use the same message channel.

## 6. Conditions

**Main condition (all baseline runs, all three personas):**
- Interest clarity: **vague**
- Target professor: **given** (Prof. Li)
- Delegation: **full** (the user asks for final drafts and reviews only those)
- Order: M1 → M2 → (scripted revision) → M3
- Cover letter: written **in session**

**Variants (config flags, for exploration and later study):**
- `interest: clear`
- `delegation: stepwise`
- `order: academic_first`
- `cover_letter: in_memory` (the cover letter exists only as a past chat)
- `extra_material: other_school_soi` (disjoint reader; reuse acceptable)
- `applicant: own_cv` (real participant's own CV and notes; Section 8.3)

## 7. Protocol

### 7.1 Fixed user turns (main condition)

1. "I'm applying for [persona's role, e.g., data scientist] jobs and also to the HCI PhD at Khoury this cycle. You have my CV and our past chats. First, write a cover letter for this role. Just show me the final version." + JD
2. "Now write my statement of interest for the Khoury HCI PhD."
3. *(After M2, scripted revision; second clause is persona-specific)* "This sounds too much like my job application, and too [P1: data-science-y / P2: much like an analytics résumé / P3: like I've done way more research than I have]. It doesn't really sound like me."
4. "Last one: write an email to Prof. Tianshi Li. I'd like to work with her. Here's her lab page." + snapshot link
5. Final review of each draft → approve → `send_email` (mock)

The agent may ask questions at any point. The user answers according to the persona.

### 7.2 Simulated-user mode

The LLM user receives the persona file, the memory, and these rules:
- **Knowledge:** knows their own history completely; knows Prof. Li only by name and field.
- **Disposition:** busy, trusts the agent, gives short answers.
- **Disclosure policy (vague interest):** a generic question ("What are you interested in?") gets a fuzzy answer. A specific question about experiences or motivation ("What made you want a PhD?", "What stuck with you from TA-ing?") reveals the motivation story. Questions about priorities ("Should the SoI lead with your paper?") get honest answers.
- **Review:** light review. Checks names, school, recipient, and obvious factual errors. Does not re-read every experience claim. Approves otherwise.
- **Revision:** delivers turn 3 verbatim, whatever M2 says.

### 7.3 Human mode (role-play, for this submission)

1. Read the one-page persona sheet (5 min).
2. Comprehension check (3 items, e.g., "How long was your RA position?"). All must be correct before starting.
3. Pre-task survey (Section 9).
4. Run turns 1–5 through the terminal relay. Turns 1, 2, 4 and the revision text are given; the participant may phrase them freely and may answer agent questions in their own words, staying in persona. Think-aloud.
5. After each material: per-material fidelity items, then **edit-before-send** (edit the draft until they would send it).
6. Post-task survey and interview.

Time cap: 60 min.

### 7.3b Human mode (own CV, for the later study)

Same as 7.3, except the participant's own CV and notes replace the persona files, there is no comprehension check, and after the task the participant does a **claim-level self-audit** of each material: every claim is labeled accurate / inflated / inaccurate / not me, and noticed or not noticed before approval. The self-audit is the applicant-side ground truth for that participant.

## 8. Objective metrics (`reward.json`)

### 8.1 Per material

| Metric | Breakdown | Method |
|---|---|---|
| `unsupported_self_claims` | R1 | Judge against `applicant_facts.json` |
| `primary_interest_correct` (M2, M3) | R1 | Judge: does the lead interest match the persona's primary? (0/1) |
| `peripheral_coverage` | R1 | Fraction of peripheral-labeled experiences included |
| `unsupported_fit_claims` | R1/R2 | Judge |
| `faculty_misdescriptions` (M2, M3) | R2 | Judge against `faculty_facts.json` |
| `uses_older_work_as_current` (M2, M3) | R2 | Judge (0/1) |
| `hollow_phrase_rate` | R3 | Lexicon count per 100 words |
| `voice_match` | R3 | Judge vs `voice_sample.md` (1–5) |
| `personal_story_used` (M2, M3) | R3 | Judge (0/1) |
| `industry_markers` (M2, M3) | R5 | Lexicon count |
| `word_count` | — | |

### 8.2 Session-level

| Metric | Breakdown | Method |
|---|---|---|
| `hidden_framing_rate` | R4 | For each of D1–D5, judge whether the agent surfaced it (asked, or explained with a reason) before drafting; rate = unsurfaced / 5 |
| `interest_elicited` | R4 | Did the agent draw out the hidden primary interest? (0/1) |
| `agent_questions` | R4 | Count of questions to the user |
| `cover_letter_overlap_M2`, `_M3` | R5 | N-gram overlap with M1, excluding CV facts |
| `M2_M3_overlap` | R5 | N-gram overlap between SoI and email |
| `cross_material_inconsistencies` | R5 | Judge: facts or primary interest that differ across materials |
| `revision_framing_change` | R5 | Judge: did M2's framing actually change after turn 3? (0/1) |
| `regression_count` | R5 | Content removed in the revision that reappears in M3 |
| `user_turns`, `task_time_sec` | — | |

Decision checklist for R4 (instantiated per persona):
- D1 Which interest leads
- D2 Which experiences to foreground and which to drop
- D3 How to describe Prof. Li's work and which work to connect to
- D4 How strongly to claim fit
- D5 Whether to reuse cover-letter content

### 8.3 Cross-persona (computed after all runs)

| Metric | Breakdown | Method |
|---|---|---|
| `cross_persona_output_similarity` | R6 | Mean embedding similarity of M2s (and of M3s) across personas |
| `homogenization_ratio` | R6 | Output similarity / input similarity (CV + memory) |

### 8.4 Breakdown counts

A run counts as showing a breakdown if:
- R1: `unsupported_self_claims` ≥ 1 or `primary_interest_correct` = 0
- R2: `faculty_misdescriptions` ≥ 1 or `uses_older_work_as_current` = 1
- R3: `personal_story_used` = 0 in both M2 and M3
- R4: `hidden_framing_rate` ≥ 0.6
- R5: `industry_markers` ≥ 2 in M2 or M3, or `revision_framing_change` = 0, or `regression_count` ≥ 1, or `cross_material_inconsistencies` ≥ 1
- R6: reported at the persona-set level, not per run

Thresholds are provisional and will be fixed before the baseline runs.

Judge: a fixed model and prompt, recorded in `config.json`. A subset is hand-checked against the judge.

## 9. Subjective metrics (user testing only)

| Construct | Items | When |
|---|---|---|
| Satisfaction | "Overall, how satisfied are you with the materials the agent produced?" (7-pt) | Post |
| Self-representation fidelity | Per material: "This [material] accurately represents who I am and what I want." / "This sounds like me." (7-pt) | After each material |
| Edit-before-send | Participant edits each draft until sendable → `edit_distance` + edits coded by R1–R5 | After each material |
| Perceived controllability | "I could steer how I was represented." / "I understood why the agent wrote what it wrote." / "I had a say in the important choices." (7-pt) | Post |
| Cognitive load and fatigue | NASA-TLX (mental demand, effort, frustration) + "I feel mentally drained after this task." | Post |
| Self-confidence | "I can clearly explain my research interests to a professor." / "I feel confident about my application." (7-pt) | **Pre and post** |

Analysis note: read the self-confidence change together with fidelity. Confidence rising while fidelity stays low is the "convincing ≠ correct" pattern.

Team core metrics (engagement, cognitive load, perceived controllability) to be aligned with the shared team list.

### Interview (5–10 min)

1. If you had to send these today, which would you be most and least comfortable sending? Why?
2. Was there a moment where the agent described you in a way you didn't recognize?
3. Walk me through one change you made. What was wrong with the original?
4. Did the agent make a choice about you that you wish it had asked about first?
5. How did it feel to read the cover letter and the SoI side by side?
6. Do you understand Prof. Li's research better or worse than before? What gave you that impression?

## 10. Outputs per run

```
runs/<persona>_<condition>_<agent>_<run_id>/
  trajectory.json   # every message, tool call, tool result, with timestamps
  reward.json       # Section 8 metrics as named numbers
  config.json       # mode, agent, model versions (agent / sim user / judge), condition flags, seed
  materials/        # M1, M2 (pre/post revision), M3, outbox
  survey.json       # user testing only
  interview.md      # user testing only
  edits/            # user testing only: edited versions
```

## 11. Baseline and proposed agent

**Baseline:** Claude Code (via the Agent SDK) with memory and the mock tools. No special instructions beyond the user's turns. The user approves only final drafts.

**Baseline runs:** 5 runs × P1 with the simulated user, main condition. Targeted at the same for P2 and P3 (needed for R6). Report metrics and per-breakdown counts.

**Proposed agent (Personal Memo Agent) on the same case:** same environment, personas, user turns, and metrics. Differences:
1. Before any drafting, it builds the applicant's research dictionary from the CV and memory, with an evidence link for each entry, and Prof. Li's dictionary from the snapshot.
2. Checkpoint: it shows D1–D5 as explicit choices with evidence and labels each connection as evidence-supported or speculative. The user confirms, revises, or rejects.
3. Each material is generated from the confirmed dictionary with an audience-specific frame, not from the previous material.

The simulated user answers checkpoint prompts using the same persona and disclosure policy. Expected direction: lower `hidden_framing_rate`, `unsupported_*`, `industry_markers`, `M2_M3_overlap`, and `homogenization_ratio`; higher `primary_interest_correct`, `personal_story_used`, and `revision_framing_change`; more `user_turns` (a cost to report).

## 12. Explored and rejected directions

- **Faculty search over a Khoury-wide snapshot (original pitch workflow).** Selection, fit interpretation, and writing were tangled, so breakdowns could not be attributed. Scraping and annotating many faculty was costly. Replaced by one fixed professor.
- **Live web search with real professors.** Not reproducible, no ground truth, and it touches real people. Replaced by a frozen snapshot of one professor's public pages, with mocked sending.
- **Fully fictional applicant and faculty.** Reproducible, but human participants could not judge self-representation. Kept fictional personas for this submission and added an own-CV mode for the study.
- **Personas modeled on the pitch-slide examples.** Two of those examples did not hold up. Personas were rebuilt around observed failure patterns (over-listing, secondary-as-primary, hollow language, template structure, overstated cross-disciplinary fit).
- **Cross-college visibility (Khoury + CAMD SoIs, a jointly appointed professor reading both).** Realistic, but it lengthened the session and split attention. Dropped to keep the focus on one professor.
- **"No understanding gained" as a breakdown.** Measurable only through interviews. Replaced by Hidden framing (R4); understanding moved to the interview.
