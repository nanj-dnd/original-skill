Here's a draft built around a clear thesis, since 5 minutes isn't enough time to be balanced-to-the-point-of-saying-nothing. I've assumed the position "yes, use them aggressively — but never outsource understanding." If you want to argue a different angle, tell me and I'll rework it.

---

## Talk outline (~5 min)

**1. Opening (45 sec)** — Reframe the question
The real question isn't "AI for everything or nothing" — it's *what we're actually paid for*. (Opening paragraph below.)

**2. What AI assistants are genuinely great at (60 sec)**
- Boilerplate, scaffolding, test generation, migrations, glue code
- Reading unfamiliar codebases and APIs faster
- Being a rubber duck that talks back
- One concrete internal example if you have one (e.g. "X shipped the Y migration in two days instead of a sprint")
- Point: not using them for this stuff is leaving speed on the table for no reason

**3. Where "everything" breaks down (75 sec)**
- **Understanding debt**: code you accepted but can't explain is code you can't debug at 2am
- **Confident wrongness**: the assistant is most dangerous when it's plausible and wrong — subtle concurrency, auth logic, edge cases
- **Design is not generation**: system boundaries, tradeoffs, "should we build this at all" — the model doesn't know your users, your incidents, or your roadmap
- **Skill atrophy for juniors**: if you never struggle, you never learn why the answer is right

**4. The rule I'd propose (60 sec)**
- Use AI for anything you could review well. Don't use it for anything you couldn't.
- Practically: you own every line you merge, regardless of who or what wrote it
- Prompting is a skill; verifying is a more important one
- Optional: one or two team norms (e.g. "AI-generated tests still need a human to check they test the right thing")

**5. Close (30 sec)**
- The engineers who win aren't the ones who use AI the most or the least — they're the ones who know *which* 20% of the work still needs their full brain
- Call to action: try it everywhere, keep what makes you faster, stay sharp on what makes you *good*

---

## Opening paragraph

> I've been asked to answer a question that's been bouncing around our Slack for months: should engineers be using AI coding assistants for everything? And I want to start by saying I think it's the wrong question — because it treats "coding" as one thing. It isn't. Some of what we do is typing: boilerplate, migrations, the fourth nearly-identical API handler. And some of what we do is deciding: what to build, where the boundaries go, what happens when this fails at three in the morning. AI assistants have gotten remarkably good at the typing. They've gotten very good at *sounding* like they're good at the deciding. So the question I actually want to answer in the next five minutes is: how do we use these tools aggressively for the first kind of work without quietly handing them the second?

---

A few delivery notes: section 2 is your credibility — if you don't acknowledge the upside first, the skeptics tune out and the enthusiasts get defensive. Section 3 is where you'll run long if you're not careful; pick the two strongest points for your audience and cut the rest. And if you can replace any of my generic examples with a real incident or win from your team, do it — one specific story beats three abstract bullets.