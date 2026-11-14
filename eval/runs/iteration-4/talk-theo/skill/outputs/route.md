**Path: shortlist (step 5).** Your answers were all picked options or "don't know" (2: nothing specific, 3: everyone). They give a clear direction (yes for everything, an engineer speaking for himself, ending on an experiment), but there's no case, number or argument of your own to build on directly. Your position does differ from the default, so this isn't a case of the default already being your answer.

What's settled: you argue **yes, for basically everything** (1b), as **an engineer speaking for yourself** (4a), to **the whole company** (3), and you end on **a trial with a date and a measure** (5b). There's **no real case or number** behind it yet (2d). Every option below keeps those; they differ in angle.

## Shortlist

**A. The honest bet.** "I think we should use these tools for everything. I can't prove it yet, and nobody in this room can prove otherwise either. So here's a bet: one team, 30 days, and two numbers I'll report back at the next all-hands, whichever way they go." You make your lack of evidence the reason for the experiment, and you put your own credibility on the result.
- **Only yours because:** 1b + 2d + 5b together. A strong position with no case behind it is exactly what an experiment is for. 4a lets you say "I" and own the prediction.
- **Strongest objection:** an engineer betting that his own tools are good can sound self-interested, and the room may wonder who chose the measures.
- **Test:** before Friday, can you name a team that will agree to it, plus two measures you already track (or can track cheaply)? If you can't, the bet sounds hypothetical.

**B. Use it for everything, own every line.** No limits on usage, one rule: if it's in your PR, you wrote it, and you answer for it like you typed it. With writing nearly free, the bottleneck moves to reading and review, so the trial measures review time and bugs found after merge, not lines shipped.
- **Only yours because:** 1b (your "how we own it" framing) and 5b (the measure).
- **Strongest objection:** "review AI code carefully" is close to what everyone says. The ownership rule has to be blunt enough to stand out.
- **Test:** does the company already track bugs found after merge or review turnaround? If not, the trial needs a baseline first.

**C. What you ask for becomes the code.** Aimed at the non-engineers in the room. If engineers use AI for everything, how clear the request is (the ticket, the spec, the customer complaint) sets the quality of what ships. The trial pairs one engineering team with the people who write its requests for a month, and measures rework.
- **Only yours because:** 3 (the whole company is listening, so most of the room isn't engineers) + 1b + 5b.
- **Strongest objection:** it can sound like engineering handing the blame to everyone else.
- **Test:** ask one PM or support lead whether unclear requests really are where time gets lost now. If they shrug, drop it.

**D. Turn it off for a week (unlikely).** The way to show something is worth using for everything is to take it away. Pick one team, switch the assistants off for a week, and measure what slips. You argue "yes" by measuring what happens with "no".
- **Only yours because:** 1b + 5b, flipped.
- **Strongest objection:** it costs a real week of output and annoys the team. It also proves nothing if the team barely uses the tools today.
- **Test:** you'd need current usage first. You said there's nothing specific yet, so find out how heavily people actually use it.

**E. Point it at the worst work first (unlikely).** "For everything" should start with the work nobody wants: the legacy module, the migration that keeps slipping, the flaky tests. The trial takes the ugliest backlog item and gives it 30 days with AI.
- **Only yours because:** 1b + 5b. Nothing else in your answers.
- **Strongest objection:** the hardest legacy work is where these tools are weakest, so the trial could fail and sink your position.
- **Test:** is there a known ugly item the whole company would recognize? It only lands if people outside engineering have felt the pain.

**I'd develop A.** It's the only option that uses all of your answers, including "nothing specific": the gap between a strong view and no proof becomes the talk's engine instead of a weakness. It also gives a mixed room something to remember: a date, two numbers and a promise to report back. B's ownership rule could go in as the trial's one condition ("A with B's rule").

Your answers were mostly picked options, so this shortlist gives you variety but isn't yet tailored to you. If you have a detail (a team name, a measure, why this is on the agenda), add it with your pick.

**Which one should I develop?** Reply with a letter, or a combination like "A with B's rule".

---

**Chosen:** A with B's rule. Developed in deliverable.md.

**Check these before Friday:**
- **Dates:** next Friday is 20 November 2026. A 30-day trial starting the week after would end around 20 to 27 December, when many people are on holiday. Holiday weeks distort both review time and bug counts, so consider starting in January or comparing against the same weeks last year. Also confirm when the next all-hands actually is, since the promise depends on it.
- **"As far as I know, nobody in this room has a number that proves me wrong":** this is my guess from your answer "nothing specific". If your company already tracks AI usage or has a policy, change that line.
- **Placeholders:** everything in [brackets] needs a real detail from you, especially the one moment from your own use in section 2. I didn't make one up.
- **No statistics are cited**, so there's nothing to fact-check.

## Distance from the default
- Takes a side ("everything") instead of the balanced middle. Came from 1b.
- Turns "I can't prove it" into the structure of the talk instead of opening on a hook stat. Came from 2d.
- Ends on a dated trial with "this would prove me wrong" written down in advance, instead of "use it responsibly". Came from 5b.
- Replaces the routine-versus-judgment line with one ownership rule, so "everything" is defensible. Came from your pick, B's rule.
- Speaks as "I", an engineer with a stake, rather than a neutral commentator. Came from 4a.
- **What didn't move:** the measures (review time, bugs after merge) are standard engineering metrics. The non-engineers in the room only get one line in section 3 and one ask in section 5, because 3 was "everyone". With no real case, section 2 still depends on a moment only you can supply.

Anything you want worked in: a line, a story, or a different ending?
