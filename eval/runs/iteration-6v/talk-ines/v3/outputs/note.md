**Angle:** "AI for everything" matters less than whether "be careful" is a check anyone can see. Our AI-written checkout form passed every check we had, and the person who caught the problem was a blind customer.

**Built from:** 2 (the checkout form, two weeks, hearing it from support) is the spine. 4 (product designer, asked because of "opinions about quality") gives you the opening line and the reason you can speak from outside engineering. 3 (whole company) is why section 2 explains what a label is and section 4 speaks to non-engineers directly. 1 ("fine, probably, as long as people are careful") is the position the talk tests. Your own instinct and your own story pull against each other, and the talk uses that pull instead of hiding it. 5 ("not sure yet") left the ending open, so I chose it (see below).

**Strongest objection:** Hand-written code ships accessibility bugs too. If the form would have gone out without labels whether or not an assistant wrote it, this is a story about review and feedback, not about AI, and an engineer in the room will say so. The talk partly concedes this already (section 2: "nothing we had was looking for this"). It needs to survive the follow-up: "So why is this in a talk about AI?" The answer it gives is volume: more finished-looking work, produced faster, with the checking left undefined.

**Test:** Before Friday, ask an engineer two things. Did the form go through code review, and did that review cover accessibility at all? Do other, hand-written forms in the product have proper labels? If they're missing too, shift the weight further toward "careful has to be defined" and away from AI.

**Other directions:**
- Pro-adoption with tooling: use assistants for everything, but make accessibility checks automatic so nobody has to remember to be careful.
- Drop the AI framing and give a talk only about the two weeks: how customer problems reach the people who built the thing.

---

## Before you use it

- **No statistics or studies are cited**, so there's nothing to fact-check beyond your own story.
- **Confirm the details as you'll say them:** that the form was written with an AI assistant, that it was last quarter, that it took two weeks, and that the customer contacted support by email. The talk leans on all four.
- **Check with engineering before naming the incident.** The talk is built so it doesn't read as blame, but a team hearing about its bug for the first time at an all-hands will hear blame anyway. A heads-up to the engineering lead costs nothing.
- **The ending was my choice, since you weren't sure.** Section 5 asks for two things: a written definition of "careful" for customer-facing work, and customer problems reaching the building team within the week. If you'd rather close on one ask, or on a pilot (for example, a screen-reader check on the next three forms that ship), swap it in. The close in section 6 works with any of them.
- **Details that would make it stronger, if you have them:** in section 2, what the customer actually couldn't do (could they finish checking out at all?). In section 4, why the fix took two weeks, if you know: was it hard to fix, or slow to reach the right person? That answer decides whether section 4 is about the code or about the chain. And in section 5, whether design will commit to anything itself, such as reviewing forms with a screen reader. It's stronger if you ask for something you're also offering.

Because this is a talk, I'd normally check the angle with you before writing it out. If you want it redirected, or have a line you want worked in, say so and I'll rework it.

---

## Distance from the default

- The default opens on a hook question and a vendor statistic. This opens on a real incident at your company with a real cost (two weeks) and a real messenger (support, not engineering). That comes from answer 2.
- The default speaks as a neutral expert to engineers. This speaks as a designer asked to talk about quality, to a mostly non-technical room: it explains what a label is and tells support, sales and ops they're already part of how the company checks software. That comes from answers 3 and 4.
- The default's structure is pros, then cons, then guidelines. This one takes your own position ("fine if careful"), tests it against your own story, and turns "careful" into the thing to define. That comes from answers 1 and 2 pulling against each other.
- The default ends on best practices and "tool, not replacement." This ends on two specific asks and a callback to the customer who found the bug. The ending is mine, not yours (answer 5 was open).
- **What did not move:** the underlying stance is still close to the default's middle ground: use the tools, but check the output. You told me that's roughly where you are, so the talk doesn't fake a contrarian position. What's different is what it stands on and who it speaks to, not the verdict.
