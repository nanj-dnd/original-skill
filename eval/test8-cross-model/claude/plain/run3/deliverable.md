Here's a draft. I've taken a position — "yes for most things, no for everything" — because a 5-minute talk with no stance is forgettable. Adjust if your view is different.

---

## Outline: "Should Engineers Use AI Coding Assistants for Everything?"

**Target: ~5 minutes, ~700 spoken words**

**1. Hook (30 sec)**
- Reframe the question: the interesting debate isn't *whether* to use them, it's *where the line is*.
- One-line thesis: use them aggressively for the work that's about typing, and deliberately for the work that's about thinking.

**2. Where they clearly win (1 min)**
- Boilerplate, tests, migrations, docs, glue code, unfamiliar APIs, "how do I do X in language Y."
- The honest point: refusing to use them here is like refusing to use autocomplete — it's not purity, it's just slower.
- Optional: one concrete internal example (a task that went from a day to an hour).

**3. Where "everything" breaks down (1.5 min)**
- *Design decisions* — the assistant will happily build the wrong thing beautifully. It doesn't know our constraints unless we tell it, and we often don't know them until we've thought.
- *Code you can't verify* — if you can't review it, you can't own it. Security-sensitive paths, concurrency, anything touching money or auth.
- *Skill atrophy* — junior engineers who never debug by hand don't develop the instincts to know when the AI is confidently wrong. This is the quiet long-term risk.

**4. The practical rule (1 min)**
- Proposed norm: **AI writes the first draft; a human owns the merge.** You are accountable for every line you ship, regardless of who typed it.
- Two habits: (a) always read the diff like a code review, not a rubber stamp; (b) when the task is novel or high-stakes, think first, then prompt.

**5. Close (30 sec)**
- The tools are getting better fast; the line will move. But "I didn't write it, the AI did" will never be an acceptable incident postmortem.
- Call to action: use them more than you are now — *and* stay the engineer in the loop.

---

## Opening paragraph

> I was asked to talk about whether engineers should use AI coding assistants for everything, and I want to start by admitting that's the wrong question — because the honest answer is "obviously not," and that's a boring place to stop. The real question, the one we're actually arguing about in code review and in Slack, is *where the line is*. So here's my position in one sentence, and then I'll spend four minutes defending it: we should be using these tools far more aggressively for the work that's mostly about typing, and far more carefully for the work that's mostly about thinking. The hard part is that from the outside, those two kinds of work look exactly the same.

---

A few notes:
- Section 3 is where you'll get the most audience engagement — if you have a real story of an AI-generated bug that made it to prod (or nearly did), put it there.
- If you want to sound less cautious, cut the skill-atrophy point; if you want to sound more cautious, lead with it.
- Time check: read the opening aloud — it's about 35 seconds at a normal speaking pace.