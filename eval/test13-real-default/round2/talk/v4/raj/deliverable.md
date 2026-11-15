**Angle**: AI assistants are fine at writing code; the thing "everything" quietly drops is the step where someone asks whether the code needs to exist — and our test suite is where that shows up first.
**Built from**: 1a (keep the "use with judgment" stance, make it concrete), 2c (2,000 → 9,000 tests, 20 min → 3 hr nightly, your read that most are redundant), 3a + QA lead (plain, first person, to engineers and PMs), 4b (end on a norm).
**Strongest objection**: a 4.5× bigger suite might genuinely be catching 4.5× more — product grew, coverage grew, 3 hours is the price of safety. **Test** before Friday: compare branch coverage at the 2,000-test commit and today. If coverage moved a little and the suite moved a lot, your point holds; if coverage tracked the count, soften the claim to "we don't know what the extra 7,000 buy us" and make the norm about finding out.
**Other direction**: tell it as a tooling problem, not a judgment problem — the suite was cheap to write, so it's cheap to prune; propose an AI-assisted dedupe pass instead of a merge norm.

---

## Outline (5 minutes)

**1. The number (0:00–0:45)** — opening paragraph below. Two figures, no setup: tests went 2,000 → 9,000 in a year, nightly went 20 min → 3 hours.

**2. What that number is and isn't (0:45–1:45)**
- It isn't a story about AI writing bad tests. The tests pass. They're probably individually fine.
- It's a story about what nobody asked: does this test fail on anything the existing ones don't? My read, as the person staring at the run every morning, is that for most of the new 7,000 the answer is no.
- The tool did exactly what it was asked. "Write tests for this" became 30 tests where 3 would have done, because 30 cost the same as 3.
- Say plainly: this is a guess until we measure it. (Insert the coverage comparison if you ran it.)

**3. Why I'm talking about tests and not features (1:45–2:45)**
- Tests are just where the cost is visible: a 3-hour nightly is a number on a dashboard. The same thing is almost certainly happening in places with no dashboard — config, helpers, docs, retry logic, abstractions that exist because generating them was free.
- "Everything" doesn't mean the assistant writes everything. In practice it means the assistant *decides what gets written*, by making volume free. Volume isn't free downstream: someone runs it, reads it, waits for it, debugs it when it flakes.
- The judgment the tool can't do for you isn't "is this code right," it's "should this code be here."

**4. The norm (2:45–4:00)**
- Proposal, starting with tests because that's my patch: **a test gets merged with one line saying what would now fail that didn't before.** If you can't write that line, the test doesn't go in.
- Second half: **nightly runtime becomes a tracked number with an owner** (me), and it doesn't go up without a reason that's written down.
- Why this and not "use AI less": the norm is about the question, not the tool. Use the assistant for all of it if you like; just answer the question before merge. Most of the time the answer takes ten seconds.
- For the PMs in the room: this is the same discipline you apply to a backlog. More tickets isn't more product.

**5. Close (4:00–5:00)**
- Offer: I'll run the coverage comparison and the first prune of the suite in the next sprint and report what 7,000 tests were actually buying us. Then we can decide whether the norm goes beyond tests.
- Last line: the assistants are good enough that "can it write this" is settled. The only question left is the one we were supposed to be asking all along — "does this need to exist" — and the suite says we've stopped asking it.

---

## Opening paragraph

> A year ago our test suite had about 2,000 tests in it. Today it has about 9,000. The nightly run that used to take 20 minutes now takes three hours. Most of those new tests were written by an AI assistant, and I want to be clear up front: they pass. They're not broken. If you opened one at random you'd probably say it looks fine. I'm the QA lead, so that suite is my problem, and here's what I think the extra 7,000 tests are mostly doing: checking the same things the first 2,000 already checked. That's a guess, and I'll tell you how I'd prove it. But I'd rather start there than with the question I was given, which was whether engineers should use these tools for everything. Because I think the suite already answered it. The tools wrote exactly what they were asked to. What got skipped was the ten seconds where someone asks whether it needed writing at all.

---

**Before you use it**
- The redundancy claim is your read, not a measurement. The talk says so, but run the coverage comparison (or sample 30 new tests and look for an older one that fails on the same change) — one real figure in section 2 would carry the whole thing.
- The norm in section 4 is my proposal built from your material. Check you're willing to own the "nightly runtime has an owner" half before you say it on stage.
- If you have one example of a new test that duplicates an old one — two names, side by side — put it in section 2. It would take 15 seconds and nobody would argue with the number afterwards.

**Distance from the default**: the default (and all three samples) opens with "that's the wrong question," splits the job into typing vs. thinking, warns about judgment calls and skill atrophy, and ends on "you own every line you merge." This opens with your numbers, argues the risk is volume rather than wrongness (from 2c), and ends on a merge norm specific to tests (from 4b). It still shares the samples' move of reframing the question — yours does it after the number instead of before — and the underlying stance is the same "use with judgment" you chose in 1a.