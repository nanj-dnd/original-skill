# Evaluation of this skill, November 2026

Six rounds, 14–15 Nov 2026: a pilot of v1, a check of v2, Test 3 (generic questions), Test 4 (vague users), Test 5 (the pause), Test 6 (v3). Small samples and
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

## Test 4: vague users

8 vague personas, 4 of them holding one detail they'd give only if asked for it specifically.

| Arm | Distinct ideas of 4 (talk / blog) | Fit | Quality (talk / blog) | Score vs plain (lower = further) |
|---|---|---|---|---|
| Plain | 2 / 1 | chance | 4.0 / 4.0 | — |
| This skill (full flow) | 4 / 4 | 4/4 | 4.0 / 4.0 | 0.81 / 0.81 |
| Same answers, forced direct path | 4 / 4 | 4/4 | 4.2 / 4.8 | 0.56 / 0.62 |
| Plain model's own questions | 4 / 3 | 4/4 | 4.5 / 4.2 | 0.75 / 0.88 |

- The shortlist and the "default done well?" check didn't help. Writing directly from the
  same answers scored higher and landed further from the default. All three users offered
  the default (Bo, Jo, Raj) took it.
- These questions drew out 3 of 4 hidden details; a plain model's own drew out 4 of 4. The
  miss: the real-case question offered no option for numbers.

## Test 5: the pause before writing a talk

The pause did not recover quality (talk 3.5 vs 4.0 for v2; blog 3.75 vs 4.5). Users did add
things at the pause, but the judge marked pieces down for placeholders and "[unchecked]"
notes left inside the deliverable. Three runs were stopped by a model safety check and are
missing.

## Overall

The gain comes from asking before writing. This skill's question wording, its shortlist and
its "default done well?" check add nothing measurable on top. What still distinguishes it:
it makes the model ask, shows the default, gives objection and test lines, and flags
unchecked facts. Those flags belong in a note after the deliverable, not inside it.

## Test 6: v3

v3 drops routing (every answered run builds directly), adds a numbers question, and moves
checks into a "Before you use it" note so the deliverable has no brackets or "[unchecked]"
marks. It was replayed from the stored answers of all 16 personas.

| Arm | Mean quality (4 sets) | Distance from default, lower = further (clear talk / clear blog / vague talk / vague blog) |
|---|---|---|
| Previous skill | 4.00 | 0.38 / 0.50 / 0.81 / 1.00 |
| Plain model's own questions | 4.13 | 0.62 / 0.50 / 1.00 / 1.06 |
| v3 | 4.19 | 0.38 / 0.50 / 0.81 / 0.88 |

- Fit was 4/4 for every arm in every set; 4 distinct ideas for v3 in every set.
- v3 matched or beat the previous skill everywhere, and was further from the default than
  a plain model's own questions in 3 of 4 sets: the first measurable edge over generic
  clarifying questions. No markers leaked into any v3 deliverable.

## Test 7: first real user, blind (v3, n = 1)

Anshul, one real task (a startup pitch: positioning, paragraph, cold email). Fresh
agents ran plain_asks and v3; he answered both question sets by clicking options and
picked between the two finished pieces blind. **He picked plain_asks**, for the email's
move. Both pieces had the same angle. v3 never asked about tone and handed the writing
to his voice skill, producing lowercase founder copy where he wanted it corporate. Both
question sets were too long to answer in prose. Full write-up in
`eval/test7-real-user/`. This led to the cut-down skill: 3–4 clickable questions
including tone, no quick mode, voice skill only on request.

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

1. (Done: the simplified build, see Test 6.) A second judge pass, or a judge from another
   model family, to confirm v3's edge over plain_asks.
2. More real users and tasks (Test 7 was one task, one pick).
3. 8+ outputs per arm, two judge passes, a judge from another model family.
4. Runs with web search on, to see unverified figures actually get checked.
