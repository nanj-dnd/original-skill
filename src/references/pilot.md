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

## Tests 8 to 10: against other models (short skill)

Run on the short skill with the talk task and a New Year's resolutions blog post, 4
simulated users per task (2 clear, 2 vague). Other models ran as people use them: Gemini
Pro in its web app and ChatGPT on the free plan, both in temporary chats. Pieces were
cut down to the deliverable, shuffled under random IDs and judged blind by a Claude judge
and a Gemini judge. Data in `eval/test8-cross-model/`, `test9-head-to-head/`,
`test10-six-way/`.

- **Test 8, skill on each model** (talk task): on both Claude Fable and Gemini, the skill
  moved pieces further from the default than plain asking (3 of 4 judge-model pairs, 1
  tie) and was the only arm to draw out a vague user's hidden numbers. Quality rose on
  Claude (5.0) but not on Gemini (3.5 against 3.75 to 4.0 for asking first).
- **Test 9, head to head**: `/original` (Claude + skill) against Gemini plain, Gemini
  asking first and Claude plain, each matchup judged twice with order swapped: 45 of 48
  wins, 3 splits, no losses; "less generic" 48 of 48.
- **Test 10, six-way scorecard** (adds ChatGPT plain and asking first): head to head
  `/original` won 71 of 80, split 7, lost 2; "less generic" 80 of 80. On 1 to 5 scores
  (mean of both judges) `/original` led on use as is (3.94), originality (4.75),
  specificity (4.62), tone (4.19) and writing (5.0). ChatGPT asking first led on fit
  (4.25 against 4.12), came within 0.13 on use as is, invented nothing, and asked about
  9 questions to the skill's 4. The Gemini judge put ChatGPT asking first slightly ahead
  on use as is (3.88 against 3.5).
- **Why the Gemini judge withheld wins** (9 matchups): 6 times it penalised the skill for
  using a detail the user revealed when asked, reading the persona card's role-play note
  ("mention only if asked") as a rule for the writer, an artifact of the setup. Twice it
  preferred ChatGPT's middle-ground piece for Jo, a vague user who agrees with the
  default, over the skill's firmer stance. Once it preferred ChatGPT's tone (Marcus).
- **GPT as a third judge** (gpt-6.1-sol via Codex for 36 pieces, ChatGPT's free web app
  for the rest): head to head `/original` won 98 of 120 judged matchups and lost 8; 36 of
  48 against the two ask-first rivals (15 of 24 against ChatGPT). On three-judge means
  ChatGPT asking first edged it on use as is (3.79 against 3.59) and fit (4.25 against
  3.84); the skill led on originality, specificity and writing. GPT's main objection was
  the same as Gemini's (Jo: too firm a stance for a moderate speaker), and it counted
  3.25 invented details per skill piece against 0.38 for ChatGPT asking first: small
  made-up personal details in first-person pieces.
- **Test 11, re-testing the two fixes** (`eval/test11-fix-retest/`): fresh pieces from the
  fixed skill, scored in the same batches as the old pieces and ChatGPT asking first by all
  three judges. The mild-stance fix worked: Jo's use-as-is rose from 3.0 to 4.33, fit from
  4.12 to 4.50 and tone from 4.17 to 4.50 across users; head to head against ChatGPT asking
  first it went 19-4-1, against 15-6-3 before. A line-by-line audit (ChatGPT, with each user's
  answers included) found the invention fix worked for talks (7.25 to 2.75 invented
  details per piece) but not for first-person blog posts (5.5 to 9.25): the skill still
  writes memories and colour the user never gave. ChatGPT asking first: 2.25 on blog posts. Same pieces score differently across batches, so only
  within-batch comparisons count.
- The skill was the only contestant to use every user's own material when there was some
  (6 of 6, against 4 of 6 for both ask-first rivals) and used the fewest stock phrases.

## What runs did badly

- Cited studies from memory (web search was off) and flagged them as unchecked, but a
  real run should verify them.
- Added small invented details ("forgive myself by teatime") and did not always flag
  them.

## Limits

- 4 outputs per arm per task, one judge pass. Tests 1 to 7 used the same model family
  for runs, personas and judges; Tests 8 to 10 added Gemini and ChatGPT as contestants and
  a Gemini judge, but the simulated users were still played by Claude.
- Vivid personas with a story ready, which is when context dominates. Vague users were
  tested for routing only, not output quality.
- The personas answered fully whatever they were asked, so question design had little
  to win; Test 3 should be repeated with vague personas before concluding it never
  matters.

## Open tests, most useful first

1. More real users and tasks (Test 7 was one task, one pick).
2. A judge setup that shows the person's situation without the role-play notes, so a
   judge cannot read "mention only if asked" as a rule for the writer.
3. Vague users who agree with the default: whether the new measured-stance rule closes
   the gap the Gemini judge found.
4. 8+ outputs per arm, simulated users played by a non-Claude model.
5. Runs with web search on, to see unverified figures actually get checked.
