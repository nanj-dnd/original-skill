# Why each rule is there

The evidence behind the rules in `SKILL.md`, by step. Sources and full figures are in
`research.md` (the literature) and `pilot.md` (an evaluation of this skill). Several sources
are preprints or used older models; treat the numbers as direction, not precision.

## Default first

- Making the model look at what already exists and differ from it is the one mechanism
  with a large measured effect. Same-model answers to the same open prompt are
  near-duplicates at the level of ideas: 79% of response sets above 0.8 similarity, and
  different vendors' models 71 to 82% similar to each other.
- In the pilot, a plain model gave all four users the same answer.

## Split fixed and open parts

- Divergence on a question with one right answer is just error. Only the open parts
  get varied.

## Ask, once

- **The questions do most of the work.** In the pilot, a plain model given the users'
  answers to this skill's questions reached the same main idea as the full process for
  8 of 8 personas.
- **Few, well-chosen questions beat many.** Cutting an interview by 80% barely changed
  how well a model predicted the person (0.83 to 0.79), and a bullet summary kept 0.81.
  Survey completion fell from 68% to 47% when the announced length tripled, and later
  answers got shorter and flatter.
- **Choice of question matters more than count.** Picking each question by expected
  information roughly doubled success in one test (45% to 93%). Left alone, a model
  interviewer repeats questions and asks things it could guess, hence "don't ask what is
  already settled" and "tie every question to a default choice".
- **Rank possible questions by how much their answers would change the piece**
  (added 2026-11-14): picking each question by expected information is what took one
  test from 45% to 93%. One round of 3 to 5 can't adapt as answers come in, so the
  ranking happens before asking. Not tested in this skill's evaluation.
- **Being asked beats writing your own brief.** People rated their own prompt's coverage
  5.3 out of 7 before seeing test cases and 3.9 after.
- **At least one specifics question.** A real case was the single strongest ingredient
  in the pilot. Users whose positions matched the default still got distinct,
  well-fitted outputs when they supplied a case, a number or a constraint.
- **One round.** Long questionnaires get flatter answers, and Anshul asked for all
  questions up front.

## Route on the answers

- **What counts as specific**: in the user's own words and not guessable. A picked
  option is a direction only. The first v2 rule counted "a stated position" as specific,
  and a vague user's picked option sent him down the direct path; the tightened rule
  sent him to the shortlist.
- With specific answers, the shortlist added a user turn and about 3× the tokens
  without changing the main claim (pilot, 8 of 8).
- With no answers (quick mode), outputs moved off the default but not toward the user:
  different, not theirs. That is why quick mode and thin answers get the shortlist,
  which is where variety has to come from when there is nothing personal to build on.

## Build directly

- The objection and the test stay on the direct path because pilot users engaged with
  them and corrected their own claims. The research also recommends giving every idea a
  test: a fact it depends on, a rebuttal to survive, or a checkable prediction.
- **Confirming the angle on long pieces and talks** (added 2026-11-14, Anshul's
  choice): the direct path writes on its own reading of the answers, and a misreading
  costs a whole essay or talk. The evaluation also found that about half of v2's talk
  quality dip came from losing v1's pick step, where users added a line, an example or
  a closing. The check-in asks for those additions. Short pieces get one line inviting
  additions instead of a wait. Neither is tested yet.

## Generate, cut, shortlist

- **List, then revise to differ** brought idea similarity from 0.377 (base prompt) to
  0.255, close to a pool of human ideas (0.243).
- **Several starting points**: different prompt strategies produce pools that barely
  overlap, so mixing them adds coverage.
- **Unlikely candidates**: asking for several answers with how likely each is raised
  diversity 1.6 to 2.1 times. "Unlikely" means unlikely coming from you, not new to the
  world.
- **One ban only**: one ban nearly tripled divergence (4.5 to 11.9); by the third ban
  correctness had collapsed.
- **Two or three passes**: gains stop after two or three rounds in every system studied.
- **No personas, "be bold", tipping or threats**: all within about 0.03 of the base
  prompt. **No example ideas**: 0.403 to 0.432, worse than base. **No far analogies by
  default**: in 2,341 design concepts, more distant inspiration lowered the odds of
  being shortlisted by experts. **No rerolls**: temperature gives weak novelty at a cost
  in coherence and does not remove convergence.
- **Never score novelty**: LLM judges agreed with experts on non-obviousness 22 to 40%
  of the time and preferred machine-written ideas.
- **Pick survivors for spread**: choosing the most different ideas from a large pool
  afterwards (0.144) beat every prompting method.
- **Search for prior work** when the idea's value is being new: comparing ideas with
  existing work and regenerating raised rated novelty for about 56% of ideas per round,
  and of roughly 33 AI solutions to Erdős problems, about 15 turned out to be already in
  the literature.

## Develop

- **Check cited statistics**: runs with search off cited studies from memory (flagged as
  unchecked, correctly). With search on, check them; without it, mark them.
- **Placeholders over invention**: a vague user's run left marked placeholders where it
  had no real detail, rather than inventing a day in their life.
- **No invented anecdotes**: the output goes out under the user's name, and a made-up
  personal detail is the easiest way for it to read false or mislead. Runs in the
  evaluation added small details ("forgive myself by teatime") and did not always flag
  them.
- **One critic pass on the draft** (added 2026-11-14): the research found a critic
  weak at killing ideas but useful for depth of revision, so the pass revises thin or
  generic parts and leaves the angle alone. It never judges novelty, where model judges
  are weakest. One pass, because gains stop after two or three rounds and the angle is
  already settled. Not tested in this skill's evaluation.
- **Distance from the default**, including what did not move, keeps the skill honest
  about whether it did anything. The product search found no tool that shows this
  distance, though that search was not finished.

## Limits

- No study measures whether personal context makes a model's ideas more original, as
  opposed to better fitted to the person. Richer context can even pull answers toward
  the average.
- The evaluation used 4 outputs per arm, one judge pass and model-written personas
  with unusually clear views. Open tests are listed at the end of `pilot.md`; the most
  useful is whether generic clarifying questions do as well as these targeted ones.
