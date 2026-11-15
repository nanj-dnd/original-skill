**Angle**: When writing a test cost half an hour, that cost did the filtering — you only wrote the ones worth having. The assistant removed the cost without replacing the filter, and the 9,000-test suite is what that looks like; the open question is what the filter is now, for tests and for everything else we produce.
**Built from**: 2c (the suite numbers, your suspicion of redundancy), 1a (keeps your measured stance — use the tools, put a limit back deliberately), 3b (engineer-level detail, PMs get one hook), 4b (ends on a question, not a rule).
**Strongest objection**: 9,000 tests may genuinely catch more bugs than 2,000, and a 3-hour nightly is a CI problem — parallelise it and the talk loses its spine. **Test**: before Friday, take a random 50 of the post-growth tests and check how many add coverage no other test provides (coverage diff, or a quick mutation run). If it's under half, you have your number and "I think" becomes "I checked." If it's most of them, swap the angle to the other direction below.
**Other direction**: Keep the numbers but make the talk about feedback speed, not redundancy — "we traded a 20-minute answer for a 3-hour one, and nobody decided to."

---

## Outline (5 min, ~700 words spoken)

**1. The two numbers (0:00–0:45)**
Opening paragraph below. 2,000 → 9,000 tests in a year, mostly AI-written. Nightly 20 min → 3 hours. Your suspicion that many of the new ones check the same things.

**2. What a test used to cost, and what that cost was doing for us (0:45–1:45)**
- A hand-written test cost real time, so people wrote the one that bought the most confidence and skipped the rest. The cost was a filter nobody had to design.
- Suite size was therefore a signal: more tests meant more of the system was genuinely covered.
- Now a test costs roughly nothing to produce. The filter is gone, nothing replaced it, and the size of the suite tells us almost nothing.

**3. What we pay instead (1:45–2:45)**
- 3 hours. Anything that breaks overnight is seen the next morning instead of twenty minutes later.
- The arithmetic from the two numbers: 2,000 tests in 20 minutes is 100 a minute; 9,000 in 180 minutes is 50 a minute. On average the new tests are also heavier than the old ones.
- The honest caveat: part of this is infrastructure, and parallelising would buy time back. But that hides the question rather than answering it — we still wouldn't know which of the 9,000 we'd miss.

**4. The same shape, elsewhere (2:45–3:45)**
- Tests are just the place we happen to have a timer on. Anywhere output used to be rate-limited by effort, the same thing is likely happening: PR size, the number of abstractions in a change, docs, config.
- This is the limits part of "use it, with limits": the tools are fine; what's missing is a replacement for the filter that effort used to provide. That has to be put back on purpose now.
- For the PMs in the room: when a feature lands with 300 tests, that number no longer tells you what it told you a year ago.

**5. The question (3:45–5:00)**
Not a rule — a debate to start. Three versions of it:
- If we proved 4,000 of those tests are redundant, would we delete them? Who would be allowed to decide?
- What's our number — how long is the nightly allowed to get before it's a problem, and who's watching it?
- When producing something is free, what's the signal we're going to use instead of volume?
Close: "I don't have the answer. I'd like to argue about it afterwards."

---

## Opening paragraph

A year ago we had about 2,000 tests. Today we have about 9,000, and most of the new ones were written with an AI assistant. I'm not going to say that's bad — nobody writes 7,000 tests by hand in a year, so these are tests we wouldn't otherwise have. Here's the other number, though. The nightly run used to take twenty minutes. It now takes three hours. So we have four and a half times the tests and nine times the wait, and my honest suspicion is that a large share of the new ones are checking the same things as each other. I'm not up here to argue we should stop using these tools. I'm up here because that test suite is the clearest picture we have of what happens when producing something becomes almost free — and I think the same thing is happening in places we don't have a timer on yet.

---

**Before you use it**
- Confirm the four figures against CI history; a "2,000 → 9,000" that turns out to be "2,300 → 8,600" is fine, but say the real ones.
- Run the redundancy check above. The talk is stronger as "I checked 50 of them and 31 were redundant" than as "I think." If you can't, keep "suspicion" — don't let it harden into a claim on stage.
- If you know who owns CI, section 3's caveat lands better with a nod to them.

**Distance from the default**: The stance is the default's (you chose 1a), so the piece is more specific rather than more opinionated. What changed: the whole argument is built on the test-suite numbers (2c), it ends on a question rather than guidelines (4b), and it drops the win/breakdown structure the samples all use. What it still shares with them: acknowledging the upside before the concern, and the "verification is now the expensive part" idea is a cousin of sample 1's verification-debt point. It avoids their shared "that's the wrong question" opener, the boilerplate/architecture/skill-atrophy examples, and the typing-vs-thinking framing.