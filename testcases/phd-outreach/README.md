# Test Case: One Applicant, Three Audiences

An AI agent writes an industry cover letter, a Khoury HCI PhD statement of interest, and an outreach email to Prof. Tianshi Li for one applicant, in one session. The case measures whether the agent represents the applicant and the professor correctly and fits each material to its audience, when the user reviews only final drafts.

## What's here

| Path | Contents |
|---|---|
| `personas/p1..p3/` | CV, memory (past-chat summaries), JD, turn script, persona sheet (human mode), sim-user profile, voice sample, `ground_truth/` |
| `environment/faculty_snapshot/tianshi-li/` | Frozen snapshot of Prof. Li's public pages (fetched 2026-11-15) |
| `ground_truth/faculty_facts.json` | Professor ground truth (judge only) |
| `harness/` | Agent wrapper, mock tools, relay, simulated user, judge, survey |
| `prompts/` | Shared simulated-user prompt |
| `study/` | Survey items and interview template |
| `runs/` | One folder per run (outputs below) |
| `tests/` | Offline tests (no API calls) |

## External systems

| System | Used for | Mocked? |
|---|---|---|
| Web search | Agent looks up the professor | **Mocked**: offline keyword search over the snapshot |
| Web pages | Agent reads the professor's pages | **Mocked**: frozen snapshot; any other URL returns 404 |
| Email | Agent sends the outreach email | **Mocked**: written to `runs/<run>/outbox/`; the recipient address is `@mock.invalid` |
| Anthropic API | Agent, simulated user, judge | Real (needs an API key) |

The agent cannot use Bash, live web search, or web fetch, and is denied read/write access to everything in this repository. Its workspace is a fresh temp directory holding only `cv.md`, `jd.md`, and `memory/`.

## Setup

Requirements: Docker (recommended) or Python 3.12+, and an Anthropic API key.

All commands below run from this folder:

```bash
git clone https://github.com/Minage223/CS6983_agent-controll.git
```

```bash
cd CS6983_agent-controll/testcases/phd-outreach
```

**The key never goes into this repository.** `.env.example` holds only a placeholder. Set the key in your own shell before running anything; Docker Compose passes it through from there.

```bash
export ANTHROPIC_API_KEY=<your key>
```

No spaces around `=`. To keep the key out of your shell history, paste it at a hidden prompt instead:

```bash
read -s "ANTHROPIC_API_KEY?Paste your key: " && export ANTHROPIC_API_KEY
```

(That `read` syntax is for zsh, the macOS default. In bash: `read -s -p "Paste your key: " ANTHROPIC_API_KEY && export ANTHROPIC_API_KEY`.)

```bash
docker compose build
```

Without Docker:

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
```

## Run: simulated-user mode (baseline, 5 runs)

```bash
docker compose run --rm testcase --persona p1 --mode sim --runs 5
```

Without Docker: `.venv/bin/python -m harness.run --persona p1 --mode sim --runs 5`. Repeat with `p2` and `p3` for the cross-persona comparison.

## Run: user-testing mode (a person plays the user)

1. The facilitator gives the participant `personas/<id>/persona_sheet.md` (5 minutes), then asks the 3 comprehension-check questions at the bottom of the sheet. All must be correct.
2. Start the session. The participant answers the pre-task survey in the terminal, then talks to the agent. At each step the suggested line is shown; Enter sends it, or the participant types their own words. Type `/next` to finish a step, `/quit` to stop. Ask the participant to think aloud.

```bash
docker compose run --rm testcase --persona p1 --mode human
```

3. After the session: per-material ratings, edit-before-send (the participant edits each draft in `runs/<run>/edits/` until they would send it), then the post-task survey.

```bash
docker compose run --rm survey post runs/<run-folder>
```

4. Interview (5–10 min) using `runs/<run>/interview.md`.

Own-CV variant (later study): replace the persona's `cv.md` and `memory/` with the participant's materials in a copy of the persona folder, and add the claim-level self-audit after the survey.

## Cross-persona comparison (R6)

```bash
docker compose run --rm cross
```

With no arguments it uses every scored run under `runs/`; pass run folders to use a subset. For each material it reports the mean TF-IDF cosine between runs of the same persona (`within_persona`) and of different personas (`between_persona`). `homogenization_ratio` = between / within; near 1 means the output barely depends on who the applicant is. R6 is flagged at 0.8 or above (provisional). Needs at least 2 runs of one persona.

## Outputs per run (`runs/<persona>_<condition>_<agent>_<mode>_<timestamp>_<k>/`)

| File | Contents |
|---|---|
| `trajectory.json` | Every user message, assistant text, tool call, tool result, phase marker, with timestamps |
| `reward.json` | Objective metrics (per material, per session) and breakdown flags R1–R5 |
| `config.json` | Mode, persona, condition, agent and model versions, sim-user and judge settings, cost |
| `materials/` | Each draft as delivered, the sent email, and the judge's extracted text |
| `judge_details.json` | Judge outputs with quoted evidence for every flagged claim |
| `outbox/` | Mock-sent emails |
| `survey.json`, `edits/`, `interview.md` | User testing only |

Re-score a run with `python -m harness.run --rejudge runs/<folder>`.

## Tests

```bash
.venv/bin/python tests/test_offline.py
```
