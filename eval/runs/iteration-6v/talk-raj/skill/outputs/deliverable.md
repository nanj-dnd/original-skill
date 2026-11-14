# Use it a lot. Now let's talk about "review everything."
*5-minute all-hands talk, by the QA lead, for engineers and PMs*

## Outline

**1. Opening: the line everyone nods at (0:00–0:45)**
- I lead QA, and I'm not here to tell you to stop. Use these tools, a lot.
- Every conversation about AI assistants ends with "just review everything." Everyone nods. I want to spend five minutes on that line, because review is my team's job.

**2. Where I agree (0:45–1:30)**
- Keep this short and genuine, so the room knows this isn't an anti-AI talk.
- [your example here: one place you've seen it clearly help, such as test scaffolding, boilerplate or a faster first draft. Or cut this to one sentence.]

**3. AI-written code fails differently (1:30–2:30)**
- Bad human code often *looks* bad. Generated code usually reads clean, compiles and passes the happy path. The mistake is in an assumption, not in the syntax.
- Code that looks right is harder to review than code that looks wrong. Reviewers skim what reads well.
- [your example here: a kind of bug you've seen get through, or leave as a general point. Don't name a team.]

**4. The cost doesn't vanish, it moves (2:30–3:30)**
- Writing code got cheaper. Reading it didn't. If changes come faster and bigger, review becomes the bottleneck, whether or not anyone plans for it.
- Whatever review misses shows up later: in QA, on call, with customers. That's still a cost, just one nobody budgeted.
- For PMs: "the code is done" sooner isn't the same as "the feature is done" sooner. Ask where the time went.

**5. What "review everything" should actually mean (3:30–4:30)**
These are three questions, not a policy:
- Can the author explain every line they're merging, including the ones they didn't type?
- Is there a test that would have failed if this were wrong?
- When it breaks, who owns it? "The AI wrote it" isn't an answer.

**6. Close: start the conversation (4:30–5:00)**
- No new rule today.
- Engineers: where do you trust it least, and are we reviewing hardest there?
- PMs: are we counting "done" at merge or in production?
- My door's open. Come tell QA what you're seeing.

## Opening paragraph

> I'm [your name], and I lead QA. So you might expect me to be up here telling you to stop using AI coding assistants. I'm not. Use them, and use them a lot. But every conversation about these tools ends with the same line: "just make sure you review everything." Everyone nods, and we move on. For the next five minutes I don't want to move on. Review isn't a footnote. It's where the work goes when writing code gets cheap, and a lot of it ends up with my team. So let's talk about what "review everything" actually costs, and who's paying for it.
