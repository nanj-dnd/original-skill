Got it. Here's a draft sized for 5 minutes (roughly 650–700 words spoken), aimed at a mixed audience, measured tone.

---

## Outline: "Should engineers use AI for everything?"

**0:00–0:45 — Opening: reframe the question**
- The real question isn't "AI or no AI" — it's *where* it helps and *where* it quietly costs us.
- Set up the answer: yes for the repetitive stuff, caution for the rest.

**0:45–1:45 — Where it clearly helps (the "yes" column)**
- Boilerplate: CRUD endpoints, config, data mappers, glue code. The stuff that's tedious but mostly mechanical.
- Tests: generating test cases, fixtures, edge-case coverage we'd otherwise skip because we're busy.
- Translation tasks: "turn this SQL into an ORM query," "explain this regex," "convert this to TypeScript."
- Non-engineer framing: this is like a very fast autocomplete that's read every public codebase. It's great at the predictable.

**1:45–3:15 — Where to be careful (the "it depends" column)**
- **Business logic** — pricing, discounts, tax, inventory, checkout. This is where our actual money is, and Copilot doesn't know *our* rules. Plausible-looking code that's subtly wrong is worse than no code.
- **Architecture and design** — AI optimizes for "looks like code I've seen," not "fits how our system is built." It'll happily add a fourth way to do something we already do three ways.
- **Security and payments** — anything touching auth, PII, card data. Generated code can reproduce common patterns, including common mistakes.
- **Understanding** — if you can't explain every line of what you merged, you don't own it. Debugging at 2am is a lot harder when nobody actually wrote the code.
- One sentence on skills: for newer engineers, leaning on it for *everything* means you never build the judgment to know when it's wrong.

**3:15–4:15 — The practical rule of thumb**
- Ask: *"If this is wrong, how expensive is it to find out?"*
  - Cheap (a test fails, a lint error) → let AI draft it, review quickly.
  - Expensive (customer gets the wrong price, data leaks) → AI can assist, but a human designs it and reviews it like they'd review a stranger's PR.
- Review AI code *more* carefully, not less. It's confident and fast, which is exactly the combination that gets past a tired reviewer.
- Reinforce, don't mandate: this is a judgment call each engineer makes, and the goal is to make it consciously.

**4:15–5:00 — Close**
- We should absolutely use these tools — not using them is leaving real speed on the table.
- But "use it for everything" turns a tool into a crutch. The engineers who get the most out of it are the ones who know when to turn it off.
- Optional soft ask: "If you've got a story — a time it saved you or a time it burned you — I'd genuinely like to hear it. We'll learn more from those than from any policy."

---

## Opening paragraph

> I got asked to talk about whether engineers should be using AI coding assistants for everything, and I'll be honest — my first reaction was that it's the wrong question. Nobody's seriously arguing we should ban Copilot, and nobody serious is arguing it should write our checkout flow unsupervised. The interesting question is in the middle: where does it actually make us faster, and where does it make us *feel* faster while quietly building up problems we'll pay for later? So that's what I want to spend five minutes on — not a verdict, just a way of thinking about it that I've found useful, and that I think applies whether you write code or just depend on the people who do.

---

Two notes:

- **A story would help a lot.** Even a small one — "Copilot wrote a test that caught a bug I'd have missed" or "it generated a discount calculation that was off by one and we caught it in review." If anything surfaces before Friday, drop it into the 1:45–3:15 section. Ask around the team; someone will have one.
- **If you want to trim**, the skills point and the optional closing ask are the first things to cut. The rule-of-thumb section is the part people will remember, so protect that.

Want me to expand this into full speaker notes, or tighten it toward 4 minutes to leave buffer?