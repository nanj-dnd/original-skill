**Angle**: The "whether" question is already settled (people use these tools, nobody uses them for literally everything, and you can't enforce a line either way); the thing that actually predicts bad outcomes is code getting merged that no human on the team understands, so the ask is one review norm: if you submit it, you can explain it.
**Built from**: 1c (it's about how, not whether), 3a (engineers, one behaviour change), 4a (blunt, first person), and your "I use Copilot sometimes, it's fine" as the honest opening stance.
**Strongest objection**: "You can explain it" is just "use judgment" with a slogan on it; norms nobody enforces decay in a month, and some teams genuinely do need a hard line (auth, billing, infra) that this framing dodges. **Test**: before Friday, pick three recently merged PRs from your team and ask the authors to walk you through one chunk each. If someone can't, you've got your example and the talk is justified. If all three can, either the problem is smaller than the framing implies, or the ask needs to be sharper than "explain it."
**Other direction**: Take the 1a position outright — the job has shifted from writing code to directing and reviewing it — and make the five minutes about what that does to how we hire, level, and review, with "ownership" as a consequence rather than the headline.

---

## Outline (5 min, ~700 words spoken)

**0:00–0:45 — Kill the question** (the opening paragraph below)
Answer "should we use it for everything" in a sentence, say where you personally sit, and replace it with the real question: what happens between code appearing in the editor and code getting merged.

**0:45–1:45 — Why "whether" goes nowhere**
- You can't enforce a ban or a mandate. It's in the editor. People will use it or they won't, and you won't know which.
- Even if you could, "how much AI" isn't the variable that predicts trouble. The variable is *unread code*: code merged that nobody on the team actually understands. That existed long before AI (pasted from StackOverflow, lifted from a library's example). AI just made it fast and cheap, so there's a lot more of it.

**1:45–3:00 — The actual problem: ownership blur**
- When you type the code, you're the author. When it's generated, there's a pull toward being the *approver* of your own PR: you read it like a reviewer, it looks plausible, you ship it.
- Plausible is the failure mode. Generated code is extremely good at looking right. So the PR gets two skimmers and zero readers.
- Three shapes this takes (recognisable without naming anyone): the test that asserts what the code does rather than what it should do; the helper that reimplements something we already have in the repo; the error handling that catches and swallows.

**3:00–4:15 — The ask: one norm, from Monday**
- **If you submit it, you can explain it.** Every line in your PR is yours, however it got there.
- Reviewers get explicit licence to say "walk me through this" on any chunk. "The AI wrote it" is not an answer, the same way "I got it off StackOverflow" was never an answer.
- Not asking for disclosure labels on PRs; I don't care how it was produced. I care that the author is the author.
- It cuts both ways: if you can explain it and it's good, nobody cares that a model wrote 90% of it. Use the thing as much as you want.

**4:15–5:00 — Close**
- What this buys us: AI use probably goes *up*, because people stop being quietly embarrassed about it; junk goes *down*, because pasting something you don't understand now costs you a conversation.
- One-line restatement: *the question was never whether. It's whether somebody owns it.*
- Open the door: "If you think this is unenforceable, come find me after. I'd rather hear it than have you nod and ignore it."

## Opening paragraph

The slot I was given is called "should engineers be using AI coding assistants for everything." I'll answer that in one sentence so we can move on: no, and nobody is, and nobody's going to stop using them either. I use Copilot sometimes. It's fine. Some of you use it for most of what you write, some of you have it switched off, and I'm not here to move anyone from one of those camps to the other. The argument about *whether* is over and it ended in a draw. The thing that actually decides whether these tools make us better or quietly make the codebase worse is what happens between the moment code shows up in your editor and the moment it gets merged. That's not a tooling question. It's a process question, and it's the only one in this whole debate we can actually do something about on Monday.

---

**Before you use it**: No figures are in here on purpose; you had none and the argument doesn't need them. The three failure shapes in section 3 are generic, and that's the thin spot — a single real instance from your team ("last month we merged a helper that already existed in `utils/`") would do more than the whole section. Run the three-PR test above; it will either give you that example or tell you to soften the ask. If your team has a written review guideline, decide before Friday whether the norm goes in there, otherwise it's a talk and not a change.

**Distance from the default**: The default's claim ("use it for some tasks, not others") is gone, replaced by "the whether question is settled; what matters is whether a human owns the merged code" — that came from 1c. 3a turned the ending from "use judgment" into one enforceable norm. 4a put it in your voice rather than a presenter's. Your answer to 2 is why the examples stay generic; that's the one place the piece is closer to the default than I'd like.

Want me to export this run (task, default, your answers, angle, outline, opening, notes) as a Markdown file?