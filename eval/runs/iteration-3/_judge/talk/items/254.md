# One Day to Build, Six Days to Be Right

*5 minutes at the all-hands. About 650 spoken words. Mostly for the non-engineers in the room.*

---

## Opening paragraph (read it close to word for word)

> Last month we built calendar sync in one day. One day! An AI agent wrote basically all of the code. Then it took us six *more* days to ship it. So today I'm going to tell you where those six days went, because that's the real answer to "should engineers use AI for everything?" The short answer is: we already do. That question is settled. The more interesting thing is what it did to the job. If you've walked past an engineer lately and they weren't typing code, they were probably arguing about whether a 9am Tuesday meeting in London is still at 9am after the clocks change. That argument *is* the engineering now. The code is the cheap part.

---

## Outline

**1. Hook: calendar sync (0:00 to 0:45)**
- The opening paragraph above. Let "six more days" land, then pause.

**2. The question's already answered (0:45 to 1:15)**
- Yes, our engineers use AI for nearly everything. It's how we work and it isn't up for debate today.
- So the better question is: if the AI writes the code, what are the engineers doing all day?

**3. The job moved (1:15 to 2:15)**
- The analogy: the AI is a fast, tireless contractor who takes everything literally. It builds exactly what you asked for, *including the mistakes in what you asked for*.
- So the real work is now two things:
  - **The spec:** saying exactly what the thing should do, including the weird cases.
  - **The tests:** a checklist that proves the AI actually did it. If something isn't on the checklist, nobody checked it.
- One-liner to repeat: *Writing code got cheap. Being right didn't.*

**4. Back to calendar sync (2:15 to 3:30)**
- Day 1: we wrote 140 tests first. The agent filled in the code until they all passed. Done in a day. High fives.
- Days 2 to 7: the spec never said what happens to recurring events across time zones, so no test covered it. The agent made a reasonable guess. It was wrong.
- The point: the AI didn't mess up. *We* never asked the question. Six days went to finding the question, answering it and writing the tests for it.
- (Optional laugh line: "140 tests, and the one that mattered was test 141.")

**5. What this means for you (3:30 to 4:30)**
- **"It took a day" means the *building* took a day.** Before you promise a customer a date, ask "is the spec settled?", not "is it coded?"
- **When an engineer asks you an annoying edge-case question** ("what if the customer is in Sydney and the meeting repeats monthly?"), that isn't stalling. That's the work.
- **You're part of the spec now.** Sales and support hear the strange customer cases first. Send them to engineering. Your weird ticket might be test 141.
- (If it fits the room, one sentence on jobs: this doesn't make engineers less needed. It moves them to the harder part.)

**6. Close (4:30 to 5:00)**
- Callback: "So next time you hear something was built in a day, ask the follow-up: *and how long to be right?*"
- Last line: "The code was the cheap part. The time zones were not."

---

**If you're running long:** cut section 2 down to one sentence and drop the optional jobs line. Keep the calendar sync story whole, because it's the whole talk.
