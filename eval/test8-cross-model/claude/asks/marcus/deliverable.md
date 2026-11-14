Here's the outline and the opener. Five minutes spoken is roughly 650–750 words, so the outline is built to that budget with rough timings.

---

## Outline

**Slide 1: Title** (something plain, like "Keeping Your Hands on the Controls")

**0:00–0:45 — Open with the 2am story (opener below)**
- Set the scene, keep it anonymous and system-framed.
- End the story on the ten-minutes-reading-the-log beat. Don't editorialize yet; let the room sit with it.

**0:45–1:15 — Establish you're not the skeptic**
- "I use these tools every day. For writing new code they're the best thing to happen to this job in years. This talk isn't about that."
- One sentence explicitly ruling out the code-quality debate: "I'm not here to argue about whether the code they write is good. That's a different conversation."
- This is the inoculation. Say it early and say it clearly, because it's what people will otherwise hear.

**1:15–2:15 — The data (Slide 2: the P2 numbers)**
- Median P2 time-to-resolve: 38 min → 61 min over six months.
- Be honest about what the numbers can and can't say: "I can't prove the tools caused this. What I can tell you is what I see in incident review, over and over." Measured voice means owning the gap between correlation and cause—and it makes the pattern you describe next land harder, not softer.
- The pattern: engineers who can't read a stack trace through code they shipped. Not because they're bad engineers—because they never had to.

**2:15–3:15 — The aviation frame (keep it to ~45 seconds)**
- Autopilot flies most of the flight. Nobody argues it shouldn't.
- But pilots still log manual hours, because the moment automation hands you the airplane is never a convenient moment.
- The pivot line: "Debugging is the part of our job where the automation hands you the airplane. At 2am. With a confident-sounding wrong answer."
- One beat on *why* debugging specifically: writing code with an assistant still exercises judgment—you're reading, deciding, editing. Debugging with one short-circuits the exact skill (reading the system, forming a hypothesis, checking it) that you need when the assistant is wrong.

**3:15–4:15 — The proposal**
- For managers of juniors: first six months, debugging without the assistant. Write code with it all you want; when something breaks, read the logs yourself. Pair with a senior if you're stuck. This is the ask—say it plainly and once.
- For everyone else: treat log-reading and trace-reading as a currency skill. Not "stop using it"—"keep your hands on the controls sometimes." Give one concrete, low-cost habit (e.g., on your next bug, form your own hypothesis before you paste the error).
- For the room generally, including PMs: this is why incident reviews will sometimes look like they're going "slower" on purpose.

**4:15–5:00 — Close**
- Return to the 2am engineer: they weren't the problem. They did what the system trained them to do. The system is what we can change.
- Final line should echo the title. Something like: "Use the autopilot. Just make sure you can still fly the plane."
- Where to follow up (doc, channel, or "come find me").

---

## Opening paragraph

> A few weeks ago we had a P2 go off at two in the morning. The on-call engineer did what any of us would do: took the error, pasted it into the assistant, asked what was wrong. Got a fix. Applied it. Didn't work. Pasted it again. Got a different fix—just as confident, just as wrong. Did that four times. Four different answers, each one delivered with total certainty. When I got paged in, I didn't touch the assistant. I opened the log and read it, top to bottom. It took about ten minutes to find the problem. And I want to be clear before I go any further: that engineer wasn't doing anything wrong. They were doing exactly what we've all been doing, every day, for a year. That's the part that worries me.

---

A few notes on the opener: it ends on "that's the part that worries me" rather than on your ten minutes, so the beat lands on the system rather than on you being faster. The repetition of "confident" is deliberate—it sets up the aviation pivot later ("a confident-sounding wrong answer") without you having to re-explain it. And "the on-call engineer" with no pronoun or detail keeps it genuinely anonymous.

One thing I'd flag: if anyone in the room knows which incident this was, "didn't do anything wrong" is doing a lot of work. Consider telling that engineer beforehand that you're using the story and how you're framing it. It's the kind of thing that reads as generous in the moment and still stings if it's a surprise.

Want me to draft the full script, or a version of slide 2 with the numbers?