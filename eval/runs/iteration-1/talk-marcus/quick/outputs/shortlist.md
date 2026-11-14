# Original run (quick): 5-minute all-hands talk on AI coding assistants

## Fixed and open parts

- **Fixed:** 5 minutes of speaking (about 650 to 750 words at a normal pace of 130 to 150 words a minute); a company all-hands, so the room is the whole company, not just engineering; the deliverable is an outline plus an opening paragraph. No company facts or numbers were given, so the draft states none.
- **Open:** the claim, the angle, who the talk is really addressed to, the structure, and how literally to take "for everything".

Quick mode: no questions asked. Everything below works from the task alone.

## What everyone gets

**Main claim:** "AI coding assistants are a powerful tool, not a replacement. Use them for boilerplate, tests and docs, but keep humans in the loop for architecture, security and judgment. The answer to 'for everything' is 'it depends'."

Choices it makes:
1. **Thesis:** balanced middle ground ("tool, not a crutch").
2. **Opening:** an adoption statistic ("X% of developers now use...") or a "show of hands".
3. **Structure:** benefits, then risks, then guidelines, then a call to action.
4. **Examples:** boilerplate and tests (good), hallucinated APIs and security holes (bad).
5. **Assumed listener:** engineers, even though it's an all-hands.
6. **Leaves out:** what changes for the non-engineers in the room, and what the company should do differently apart from "be careful".

## Candidates

Banned: the default's main claim ("a tool, not a replacement; keep a human in the loop; it depends on the task").

1. **The bottleneck moves to the rest of the room.** For engineers the answer is mostly yes. The bigger change is that once code is cheap, the slow part is deciding what to build, and that falls on product, sales, legal and leadership. *(Starting point: a constraint they named, the all-hands audience.)*
2. **If it's merged, it's yours.** Authorship stops mattering and ownership is what counts. The talk sets a single accountability rule: you answer for every line you ship, whoever or whatever typed it. *(Starting point: the reader who would disagree, someone who has been on call for a bad AI-written change.)*
3. **Reading becomes the job.** AI moves engineering effort from writing to reviewing. Teams that don't invest in review get slower, not faster. *(Starting point: an inverted default choice, "AI saves time".)*
4. **Where do the next seniors come from?** Deliberately keep some work hand-written as an apprenticeship, because juniors who never struggle with code can't later judge AI output. *(Starting point: an inverted default choice, the timeframe. The default looks at this quarter; this looks five years out.)*
5. **Run an experiment, not a policy.** Don't answer the question from the stage. Announce a 4-week opt-in trial with two measured outcomes and report back at the next all-hands. *(Starting point: the 5-minute constraint. Five minutes is too short to settle it and long enough to launch something.)*
6. **Speed isn't the constraint.** Most cycle time is spent waiting on review, deploys and decisions, so "AI for everything" changes typing time and not delivery dates. *(Starting point: a fact that sits badly with the default's implied productivity win.)*
7. **Nobody asks this about other roles.** Nobody asks whether finance should use spreadsheets for everything. The question is about trust, not tools. *(Starting point: inverting who the question is asked of.)*
8. **Shadow use is the real problem.** People already use these tools quietly and don't say so. The ask is disclosure norms, not usage rules. *(Starting point: the reader who would disagree, the engineer who already uses it every day.)*
9. **Yes, for everything, taken literally.** Argue for the literal maximum, including design docs and postmortems, and keep only one thing human-only: deciding what to delete or not build. *(Starting point: the word "everything" in the task.)*
10. **The customer's view.** Customers don't care how code was written. They care about incidents and response time, so tell the talk through one support ticket. *(Starting point: a reader outside the room.)*
11. **The competence asymmetry.** "For everything" is safe for people who could have written it themselves and dangerous for people who couldn't. *(Starting point: the reader who would disagree, the skeptical senior.)*
12. **Steelman the skeptic.** Give the burned senior engineer's case its strongest version, then show exactly where it stops holding. *(Starting point: the reader who would disagree.)*
13. **(unlikely) Spend the five minutes on a live demo.** Hand an assistant a real ticket from the backlog on stage, let the room watch what it gets right and wrong, and finish with two observations. *(Starting point: the 5-minute constraint, show instead of argue.)*
14. **(unlikely) The spec is the new code.** If assistants write the code, the prompt is the product requirement. So the people who write requirements (PMs, support, sales) become part-time programmers whether they like it or not. *(Starting point: the all-hands audience combined with the word "everything".)*
15. **(unlikely) Argue the opposite of the room's mood.** Whichever way the company currently leans (hype or skepticism), argue against it for five minutes. *(Starting point: inverting the default's neutral, balanced tone.)*

