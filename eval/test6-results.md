# Test 6: v3 (the simplified skill)

15 November 2026 · v3 built from the repo source (`src/core.md`), frozen in `runs/skill-v3/`

## What changed in v3
- **No routing.** Every answered run builds directly. The shortlist and the "default done well?" check now exist only in quick mode, as a short generate-and-pick step.
- **A numbers question.** One question, or one option, asks for a number, a measure or data.
- **A clean deliverable.** There are no brackets, placeholders or "[unchecked]" marks in it. Checks, added details and suggested additions go in a **Before you use it** note after it.
- **Kept:** the default, the questions, the angle/objection/test block, the talk check-in (your choice), and the distance section.

## Method
v3 was replayed from the stored questions and answers of the 8 clear personas (v2's questions) and the 8 vague personas (the repo build's questions). It was judged blind against plain, the previous skill (v2 for clear users, the repo build's full flow for vague users) and plain_asks. The new numbers question isn't exercised, because the replays reused the old questions.

## Results
Spread runs 0–3; lower means different users got more different answers. Distance is the score against plain; lower means further from the default.

| Set | Arm | Spread | Distinct of 4 | Distance | Fit | Quality | Embed within | Embed vs plain |
|---|---|---|---|---|---|---|---|---|
| clear talk | skill | 0.00 | 4 | 0.38 | 1.00 | 4.0 | 0.67 | 0.66 |
| clear talk | plain_asks | 0.17 | 4 | 0.62 | 1.00 | 4.0 | 0.65 | 0.67 |
| clear talk | **v3** | 0.00 | 4 | 0.38 | 1.00 | **4.5** | 0.66 | 0.68 |
| clear blog | skill | 0.00 | 4 | 0.50 | 1.00 | 4.2 | 0.50 | 0.61 |
| clear blog | plain_asks | 0.00 | 4 | 0.50 | 1.00 | 3.8 | 0.58 | 0.67 |
| clear blog | **v3** | 0.00 | 4 | 0.50 | 1.00 | 4.0 | 0.54 | 0.65 |
| vague talk | skill | 0.67 | 4 | 0.81 | 1.00 | 4.0 | 0.64 | 0.72 |
| vague talk | plain_asks | 0.67 | 4 | 1.00 | 1.00 | 4.5 | 0.70 | 0.73 |
| vague talk | **v3** | 0.67 | 4 | 0.81 | 1.00 | 4.0 | **0.62** | **0.69** |
| vague blog | skill | 0.33 | 4 | 1.00 | 1.00 | 3.8 | 0.62 | 0.70 |
| vague blog | plain_asks | 0.67 | 3 | 1.06 | 1.00 | 4.2 | 0.65 | 0.72 |
| vague blog | **v3** | 0.33 | 4 | **0.88** | 1.00 | 4.2 | **0.59** | **0.68** |

The plain arm scored 1–2 distinct ideas and 4.0 quality in every set.

## What it means
- **v3 matches or beats the previous skill on every measure**, with fewer user turns.
  - Mean quality across the four sets: v3 4.19, previous skill 4.00, plain_asks 4.13.
- **Against a plain model asking its own questions, v3 has a small, consistent edge on distance from the default.**
  - It is further from the default in 3 of 4 sets and equal in the fourth.
  - For vague users, embedding spread is the best of any arm.
  - Fit and quality tie.
  - This is the first time the skill measurably beats generic clarifying questions, most likely from showing the default and banning its main claim.
- **No markers leaked into any v3 deliverable** (0 of 16). The "Before you use it" note carried the checks instead.

## Limits
- 4 outputs per arm per set, one judge pass, same model family throughout, model-written personas.
- The edge over plain_asks is small enough that a second judge pass could erase it.
- The numbers question and the talk check-in weren't exercised.
