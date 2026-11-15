**Angle**: AI assistants make code cheap to write and no cheaper to carry — so use them for everything, but the thing to watch isn't what they produce, it's what we're now maintaining.
**Built from**: your test-suite numbers (2), the balanced stance (1d), engineers plus PMs in the room (3), peer-to-peer tone (4).
**Strongest objection**: 9,000 tests might be real coverage you didn't have before, and the slow nightly might be infra, not count. "Pretty sure a lot are the same" is a hunch. **Test**: before Friday, take 50 of the new tests at random and sort them into "covers something no other test does" vs "duplicate." If fewer than a third are duplicates, soften the claim; if it's half or more, you have the number for the talk.
**Other direction**: lead with the PMs instead — "velocity went up and here's the bill nobody sees" — a maintenance-cost framing for the people who read the dashboards.

---

## Outline (5 minutes)

**0:00 – 0:45 — The number**
Open with the test suite. 2,000 tests to 9,000 in a year. Nightly from 20 minutes to 3 hours. Most of the new ones AI-written. Let it sit before explaining.

**0:45 – 1:30 — The reframe**
This isn't a story about AI writing bad tests. The tests probably pass. It's a story about how the cost of code moved: writing it is now nearly free, but reading it, running it, and deciding whether it still matters costs exactly what it always did. Every tool that makes output cheap makes volume the new problem.

**1:30 – 2:45 — What that looks like day to day**
Three concrete shapes of the same thing, for engineers:
- Tests that assert the same behaviour three ways because each was generated fresh without looking at the file.
- PRs that are twice the size they'd have been by hand — more to review, same number of reviewers.
- Code that's correct and nobody on the team could explain, because nobody had to think it through to produce it.
Short line for the PMs: when a ticket closes faster, ask what got added to the pile that runs every night.

**2:45 – 3:45 — So should we use it for everything?**
Yes, mostly — the hour it saves is real. The rule that keeps it honest: if it was cheap to generate, it has to earn its place. Before merging generated tests, ask what would break if this test were deleted. Before merging a generated function, be able to say what it does without reading it back. Not more process — one question per PR.

**3:45 – 4:30 — The ask**
A concrete, small one: this quarter, treat the test suite as the experiment. Pick a module, dedupe its tests, see how far the nightly drops. If the suspicion is right, that's hours back every night and a clear picture of how much of the 9,000 was carrying its weight.

**4:30 – 5:00 — Close**
Back to the number. The question for the next year isn't how much code we can generate. It's whether, a year from now, the nightly runs in 20 minutes again.

---

## Opening paragraph

A year ago our test suite had about 2,000 tests. Today it has about 9,000. Most of the new ones were written with an AI assistant, and nearly all of them pass. Over the same year the nightly run went from twenty minutes to three hours. I'm fairly sure a lot of those tests check the same things — not because anyone was careless, but because when writing a test costs nothing, nobody opens the file to see what's already there. That's the version of the AI question I want to talk about. Not "is the code good," because mostly it is. The question is what happens when producing code gets cheap and everything after producing it doesn't.

---

**Before you use it**
- The "same test three ways" and "PRs twice the size" examples in the middle section are illustrations, not your data. Keep them if they match what you see; swap in a real PR if you have one.
- Confirm the 20 min → 3 hr is mostly test count, not a runner or CI change, or someone will say so from the floor.
- The test on 50 random tests would turn "pretty sure" into a number, which is the strongest thing you could add.

**Distance from the default**: the stance is the balanced one you chose, so it's close in position; what changed is the whole talk now hangs on your 2,000-to-9,000 number and the writing-vs-carrying framing, instead of generic "hallucination" examples and a "find the balance" close.

Want me to export this run (task, default, your answers, angle, outline, paragraph, notes) as a Markdown file?