# Tests 4 and 5: vague users, and the pause before writing

14–15 November 2026 · skill under test: the repo's claude.ai build (`dist/claude-ai/original`, frozen in `runs/skill-repo/`)

## Test 4: vague users

8 new vague personas (4 per task: Jo, Ines, Raj, Theo; Max, Grace, Bo, Hana). Four of them hold one useful detail they share only if a question asks for it specifically (Ines: an AI-written checkout form with no screen-reader labels; Raj: the test suite grew from 2,000 to 9,000 tests and the nightly run from 20 minutes to 3 hours; Grace: a 700-day Welsh streak kept with her daughter; Hana: a gardening blog, and "nothing grows in January"). Arms:
- **skill**: the full flow, including routing, the shortlist and the "default done well?" check.
- **skill_direct**: the same questions and answers, forced down the direct path.
- **plain_asks**: a plain model asks its own questions.
- **plain**: no questions.

| Task | Arm | Spread (0–3, lower = more spread) | Distinct of 4 | Score vs plain (lower = further) | Fit | Quality | Embed within | Embed vs plain |
|---|---|---|---|---|---|---|---|---|
| talk | plain | 1.67 | 2 | — | 0.50 | 4.0 | 0.81 | — |
| talk | skill | 0.33 | 4 | 0.81 | 1.00 | 4.0 | 0.64 | 0.72 |
| talk | skill_direct | 0.33 | 4 | **0.56** | 1.00 | 4.2 | 0.68 | 0.72 |
| talk | plain_asks | **0.17** | 4 | 0.75 | 1.00 | **4.5** | 0.70 | 0.73 |
| blog | plain | 2.67 | 1 | — | 0.25 | 4.0 | 0.83 | — |
| blog | skill | 0.17 | 4 | 0.81 | 1.00 | 4.0 | 0.62 | 0.70 |
| blog | skill_direct | 0.17 | 4 | **0.62** | 1.00 | **4.8** | **0.59** | **0.69** |
| blog | plain_asks | 0.50 | 3 | 0.88 | 1.00 | 4.2 | 0.65 | 0.72 |

**Routing:**
- Shortlist: Max, Theo.
- "Default done well, or a shortlist?" check: Bo, Jo, Raj. All three chose the default.
- Direct path, because their answers included a specific: Ines, Grace, Hana.

**Hidden details drawn out:**
- Skill's questions: 3 of 4 (missed Raj's number; the skill's real-case question gave no option for numbers).
- Plain model's own questions: 4 of 4.

**What it means:**
- Even vague users gave enough (their role, audience, one view) that every arm with questions reached 4 distinct ideas and perfect fit.
- **The shortlist and the "default done well?" check didn't help vague users.** Forced-direct from the same answers scored higher on quality (talk 4.2 vs 4.0, blog 4.8 vs 4.0) and landed further from the default (0.56/0.62 vs 0.81/0.81). When offered the default, vague users took it, so the check pulled outputs back toward it.
- **The skill's questions still didn't beat a plain model's own**, now for vague users too. Fit was the same and quality was similar or higher for plain_asks, and plain_asks drew out the one detail the skill missed.

## Test 5: the pause before writing a talk (repo build)

The repo build pauses before writing a talk, and invites additions after shorter pieces. This test replayed the 8 clear personas with their v2 answers; personas replied to the pause. **Three runs (Marcus, Dana, Leah) were stopped by a model safety check (`reasoning_extraction`) and are missing or partial.** Leah's and Ruth's posts had already been saved before the stop.

| Task | v1 full | v2 | repo build (pause) |
|---|---|---|---|
| talk quality (Priya, Sam) | 4.5 | 4.0 | **3.5** |
| blog quality (Kev, Leah, Ruth, Tomás) | 4.75 | 4.5 | **3.75** |

**What it means:**
- The pause didn't recover talk quality. Personas did use it: Priya added her three rules and kept her seniors anonymous; Sam corrected the audience and named the compliance team. But the judge still rated the result lower.
- Most of the drop comes from things left inside the finished piece: bracketed placeholders, "[unchecked]" notes, editorial brackets. Kev and Tomás each dropped to 3 for this reason. The judge reads "would the asker be glad to use it as is", so honesty markers inside the text cost points.
- Putting these checks in a short note *after* the deliverable would likely keep the honesty without the cost.

## Overall, across all five tests

- **The value is in asking before writing.** In every test, outputs with the user's answers spread to 4 ideas with perfect fit, against 1–2 ideas for the plain model.
- **The skill's specific question design adds nothing measurable over a plain model asked to clarify first**, for clear or vague users.
- **The generate–shortlist–pick machinery and the "default done well?" check don't improve outputs**, and the check pulls vague users back to the default.
- **What still distinguishes the skill:** it makes the model ask; it shows the user the default; it gives objection and test lines (which users acted on); and it is honest about unchecked facts and invented details. The last of these should move out of the deliverable into a note.

## Limits

4 outputs per arm per task, one judge pass, same model family throughout, model-written personas (the hidden-detail design is engineered), 3 safety-stopped runs in Test 5.
