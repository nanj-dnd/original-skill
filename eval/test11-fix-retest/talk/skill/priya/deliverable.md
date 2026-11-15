**Angle**: "Should engineers use AI for everything" is the wrong question — they already do, and it's working; the real question is who pays for the code it produces, and right now the answer is two people, so the author has to start paying.
**Built from**: your stance in 1 (not a ban, a rule), the three numbers and the August migration in 2, the fact that half the room never sees the review cost in 3, and "blunt, no jargon, not pro/con" in 4.
**Strongest objection**: the three rules stop bad merges but don't obviously bring 11 hours back down — splitting PRs could mean *more* review requests landing on the same two seniors. **Test**: pull last month's PRs. Count how many were over 400 lines and roughly how much senior review time they ate. If big PRs are a minority of the hours, the cap is the wrong lever and the talk should ask for more reviewers instead.
**Other direction**: skip the rules entirely and make the five minutes an ask to the non-technical half — "the fast ramp you're enjoying is being paid for by two people; here's what it costs and what I need" — so the room leaves owing something rather than agreeing to a policy.

---

## Outline (5 minutes, ~650 words spoken)

**0:00–0:45 — The question you were expecting, and why I'm not answering it**
- Everyone wants a yes/no on AI coding tools. Not giving one. The engineers already use them every day, and I'm not stopping that.
- One thing that's true: new hires are productive in about half the time they used to be. That's real, and I'm not giving it up.
- Reframe: the question isn't *whether*. It's *who pays*.

**0:45–2:00 — The cost didn't disappear, it moved**
- Explain for the non-technical half: writing code used to be the slow part. Now it's fast. But every change still has to be read and checked by a second person before it goes live. That checking is called review.
- Numbers, said slowly: since spring, the number of changes submitted is up about 60%. Review time for each of my two senior engineers went from roughly 4 hours a week to 11.
- Land the point: a quarter of their week now goes to reading code someone else — or something else — wrote. They are the two people in the building you least want doing that, and they're the only two who can.

**2:00–3:15 — What happens when nobody really owns it (August)**
- Tell the migration story in plain words. A change to how the database is laid out went through. It quietly removed a safety check — a rule that says "this field can never be blank." Nobody noticed.
- Three weeks later, numbers in two systems stopped agreeing. It took three weeks to trace back to that one change.
- The kicker, and the reason this talk exists: when we asked the engineer who merged it what the change did, they couldn't say. The tool wrote it; they shipped it.
- That's not an AI problem. That's an ownership problem. The tool is a very fast junior who never gets tired and never gets blamed. Someone has to be the senior.

**3:15–4:30 — Three rules**
1. **You own every line you submit.** If a reviewer asks you to walk through it and you can't, it doesn't go in. Doesn't matter who or what wrote it.
2. **"The AI wrote it" is never an answer.** When something breaks and we write up why, that sentence is not allowed in the write-up. The name on the change is the name that explains it.
3. **Big changes get split.** Any single submission over 400 changed lines gets broken into pieces before review. Nobody can honestly read 400 lines of someone else's work in one sitting, and we've been pretending otherwise.
- One sentence on why this helps the seniors: smaller pieces they can actually check, and authors who've already done the first pass themselves.

**4:30–5:00 — Close**
- Restate: not a ban, not a cheer. Use the tools. Ramp fast. But the speed has to come with a name attached.
- For the half of the room that doesn't write code: the thing you're enjoying — faster output — is currently being paid for by two people. These rules are how we spread the bill.
- Rules start Monday. Questions to me.

---

## Opening paragraph

I know what this slot looks like on the agenda. "Should engineers be using AI to write code?" and you're expecting me to say yes or no. I'm not going to, because it's the wrong question. They already use it. All of them, every day. And it works — a new engineer is now useful in about half the time it used to take, and I'm not giving that up. So the question isn't whether we use it. The question is who pays for it. Because the cost of writing code didn't go away this year. It moved. And right now it's sitting on two people's desks.

---

**Before you use it**
- The "if you can't walk through it, it doesn't go in" mechanism in rule 1 is my sharpening of "the author owns every line." It gives the rule teeth, but confirm it's what you mean before you say it on the record.
- Say "two senior engineers" or name them? Naming them makes the cost real to the non-technical half; it also puts them on the spot. Your call, and decide before Friday.
- "Rules start Monday" assumes you have the authority to just do this. If it needs sign-off, change the close to "here's what I'm proposing."
- The three-weeks-to-trace figure is strong; if you know the dollar or customer impact of the reconciliation mismatch, one sentence on that would land harder with sales and compliance than any engineering detail.

**Distance from the default**: large. The default argues both sides of "should we use AI"; this refuses the question and argues "who owns the output," which came entirely from your answer to 1. Every example is yours, and the structure dropped the pro/con shape because you asked it to.

Want me to export this run — task, default, your answers, angle, outline and opening — as a Markdown file?