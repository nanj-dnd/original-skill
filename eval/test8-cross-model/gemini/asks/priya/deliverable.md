**Opening Paragraph**

Let’s just state the obvious right up front: our engineering team is using AI to write code, and I am not here today to announce a ban or pretend we can put that genie back in the bottle. It is an incredibly powerful tool, and everyone is already using it. But here is the reality check: while AI has made *writing* code incredibly fast and cheap, it has quietly shifted our biggest operational cost to something else entirely—reading it. Today, I want to share a quick look at what that is doing to our team, and introduce a few new guardrails so we can keep moving fast without breaking our own people.

**5-Minute Talk Outline**

**Minute 1: The Elephant in the Room (Context)**

* **Deliver the opening paragraph.**
* **Translate for the room:** Briefly explain to sales, ops, and compliance what this looks like in practice. AI acts like a super-powered autocomplete, letting an engineer generate chunks of a feature in seconds instead of hours.
* **The Thesis:** We are producing code faster than ever, but that code still requires human verification before it hits our customers.

**Minute 2: The Hidden Bottleneck (The Data)**

* **The PR Surge:** Explain what a Pull Request (PR) is—a proposal to merge new code into our product. Since spring, our PR volume is up by roughly 60%.
* **The Human Toll:** AI doesn't review code; our senior engineers do. Because of this massive spike in volume, our two senior engineers have gone from spending ~4 hours a week reviewing code to ~11 hours a week each.
* **The Risk:** That is a quarter of their week lost just to reading AI-generated output. It is unsustainable and creates a massive bottleneck for the whole company.

**Minute 3: The Mindset Shift (The "Why")**

* **The Economic Shift:** The fundamental cost of software development on our team has moved from *generation* to *verification*.
* **The Goal:** We want to keep the momentum and productivity gains that AI gives us, but we have to protect our senior talent from becoming full-time AI proofreaders. We need a system that forces the original author to do the heavy lifting of quality control.

**Minute 4: The Three Guardrails (The "How")**

* **Rule 1: You own every line.** It doesn't matter if you typed it character-by-character or hit 'Tab' to let an AI generate it. If you commit it, it is your code.
* **Rule 2: No AI excuses.** If a bug takes down the system and we are doing a postmortem, "the AI wrote it" is not a valid defense. The AI is just a tool; the engineer is the decision-maker.
* **Rule 3: The 400-line limit.** If an AI writes a mountain of code in ten seconds, you cannot dump that mountain on a senior engineer's desk. Any PR over 400 changed lines will now be rejected and must be split into readable chunks.

**Minute 5: The Takeaway**

* **Reassurance for the org:** We are embracing the future, but we are doing it with discipline. These guardrails ensure our product remains stable and our engineering team stays healthy.
* **Call to action for engineering:** Check your PR sizes starting Monday.
* **Wrap up / Transition** to the next agenda item.