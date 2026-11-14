# Should Engineers Use AI Coding Assistants for Everything?
*5-minute all-hands talk: outline and opening*

**Core message (the one line people should remember):**
Use AI assistants for almost everything, but never for the part that makes you accountable. *If you ship it, you own it.*

---

## Opening paragraph

> Quick show of hands: who here used an AI coding assistant this week? Keep it up if you used it today. Okay, so that's most of us, and I think that's a good thing. The question I was asked to talk about is whether engineers should be using these tools for *everything*. My answer is no. That's not because the tools are bad. They're really good, and they're getting better fast. It's because "everything" includes the one part of our job a tool can't do for us, which is being the person who understands the code, stands behind it, and gets paged when it breaks. So for the next five minutes I'm not going to argue for or against AI. I want to talk about where the line is, and give you a simple way to find it.

*(About 45 seconds at a relaxed speaking pace. If you don't want the show of hands, start at "The question I was asked...")*

---

## Outline

### 1. Opening: the hook and the answer (0:00 to 0:45)
- Show of hands to make it concrete and get the room involved.
- Answer the question directly up front: "Not everything."
- Frame the talk: this is about where to draw the line, not whether to use the tools.

### 2. Where AI assistants clearly earn their keep (0:45 to 1:45)
- **Boilerplate and scaffolding:** config, glue code, test setup, migrations.
- **Getting unstuck in unfamiliar territory:** a new library, a language you rarely use, a cryptic error message.
- **Reading old code:** "explain what this 600-line function does" before you touch it.
- **Mechanical refactors and first drafts of tests and docs.**
- *Add one real example from our team here, ideally something that saved hours. A specific story will land better than a list.*
- Point to make: in these cases, hesitating to use the tool just costs us time.

### 3. Where "everything" breaks down (1:45 to 3:00)
- **Code nobody on the team understands.** It passes review today and becomes an incident next quarter. "The AI wrote it" doesn't help anyone at 2 a.m.
- **Review gets harder, not easier.** Code that's quick to generate can be slow to verify, so the work moves to the reviewer instead of going away.
- **Confident and wrong.** Plausible-looking bugs, invented APIs, and subtle security problems such as auth checks, input handling, and secrets.
- **Skill building.** Our newer engineers in particular need to struggle through some problems themselves to build the judgment that lets them catch the tool's mistakes later.
- **Design decisions.** Architecture, trade-offs, and "should we build this at all?" depend on context the tool doesn't have.
- *Optional: name our company's policy on what code or data can be shared with external tools, if one applies.*

### 4. A simple rule of thumb: three questions before you accept AI output (3:00 to 4:15)
1. **Could I explain this in code review without rereading the AI's explanation?**
2. **Would I notice if it were subtly wrong?**
3. **Is this something I need to learn to do myself?** If yes, write it yourself first and compare afterward.
- If the answer to 1 or 2 is no, slow down. If the answer to 3 is yes, use the tool as a tutor, not a ghostwriter.
- Come back to the core line: *If you ship it, you own it.*

### 5. Close: the ask (4:15 to 5:00)
- Using AI isn't the goal and avoiding it isn't either. The goal is good software and engineers who keep getting better.
- **Concrete ask for the room:** this month, share one place the tool saved you real time and one place it led you astray, in [team channel / retro / eng sync]. That turns individual habits into team knowledge.
- Closing line suggestion: "Let the tools do the typing. Make sure we still do the thinking."

---

### Delivery notes
- Five minutes is roughly 650 to 750 spoken words. Sections 2 and 3 are the easiest to trim if you run long.
- Keep the tone even-handed. The room likely includes both enthusiasts and skeptics, and the "where's the line" framing lets both of them listen.
- One slide with the three questions from section 4 is enough. It's the part people are most likely to screenshot.