## Cuts

- **11 (competence asymmetry):** near-duplicate of 4, which says the same thing about juniors with a longer horizon. It also slides back toward "human judgment still matters", which is the default reworded.
- **12 (steelman the skeptic):** this is a structure, not a claim. Filled in, it lands on balance, which is the default reworded.
- **10 (customer view):** near-duplicate of 2. Both are about accountability for shipped code.
- **7 (nobody asks other roles):** sidesteps the question. A room that was promised an answer gets a reframe, and it has nothing left for minutes 2 to 5.
- **15 (argue against the mood):** depends on knowing the company's current mood, a fixed fact we don't have.
- **6 (speed isn't the constraint):** needs real cycle-time numbers from this company to land, and we have none. The useful part (the bottleneck moves) lives on in 1.
- **3 (reading becomes the job):** strong, but it speaks only to engineers and sits close to 2. Kept as one beat inside the developed talk.
- **9 (literally everything):** close to 1 and 14 once developed. All three say the human work moves to deciding.
- No prior-work search: this is a talk, so its value doesn't depend on being new to the world.

## Shortlist (picked for spread)

### A. The bottleneck moves to the rest of the room (candidate 1)
For engineers the honest answer is "mostly yes". The more important point for an all-hands is what happens next: when building gets cheap, deciding, approving and saying no become the slow part, and that's everyone else's job.
- **Only yours because:** nothing you answered (quick mode). It depends on the one fixed fact you gave: this is an all-hands, not an engineering meeting.
- **Strongest objection:** non-engineers may hear "engineers are fine, now it's your problem" as a deflection, and engineers may feel the question was dodged.
- **Test:** whether most of the room really is non-engineers. If engineers are the majority, the angle weakens and B or D fits better.

### B. Where do the next seniors come from? (candidate 4)
Using AI for everything works today because today's seniors learned without it. Argue for keeping some work hand-written on purpose as training, so the company still has people who can tell when the AI is wrong.
- **Only yours because:** nothing; this is available to anyone.
- **Strongest objection:** juniors learn fine by reviewing AI output, the way people learned from Stack Overflow, and the "struggle" may be nostalgia.
- **Test:** a prediction you can check later. Juniors who mostly prompt will be measurably slower at debugging production incidents in two years than juniors who mostly wrote code.

### C. Disclosure, not rules (candidate 8)
The real risk isn't use but hidden use. Instead of a usage policy, ask for one norm: say when AI wrote a meaningful part of a change, so reviewers know where to look.
- **Only yours because:** nothing; this is available to anyone.
- **Strongest objection:** labeling invites stigma, people will under-report, and soon most code will qualify, so the label carries no information.
- **Test:** a rebuttal it has to survive. If nearly every PR gets the label within a month, the norm needs a threshold or it's noise.

### D. (unlikely) Live demo on a real ticket (candidate 13)
Spend three of the five minutes letting an assistant work a real backlog ticket live, then name the two things the room just saw: what it did that would have taken an hour, and what a person had to catch.
- **Only yours because:** nothing; it depends on your having a real ticket and a working setup.
- **Strongest objection:** live demos fail on stage, and a cherry-picked success is propaganda while a failure derails the five minutes.
- **Test:** a fact it depends on. Can you do a full rehearsal on the actual all-hands setup (screen share, network) before Friday?

## Recommendation and pick

**Developing A.** It is the only candidate that comes from a fixed fact in your task (the audience is the whole company), and it is the furthest from the default, which assumes a room of engineers. B and C are good talks, but at engineering meetings. D is a format, not a claim, and a format can carry A later if you want it. If your all-hands is mostly engineers, switch to B.
