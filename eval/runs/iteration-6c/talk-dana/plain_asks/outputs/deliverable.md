# The Code Is the Cheap Part
*All-hands, 5 minutes*

## Outline

**1. The one-day feature (0:00–0:45)**
- Start with calendar sync. We built it in one day, then needed six more days to ship it.
- Name the question people have been asking: "It was done, so why wasn't it out?"
- Say what the talk is: where those six days went, and why that's where engineering happens now.
- *Slide: "1 day" then "+6 days"*

**2. How we build now (0:45–1:45)**
- Engineers don't spend much of the day typing code anymore. An AI agent does that, and it's fast.
- What we do instead:
  - **Spec**: we write down exactly what the feature should do, including the odd cases.
  - **Tests**: we write checks that prove it does that.
- Analogy for non-engineers: the agent is a builder who works incredibly fast and follows the blueprint exactly. That includes the mistakes in the blueprint.
- So the code is the cheap part. The blueprint is the job.
- *Slide: "Spec → Tests → Code", with "Code" in small type*

**3. Where the six days went (1:45–3:15)**
- For calendar sync we wrote 140 tests first. The agent wrote code that passed all of them, all in one day.
- But the spec was wrong about recurring events across time zones, and none of the 140 tests checked that case.
- So we had 140 green checkmarks and a feature that was wrong. The agent did exactly what we asked. What we asked for was wrong.
- The six days went to figuring out the right behavior, fixing the spec, writing the tests we'd missed, and building it again.
- *Slide: "140 / 140 passing ✓", then "recurring events × time zones ✗"*

**4. What "done in a day" really means (3:15–4:15)**
- When you hear "we built it in a day," that means the cheap part is finished.
- The slow part didn't go away when AI arrived. It moved into the spec and the tests.
- That's why engineers argue about specs for an hour. The arguing is the work, because it's how we find the time-zone bugs before customers do.

**5. Close: you're part of the spec (4:15–5:00)**
- Sales and support hear the strange cases from customers all the time. That's spec material.
- The ask: instead of "is it out yet?", try "did you think about ___?" One good answer from you can save us a week.
- Last line: the code is the cheap part. Knowing what to build is the expensive part, and a lot of that knowledge is in this room.
- *Slide: "The code is the cheap part."*

## Opening paragraph

Last month we built calendar sync in one day. We wrote 140 tests, gave them to an AI agent, and by the end of the day every test passed. Then it took us six more days to ship it. A few of you noticed. Some of you asked me, very politely, "Wasn't that done?" It was, and it was also wrong. So I want to use my five minutes on where those six days went. The answer is that most of an engineer's job here isn't writing code anymore. The code is the cheap part now. The expensive part is something you can help with.
