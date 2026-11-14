# Shortlist (quick mode: no questions asked)

## Fixed and open parts

- Fixed: 5 minutes of speaking (roughly 650-750 words at a normal pace of 130-150 words a minute); a company all-hands, so the room is not only engineers; the topic is AI coding assistants used "for everything". No company-specific numbers were given, so none are invented.
- Open: the claim, the angle, who the talk is addressed to, the structure, the examples.

## What everyone gets

Main claim: AI coding assistants are powerful tools but no replacement for engineering judgment, so use them for some things, not everything.
Choices it makes:
1. Thesis: the balanced middle ("it depends").
2. Angle: productivity versus risk (speed vs. bugs, security, IP).
3. Examples: yes for boilerplate, tests and docs; no for architecture and security-critical code; a headline productivity stat.
4. Structure: hook stat, pros, cons, guidelines, call to action.
5. Assumed listener: engineers, even though it is an all-hands.
6. Leaves out: what the rest of the company should do differently, and the word "everything" itself.

## Candidates

Starting points used (quick mode has no user answers, so: inverted default choices, constraints the user named, the listener who would disagree, a fixed fact that sits badly with the default).

1. Inverted thesis: say yes, for everything, with one rule: you merge only what you can explain.
2. Constraint (all-hands): if code gets cheap, the bottleneck moves to deciding what to build, which is everyone's job, so the talk is addressed to the whole room.
3. Constraint (5 minutes can't settle a policy): don't decide on stage; propose a two-week experiment with a shared log, report at the next all-hands.
4. Listener who disagrees (a junior engineer): protect the work that builds skill; AI for everything means nobody learns the hard parts.
5. Inverted angle: the issue is not writing, it's reading: who is accountable for understanding what ships.
6. Fixed fact (all-hands, "should"): argue against any mandate either way; tool choice belongs to whoever is paged when it breaks.
7. Inverted examples: the metric trap; PR counts and lines go up, so watch incidents and review time instead.
8. Listener who disagrees (skeptical senior engineer): the skeptic's objection is really about taste, and taste is what to apply to AI output.
9. Constraint: put a price on "everything"; compare tool spend to engineer time.
10. Inverted structure: ownership at 3am; use it for anything you would be willing to debug when paged.
11. Constraint (all-hands): "engineers using AI" is the same question everyone in the room faces in their own job.
12. Inverted angle: vague asks get more expensive; an assistant builds exactly what an unclear ticket says, quickly, so ambiguity gets caught later.
13. (unlikely) Use AI to delete code: cheap writing grows the codebase faster than anyone can understand it, so point the tool at removal.
14. (unlikely) Use it for everything except the thing you're best at, to keep your sharpest skill in practice.
15. (unlikely) Same tool, same blind spots: if every engineer uses the same assistant, the codebase converges on the same patterns and the same mistakes.

Banned: the default's main claim ("useful tool, not a replacement for judgment; some things, not everything").

## Cuts

- 10: near-duplicate of 1 (same "you must understand it" rule).
- 11: near-duplicate of 2, and weaker (generic, not about this question).
- 12: folded into 2 as its main evidence rather than a separate talk.
- 4: the default already gestures at juniors as a caveat; close to the default reworded.
- 8: "apply judgment/taste" is the default's main claim reworded.
- 5: close to the default's "review everything" guideline.
- 9: depends on company numbers that weren't given and can't be verified.
- 7: a good point but too narrow for a whole talk; usable inside another one.
- 6: sits close to 1 (accountability) and loses on spread.

No web search: a talk angle's value doesn't depend on being new to the world.

## Shortlist (chosen for spread)

**A. The bottleneck moved (from 2 + 12).** Mostly yes to AI for the typing, but cheap code moves the hard part to deciding what to build, and that's the whole room's job. Vague asks now cost more because the build finishes before anyone asks "what did you mean?"
- Only yours because: nothing from answers (quick mode); it depends on the fixed fact that this is an all-hands, not an engineering meeting.
- Strongest objection: non-engineers may hear it as engineers blaming everyone else for their tools.
- Test: does the room really have a lot of non-engineers? If it's mostly engineers, the second half loses its listener.

**B. Yes, everything, with one rule (from 1).** Say yes outright, which the default never does, with one line: you merge only what you can explain, because someone gets paged.
- Only yours because: nothing; this is available to anyone.
- Strongest objection: "explain" is easy to claim and hard to check; in practice it collapses into "review carefully".
- Test: has the team had an incident in code nobody on call could explain? If yes, it lands; if no, it's hypothetical.

**C. Don't decide on stage (from 3).** Five minutes can't settle a policy, so propose a two-week experiment: everyone logs where the assistant saved or cost time, and the results come back at the next all-hands.
- Only yours because: depends on the 5-minute constraint.
- Strongest objection: sounds like dodging the question you were given.
- Test: will anyone actually fill in the log? Predict participation and check it.

**D. Point it at deletion (13, unlikely).** The risk of "everything" isn't bad code, it's more code; use the assistant to remove, simplify and consolidate, not just to add.
- Only yours because: nothing; this is available to anyone.
- Strongest objection: niche for non-engineers in an all-hands.
- Test: does the codebase's size or the number of services grow noticeably once assistant use goes up?

**E. Everything except your best skill (14, unlikely).** Hand over the rest, and keep doing your strongest skill by hand so it doesn't fade.
- Only yours because: nothing; this is available to anyone.
- Strongest objection: there's no evidence that skills fade at the rate this implies.
- Test: ask engineers whether they've felt a skill slip since adopting assistants.

## Developing

**A. The bottleneck moved.** It's the only candidate built on the fact that this is an all-hands: it gives everyone in the room something to do, not just the engineers, and it still answers the question asked ("mostly, yes"). B and D are engineer-only; C answers no question at all.
