# Outline: "Your call, except for one thing" (5 minutes, tech division, about 80 people)

**0:00 to 0:45. Opening: answer the question, then name the exception.**
Answer the question asked ("for everything?") with a straight no, say that where to use it is mostly each engineer's call, and announce that there is one thing that is not a call. State the line once here so nobody misses it.

**0:45 to 2:00. The part that is your call: speed against quality.**
- Where it pays: work you can check faster than you could write it.
- Where it costs: output that looks done but adds review load and rework later. A test anyone can use: if reviewing it takes longer than writing it would have, it didn't save time.
- Keep this short and unprescriptive. The point is that the room already has the judgment; you're not adding rules here.

**2:00 to 2:45. The turn: why one thing is different.**
- A speed or quality mistake gets caught in review and fixed. Customer data or a production log pasted into an external tool can't be pulled back.
- Say plainly that this keeps almost happening. Describe the pattern, not any person or incident: someone debugging under pressure reaches for the fastest way to get help, and the fastest way is to paste what's on the screen.

**2:45 to 3:45. The line (the one minute).**
- Say it slowly, then say it again: **No customer data. No production logs. In any external tool.**
- Name what counts, because "I know the rule" isn't the problem: log excerpts, stack traces with real payloads, error messages that include customer fields, screenshots of prod dashboards, test fixtures copied from production, "just one row."
- What to do instead: reproduce with synthetic or redacted data, describe the shape of the data rather than pasting it, and when in doubt, ask before you paste. (Add who to ask; see note.)
- Turn to the risk/compliance people in the room and invite them to confirm or correct the line on the spot. It shows the line is shared, not yours alone.

**3:45 to 5:00. Close: back to the question.**
- Restate: use these tools for whatever you judge they're good at; that's your call.
- The one exception, a third and final time, in the same words.
- End on the line itself, not on "use it wisely."

**Notes to check before Friday**
- Confirm the exact wording of the compliance rule and whether your approved assistant counts as an "external tool." The line on the slide must match the policy.
- If your assistant can read files or terminal output in the workspace by itself, add "or let it read" next to "paste."
- "Who to ask" is a placeholder: fill in the real person or channel.

---

## Opening paragraph

I was asked to talk about whether we should be using AI coding assistants for everything. My short answer is no, but I'm not going to spend my five minutes telling you which tasks to use them for. Most of you already have a better feel for that than any rule I could write, and where you use these tools is your call. There is one thing that isn't a call, though, and I'm going to be blunt about it because we keep getting close to it: no customer data and no production logs go into any external tool. Not one row, not a trimmed log line, not "just this once to debug it." I'll come back to that before I finish, and I'll say it more than once.
