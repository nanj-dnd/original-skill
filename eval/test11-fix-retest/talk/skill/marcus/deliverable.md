**Angle**: The risk of AI assistants isn't the code they write, it's that debugging skill decays when nobody practices it — so keep using them to build, and hand-fly incidents: engineers work from the logs before opening an assistant, and new hires debug without one for their first six months.

**Built from**: 1d (autopilot framing, not anti-tool, six months for juniors), 2b (the 2am outage, 38→61 minutes, "can't follow a stack trace"), 3a (engineers and managers; habit plus a norm proposal), 4a and your role (incident-review voice, recommend not mandate).

**Strongest objection**: 38→61 minutes over six months has other candidate causes — more services, more P2s, a rotation with more new people, a different mix of incident types — and you're conceding the assistant isn't the only one. Someone will say you're pinning a trend on your pet theory. **Test**: before Friday, pull the P2s from both periods and tag each one for whether the on-call engineer could point at the cause from logs/trace alone or went straight to pasting the error. If the slow ones cluster in the second group, you have a slide. If they don't, soften the number to "the trend I'm watching" and let the outage story carry it.

**Other direction**: Drop the six-month proposal entirely and make it purely a personal habit talk — "try the logs first" — which nobody can argue with but which also gives managers nothing to act on.

---

## Outline (5 minutes, ~700 words spoken)

**0:00–0:45 — The outage** (opening paragraph below)
2am, on-call pastes the error four times, four confident fixes, none right. You read the log, ten minutes, done. State the point plainly: the problem wasn't the assistant's answers, it was that nobody could read the system without one.

**0:45–1:30 — What I'm not saying**
Head off the "doesn't like AI" reading in two sentences, no more. You use the tools. You want people writing new code with them. This is not a talk about the tools; it's a talk about one skill.

**1:30–2:30 — The number**
P2 median time-to-resolve: 38 minutes to 61 over six months. You run the reviews, you've watched it. The pattern in the room: engineers who can't follow a stack trace through code they shipped. Say out loud that the assistant isn't the only cause, then say the pattern is hard to ignore. Conceding it first makes it harder to dismiss.

**2:30–3:30 — Autopilot**
Nobody serious argues airliners should fly manually. But pilots still hand-fly on a schedule, because when the automation hands you a mess at the worst possible moment, the stick-and-rudder skill has to already be there — you can't build it during the emergency. Debugging is that skill. It's only ever needed at 2am, and it's the one the assistant lets you skip every day.

**3:30–4:30 — Two asks**
For engineers, Monday: work the next incident from the logs and the stack trace first. Open the assistant after you have a theory, not instead of one. For managers, a proposal, not a mandate — you can't make this call: an assistant-free debugging period for new hires, six months, the same way you learn to fly manually before you get to lean on the automation. Build the skill while the stakes are low.

**4:30–5:00 — Close**
Bring it back to the outage. The assistant was never going to find that bug, and the next one will look different anyway. You want the person on call at 2am to be able to read what's in front of them. That's all this is.

---

## Opening paragraph

A while back we had a P2 at two in the morning. The on-call engineer did what most of us would do: pasted the error into the assistant. It came back with a confident fix. That didn't work, so they pasted it again. Four times, four different fixes, all confident, none of them right. I got paged in, opened the log, and found the cause in about ten minutes. I want to be clear about what went wrong there, because it's not the obvious thing. The assistant didn't write bad code. The problem was that when the assistant was wrong, nobody on the call could read the system without it. That gap — between pasting an error and being able to follow it through the code yourself — is what I want to spend my five minutes on. And I want to spend them on it because I run our incident reviews, and I've been watching that gap get wider.

---

**Before you use it**
- The 38→61 figure is yours; run the tagging test above so you can answer "what else changed?" from the stage.
- Confirm "a while back" is accurate for the outage, or replace it with the real timeframe — I didn't have one.
- Worth adding if true: how many of the recent P2 reviews showed the "paste first, read never" pattern. Even a rough count ("more than half of the last ten") turns an impression into evidence.
- The autopilot comparison is your framing and stands on its own; I'd avoid citing a specific crash from the stage unless you've checked it, because someone in the room will have read the report.

**Distance from the default**: Far. The default was "use it, but review everything." Yours is "the output is fine, the atrophy is the problem," which came entirely from 1d; the outage and the 38→61 number (2b) replaced generic examples, and your role turned the six-month idea from a rule into a proposal aimed at managers.

Want me to export this run as a Markdown file (task, default, your answers verbatim, angle, outline, paragraph, notes)?