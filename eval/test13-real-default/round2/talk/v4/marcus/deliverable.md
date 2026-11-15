**Angle**: The tools are fine for writing code; the skill we're losing is debugging without them, and the fix is to make juniors build that skill by hand for six months, the way pilots keep training on manual flying even though they fly on autopilot.

**Built from**: Your answer to 1 (the pilot framing and the junior proposal), the 2am P2 and the 38→61 number, your role as the person who runs on-call and incident reviews, and "a touch of c" on the debugging point.

**Strongest objection**: The 38→61 shift could be mostly something else — more complex systems, more incidents, more juniors on rotation, team growth — and the 2am story is one engineer on one night. **Test**: before Friday, split the last six months of P2s by whether the resolver was a senior or a junior. If time-to-resolve climbed for seniors just as much, the atrophy story is weaker (or broader than juniors), and someone in the room will spot that.

**Other direction**: Instead of a rule for juniors only, a "manual" on-call shift once a month for everyone, like recurrency training — less of a hierarchy fight with managers, and seniors who haven't debugged by hand in a year get caught too.

---

## Outline (5 minutes)

**1. The 2am P2 — 0:00 to 0:50**
The opening paragraph below. Four pastes, four confident wrong fixes, ten minutes with the log. Say what you're not here to say: not anti-AI, fine with using it to write code.

**2. What I see from the on-call seat — 0:50 to 1:40**
- Over the last six months, median time-to-resolve on P2s went from 38 minutes to 61.
- In incident reviews, engineers who can't follow a stack trace through code they "wrote."
- Name it precisely: this isn't a code quality problem. The code is mostly fine. It's a debugging problem, and debugging is the one thing the assistant can't do for you on the night the assistant is what's wrong.

**3. Why "use judgment" is how we got here — 1:40 to 2:30** *(the sharp bit)*
- We already have a use-judgment policy. Everyone in this room agrees with it. The number went up anyway.
- Judgment about when to put the tool down is built by debugging without it. Telling a first-year engineer to use judgment assumes they already have the skill the tool is replacing.
- One line to land it: you can't fall back on a skill you never built.

**4. Autopilot — 2:30 to 3:30**
- Pilots fly most of the flight on autopilot. Nobody calls that cheating. They still train manual flying, because the automation hands control back at the worst possible moment, and that's when you need stick-and-rudder.
- 2am with a P2 is the moment the automation hands it back.
- Our version of manual flying is reading a log and a stack trace with nothing but your head.

**5. The proposal — 3:30 to 4:30**
- Juniors: first six months, debugging without an assistant. Write code with it, fine. When something breaks, you read the log, the trace, the code, and you work it. Pair with a senior if you're stuck.
- Be honest about the cost: some fixes will take longer for six months, on a small share of tickets.
- What it buys: an on-call rotation where everyone can find it in ten minutes when the tool is confidently wrong four times in a row.

**6. The ask — 4:30 to 5:00**
- To managers: this needs your sign-off, and I'm asking for it.
- To engineers: I'll keep tracking P2 time-to-resolve and report back in six months. If it doesn't move, I'll say so.
- Close on the number, not a slogan: 38 to 61. I'd like the next number I read out to be going the other way.

## Opening paragraph

We had a P2 go off at two in the morning. The engineer on call did what most of us would do now: pasted the error into the assistant. It came back with a fix, confident, clean. Didn't work. Pasted it again. Different fix, just as confident. Didn't work. Four times, four different answers, none of them right. I got pulled in, opened the log, and found it in about ten minutes. I'm not telling you that to make anyone look bad, and I'm not here to tell you to stop using these tools. I'm not sceptical of them, and I'm fine with people using them to write code. But I run on-call and I run the incident reviews, so I'm the person who sees what happens when the tool is wrong and the human has to take over. What I'm seeing is a skill going away, and I've got five minutes to tell you which one and what I want to do about it.

---

**Before you use it**
- Confirm 38 and 61 are both medians over the same window, and have a one-line answer ready for "did incident count or severity change in that period?"
- The pilot analogy is yours and stands on its own; if someone pushes, the FAA has published guidance encouraging airlines to keep manual flying skills current (SAFO 13002, 2013) — check it before citing it out loud.
- Make sure the on-call engineer is fine with the story being told, even unnamed; in a company that size people will work out who it was.
- Section 3 is where you'll run long. If you're over, cut the second bullet of section 2, not any of section 3.

**Distance from the default**: Far. The default (and all three samples) argues "use it for typing, not for thinking" and opens with "that's the wrong question"; your answer to 1 flipped the stance to a specific proposal about debugging and skill, and your 2a material replaced the reframe opener with the real outage. There's no "where the tools win" section, because you don't need to earn credibility you already have from the on-call seat. What it still shares with the samples: skill atrophy and "can you debug it at 2am" both appear in them as one bullet among several; here they're the whole talk, and the 2am is a real one.