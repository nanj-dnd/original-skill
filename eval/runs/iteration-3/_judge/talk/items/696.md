# The Cost Moved: Who Owns AI-Written Code

**Format:** 5 minutes, about 650 spoken words, 4 slides, mostly you talking.
**Goal:** The room backs the ownership rule, and the non-engineers leave knowing why it affects them.

---

## Outline

### 1. Opening: the cost moved (0:00–0:50)
- Read the opening paragraph below.
- Say right away that this is not a debate about whether the tools are good. We use them and we'll keep using them. This talk is about who owns what they write.
- **Slide 1:** "The cost didn't go away. It moved."

### 2. Where the cost went (0:50–1:50)
- Be clear about the upside: new hires ramp about twice as fast. You're glad about that, so say it plainly, once.
- Then the numbers: PR volume is up about 60% since spring. Review time for each senior engineer went from about 4 hours a week to about 11.
- Writing code got cheap. Reading and understanding it didn't. That work now sits mostly with two people, and nobody planned it that way.
- For the non-engineers, put it in their terms: a review is the step where someone checks that a change does what it claims and nothing more. It's the four-eyes check.
- **Slide 2:** Two numbers, large: "PRs +60%" and "4 → 11 hrs/week".

### 3. What happens when nobody fully owns a change (1:50–3:00)
- The August incident, told without a name and without blame:
  - An AI-generated database migration quietly removed a rule that said a certain field must always have a value. In engineering terms, it dropped a NOT NULL constraint.
  - Nothing broke that day. Weeks later the numbers stopped reconciling, and it took three weeks to trace the problem back to that change.
  - When we looked at the change, nobody could fully explain what it did. That includes the person who merged it.
- Frame it as a process gap: "This wasn't one person's mistake. Our process had no step that required someone to understand the change before it shipped. The tool made that gap bigger, but the tool didn't create it."
- **Slide 3:** A short timeline: "Merged → (quiet) → mismatch → 3 weeks to trace".

### 4. Why this matters if you don't write code (3:00–3:50)
- We're a fintech. Our product is numbers that people trust.
- **Ops:** a reconciliation mismatch turns into your manual work and your weeks.
- **Compliance:** for every change that touches money or data, someone has to be able to explain what changed and why. "A tool generated it" is not an answer an auditor accepts.
- **Sales:** customers buy because they trust our numbers. Each quiet error spends some of that trust.
- Light moment (keep it short): "Nobody in compliance has ever accepted 'the spreadsheet did it' as an explanation. We're not going to accept 'the AI did it' either."

### 5. The proposal (3:50–4:40)
- **Slide 4:** The rule, three lines:
  1. The author owns every line they merge, whoever or whatever wrote it.
  2. "The AI wrote it" is never an explanation in a postmortem.
  3. Any PR over 400 changed lines gets split before review.
- Why each one helps:
  - Ownership: if you can't explain it, it isn't ready to merge.
  - The postmortem line: it keeps the focus on understanding, not on finding fault.
  - The 400-line limit: no one can review 1,500 lines properly. Smaller PRs make real review possible again and take weight off the two seniors.
- Name the trade-off honestly: some changes will take a bit longer to land. That's a deliberate choice, and it's cheaper than three weeks of tracing.

### 6. Close: the ask (4:40–5:00)
- Engineers: adopt the rule starting [date / next sprint].
- Everyone else: back it when a change takes a day longer, and ask "who owns this?" whenever something goes wrong.
- Last line: "Use the tools as much as you like. Just make sure every line has an owner."

---

## Opening paragraph

> Since spring, our engineering team has been shipping about 60 percent more code. Part of that is a real win: new engineers now get up to speed about twice as fast as they used to, and I'm glad about it. But the work didn't disappear. It moved. Every line still has to be read by someone who understands it, and right now that's mostly two of our senior engineers. Their review time has gone from about four hours a week to about eleven. So I'm not going to argue today about whether AI coding tools are good or bad. We use them, and we're going to keep using them. I want to talk about who owns the code they write, because in August we learned what it costs when that answer gets fuzzy.
