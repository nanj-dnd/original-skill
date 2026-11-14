**Angle**: Using AI assistants should be the default for writing code; the hard line is letting them *add to things the whole team pays to carry* — and the test suite is the proof.
**Built from**: 1b (yes, with named limits), 2b (2,000→9,000 tests, nightly 20 min→3 h), 3a (engineers, habit change), 4c (measured).
**Strongest objection**: The slowdown might not be the assistants' fault. 7,000 genuinely useful tests would also be slow, and a slow suite is an infrastructure problem (sharding, parallelism), not an authorship problem. **Test**: before Friday, pull a random 50 of the new tests and check whether they add any line or branch coverage the pre-existing suite didn't have. If most don't, your claim holds. If most do, this is an infra talk, not an AI talk.
**Other direction**: Make it about accountability rather than accretion — "AI changed who writes the code, not who is responsible for it" — with review discipline as the single limit.

---

## Outline (5:00)

**0:00–0:45 — Open on the number** (the paragraph below). Two figures, one hedge, one reframe.

**0:45–1:30 — What this talk is not.** Not anti-AI. You use the assistants daily; adoption was the right call; most of what they produce is fine. Split the question: "should we use them" (yes, settled) from "should we use them for everything" (the actual question). The answer is nearly everything, with one exception worth naming.

**1:30–2:45 — The suite as the case.** The timeline. Point out the mismatch: tests grew 4.5×, runtime grew 9×, so the average new test is also heavier than the ones it joined. What you think is happening: overlapping coverage, setup repeated per test. Be explicit that this isn't audited yet — and that's the point. Nobody decided to add 7,000 tests. Each PR was reasonable on its own. What it costs: feedback that used to arrive in 20 minutes now arrives the next morning, for every engineer, every day.

**2:45–3:45 — The principle.** The assistant is very good at *producing* and has no stake in *carrying*. It will always say yes to one more test, one more dependency, one more abstraction. The limit, then, isn't about what kind of code — it's about anything that accrues to shared infrastructure: tests, dependencies, config, CI steps, internal libraries. For those, a human has to answer "what does this cost everyone every day," because the tool can't. The question in review shifts from "is this correct" to "would I have added this if I'd had to type it."

**3:45–4:30 — The ask.** For engineers: when the assistant generates tests, keep the ones that fail for a reason you can name; treat deletion as a contribution. For PMs: when throughput numbers go up, ask what's accumulating alongside them. One concrete suggestion, if you can stand behind it: an audit of the new tests next sprint, with a target of getting the nightly back under an hour.

**4:30–5:00 — Close.** Return to the number. Use the assistants for nearly everything — just not for deciding what we keep.

---

## Opening paragraph

A year ago our test suite had about two thousand tests, and the nightly run took twenty minutes. Today it has about nine thousand, and the nightly takes three hours. Most of those new tests were written with AI assistants, and as far as we can tell, a lot of them check the same things the old ones already did. I want to be careful about what I'm claiming here. I'm not saying the assistants are the problem — I use them every day, and I think most of us should be using them more, not less. What I want to talk about is the one thing they aren't good at, which is knowing when to stop, and why that turns out to matter more for a team than it does for any one of us.

---

**Before you use it**
- The 4.5× vs 9× observation is derived from your figures; confirm the numbers are current before you say them aloud, since it's the spine of the talk.
- "Most of the new ones check the same stuff" is your hedge, not a finding. The 50-test sample above would let you say "we checked" instead of "we think" — a different talk.
- The audit-and-target in the ask is a suggestion; cut it or soften it if you can't commit the team's time.
- If there's a specific PR that took a day to merge because of the nightly, one sentence on it would land harder than the aggregate.

**Distance from the default**: Substantial. The default argued "use judgment about *which* code"; your test-suite figures (2b) shifted it to "the limit is what *accumulates*," and 1b kept it pro-adoption rather than cautionary.

Want me to export this run as a Markdown file (task, default, your answers, angle, outline, paragraph, notes)?