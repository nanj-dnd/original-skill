# Should Engineers Use AI Coding Assistants for Everything?
**All-hands talk: 5 minutes, about 650–700 spoken words**

**Thesis:** Almost everything, but not quite. Hand the AI the typing. Keep the understanding, the judgment, and the accountability.

---

## Outline

### 1. Opening: the hook and the honest answer (0:00–0:45, ~100 words)
- Start with a show of hands, written out below.
- Reframe the question. The real question is what we stay responsible for, not whether to use AI or avoid it.
- Give the thesis early: *almost* everything.

### 2. Where AI earns its place (0:45–1:45, ~140 words)
- Good uses: boilerplate and scaffolding, first drafts of tests, picking up an unfamiliar API or codebase, mechanical refactors, explaining legacy code, and drafting docs and commit messages.
- Point to make: refusing these tools on principle means working slower for no good reason.
- *[Placeholder: one short, real example from our team where an assistant saved real time. One sentence is enough.]*

### 3. Why "everything" goes too far (1:45–3:00, ~180 words)
Three risks, about 25 seconds each:
1. **Confident wrong answers.** AI code looks right, and that makes it easier to wave through review. Plausible is not the same as correct.
2. **Skill atrophy, especially for early-career engineers.** Most of the learning happens while you struggle with a problem. If you skip that every time, you can't spot the AI's mistakes later.
3. **Ownership and risk.** Watch for secrets or customer data pasted into prompts, dependencies nobody checked, and licensing questions. During an incident at 2 a.m., "the AI wrote it" is no defense. Your name is on the commit.

### 4. A rule of thumb people can remember (3:00–4:15, ~170 words)
- **The line to repeat: "Delegate the typing, not the understanding."**
- Three habits that follow from it:
  1. **If you can't explain it in code review, it doesn't ship.** That goes for AI-written lines too.
  2. **AI drafts, humans decide.** People make the final call on architecture, security boundaries, data handling, and anything else that's hard to reverse.
  3. **Early-career engineers: try it yourself first, then compare.** Use the assistant as a second opinion while you're still building intuition.
- Mention the guardrails: which tools are approved and what code or data may go into them. *[Placeholder: confirm current policy with Security/IT before Friday.]*

### 5. Close: callback and the ask (4:15–5:00, ~90 words)
- Call back to the raised hands: "Next time you accept a suggestion, make sure you could have written it, or at least defend it."
- One concrete ask for the week: in your next PR, flag one AI-assisted change and say how you checked it.
- End on the thesis: use it for almost everything, and stay the engineer in charge.

---

## Opening Paragraph

> Quick show of hands: who here has used an AI coding assistant in the last week? *[pause]* Keep your hand up if you've accepted a suggestion you didn't fully read. *[pause]* Yeah, me too. That second hand is what I want to talk about for the next five minutes. I was asked whether engineers should use AI assistants for everything, and my honest answer is: almost. These tools have earned a spot in nearly every part of how we build software, and anyone telling you to avoid them is asking you to work slower for no good reason. But "almost everything" and "everything" aren't the same, and the gap between them is the part of the job that's still ours: understanding the code, making the judgment calls, and owning the commit.

*Delivery note: if many people are joining remotely, swap the hands for "think about the last time you…" and keep the pauses. The paragraph runs about 45 seconds at a relaxed pace.*
