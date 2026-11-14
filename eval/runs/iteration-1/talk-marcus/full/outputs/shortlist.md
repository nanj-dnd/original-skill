Your answers mostly move away from the default. You reframed the question (1c), named a real incident and a number (3a), and asked for one concrete rule rather than guidelines (5b). The only default choice you kept is the audience: engineers and their managers, with everyone else getting the gist.

Banned: the default's main claim, "AI assistants are powerful tools, not a replacement; use them for some things, not everything, and keep a human in the loop."

**Candidates**

1. **Writing is cheap now; debugging is the job.** The skill that matters has moved from writing code to reading it, and we're training juniors on the wrong one.
2. **The 2am outage as the spine.** The whole talk is one night: four confident fixes from the assistant, against 10 minutes of reading the log.
3. **The number as the spine.** P2 time-to-resolve went from 38 to 61 minutes. "We got 23 minutes slower at the thing customers feel most."
4. **The autopilot rule.** Juniors log manual debugging hours the way pilots log hand-flying hours, and the talk explains why.
5. **"I use it every day, and that's why I'm worried."** A pro-AI speaker argues for one narrow exception, and the credibility comes from inside.
6. **Assistants generate; debugging diagnoses.** An assistant produces plausible variations, and that's its job. A bug has one cause, so four different confident fixes is the tool working as designed, pointed at the wrong kind of problem.
7. **The incident review as evidence.** What you see in reviews: people who can't explain code they shipped. If you can't trace it at 2am, you don't own it.
8. **Two ledgers.** AI's gains are counted in daytime metrics (PRs, velocity). Its costs get paid on the on-call rotation at night, in a ledger nobody added up until now: 38 to 61 minutes.
9. **This is a training question, not a tool policy.** Aimed at managers: the struggle that used to teach juniors to debug is gone, so something has to replace it on purpose.
10. *(unlikely)* **Run it as an experiment.** Make the six-month rule a bet with a measurement. Track that cohort's time-to-resolve, and drop the rule if it makes no difference.
11. *(unlikely)* **Make the room do it.** Put the actual log line on screen and ask who can spot the cause.
12. *(unlikely)* **It isn't only juniors.** The 61-minute median covers everyone on call, not just juniors. The rule protects the pipeline, but seniors are losing this too.
13. **Confidence isn't a diagnosis.** A short lesson for the whole room on telling a guess from a cause, which sales and support also run into.
14. *(unlikely)* **The rule protects our AI bet.** The more code we write with assistants, the more code nobody wrote by hand, and the more we need people who can debug it. The rule is what makes going all-in on AI for writing safe.

**Cuts**

- **3 (number as spine):** Folded into 8, which uses the same number and explains why nobody saw it coming.
- **4 (autopilot rule):** This is your ask. It closes every version below, so it isn't a separate angle.
- **5 ("I use it every day"):** This is your stance and belongs in any version, since you asked not to sound anti-AI. As an angle on its own, it's mostly a framing device.
- **7 (incident review):** Close to 2. Your seat as the person who runs reviews becomes the narrator of 2.
- **11 (room does it):** Most of the room isn't engineers, so a raw log line won't land, and it spends a fifth of your five minutes.
- **13 (confidence isn't a diagnosis):** Near-duplicate of 6, and weaker.
- **1 (writing is cheap, debugging is the job):** Close to 14. I kept 14 because it's further from the default.
- **9 (training question):** Kept as the frame for the managers in whichever version you pick, but it sits close to the shared ending.
- **10 and 12:** Folded into the objections and tests below rather than standing alone.

**Shortlist**

**A. The 2am outage, told straight.**
The talk is one night. An outage, an on-call engineer who pastes the error into the assistant four times and gets four confident, different fixes, and you reading the log and finding the cause in 10 minutes. Then: this is what our incident reviews keep showing, here's the number, here's the rule.
- **Only yours because:** your 3a story, your seat running incident reviews (4), and the 38 to 61 minute number.
- **Strongest objection:** One story can sound like an anecdote picked to blame one person, and the on-call engineer may be in the room.
- **Test:** It has to survive "that's one night." The 38 to 61 median is what makes it more than a story, so check that the median is over enough P2s to mean something.

**B. Two ledgers.**
The gains from assistants show up in daytime numbers everyone already tracks. The costs show up at night on the on-call rotation, in a number nobody connected to it: P2 time-to-resolve went from 38 to 61 minutes in six months. The talk adds up the second ledger.
- **Only yours because:** your number, plus your point that the worry is skills rather than code quality (1c).
- **Strongest objection:** Correlation isn't cause. Time-to-resolve can rise because of system growth, team churn, new services or harder incidents.
- **Test:** Does the 61 minutes hold after you set aside incidents in new or unfamiliar systems? If you can say "same kinds of incidents, slower," the claim holds.

**C. Assistants generate; debugging diagnoses. (Recommended)**
The assistant is built to produce plausible answers, and for writing new code that's exactly what you want: many good-enough options. Debugging is the opposite kind of problem: one true cause. Four different confident fixes at 2am isn't the tool failing. It's the tool doing its job on the wrong kind of question. That's why your line falls between writing and debugging rather than at "everything vs. some things," and why you can be pro-AI and still ask for the rule.
- **Only yours because:** your write-yes/debug-no split (1 and 5), the four-fixes incident (3a) and the autopilot rule.
- **Strongest objection:** Assistants do help with debugging when you give them the full context, so the line may be "how you use it" rather than "whether."
- **Test:** It has to survive "better prompting fixes this." Your answer has to be that the rule is about building the skill, not about the tool's ceiling. Pilots train hand-flying even with excellent autopilots.

**D. The rule protects our AI bet.** *(unlikely)*
Make the most pro-AI case in the room: we should write more and more code with assistants. The consequence is a growing body of code no human typed, which means debugging becomes a larger and scarcer skill. Six months of manual debugging for juniors isn't a brake on AI. It's what makes going further with AI safe.
- **Only yours because:** "don't make me sound anti-AI" plus your rule (5b). It reuses your autopilot logic: more automation means more manual training, not less.
- **Strongest objection:** It may sound like a trick, using a pro-AI argument to land a restriction, and the AI skeptics in the room get nothing.
- **Test:** Prediction: as AI-written code rises, P2 time-to-resolve keeps rising without the rule and flattens with it. Measure it on the first cohort.

**My pick: C.** It's the only one that explains why your line goes between writing and debugging. That's what keeps you from sounding anti-AI, and it makes the rule feel like a consequence rather than a preference. The 2am story becomes its evidence, and the 38 to 61 number its stakes. B's correlation problem is also smaller here, because the number supports the argument instead of carrying it alone.

Which one should I develop? Reply with a letter (A, B, C or D), or a combination like "C, opened with A's story."
