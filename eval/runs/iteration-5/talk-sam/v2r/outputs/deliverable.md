# AI coding assistants: where judgment stops
*Tech division meeting, 5 minutes*

## Outline

**1. Opening: the near-miss (about 30s)**
- The moment everyone recognises: stuck on a bug, the prod log is right there, the assistant is open, and one paste would get you an answer.
- People here have come close to that paste more than once. No names and no blame. It happens because it's the fastest thing to do.

**2. The honest middle (about 1 min)**
- Should we use these tools for everything? No blanket rule on tasks. For most work the answer is to use your judgment.
- Judge them the way we judge anything else: does it get us there faster *without* costing quality? Count the bugs, the review load and the rework, not just the time saved.
- You own what you ship. AI-written code gets reviewed like any other code.

**3. Where judgment stops (about 1 min, the core)**
- One thing isn't up to judgment, and it's not about which task you're doing. It's about what you put *into* the tool.
- Say it slowly, once: **No customer data. No production logs. In any external tool.**
- Why this one is absolute when everything else is judgment: once it's pasted, it has left our hands and you can't take it back. Compliance already forbids it. This is that rule, said out loud.
- Be honest about the cost: sometimes this will be slower. That's the one trade-off we don't make for speed.

**4. What to do instead (about 1 min)**
- Use redacted or made-up sample data.
- If you're not sure whether something counts, ask the compliance team first.
- [Before Friday: check with compliance whether there's an approved internal tool. If there is, name it here and make sure "any external tool" still holds.]

**5. Close (about 30s)**
- Back to the opening moment: the log is right there, and this time you know where the line is.
- Repeat it word for word: **No customer data. No production logs. In any external tool.**

## Opening paragraph

You know the moment. You're stuck on a bug that only shows up in production, the log that explains it is sitting in your other window, and the assistant is open right next to it. One paste and you'd probably have your answer in thirty seconds. More than once, people in this division have been that one paste away. Not because anyone was careless, but because it's the fastest thing to do. So I'm not here to tell you to stop using these tools. For most of what we do, the right answer is to use your judgment. I'm here to talk about the one place where judgment isn't the answer.
