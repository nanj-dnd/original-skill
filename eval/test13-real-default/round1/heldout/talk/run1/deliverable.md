The Python at the bottom of your message looks like a benchmark harness that got pasted in by accident — I'm ignoring it and answering the talk request. Let me know if you actually wanted something done with it.

Five minutes is roughly 650 words spoken, so this is built for one clear position, three supporting points, and a landing. The position I'd recommend: **no, not for everything — but the line isn't "simple vs. hard," it's "can you verify it faster than you could write it."** That's a framing an all-hands audience (including non-engineers) can follow, and it avoids both the hype and the grumpy-refusenik posture.

---

## Outline

**0:00–0:40 — Open with the real question**
- Nobody's actually debating "should we use AI assistants." We already do. The question is whether there's anything we *shouldn't* hand to them.
- Stake the claim: the right test isn't how hard the task is, it's whether you can check the output faster than you could have produced it.

**0:40–1:40 — Where "everything" is correct (and we should lean in harder)**
- Boilerplate, tests for existing behavior, migrations, config, translating between formats, "what does this error mean"
- Common trait: verification is cheap. Run the tests, diff the output, read ten lines. If it's wrong, you know in seconds.
- One concrete internal example if you have it (a PR that would've taken an afternoon and took 20 minutes). Specific beats abstract here.

**1:40–2:50 — Where "everything" breaks down**
- Code whose correctness you can't eyeball: concurrency, auth boundaries, anything touching money or data deletion, subtle performance paths
- The failure mode isn't that the AI is bad — it's that the output is *plausible*. Plausible-and-wrong is more expensive than obviously-wrong, because it sails through review.
- Second cost: understanding. If you accept a 400-line change you didn't write and don't fully follow, you now own a system you can't debug at 2am. The incident cost lands later and lands on someone else.

**2:50–3:50 — The actual rule: match your effort to your ability to verify**
- Cheap to verify → let the assistant drive, you review the diff
- Expensive to verify → you drive, the assistant helps (explains, drafts, suggests, spots what you missed)
- Corollary: if you can't explain a change in the PR description, you're not done with it
- This isn't a policy, it's a habit. Policies get gamed; habits scale.

**3:50–4:30 — What this means for us specifically**
- One or two concrete asks: e.g. "PR descriptions say what was AI-generated and what you verified," or "we're measuring incident rate on AI-heavy changes for the next quarter," or whatever's true for your org
- Reassure non-engineers: this is about shipping *faster and safer*, not slower

**4:30–5:00 — Land it**
- Callback to the opening: the tool isn't the risk. Unverified trust is the risk, and that was true before AI too.
- Close line (something like): "Use it for everything you can check. Think hard about everything you can't."

---

## Opening paragraph

> I want to start by admitting the title of this talk is a bit of a fake question. Should engineers use AI coding assistants for everything? We already use them for almost everything — I checked, and about seventy percent of the PRs merged last month had assistant-generated code in them somewhere. So the honest version of the question isn't *whether*. It's *whether there's anything left that we shouldn't hand over*. And I think there is, but the line isn't where most people put it. It's not "easy tasks yes, hard tasks no." The line is this: can you verify what came back faster than you could have written it yourself? If yes, let the tool drive. If no, you drive. That one test explains almost every good and bad outcome I've seen with these tools in the last two years, and I want to spend the next four minutes convincing you of it.

Swap in your real numbers for the "seventy percent" line (or cut it if you don't have one — the paragraph works without it, it's just stronger with a concrete hook).

A couple of things worth deciding before Friday:

1. **Do you have a real internal example for each side?** One win and one near-miss, each in two sentences, will do more than any amount of framing. If you tell me a bit about the codebase I can help you pick which ones land.
2. **Is this a "here's how I think" talk or a "here's what we're changing" talk?** The outline above hedges toward the former. If leadership expects an actual policy ask at the end, section 5 needs to be sharper and I'd pull 20 seconds from section 2 to pay for it.