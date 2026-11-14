**Path: specific answers, so I'm building directly (step 4).** Your answers have things I couldn't have guessed: a real case with numbers (140 tests, 1 day, then 6 more days), a named audience (7 of 12 are non-engineers, including your cofounder), your stake (CTO, you set the policy) and a position you argued for (the question's settled; the job changed).

## Angle

"Should engineers use AI for everything?" is already settled here, and the more useful thing to explain is how it changed the job: the code is now the cheap part, and the engineering is deciding exactly what "correct" means. The calendar sync story shows both sides, because the code really did take a day, and the week went on a spec that was wrong. So "it took a day" and "it ships next week" are both true, and the talk shows the room why.

## Built from

- **1:** the question is settled and the job changed (spec and tests are the engineering). That's the thesis, so there's no pros and cons.
- **2:** the non-engineers, 7 of 12. Every example is pitched at sales, support and your cofounder, and the payoff is a line they can use: why "done in a day" still means a week.
- **3:** CTO and cofounder. You can describe how the team works now as a fact, not a proposal, and you're the right person to admit the spec miss.
- **4:** calendar sync. It's the spine of the talk, told in order: 140 tests, one day, then six days on recurring events across time zones.
- **5:** already how you work. No adoption stat and no "should we", so the time goes to explaining.
- **Tone:** fun and short. One story, one idea, a callback ending, under 5 minutes.

**The tension I'm keeping:** 140 tests written first and the feature still slipped six days. Told carelessly, that sounds like "the tests didn't work", which is the opposite of your point. The talk takes it head on: the tests did their job and proved the code matched the spec, but the spec was wrong. That's why spec and tests are the hard part now. Writing 140 tests isn't enough if the 141st, the one nobody thought of, is the one that matters. I won't smooth that over, because it's the most honest and most memorable moment in the talk.

## Strongest objection

Someone non-technical (maybe your cofounder) hears "the code is cheap now" and asks, out loud or later: "Then why does it still take a week? And if the AI writes the code, what are we paying engineers for?" The first half is what the talk answers. The second half is the jobs question, and if the talk sidesteps it, people will fill it in themselves.

**Test before you use it:** (a) Check the numbers with whoever built calendar sync: was it really 140 tests, one day of code, and six days that were *all* spec and time-zone fallout, or did review and other work take some of that time? The whole talk rests on that split. (b) Have a one-sentence answer ready to "so do we need fewer engineers?". Even if it stays out of the script, you'll get it in Q&A or the hallway.

## Other directions

- **Turn it into an invitation:** the recurring-events-across-time-zones edge case is exactly what support and sales hear from customers every week. Close with "the spec is now everyone's job: bring us the weird cases."
- **Make it a game:** show the room the calendar sync spec in one slide, ask "what's missing?", then reveal the time-zone bug. That's more fun, but it needs a slide and takes about a minute of your five.

---

Want me to go ahead with this? Or redirect it, or tell me anything to work in: a line you want to say, how you want it to end (callback, invitation, a joke), whether you'll have slides, or a name to credit for calendar sync.
