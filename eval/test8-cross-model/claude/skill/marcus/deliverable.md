**Angle**: The thing that breaks in production isn't AI-written code, it's the engineer who never learned to read it, so juniors should spend their first six months debugging without an assistant, and managers have to protect that time.

**Built from**: 1b with your caveat (not anti-AI, worry is atrophy not quality), the 38→61 minute figure and the 2am outage, the manager-as-real-audience point in 3, and 4a.

**Strongest objection**: 38 to 61 minutes over six months has many possible causes: more services, new hires, a change in what counts as P2, a few long-tail incidents dragging the median. Someone in the room will think it, and if they say it out loud the talk loses the number. **Test**: before Friday, split your last six months of P2 reviews two ways: by whether the on-call engineer used an assistant during triage, and by tenure under or over 18 months. If the slowdown sits where you think it does, say so in the talk ("I checked, and it's concentrated in…"). If it doesn't, drop the number and lean on the outage and what you see in reviews, which you can defend firsthand.

**Other direction**: Instead of a six-month rule, make it a drill: every new engineer works their first ten incidents without an assistant, with a senior pairing. Easier for managers to say yes to, harder for anyone to call a ban.

---

## Outline (5 minutes, roughly 700 words spoken)

**0:00 – 0:45 — The 2am outage** (opening paragraph below)
On-call engineer, four pastes, four confident fixes, none of them right. You read the log, found it in ten minutes. Land it on: the assistant wasn't the problem. The problem was that nobody in the loop could read the error.

**0:45 – 1:15 — Where I stand, so nobody mishears this**
"I use these tools every day. I'm fine with them writing new code. This is not a talk against AI assistants." Say it plainly and early, so the skeptics don't tune out and the enthusiasts don't get defensive.

**1:15 – 2:15 — What I see in incident review**
Median time-to-resolve for P2s: 38 minutes to 61 over six months. You run the reviews, this is firsthand. The pattern underneath the number: engineers who can't trace a stack trace through code they shipped. Name it as skill atrophy, not code quality. The code is often fine. The person who has to fix it at 2am is not.

**2:15 – 3:15 — The autopilot analogy**
You fly. Modern autopilots are excellent, and every pilot still learns to hand-fly first, because the moment automation gives you the airplane back is always the worst possible moment, and the stick-and-rudder skills have to already be there. Autopilot is great. You don't learn to fly on it. Debugging is our stick-and-rudder.

**3:15 – 4:15 — The ask**
Juniors do their first six months of debugging without an assistant. New code with AI, fine. Incidents, bugs, "why is this test red": by hand, with a senior nearby. Then turn to managers directly: this costs you. A junior debugging the slow way will take two hours on something the assistant would have patched in ten minutes, and you have to make room for that and not ding them for it. If you don't, the rule is dead on arrival, and we keep paying for it at 2am instead.

**4:15 – 5:00 — Close**
Back to the outage. Nobody wants to be the engineer with four fixes and no idea. Six months of the slow way is how you make sure that isn't you. Offer to talk to any manager who wants to figure out what this looks like on their team.

---

## Opening paragraph

A few months ago I got paged at two in the morning. We had an outage, and by the time I was awake enough to log in, the on-call engineer had already been at it for a while. They'd pasted the error into the coding assistant, got a fix, applied it, and it didn't work. So they pasted it again. Different fix, same result. They did that four times. Four confident answers, four wrong ones. I opened the log, read it top to bottom, and found the actual cause in about ten minutes. I want to be clear about what went wrong there, because it's not what it sounds like. The assistant didn't break anything. The problem was that at two in the morning, with production down, the person holding the pager couldn't read a stack trace through code they had shipped themselves. And I'm seeing that more and more.

---

**Before you use it**: The 38→61 figure and the outage are yours and I couldn't check them; run the tenure/assistant split above so the number survives a challenge. The "two hours vs ten minutes" line in the ask is illustrative, not measured; swap in a real example from a review if you have one, or soften it to "slower." Check whether the on-call engineer is identifiable to the room and whether they're okay with the story being told; it lands better if you can say you've talked to them. If you have a count of how many of the recent reviews showed the can't-read-the-trace pattern, that's worth one sentence.

**Distance from the default**: Large. The default argued "use it for everything except judgment calls"; this argues the opposite for one group for one period, and the shift came from your caveat on 1 (atrophy, not quality) plus the outage and the manager point, which turned a general-audience talk into an ask aimed at one row of seats.

Want me to export this run (task, default, your answers, angle block, outline, opening, notes) as a Markdown file?