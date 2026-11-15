**Angle**: AI made writing tests nearly free, but it didn't make running, reading or maintaining them any cheaper — so the question isn't whether to use the assistants, it's who decides what gets kept.
**Built from**: 1b (use it, carefully) plus your numbers in 2b; 3a sets the ask at engineers' habits; 4b sets the tone.
**Strongest objection**: 9,000 tests might be real coverage you didn't have before, and a 3-hour nightly could be infrastructure, flaky waits or parallelism rather than count. **Test**: pick 40 of the new tests at random and, for each, name the behaviour it checks in one line; count how many lines repeat. Separately, time the suite with the 2,000 originals alone. If both come back clean, soften section 3.
**Other direction**: make it a QA-process talk ("here's the gate I'm adding to CI") rather than a habits talk — safer, but it lets engineers off the hook.

---

## Outline (5 minutes, ~650 words spoken)

**1. The number (0:00–0:45)**
Open with the two figures, no preamble. Say plainly you're not here to call it a mistake. Opening paragraph below.

**2. What the number means (0:45–1:30)**
Walk through it once more slowly: tests ×4.5, nightly ×9. The run time grew faster than the test count — that's the first hint something isn't scaling cleanly. For the PMs: a 3-hour nightly means feedback on a change arrives next morning instead of before lunch, and that compounds into slower releases.

**3. My suspicion, stated as a suspicion (1:30–2:15)**
You think a lot of the new tests check the same things. Say you haven't audited it yet and you're going to. Be honest that this is a QA lead's hunch from reading PRs, not a finding. The credibility of the talk rests on not overclaiming here.

**4. The principle (2:15–3:00)**
The assistant collapsed the cost of writing. Every other cost stayed where it was: someone reviews the test, the suite runs it every night forever, someone fixes it when it breaks. When one input gets free and the others don't, the free one floods. That's not a tool problem; it's an economics problem, and it will show up anywhere generated code lands, not only in tests.

**5. What I'm asking engineers to change (3:00–4:15)**
Three habits, kept small:
- Before merging a generated test, write the one-line behaviour it checks in the test name or docstring. If you can't, it's probably a duplicate.
- Review generated tests with the same attention as generated code. Right now they get waved through because "more tests is good."
- Treat suite time as a shared budget, like PR size. Adding a minute to nightly is a cost to everyone; say so in the PR.

**6. Close (4:15–5:00)**
Bring it back to 1b: you use the assistants, you want the team to use them, and the point of a QA lead is that someone owns what's in the suite. Right now, for seven thousand tests, nobody does. End on the fix being ownership, not restraint.

---

## Opening paragraph

A year ago our test suite had about two thousand tests and the nightly run took twenty minutes. Today it has about nine thousand, and the nightly takes three hours. Most of those seven thousand new tests were written by an AI assistant, and I want to say up front that I'm not standing here to call that a mistake. I'm here because I run QA, which means I've spent the last year watching the suite grow faster than any of us could actually read it, and I've started to suspect that a lot of those tests are checking the same things. If I'm right, the tool didn't cause that. What caused it is that writing code became nearly free while reading it, running it and maintaining it stayed exactly as expensive as they always were. So the question I want to put to the room isn't whether we should be using these assistants. It's who decides what we keep.

---

**Before you use it**
- The "I'm going to audit it" line in section 3 commits you to doing it before people ask. If you'd rather not, drop that sentence and let the suspicion stand on its own.
- Running the 40-test sample above before Friday would turn section 3 from a hunch into a number, which is the single strongest thing you could add.
- "Tests ×4.5, nightly ×9" is derived from your figures; double-check the 2,000 and 20-minute baselines are the ones you want quoted in front of leadership.

**Distance from the default**: the stance is the default's (you chose 1b), but the piece is built on your suite numbers and the writing-is-free/running-isn't framing, which came from 2b; the default would have argued from invented boilerplate-and-hallucination examples. Moderate distance.

Want me to export this run as a Markdown file (task, defaults, your answers, angle, piece, notes) to the scratchpad?