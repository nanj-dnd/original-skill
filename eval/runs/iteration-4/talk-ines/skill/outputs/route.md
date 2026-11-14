**Path: specific answers, so I'm building directly.** Your answer to 2 is a real case I couldn't have guessed: an AI-written checkout form, no screen-reader labels, a blind customer, two weeks to fix, and you heard about it from support. Your answer to 4 gives a real stake: a product designer asked to speak because you "have opinions about quality". Your position (1) is close to the default and you said you're unsure, so I'm building from the case, not from a contrarian stance you don't hold.

**Angle:** "Be careful" only covers the things you think to check. Last quarter nobody thought to check for a customer who can't see the screen, and engineering didn't hear about it; support did. So the question for the whole company isn't "AI for everything, yes or no." It's "who would notice what it leaves out?"

**Built from:** 2 (the checkout form, and the fact that support found it), 4 (a designer's view of quality, from outside engineering), 3 (the whole company, so the talk gives support, sales and ops a part to play instead of being an engineers' best-practice list), and 1, used as a tension. Your "fine as long as people are careful" is the view most of the room holds. The talk takes it seriously, then shows what "careful" missed.

**Strongest objection:** Hand-written forms ship without labels all the time. Accessibility gaps were around long before AI, so this may not be an AI story at all, and the engineers in the room may hear it as blame. The answer the talk has to earn is that you're not saying AI is worse than people. You're saying it lets us ship more code, faster, so whatever we don't check for grows at the same speed. **Test before you use it:** confirm the form really was AI-written and that review didn't flag the missing labels, check the details (two weeks; the customer emailed support), and ask the team involved whether they're OK with it being told at an all-hands. Keep the customer anonymous.

**Other directions:**
- **The feedback loop:** the real failure is that quality news reached engineering second-hand, through support. Make it a talk about how problems travel inside the company, with AI as the background.
- **"Careful" made concrete:** name the two or three things an assistant won't raise unless you ask (who can't use this? what happens when it fails? what did we not test?) and end on one practice.

**Before I write, three things to settle (reply like `A2 B: yes C: <words>`):**

- **A. The ending.** You said 5 was "not sure yet". Pick one, or give your own:
  1. A small, concrete ask of engineering: any AI-written UI gets a screen-reader check before it ships.
  2. An ask of everyone: when a customer tells you something is broken, it reaches the team who built it that week, not two weeks later.
  3. A question to take away, with no rule attached: "Who would notice?"
  4. Your own words.
- **B. Can you tell the story on stage**, anonymised (no customer name, no engineer named)? Yes / no / only parts of it.
- **C. Anything to work in:** a line you want to say, what the support email actually said (paraphrased is fine), how the fix went, or a tone (wry, serious, gentle).

---

**Your reply:** A: not sure, whichever works best. B: not sure, would have to check. C: nothing to add.

**Ending chosen (by me, since A was open):** option 2 as the one ask, with option 3, "Who would notice?", as the closing line. Why: you're not sure about a position, so a rule for engineering (option 1) would have you arguing for a policy you don't hold. The room is the whole company, so the ask is one anyone can act on. And the thing that actually went wrong in your story was the route the news took, through support. I kept the screen-reader check as an optional line for the engineers.

**Story:** anonymised (no customer name, no engineer or team named), with [CHECK] markers in the outline. Before Friday, confirm that the form was AI-written, that code review didn't flag it, the two weeks, and that the team is OK with it being told.

**Details I added, please check:**
- "It looked fine": I inferred this from the fact that it shipped.
- "A row of boxes with no names": my description of what a screen reader user meets on unlabelled fields. It's broadly how fields without labels come across, but it isn't something you told me.

No statistics are cited.

(Deliverable: deliverable.md)

**Distance from the default**
- Built on one real incident from your company instead of generic boilerplate examples and a vendor statistic (answer 2).
- Quality here means "who gets left out," not bugs and security, because it's told by a product designer from outside engineering (answer 4).
- It gives support and the rest of the company a part to play, because the room is the whole company, not engineers (answer 3).
- It swaps "AI for everything, yes or no" for "who would notice?" That comes from the tension between "fine if careful" (answer 1) and what careful actually missed (answer 2).
- What did not move: the position itself is still close to the default ("probably fine if you're careful"), and the ending was my choice, not yours.
