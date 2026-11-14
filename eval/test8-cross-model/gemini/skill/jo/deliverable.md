**Angle**: AI coding assistants are handy for speeding up the boring stuff, but you still own the PR and need to verify the code because the AI doesn't understand our system's larger context.
**Built from**: Your choice of a balanced stance (1c) and a casual, peer-to-peer tone (3a), working without a forced anecdote (2).
**Strongest objection**: AI is improving so rapidly that insisting on manual human review for every line of boilerplate is already becoming a waste of engineering time.
**Test**: Ask your team if they've ever spent more time debugging a subtle AI-generated hallucination than it would have taken to write the code from scratch.
**Other direction**: Push everyone to use AI for *every* keystroke to explicitly find its breaking points.

---

**Opening Paragraph**

Hey everyone. I'm going to take five minutes today to talk about something most of us are already doing: using Copilot and other AI assistants to write code. Look, I use it myself, and it's fine. It's genuinely great for knocking out boilerplate or remembering syntax you haven't used in a month. But there's a growing temptation to just let it write *everything*, and that’s where things get a little sketchy. The autocomplete often looks incredibly convincing, but it doesn't actually know how our systems talk to each other. So today, I just want to quickly cover how we can keep using these tools to move faster, without accidentally merging garbage into production.

**Outline (5 Minutes)**

* **The Good Stuff (1 min):** Where Copilot actually shines. Taking the friction out of the grunt work (repetitive blocks, standard tests, standard regex) so we can focus on the hard problems.
* **The Danger Zone (2 mins):** The "Confidence Illusion." The AI doesn't know our architecture, our edge cases, or the weird tech debt we're working around. It writes code that *compiles* and *looks* right, but can easily introduce subtle logic bugs or miss the broader context of what we're building.
* **The Rule of Thumb (1.5 mins):** You own the PR, not the AI. If an assistant writes it, you still have to read it, understand it, and be able to defend it in code review. Treating AI as a junior dev who occasionally lies to you.
* **Takeaway (30 sec):** Keep using it to skip the boring typing. But don't turn your brain off when the autocomplete pops up.

---

**Before you use it:** Even though you didn't have a big story, try to notice if Copilot suggests something slightly goofy to you between now and next Friday. Dropping in a tiny, 10-second real example of a bad suggestion ("yesterday it tried to import a library we deprecated three years ago") will make the whole talk land perfectly.

**Distance from the default:** The core argument is almost identical to the default, but the tone shifted completely—moving away from a rigid management policy into practical, peer-level advice because of your choices.

Let me know if you want me to export this entire run (the default, your answers, the angle, and the piece) as a Markdown file or PDF for your records.