Here's a draft. I leaned into your QA angle since it gives you a natural, credible "it depends" position — the tools are great, but they shift the work rather than remove it. Adjust anything that doesn't sound like you.

---

## Outline (~5 minutes)

**1. Opening (30 sec)**
- Frame the question: not "should we use AI assistants" (we already do) but "how much should we lean on them"
- Your answer upfront: lean on them a lot — but know what you're leaning on

**2. What they're genuinely good at (60 sec)**
- Boilerplate, scaffolding, tests, glue code, unfamiliar APIs
- Getting unstuck, first drafts, "what does this error mean"
- The time savings are real; no need to be precious about writing every line by hand

**3. Where it gets risky — the QA view (90 sec)**
- AI code is confident and plausible, which is exactly the kind of code that slips through review
- The failure mode isn't obvious bugs — it's subtle ones: wrong edge case, outdated API, a test that passes but doesn't test anything
- The bottleneck moves from *writing* code to *understanding and verifying* it. If the tool writes it in 10 seconds and you review it in 10 seconds, you haven't saved time — you've deferred the cost to QA or prod

**4. A simple rule of thumb (60 sec)**
- Lean on it as hard as you want, as long as you can still explain the code you're shipping
- If you can't explain it, you can't review it — and neither can QA, not really
- Generated tests need the same scrutiny as generated code (maybe more)

**5. Close + discussion prompt (30 sec)**
- We don't have a policy, and I'm not proposing one today
- But worth talking about: what's our norm for reviewing AI-generated code? Should PRs flag it? Do we even need to know?
- Invite reactions

---

## Opening paragraph

> Most of us are already using AI coding assistants, so I'm not here to ask whether we should. The more useful question is how much we should lean on them — and I'll give you my answer upfront: a lot, honestly. They save real time, and I don't think anyone should feel like they need to hand-write code that a tool can scaffold in seconds. But I'm coming at this from QA, and from where I sit, the interesting thing isn't how fast the code gets written. It's what happens after. AI-generated code tends to look right — it's confident, it's clean, it compiles — and that's precisely the kind of code that gets a quick skim in review and then surprises us later. So the question I'd put to the room isn't "use it or don't." It's: when the tool writes the code, who actually understands it before it ships?

---

A couple of optional touches if you want them:
- If there's been a real incident (even a small one) where AI-generated code caused a bug, dropping it into section 3 would make the talk much stickier.
- If you'd rather not sound like QA is scolding engineering, you could soften section 4 to "this is a habit I'd want for myself" framing.