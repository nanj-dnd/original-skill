# Why each rule is there

The evidence behind each step of `SKILL.md`. Sources and full figures are in
`research.md` (the literature) and `pilot.md` (seven tests of this skill). Many sources
are preprints or used older models, and the skill's own tests are small: read the
numbers as direction.

## What the evidence says overall

- Same-model answers to the same open prompt are near-duplicates at the level of ideas
  (79% of response sets above 0.8 similarity). In every test of this skill, a plain
  model gave different users the same 1 or 2 ideas.
- **Asking before writing fixes that.** Every arm that had the user's answers spread to
  4 distinct ideas with perfect fit.
- **The skill's extra machinery adds little over asking, inside one model.** A plain
  model told to ask its own clarifying questions matched the skill on clear and vague
  users (Tests 3 to 4), and in the one real blind test (Test 7) the user picked the plain
  version. So the skill is kept short.
- **Against other assistants it leads, mostly on originality and craft.** In Tests 8 to
  10 `/original` won 71 of 80 judged matchups against Gemini, ChatGPT and plain Claude,
  and every "less generic" matchup. Its closest rival, ChatGPT asking first, matched it
  on fit and came within 0.13 on "use as is", while trailing on originality (+1.4 for the
  skill), specificity (+1.2) and writing (+0.9). Part of the lead is the Claude model
  itself (Test 8), and the Gemini judge rated ChatGPT asking first slightly higher on
  "use as is".

## 1. Default

- Showing the model what already exists and asking it to differ is the one prompting
  method with a large measured effect on idea diversity. v3's only measured edge over
  generic questions was distance from the default (Test 6), most likely from this step.
- Divergence on a question with one right answer is just error, so closed tasks get a
  plain answer.

## 2. Ask

- **Few questions, one round.** Cutting an interview by 80% barely changed what a model
  knew about the person; long questionnaires get shorter, flatter answers. In Test 7 the
  user found both question sets too long to answer in prose and answered by clicking.
- **Rank possible questions by how much they would change the piece.** Choosing each
  question by expected information took one test from 45% to 93%. Left alone, models ask
  things they could guess.
- **Real material, including a number.** A real case was the strongest single ingredient
  in every fitted output; in Test 4 a user's best material was a figure no "real case"
  option had room for.
- **Tone.** In Test 7 the skill never asked about tone, wrote in the user's casual
  founder voice, and the user wanted formal copy for that reader. The plain model asked.

## 3. Angle

- Building from the answers directly matched the full shortlist process for 8 of 8
  personas, with one fewer turn and a third of the tokens.
- Users engaged with the objection and test lines and corrected their own claims because
  of them. The research also recommends giving every idea a test.
- Agreeing users still got distinct, well-fitted outputs from their specifics, so the
  skill builds from those rather than inventing a contrarian stance.

- **Match a mild view** (added 2026-11-15): in Tests 9 and 10 the Gemini judge twice
  preferred ChatGPT's middle-ground piece for Jo, a vague user who agrees with the
  default, because the skill's piece took a firmer stance than Jo holds. Originality
  should come from specifics and structure, not from a stronger opinion. Untested.

## 4. Write

- **Check cited figures.** Runs with search off cited studies from memory.
- **Clean piece, note after.** Placeholders and "[unchecked]" marks inside the text cost
  quality points (Test 5); moved to a note after, they leaked into 0 of 16 pieces
  (Test 6).
- **No invented details, including small colour** (tightened 2026-11-15): runs added small personal
  details the user hadn't given. In Test 10 the GPT judge counted 3.25 invented details per skill
  piece against 0.38 for ChatGPT asking first; one first-person blog post made up past
  resolutions about running and a reading list. The push for specifics fills gaps with plausible
  details, so the rule now names that colour and the reread checks each personal detail against
  the answers. Test 11: invented details in talks fell from 7.25 to 2.75 per piece, but in
  first-person blog posts they rose from 5.5 to 9.25, so the rule is not yet enough there.
- **Voice skill only on request.** See Tone above.
- **One critic pass.** The research found a critic weak at killing ideas but useful for
  depth of revision; one pass, since gains stop after two or three rounds.

## Removed, and why

- **Quick mode and the candidate shortlist**: quick mode moved off the default but not
  toward the user (fit at chance); the shortlist didn't change the main idea for clear or
  vague users.
- **Routing and "the default done well?" check**: vague users offered the default took
  it, pulling outputs back toward it (Test 4).
- **The pause before writing a talk**: it did not recover quality (Test 5).
- **A stored profile and notebook**: removed by the user's choice.

## Limits

- No study shows personal context makes ideas more original rather than better fitted.
- Tests 1–6 used model-written personas and model judges from the same family; Test 7
  was one real task and one pick, with tone as a confound.
