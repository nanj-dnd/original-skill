**Angle**: AI assistants are fine for writing code; the problem is that debugging with them is quietly eroding the one skill that matters at 2am, so new engineers should do their first six months of debugging by hand.

**Built from**: 1 (not anti-AI, skill atrophy, debugging and juniors, the six-month proposal, the pilot analogy), 2 (the 2am outage, 38→61 minutes), 3 (managers are the real audience), 4 (incident-review register).

**Strongest objection**: The 38→61 jump has other candidate causes: more services, more incidents, headcount changes, a different mix of what counts as P2. A skeptic will say you've paired one anecdote with a trend and called it causation. **Test**: before Friday, go through the last 15–20 P2 reviews and count how many show the paste-the-error-and-try-the-fix loop. If it's a clear majority, say the number. If it isn't, present 38→61 as "this is what made me look" rather than as proof.

**Other direction**: Make the rule about the situation, not the person: nobody uses an assistant on a live incident until they've read the trace themselves. Applies to everyone, doesn't single out juniors, and is easier for managers to back.

---

## Outline (5 minutes, ~700 words spoken)

**0:00–0:45 — The incident**
Open on the 2am outage. On-call pastes the error into the assistant. Four tries, four different confident fixes. The problem was in the log; it took about ten minutes to read it and find it. Don't name the engineer. Don't editorialise yet; just tell it the way you'd open a review.

**0:45–1:30 — The pattern, with the number**
This isn't one night. Median time-to-resolve for P2s has gone from 38 minutes to 61 over the last six months. In reviews you keep seeing the same thing: engineers who can't read a stack trace through code they wrote. Say the quote marks out loud: code they "wrote."

**1:30–2:00 — Clear the room's first objection**
This isn't an anti-AI talk. You use it, your team uses it, and for writing new code you're happy with it and not proposing any change. Say that plainly and early so the rest of the talk isn't heard as "AI bad."

**2:00–3:00 — Why debugging is different**
Writing code with an assistant: you review the output, you're still the author. Debugging with one: you paste a symptom and get a plausible story, and the thing you skip is the reading. Reading a trace, reading a log, forming a hypothesis before touching anything. That's the skill that atrophies, and it's the one that doesn't come back from a prompt. The pilot analogy goes here: autopilot is better than the pilot most of the time, and pilots still train on hand-flying, because the day the automation gives you the airplane back is the worst possible day to be learning.

**3:00–4:00 — The proposal**
New engineers: first six months of debugging without an assistant. Not writing code; debugging. Be precise about scope so nobody hears a ban. Address the obvious counter: yes, it will be slower for them for six months. That's the point; you're buying a skill, not shipping fixes faster in month two. Then speak directly to managers: this only works if it's a norm you back, in the moment, when the junior is stuck and the assistant is right there. Say that's the ask.

**4:00–4:45 — What non-engineers should take away**
One line for the rest of the room: nothing is being banned, there is no new policy for the company, this is an engineering norm about how we train people. Then what you'll measure: P2 time-to-resolve, and whether the paste-and-pray pattern shows up in reviews. Report back in six months.

**4:45–5:00 — Close**
Back to 2am. Four confident answers, none of them right, and the real one sitting in the log. The point of the next six months is that the next person on call reads the log first.

## Opening paragraph

A couple of weeks ago we had an outage at two in the morning. The on-call engineer did what most of us would do now: pasted the error into the assistant. It gave a fix. Didn't work. Pasted again. Different fix, just as confident. Four rounds of that. When I got on, I read the log, and it took about ten minutes to find the problem. I'm not telling you this to make anyone look bad, and I'm not telling you it to make the case that AI is bad; I use it every day and so does my whole team. I'm telling you because I run our incident reviews, and this is not a story about one night anymore. Six months ago our median time to resolve a P2 was 38 minutes. It's 61 now. And in review after review I'm watching engineers who can't read a stack trace through code they "wrote." So this is a talk about one specific thing: debugging, and what the assistant is doing to the skill of debugging, and one change I think we should make for the people who are newest here.

---

**Before you use it**
- "A couple of weeks ago" in the opening is a placeholder for whenever the outage was; swap in the real timing.
- Run the P2 review count from the test above. If it supports you, add the number after "61 minutes"; it's the line that turns the anecdote into a case.
- The 38→61 figure is yours; confirm the window and that the P2 definition hasn't changed in that period, because that's the first thing a manager will check.
- If you can say how many new engineers this would affect, say it in the proposal section so it sounds scoped rather than sweeping.

**Distance from the default**: Nearly all of it. The default argued the "tool not crutch" middle with made-up examples; answer 1 narrowed it to debugging and juniors with a concrete six-month rule, answer 2 gave it a real incident and a trend line, and answer 3 aimed the ask at managers instead of the room in general.

Want me to export this run (task, default, your answers, angle block, outline, opening, notes) as a Markdown file?