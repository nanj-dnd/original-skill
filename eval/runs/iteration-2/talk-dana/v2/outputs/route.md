**Path: step 4, build directly.** Your answers are specific: a stated position of your own (1), a named audience with a number, 7 of 12 non-engineers (2), your role (3), a real case with numbers, calendar sync with 140 tests, 1 day, then 6 more (4), and where the company is now (5). That's enough to build on, so there's no shortlist.

**Angle:** "Should engineers use AI for everything?" is already settled here: they do. What it changed is the job. Code is now the cheap part, and the real engineering is deciding what "right" means. The proof is that 140 green tests still shipped the wrong thing, because nobody had decided what a recurring event across time zones should do. That's why "it took a day" still means a week.

**Built from:** 1 (job changed: spec and tests are the work), 2 (non-engineers, and the day-vs-week gap), 3 (CTO and cofounder, so no "here are some guidelines" section), 4 (calendar sync), 5a (AI-first is already settled, so the talk skips the debate), plus your note to keep it fun and short.

**A tension I used instead of smoothing over:** answer 1 says writing the tests *is* the engineering now. But in your story the 140 tests all passed and the feature was still wrong. So the talk sharpens your claim a little. The tests aren't the job. Deciding what the tests should say is the job, and tests only check the questions you thought to ask. I think that's the most interesting line in the talk, and it's also the one to check against how you really see it.

**Strongest objection:** "Six days of fixing is still coding, so the code isn't the cheap part." Someone in engineering could say this, and a sharp non-engineer could too.
**Test:** before Friday, ask yourself how those 6 days split. Was most of the time spent working out what recurring events across time zones *should* do (spec), or rewriting code once you knew? If it was mostly figuring out the behaviour, the story proves the point. If it was mostly rework, soften the line to "the code was the fast part".

**Other directions:**
- Make it a talk for the non-engineers as spec sources: sales and support are where the weird customer cases live, so they're part of the engineering now.
- Make it about estimates only: a short "how to read an engineer's 'done'" guide for the company.
