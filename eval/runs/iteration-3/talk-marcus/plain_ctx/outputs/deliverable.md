# Keep Your Hands on the Controls
*5-minute all-hands talk, about 650–700 words spoken*

## Opening paragraph (about 45 seconds)

> A while ago, at two in the morning, we had an outage. The engineer on call did what most of us would do now: they pasted the error into the AI assistant. It came back with a fix and sounded completely sure. The fix didn't work. So they pasted it in again and got a different fix, just as sure of itself. That happened four times: four different answers, each one stated with total confidence. When I looked at it, I opened the log and read it, and I found the cause in about ten minutes. I'm not telling you this because that engineer did something unusual. I'm telling you because it's becoming normal. I'm a staff engineer, I'm on the on-call rotation, and I run our incident reviews. I use these assistants every day, and I'm not here to tell you to stop. I'm here because I think "should we use AI for everything?" is the wrong question.

---

## Outline

### 1. Opening: the 2am outage (0:00–0:45)
- The paragraph above. Keep it blameless: no name, no team, no service.
- Say early who you are and that you use the tools yourself, so nobody files this under "anti-AI."

### 2. The real question (0:45–1:30)
- "Everything or not" isn't the question. The question is **what we stop learning when the assistant does it for us.**
- Be specific: my worry isn't code quality. Assistants write decent code, and using them to write new code is fine.
- What's wearing away is the skill you need when things break: reading a log, following a stack trace, building a picture of what the system is actually doing.

### 3. What I'm seeing (1:30–2:30)
- **The number:** over the last six months, our median time to resolve P2 incidents went from **38 minutes to 61**.
- **The pattern from incident reviews:** engineers who can't follow a stack trace through code they supposedly wrote.
- **Be honest about the limits:** I can't prove the assistant caused every one of those 23 minutes. But the number matches what I see in the room when we take incidents apart. (Saying this first takes away the easy objection from the engineers in the audience.)
- **One line for everyone else:** for sales and support, those 23 minutes are customers waiting and tickets piling up. This isn't a niche engineering argument.

### 4. The autopilot analogy (2:30–3:15)
- Autopilot is great, and pilots use it all the time. They still have to be able to fly by hand when it drops out, so they keep training on manual flying.
- **The twist for us:** our autopilot doesn't switch off with a warning light. It drops out by staying confident and being wrong, four times in a row, at 2am. That's exactly when you need someone who can fly the plane by hand.

### 5. The ask: one change, starting Monday (3:15–4:15)
- **For engineering managers:** juniors do their first six months of **debugging** without an assistant.
- **What it isn't:**
  - Not a ban. Juniors still use the assistant to write code.
  - Not a rule for senior engineers.
  - Not about trusting the tool less. It's about making sure the skill exists before people lean on the tool.
- **Why debugging specifically:** it's the skill we need most under pressure and the one that only grows through repetition. It's the same as pilots logging manual hours before they rely on automation.
- **How we'll know:** watch P2 time to resolve and what comes up in incident reviews, and look at it again together in six months.

### 6. Close (4:15–5:00)
- Go back to the opening: the next time it's 2am and the assistant gives four confident answers, I want whoever is on call to be able to open the log and read it.
- Closing line: **"Use the autopilot. Just make sure every one of us can still fly the plane."**

---

### Notes before Friday
- **Make sure the ask can actually happen.** If the six-month rule needs sign-off from engineering leadership, get it before Friday. Then "starting Monday" is a real plan and not just a hope.
- **Check the 38 → 61 figure** against your incident tracker and know what counts as a P2. Someone will ask.
- **If you go over time,** cut section 3's line for non-engineers down to one sentence before you cut anything else. The ask in section 5 is the part to protect.
