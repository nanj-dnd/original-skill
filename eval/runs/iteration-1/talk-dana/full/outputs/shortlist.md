Your answers moved away from the default on every question but one, so there's a lot to work with. The default's central question ("should engineers use it for everything?") is settled for you, so it isn't the talk. The real tension is in your own story: the code took **one day**, and getting it right took **six more**. Your 7 non-engineers only ever see the first number.

Banned: the default's main claim, "not for everything; it's a tool, not a replacement for judgement."

## Candidates

1. **The seven-day mystery.** Tell calendar sync as a whodunit: a feature was "done" in a day, so where did the other six go? Reveal: the spec.
2. **Engineers are now professional question-askers.** The job used to be typing code. Now it's arguing about what "repeats every Tuesday" means when the customer moves to another time zone.
3. **The 141st test.** Build the talk around the one test nobody wrote. 140 tests passed; the missing one cost six days.
4. **You're in engineering now.** The bug was a customer question nobody asked, and support and sales know those questions best. The call to action is to bring engineers the weird cases.
5. **Tests are the product, code is disposable.** The 140 tests describe what we sell. We could throw the code away and regenerate it.
6. **How to read "it took a day."** A short translation guide for non-engineers: "built in a day" means the first draft, "done" means the spec held up, and "still arguing" means the work is happening.
7. **Spec arguments are the factory running.** When sales hears engineers bickering about edge cases, that isn't dysfunction. It's the production line.
8. **Ask "how sure are we?" not "how long?"** Change the question the business asks engineering, because build time is now near zero and the uncertainty sits in the spec.
9. **The CTO's confession.** "I set this process, and the spec was wrong." The talk is the cofounder owning the miss, then showing what changed.
10. **The cost of a mistake moved upstream.** A wrong line of code is cheap now and a wrong sentence in the spec is expensive. Put a price on each.
11. **Live vote: what time is the meeting?** *(unlikely)* Open with one recurring meeting (say, weekly 9am set up from one city and attended from another) and have the 12 of you vote on what should happen when someone travels or the clocks change. The room won't agree, and that disagreement is the six days.
12. **The agent was right; we were wrong.** *(unlikely)* The AI did exactly what the 140 tests asked, perfectly. It works like a mirror, and what it showed us was how vague we were.
13. **A Friday "weird customer case" ritual.** *(unlikely)* End the talk by starting a standing habit: each week, someone outside engineering brings one strange real-world case, and it becomes a test.

## Cuts

- **5 (tests are the product):** this is your thesis stated plainly. Every survivor already carries it, so as a standalone angle it's available to anyone.
- **10 (cost moved upstream):** too close to 5 and 3. It's the same point in pricing language.
- **2 (professional question-askers):** too close to 7. Kept 7's version because it's aimed at what non-engineers actually see.
- **8 (how sure, not how long):** merged into 6, the translation guide, since both reframe how non-engineers read engineering time.
- **13 (Friday ritual):** merged into 4. It's the same recruitment idea, so it works as 4's closing move rather than a separate talk.
- **9 (CTO's confession):** kept as an ingredient any version can use, but it's thin as a whole 5-minute talk.
- **12 (agent was right):** a strong line, and it fits inside 3 or 11. On its own it still leaves engineers at the centre.
- **1 (seven-day mystery):** close to 3. Kept 3 because "the missing test" gives the mystery a concrete answer.
- **7 (spec arguments):** close to 6. Kept 6 because it gives the non-engineers something they can use on Monday.

## Shortlist

**A. Live vote: what time is the meeting?** *(was unlikely)*
Open by putting one recurring-meeting scenario on screen and having the room vote. The votes split, and you say: "That disagreement cost us six days last month." Then you tell the calendar sync story briefly. The point for the room is that writing code is now the cheap part and deciding what's right is the job, and that the people in this room are the ones who know what's right.
- **Only yours because:** the calendar sync story (4), a room that's 7/12 non-engineers (2), and "keep it fun." A 12-person room is small enough to vote by hand.
- **Strongest objection:** live votes can fizzle, and if everyone agrees, the opening falls flat.
- **Test:** before Friday, ask 3 colleagues the question cold. If they don't split, pick a different case.

**B. The 141st test.**
Story first, and nearly the whole talk. 140 tests, written first, all passed, and the agent wrote the code in a day. Then: "The most important test is the one we didn't write." The six days went to finding test #141. Close with the idea that engineering now means hunting for the missing test.
- **Only yours because:** the 140 tests, one day plus six days, and the recurring/time-zone gap (4), from a CTO who set the process (3).
- **Strongest objection:** non-engineers may not care what a "test" is, so the story could land as an engineering inside joke.
- **Test:** can you explain "a test" to sales in one sentence ("a written promise about what the product does, which the computer checks")? If not, this angle struggles.

**C. You're in engineering now.**
Aimed squarely at the 7. The bug that cost six days was a customer question: what happens to a recurring meeting across time zones? Support hears questions like that every week. So the bottleneck isn't engineers typing; it's engineers knowing the weird cases. End with a concrete ask: bring one weird customer case a week, and it becomes a test.
- **Only yours because:** the 7/12 split including support and sales (2), your authority to set process as CTO (3), and AI already being how you work (5), which is why the bottleneck has moved.
- **Strongest objection:** asking sales and support to take on spec work can feel like extra homework handed out at an all-hands.
- **Test:** did anyone in support or sales know about the recurring/time-zone problem before engineering hit it? If yes, this is the strongest version. If not, the claim is weaker.

**D. How to read "it took a day."**
A fast, funny translation guide for non-engineers. Three or four phrases engineers say ("it's built," "it's done," "we're arguing about the spec," "tests are green"), with what each one actually means now that the code is the cheap part. Calendar sync is the worked example: "built" on day 1, "done" on day 7.
- **Only yours because:** the "it took a day still means a week" gap you named (2), and the calendar sync dates (4).
- **Strongest objection:** a glossary format can feel like a lecture with jokes, and it risks sounding like engineers explaining themselves defensively.
- **Test:** ask your cofounder which engineering phrase confuses them most. If it isn't on the list, the guide is aimed wrong.

## My recommendation

**A, with C's ask as the ending.** It's the most fun. The 7 non-engineers feel the problem before they hear the explanation. And it turns your one story into something the room takes part in, not just listens to. B is the safest if you'd rather just tell the story well.

**Which one should I develop?** Reply with a letter, or a letter plus a tweak (e.g. `A, but skip the vote and just ask one person`).
