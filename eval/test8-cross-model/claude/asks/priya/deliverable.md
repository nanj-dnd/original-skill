Here's the outline and opener.

---

## Outline (5 min, ~700 words spoken)

**0:00 – Open: the bill came due (45s)**
Start with the August migration. Don't name the engineer. Land the punchline: the person who merged it couldn't explain what it did. Then pivot: this isn't a story about AI being bad. It's a story about who's reading the code.

**0:45 – What actually changed (60s)**
- We're not banning anything. AI tools are staying. New hires ramp about twice as fast now and I'm not giving that up.
- But the expensive part of shipping software moved. It used to be writing. Now it's reviewing.
- Numbers, plainly: PR volume up ~60% since spring. My two senior engineers went from ~4 hours a week reviewing to ~11. Each.
- Translate for the non-engineers in the room: that's a day and a half a week, per person, spent checking work instead of doing it. The speed showed up in the "writing" column. The cost showed up in the "reviewing" column, and nobody's been looking at that column.

**1:45 – Why review is where the risk lives (45s)**
- The August migration passed review. It wasn't malicious or even obviously wrong. It looked like every other migration.
- When code gets cheap to produce, the only thing standing between a plausible-looking mistake and production is a human who understands it. If that human is skimming because they have eleven hours of this, the system has no backstop.
- For compliance and ops folks: three weeks of reconciliation mismatch is the kind of thing that ends up in an audit finding.

**2:30 – The rule (90s)**
Three parts. State each one, give a sentence of why.
1. **The author owns every line.** If you merge it, you can explain it. Not "the tool suggested it"—*what it does and why it's there.*
2. **"The AI wrote it" is never an excuse in a postmortem.** We don't accept "the intern wrote it" either. Accountability stays with the person who hit merge. This isn't about blame; it's about making sure someone actually understood the change before it shipped.
3. **PRs over 400 changed lines get split.** Reviewers can't hold 1,200 lines in their head. Nobody can. Big PRs are where things hide. If it's genuinely one atomic change, make the case—but the default is split.

**4:00 – What this costs and what it buys (45s)**
- Honest: this slows some things down. Fewer giant PRs, more "wait, explain this to me."
- What it buys: reviewers who can keep up, engineers who understand their own code, and a lot fewer three-week mysteries.
- The 60% more output is real. I just want it to be output we can stand behind.

**4:45 – The ask (15s)**
- I'm proposing this as engineering policy starting [date]. I want engineers to try it for a month and tell me where it hurts.
- To everyone else: if you hear "it was fast," ask "who reviewed it." That's the question now.

---

## Opening paragraph (spoken)

> In August we shipped a database migration. It passed review, it deployed clean, and it quietly dropped a constraint that said a certain field could never be empty. Nobody noticed. Three weeks later, finance and ops were staring at numbers that didn't reconcile, and it took us most of a month to trace it back. When we finally did, I asked the engineer who merged it to walk me through what the migration did. They couldn't. Not because they're careless—they're good. They couldn't because they didn't write it. An AI tool did, and they approved it, and so did a reviewer, and it looked exactly like every other migration we've ever shipped. I'm not here to tell you we should stop using these tools. We shouldn't, and we won't. I'm here to tell you that the cost of shipping code didn't go away this year. It moved. And right now it's landing on about two people.

---

A few notes:

- **"About two people"** is the hook into your seniors' hours. If you'd rather not single them out even implicitly, swap to "landing on the people doing code review."
- The 400-line rule will get the most pushback. I'd have one concrete example ready of a recent PR that should've been split, so it doesn't sound arbitrary.
- If you do slides: one slide with the 4→11 hours number, one with the three rules. Nothing else. The migration story works better without a slide.
- You're at roughly 700 words with the outline fleshed out. If you run long, cut the "why review is where the risk lives" section—the opener already does most of that work.