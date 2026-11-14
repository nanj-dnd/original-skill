# Evaluation of this skill, November 2026

Three rounds, 14 Nov 2026: a pilot of v1, a check of v2, then Test 3 (generic questions). Small samples and
model-written personas, so read the numbers as direction, not effect size.

## Setup

- **Tasks**: a 5-minute all-hands talk on AI coding assistants (default: "powerful tool,
  not a replacement; review everything") and a ~400-word post on why New Year's
  resolutions fail (default: "too vague, too big, willpower; build small habits").
- **Personas**: 8 hand-written, 4 per task, each with a view, a real case with numbers,
  an audience and an answering style. Two (Sam, Kev) mostly agree with the default.
  The v2 check added two vague personas (Jo, Max) with no case and soft views.
- **Arms**: plain (task only) · plain + answers (the persona's answers to this skill's
  questions, without "What everyone gets") · quick mode · full v1 · v2 (replaying the
  same answers) · plain_asks (the plain model asks its own questions; Test 3).
- **Judging**, blind: main claim and choices extracted per output; pairs scored 0–3 for
  sameness of idea; fit (which of two personas was this written for; chance 50%);
  quality 1–5; embedding similarity as a second spread measure.

## Pilot (v1)

| Arm | Distinct main ideas of 4 | Fit | Quality |
|---|---|---|---|
| Plain | 1 per task | chance | 4.0–5.0 |
| Plain + answers | 4 | 4/4 | 4.0–4.2 |
| Quick mode | 3–4 | chance | 4.2–4.8 |
| Full v1 | 4 | 4/4 | 4.0–4.2 |

- With no skill, every user got the same answer.
- Full v1 and plain + answers reached the same main idea for 8 of 8 personas. The
  shortlist added a user turn and about 3× the tokens without changing the idea.
- The pick step still mattered: users added tweaks when choosing (a line from another
  candidate, an anonymised example, a closing), and those reached the deliverables.
- Quick mode moved furthest from the default but nobody could tell whose output it was.
  It also got the top blog quality score, possibly the judge favouring novel framings.
- Agreeing users (Sam, Kev) were told they agreed with the default, and still got
  distinct, well-fitted outputs from their specifics.
- Users engaged with the objection and test lines and corrected their own claims.

## v2 check

- Replayed with the same answers, v2 matched v1 on spread, distance and fit for all 8
  personas, with 2 user turns instead of 3.
- Talk quality fell from 4.8 to 4.2; blog rose from 4.8 to 5.0. Of the talk dip, one
  point was a test-harness leak; about half was the lost pick-time tweaks.
- **Routing bug, fixed**: the first rule counted "a stated position of their own" as a
  specific, so vague Max's picked option ("the date is the problem") sent him down the
  direct path. The fix: specifics must be in the user's own words and not guessable; a
  picked option is a direction. Max then went to the shortlist.
- Jo (vague) went to the shortlist. With no real day to draw on, the run wrote
  placeholders instead of inventing one, and said the position had not moved.

## Test 3: this skill's questions vs a plain model's own

A plain model told only to "ask whatever clarifying questions would help, then write"
(plain_asks) matched this skill on every measure, with the same 8 personas.

| Arm | Distinct ideas of 4 (talk / blog) | Fit | Quality (talk / blog) |
|---|---|---|---|
| Plain | 1 / 1 | chance | 4.0 / 4.0 |
| Plain + this skill's questions | 4 / 4 | 4/4 | 4.5 / 4.2 |
| Plain + its own questions | 4 / 4 | 4/4 | 4.5 / 4.0 |
| v2 | 4 / 4 | 4/4 | 4.2 / 4.2 |

- plain_asks reached the same main idea as v2 for 6 of 8 personas, and the same idea
  with different supporting choices for the other 2.
- The plain model's questions were already good: 4–6 each time, every set asked for a
  real story or specifics, and most named the generic version to avoid.
- So the gain is from asking before writing, which a plain model never does unasked;
  the wording of these questions added nothing measurable with clear-view users. What
  this skill adds on top: it makes the model ask, it shows the default, its objection
  and test lines (which users acted on), and the shortlist for vague users (untested
  for quality).

## What runs did badly

- Cited studies from memory (web search was off) and flagged them as unchecked, but a
  real run should verify them.
- Added small invented details ("forgive myself by teatime") and did not always flag
  them.

## Limits

- 4 outputs per arm per task, one judge pass, same model family for runs, personas and
  judges.
- Vivid personas with a story ready, which is when context dominates. Vague users were
  tested for routing only, not output quality.
- The personas answered fully whatever they were asked, so question design had little
  to win; Test 3 should be repeated with vague personas before concluding it never
  matters.

## Open tests, most useful first

1. Vague users for quality: 4+ per task, comparing v2's shortlist path, writing directly
   from thin answers, and plain_asks. This is where question design should matter most.
2. (Done: plain_asks, see Test 3.)
3. Whether a cheap "anything to add?" moment recovers the pick-time tweaks without a
   mandatory extra turn.
4. Real users on 2–3 real tasks.
5. 8+ outputs per arm, two judge passes, a judge from another model family.
6. Runs with web search on, to see unverified figures actually get checked.
