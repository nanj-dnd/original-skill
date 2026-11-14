# AI Coding Assistants: Faster, Not Better
*5-minute talk, tech division all-hands*

## Opening paragraph

"Hi, I'm [name]. I've been a backend dev here for about four years, and my manager asked me to answer one question: should we be using AI coding assistants for everything? The short answer is no, but we should be using them for more than some of you probably are. Here's the whole talk in one line: use it for the boring stuff, check everything it gives you, and never give it customer data or production logs. That's it. You can go now. Please don't, though, my manager's watching. Let me spend the next four minutes on why."

---

## Outline

**1. Opening (0:00–0:40)**
- The paragraph above.
- **Slide 1:** the title, plus the one-line summary: *Use it for the boring stuff. Check everything. Never give it customer data or prod logs.*

**2. Where it actually helps (0:40–1:40)**
- **Boilerplate:** config, DTOs, wiring, the code you've written a hundred times and still have to type out.
- **Tests:** scaffolding, edge cases you might not think of, filling in the repetitive setup.
- **APIs you don't know yet:** getting a working first example in minutes instead of an hour in the docs.
- Point to make: this is where it saves real time, so use it there.
- **Slide 2:** three words, *Boilerplate / Tests / Unfamiliar APIs*

**3. The catch: it makes you faster, not better (1:40–2:50)**
- It doesn't know our codebase, our conventions, or why something was built the way it was. It sounds confident whether it's right or wrong.
- Every line it writes is your code once you commit it. Review it like a PR from someone who's never seen our system.
- Tests: check they're testing the right thing, not just passing.
- Unfamiliar APIs: this is the tricky one. It's exactly where it's most useful *and* where you're least able to spot a mistake, like a method that doesn't exist or a deprecated pattern. Check its output against the real docs.
- Line to land: *"If you couldn't have written it, you need to be able to explain it before you ship it."*
- **Slide 3:** *Faster, not better. You own what you commit.*

**4. The line (2:50–3:50): about a minute, serious tone, no jokes**
- Change your tone here on purpose. Slow down.
- State the rule plainly: **customer data and production logs do not go into any external AI tool. Ever.**
- Say up front: this isn't a new policy. It's the existing compliance rule. I'm just saying it out loud because it's easy to nearly break.
- What "nearly" looks like: you're debugging something under pressure, you have a log line or a customer record in front of you, and pasting it into the assistant to ask what's wrong feels like the obvious next step. Plenty of us have come close to doing exactly that.
- What to do instead: describe the problem in your own words, or write a made-up example with the same shape. If you're not sure whether something counts, don't paste it. Ask first.
- Name who to ask (the risk and compliance folks in the room, or the right channel).
- **Slide 4:** the rule alone, in large text, on a plain background. Nothing else on the slide.

**5. Close (3:50–4:30)**
- Come back to the three-part summary:
  1. Use it for boilerplate, tests, and unfamiliar APIs.
  2. Review everything. It makes you faster, not better.
  3. Customer data and prod logs never go in.
- Closing line, something like: *"Use it to get to a first draft faster. The judgment part is still our job."*
- **Slide 5:** the same three points as slide 1.

**6. Buffer / questions (4:30–5:00)**
- Leave about 30 seconds. Five-minute slots always run over.

---

## Notes for prep

- **Check the wording of the rule with compliance before Friday.** There are compliance people in the audience, so the way you state it in section 4 should match the policy exactly, especially what counts as "customer data" and whether redacted or trimmed logs are also off-limits. If they're happy for you to name them as the contact, do that.
- **Keep the tone change in section 4 clear.** The light tone in the opening and the serious tone here work because they contrast. Don't soften the rule with a joke on either side of it.
- **Length:** five minutes is about 650–700 spoken words. Sections 2 and 3 are the easiest to trim if a run-through goes long. Don't cut section 4.
- **Optional:** if anyone on the team has a quick, harmless story of the assistant confidently getting something wrong, it would fit nicely in section 3. Get their OK first.
