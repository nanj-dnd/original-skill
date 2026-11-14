# Pilot: does `original` move answers off the default?

13 November 2026 · iteration 1 · 2 tasks × 4 personas × 4 arms = 32 outputs

## Answer

**Yes, outputs move a long way off the default. But almost all of the gain comes from the skill's questions, not from its generate-and-shortlist steps.** A plain model given the same questions and answers wrote the same main idea as the full skill for 8 of 8 personas.

## Setup

- **Tasks:** a 5-minute all-hands talk on AI coding assistants, and a 400-word blog post on why New Year's resolutions fail. Both have a strong default.
- **Personas:** 8 hand-written people, each with specific views, numbers and a real case (`personas/`). Two of them (Sam, Kev) mostly agree with the default, to test that path. A separate agent role-played each persona and answered the skill's questions and shortlist pick.
- **Arms:**
  - `plain`: the model, with no skill and no questions.
  - `plain_ctx`: the model plus the persona's answers to the skill's own questions, with "What everyone gets" removed.
  - `quick`: the skill in quick mode, with no questions.
  - `full`: the whole skill, including the questions, the shortlist and the persona's pick.
- **Judging:** all blind, using random IDs. One judge pulled out each output's main claim and key choices and rated quality from 1 to 5. A second judge scored pairs from those extracts on a 0–3 "same idea?" scale and grouped them into clusters. A third judge was shown each output with the true persona and a decoy, and had to pick the true one. Separately, embedding cosine similarity was computed with all-mpnet-base-v2.

## Results

"Same-idea score" is how similar the outputs within one arm are, from 0 to 3; lower means different users got different answers. "Score vs plain" is the same scale measured against the plain arm, so lower means further from the default. Fit is how often the judge picked the true persona; chance is 0.50.

**Talk**

| arm | same-idea score | distinct main ideas (of 4) | score vs plain | fit | quality | embed within | embed vs plain |
|---|---|---|---|---|---|---|---|
| plain | 2.50 | 1 | — | 0.75 | 5.0 | 0.81 | — |
| plain_ctx | 0.17 | 4 | 0.75 | **1.00** | 4.0 | 0.70 | 0.69 |
| quick | 0.50 | 3 | **0.06** | 0.50 | 4.2 | 0.79 | 0.72 |
| full | **0.00** | **4** | 0.69 | **1.00** | 4.0 | **0.56** | **0.60** |

**Resolutions**

| arm | same-idea score | distinct main ideas (of 4) | score vs plain | fit | quality | embed within | embed vs plain |
|---|---|---|---|---|---|---|---|
| plain | 3.00 | 1 | — | 0.50 | 4.0 | 0.83 | — |
| plain_ctx | **0.00** | 4 | 0.38 | **1.00** | 4.2 | 0.57 | 0.64 |
| quick | 0.33 | 4 | 0.81 | 0.50 | **4.8** | 0.68 | 0.72 |
| full | **0.00** | 4 | 0.38 | **1.00** | 4.2 | **0.51** | **0.63** |

**Full skill vs. context only, persona by persona:** the "same idea?" judge gave 3 out of 3 to all 8 pairs. The full skill and the plain model with the same answers landed on the same main claim and mostly the same choices every time.

## What this says

1. **The core problem is real here too.** With no skill, 4 runs gave 1 main idea per task. In the resolutions task all four plain posts were the same "vague goals and willpower, build small habits" post.
2. **The questions are the active ingredient.** Once the answers exist, the plain model and the full skill reach the same idea, with the same fit and quality. On this evidence, steps 3–5 (12–15 candidates, cuts, shortlist, pick) cost a user turn and about 3–4× the tokens of the context-only arm without changing the main claim.
   - The full arm does spread slightly more by embeddings in the talk task (0.56 vs 0.70). That likely reflects structure and framing more than the main idea: the postmortem shape, the live vote.
3. **Quick mode gets off the default without knowing the user.** It produced 3–4 distinct ideas, and in the talk task its ideas were the furthest from the default of any arm (0.06). But fit stays at chance: different, not yours. It also scored the highest quality on resolutions (4.8), which may be the judge favouring novel framings, as the research warns.
4. **The "agrees with the default" path held up.** Sam and Kev mostly took the default's options, and the skill said so and built from their specifics. Both still ended up with distinct, well-fitted outputs, though so did their context-only versions.

## Why not to over-read this

- **n = 4 per arm per task**, with a single judge run for each measure. Treat the direction as a signal, not the size.
- **The personas are vivid.** Each one has a strong, unusual view and a story ready to tell. That is exactly when context dominates. The generate-and-shortlist step could matter more for real users with half-formed views, which this pilot didn't test.
- **`plain_ctx` was given the skill's own questions.** So this shows the skill's questions plus a plain model are enough. It does not show that any questions would be. Each of those questions names a default choice, so some of the skill's method leaked into this arm.
- The judges are the same model family as the runs, and quality is judged by a model.

## Suggested next round

1. **Add a `plain_asks` arm.** The plain model writes its own clarifying questions with no skill, the persona answers, and then it writes. This shows whether the skill's question design (each question targeting a default choice) beats generic clarifying questions. It's the most useful single test.
2. **Add 2–3 "thin" personas** with vague or half-formed views, to see whether steps 3–5 earn their cost when the answers are weak.
3. **If both confirm this pilot,** consider a skill change: when the answers are specific and move away from the default, skip the shortlist and write directly (what quick mode does now), and keep the shortlist for thin or default-matching answers. That saves the user a turn. I haven't made this change.

## Files

- `/home/user/original-eval/pilot-viewer.html`: all 32 outputs to read side by side
- `/home/user/original-workspace/iteration-1/pilot_scores.md`, `embed_scores.md`: raw scores
- `/home/user/original-workspace/iteration-1/<case>/<arm>/outputs/`: every output. Full runs also hold `questions.md`, `answers.md`, `shortlist.md` and `distance.md`.
- `/home/user/original-eval/`: tasks, personas, prompts and scripts to rerun it
