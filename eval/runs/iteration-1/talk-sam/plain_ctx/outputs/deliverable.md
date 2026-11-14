# AI Coding Assistants: Use Your Judgment, Except for One Hard Line

**Tech division all-hands, next Friday · 5 minutes · about 80 people (mostly engineers, plus risk and compliance)**

**The one thing to remember:** No customer data and no production logs go into any external tool.

---

## Opening paragraph (about 45 seconds)

> I was asked whether we should be using AI coding assistants for everything. My answer is no, but probably not for the reason you'd guess. For a lot of our work these tools make us faster, and I want us to use them. For some work the speed isn't worth it, because we pay it back later in bugs, review load and rework. You're the best people to judge where that point is, so I'm not going to give you a list of approved tasks. One thing isn't up to judgment, though, and I'm spending a full minute of my five on it because people here keep coming close to getting it wrong: **no customer data and no production logs go into any external tool.** That means not once, not a trimmed version, and not "just this one error message."

---

## Outline

### 1. Opening: "for everything" is the wrong question (0:00–0:45)
- Read the paragraph above.
- Tell the room how the talk is laid out: most of it is judgment, and one part is a rule.

### 2. Where it pays off (0:45–1:45)
- The speed is real for well-scoped work: boilerplate, test scaffolding, getting started with an unfamiliar API or library, and mechanical refactors that good test coverage protects.
- Measure the time it takes to get code merged and stable, not the time to a first draft. A draft that arrives in 30 seconds isn't a win if it takes an hour to review.
- Give one short example from our own work if you have one (keep it under 15 seconds).

### 3. Where it costs more than it saves (1:45–2:45)
- The quality risk: code that looks right and is subtly wrong, and edge cases nobody thought about because nobody wrote that code line by line.
- Review load moves to the reviewer. A large AI-generated PR that the author hasn't fully read is a cost passed on to someone else.
- A rule of thumb: if you couldn't review the code confidently yourself, don't generate it. The author owns what they ship, whoever or whatever wrote it.
- The point isn't to avoid these tools. Know which side of the line a task falls on and be honest about it.

### 4. The line: no customer data, no production logs, in any external tool (2:45–3:45)
*This section gets its full minute. Slow down here.*
- **Say the rule plainly:** no customer data and no production logs, in any external tool. That covers chat assistants, IDE plugins, browser extensions and "just checking something quickly."
- **Why it happens:** it's rarely careless. You're debugging under pressure, and the stack trace or log line you're about to paste contains an account ID, an email address or a payload. People here have come very close.
- **Why it matters:** compliance forbids it, and once data is pasted it's out of our control. We can't take it back.
- **What to do instead:** reproduce the problem with fake or synthetic data, describe the shape of the data instead of pasting it, and strip identifiers before anything leaves your machine.
- **If you're not sure, don't paste it.** Ask first. [Name the compliance contact or channel. If there's an approved internal tool that's cleared for this data, name it here. If there isn't one, say so.]
- [Optional: say what to do after a slip, such as "tell X right away; reporting it fast matters more than blame." Confirm this with risk/compliance before you say it.]
- Thank the risk and compliance people in the room and point people to them as the ones to ask.

### 5. Close (3:45–4:30)
- Summary: use the tools where they actually make you faster all the way to merged and stable, and use your judgment on everything else.
- Repeat the rule word for word: **no customer data, no production logs, in any external tool.**
- Stop there. Keep about 30 seconds in reserve for overrun or one question.

---

## Delivery notes
- Say the rule with the **same wording** all three times (in the opening, in section 4 and in the close). If you repeat it the same way, it's the line people remember.
- Sections 2 and 3 can be cut down if you run long. Section 4 can't.
- Check the bracketed items with risk/compliance before Friday so the "what to do instead" advice matches what they actually allow.
