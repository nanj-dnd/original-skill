Here's a draft. I've assumed a "yes, by default — but not for *everything*" stance since that's the position most engineering orgs land on in practice. If you want to argue a harder line in either direction, tell me and I'll re-angle it.

---

## Outline (5 min ≈ 650–700 spoken words)

**0:00 – 0:45 — Open with the tension**
- The honest framing: the question isn't "should we use them," it's "where does the default flip."
- Set up the one-sentence thesis: *AI assistants should be the default for most code we write, and explicitly *not* the default for a short, specific list.*

**0:45 – 1:45 — Where they clearly win (the "default yes" zone)**
- Boilerplate, glue code, tests for existing behavior, migrations, one-off scripts, reading unfamiliar code.
- Concrete number if you have one (e.g. "the X team cut PR cycle time by ~Y%"). If you don't, use a short anecdote from your own week instead — a specific story beats a vague stat.
- Key point: the cost of being wrong here is low and the review catches it.

**1:45 – 3:00 — Where "everything" breaks down (the "default no" zone)**
- Security-sensitive paths (auth, payments, permissions): the model writes plausible code, and plausible is exactly what you don't want here.
- Core architectural decisions: the assistant optimizes for *a* working answer, not *our* constraints.
- Anything where the engineer can't evaluate the output — if you can't review it, you can't own it.
- The real risk isn't bad code, it's *unowned* code: nobody can explain why it's there.

**3:00 – 4:00 — The actual proposal (keep this concrete)**
- Three norms, not a policy doc:
  1. Use it freely; you're still the author of record.
  2. For the "default no" list, you can still use it — but you say so in the PR, and review scrutiny goes up.
  3. If you can't explain a line, delete it and rewrite it.
- Mention who owns the "default no" list and that it'll change as tools improve.

**4:00 – 5:00 — Close**
- Reframe: the tools are changing what "being a good engineer" means — less typing, more judgment.
- One-line call to action (e.g. "try it on something you'd normally avoid, and tell us what broke").
- Stop. Don't do Q&A inside your 5 minutes; offer a channel/thread instead.

---

## Opening paragraph

> "I want to start by admitting the question in the title is a bit of a trap. 'Should engineers use AI coding assistants for everything?' — the honest answer is obviously no, and if I stopped there you'd have four and a half minutes back. But the *interesting* question, the one we actually have to answer as a team, is: where does the default flip? For most of the code we write, I think the default should now be 'yes, use it, and you'd better have a reason if you didn't.' And for a short, specific list of things, the default should be 'no, and you'd better have a reason if you did.' I want to spend the next few minutes telling you what's on each side of that line, why, and the three norms I'd like us to adopt so that we get the speed without losing the thing that actually makes us good at this job — knowing why the code we ship is there."

---

A couple of notes:
- The opening is ~160 words, about 60–70 seconds spoken at a normal pace. If you want to get to the content faster, cut the "four and a half minutes back" joke.
- The talk is much stronger if section 2 has one real number or story from your own org. Swap my placeholder for whatever you've actually got.
- If your audience is mixed (non-engineers too), the "unowned code" line in section 3 is the one non-engineers will remember — consider making it the closing line instead.