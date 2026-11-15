**Angle**: AI didn't make writing code cheap, it moved the cost to reviewing — and we haven't moved responsibility with it. Three rules put it back on the author.
**Built from**: 1b (specific harm, not anti-AI), 2a (the August migration, +60% PRs, seniors 4→11 hrs), 3b (40 people, half non-engineers, want buy-in on the rule), 4a (plain), no pro/con.
**Strongest objection**: The August bug was a review failure that could have happened with hand-written code; the 400-line cap is an arbitrary number that could just produce more small PRs for your two seniors to review. **Test**: before Friday, check how many changed lines the migration PR had. If it was under 400, the cap wouldn't have caught it — lead with the ownership rule and present the cap as about review load, not that bug. Also count how many of last month's PRs were over 400 lines, so you can say what the rule actually touches.
**Other direction**: Skip the rules and make the talk an ask for resources — review is now the bottleneck, so count it as real work and staff it.

---

## Outline (5 minutes)

**1. The August bug (0:00–1:15)**
Tell it plainly for the non-engineers: an AI-written database change removed a safety rule, nothing broke immediately, numbers slowly stopped matching, three weeks to trace, and the person who merged it couldn't explain it. Don't name them. Land on: that last part is the problem, not the AI.

**2. What it revealed: the cost moved (1:15–2:30)**
Writing code got fast. Reviewing it didn't. Numbers: PRs up about 60% since spring; two senior engineers' review time went from roughly 4 hours a week to 11, each. Translate for sales/ops/compliance: our most experienced people now spend a day and a half a week reading code they didn't write, and the backlog of unread code is where the next August bug lives. We've been counting the speedup and not the bill.

**3. The question isn't "should we use AI" (2:30–3:00)**
Say it directly: we're going to keep using these tools. The question is who answers for what they produce. Right now the honest answer is: it's unclear, and nobody's talking about it.

**4. The three rules (3:00–4:15)**
- Author owns every line. If you merge it, you can explain it.
- "The AI wrote it" is never an excuse in a postmortem. Same standard as "I copied it from somewhere."
- PRs over 400 changed lines get split. Not to slow anyone down — so that reviews are something a person can actually do.
One sentence each on why it's fair: these are the standards we'd apply to a contractor or a library, and the tool doesn't get a lower bar.

**5. The ask (4:15–5:00)**
What you want from this room: engineers, start now; leads, enforce it in review; everyone else, this is why you'll hear "no" or "split this" more often, and it's the system working. Close by returning to August: the goal is that next time, the person who merged it can tell you what it did.

---

## Opening paragraph

In August, one of our engineers merged a database change that an AI assistant had written. Buried in it was a line that quietly removed a safety rule, the kind that says a particular field can never be left empty. Nothing broke that day. Nothing broke that week. What happened instead is that two sets of our numbers slowly stopped agreeing, and it took three weeks to trace that back to one line in one change. When we found it and asked the engineer who merged it what the change actually did, the honest answer was that they didn't know. I want to be clear about why I'm telling this story. It's not a story about AI being bad at writing code. It's a story about a change going into our system that nobody understood, and about the fact that we didn't have a clear answer for whose job it was to understand it. We're not going to stop using these tools. But we need to decide who's responsible for what they produce, and I'd like us to decide that today.

---

**Before you use it**
- Confirm the migration PR's line count before leaning on the 400-line rule as the fix for August (see test above).
- The engineer from August may be in the room. The paragraph doesn't name them, but "the honest answer was that they didn't know" is identifiable to anyone who was there. Consider telling them first.
- The 4→11 hours figure is yours; if it's an estimate, say "roughly" out loud.
- If you have the number of PRs that were over 400 lines last month, add it in section 4. It makes the rule concrete.

**Distance from the default**: Far. The default would have been a balanced survey with made-up examples; this is a single incident and two numbers driving three specific rules, with no pro/con section. All of that came from 2a and 3b.

Want me to export this run as a Markdown file (task, default, your answers, angle, outline, paragraph, notes)?