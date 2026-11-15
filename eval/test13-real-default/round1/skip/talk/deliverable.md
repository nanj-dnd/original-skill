**Angle**: "Should we use AI for everything" is the wrong question — the useful line isn't which kind of code, it's whether the person who ships a change can explain every line of it.
**Built from**: the task's own wording ("for everything"), no answers. Written without personal details; the only "I" sentences are ones a speaker can say without a specific memory.
**Strongest objection**: "Explain every line" is a standard nobody fully meets for library code or framework internals either, so it's either hypocritical or unenforceable. **Test**: before Friday, pick three recent merged PRs and ask their authors to walk you through one generated function each, cold. If all three can, the standard is realistic; if none can, say that out loud in the talk, because it's your strongest evidence.
**Other direction**: argue the opposite — that worrying about understanding is nostalgia, and the thing to protect is test coverage and review, not comprehension.

---

## Outline (5 minutes)

**0:00 – 0:45 — Reframe the question**
"For everything" sounds like a question about tools. It's a question about accountability. State the line: use the assistant on anything, as long as you can explain what you shipped.

**0:45 – 1:45 — Why "which kind of code" doesn't work as a rule**
The category rule (fine for tests and boilerplate, not for auth or payments) breaks in practice: boring code hides serious bugs, and the "serious" code is often where people need the most help. Categories also go stale every quarter as the tools change. A rule based on the person doesn't.

**1:45 – 3:00 — What "can explain it" actually means**
Three concrete checks, each a sentence:
- You can say why it does it this way and not another way.
- You can name what it would do with a bad input.
- You'd be comfortable being paged for it at 2 a.m. without the assistant open.
Note that this is the same bar we already apply to a human colleague's code at review — it's not a new standard, it's the old one applied to a new source of code.

**3:00 – 4:00 — What this means on Monday**
- Author: generate freely; before you open the PR, read it as if a stranger wrote it, because one did.
- Reviewer: it's fair to ask "walk me through this" on any change, and "the tool wrote it" is not an answer.
- Team: when a generated change causes a problem, the post-mortem question is "did the author understand it," not "was AI used."

**4:00 – 5:00 — Close**
Return to the title. Yes, use it for everything you're willing to own. The tool is allowed to write the code; it isn't allowed to be the one who understands it. Ask the room to try the walk-through test on their own next PR.

---

## Opening paragraph

The question on the slide is whether engineers here should be using AI coding assistants for everything. I want to suggest it's the wrong question, or at least the wrong word. "Everything" makes it sound like a debate about which files the tool is allowed to touch, and I don't think that's where the risk lives. The tool can touch anything. What matters is what happens after it does — whether the person who clicks merge can stand behind the change, explain it to a reviewer, and fix it at two in the morning without the assistant open. So here's the line I'd propose, and it's shorter than a policy: use it for anything you're prepared to own. For the next four minutes I'll try to show why that's a better rule than any list of approved and forbidden code, and what it would change about how we work from Monday.

---

**Before you use it**: the three-PR walk-through test above is worth running — if you get a real result either way, put it in the 1:45 section in place of the abstract checks. If there's an incident or a number from the team, it belongs in the opening instead of the generic "two in the morning" line.

**Distance from the default**: moderate. It drops the default's "boring code yes, sensitive code no" split and the promise/risks/middle structure, replacing them with an accountability line. It still shares the default's measured tone and its "tool, not a replacement for judgment" conclusion, since no answer pushed it further; with your actual stance and a real case it would move more.