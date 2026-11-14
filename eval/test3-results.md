# Test 3: the skill's questions vs a plain model's own clarifying questions

14 November 2026 · iteration 3 · 8 personas · arms: plain, plain_ctx (skill's questions), plain_asks (model's own questions), v2

## Answer

**With these personas, the skill's question design added nothing measurable.** A plain model told only to "ask whatever clarifying questions would help, then write" matched the skill on spread, fit, distance from the default and quality. It reached the same main idea as v2 for 6 of 8 personas; for the other 2 (Priya, Sam), the idea was the same with different supporting choices.

| Task | Arm | Spread (0–3, lower = more spread) | Distinct ideas of 4 | Score vs plain | Fit | Quality | Embed within | Embed vs plain |
|---|---|---|---|---|---|---|---|---|
| talk | plain | 2.33 | 1 | — | 0.50 | 4.0 | 0.81 | — |
| talk | plain_ctx | 0.00 | 4 | 0.75 | 1.00 | 4.5 | 0.70 | 0.69 |
| talk | plain_asks | 0.17 | 4 | 0.75 | 1.00 | 4.5 | 0.65 | 0.67 |
| talk | v2 | 0.00 | 4 | 0.75 | 1.00 | 4.2 | 0.67 | 0.66 |
| blog | plain | 3.00 | 1 | — | 0.75 | 4.0 | 0.83 | — |
| blog | plain_ctx | 0.00 | 4 | 0.50 | 1.00 | 4.2 | 0.57 | 0.64 |
| blog | plain_asks | 0.00 | 4 | 0.50 | 1.00 | 4.0 | 0.58 | 0.67 |
| blog | v2 | 0.00 | 4 | 0.50 | 1.00 | 4.2 | 0.50 | 0.61 |

## Why

- **The plain model's questions were already good.** It asked 4–6 questions every time. Every set asked for a real story or company specifics, and most asked for the user's position and named the generic version to avoid ("so it isn't a generic pros-and-cons list"). Current models already do what the skill's step 2 asks for, once they're told to ask.
- **The personas answered fully whatever they were asked.** Each one had a ready case with numbers and gave it in response to any "do you have a story?" question. Ruth's persona added new details (garden-centre laps, filing deadlines) that weren't on her card.

## What this means

The value is in **asking before writing**. The plain model never asks unless told to, and that is the one thing that reliably mattered here. What's left of the skill:
1. It makes the model ask, which a plain prompt doesn't.
2. The "What everyone gets" step and the distance section make the default visible. This is useful for the user's understanding; it wasn't measured here.
3. The objection and test lines, which users acted on.
4. The shortlist for vague users. Whether it improves their outputs is still untested, and that's where question design is most likely to matter.

## Limits

Same as before: 4 per arm per task, one judge pass, model-written personas who are easy to interview. A vague-persona version of this test is the deciding one.
