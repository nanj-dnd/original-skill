**Angle**: Use the assistant to write code; keep debugging manual for a junior's first six months, because debugging is the skill the automation hands back to you at 2am, and our incident data says it's already slipping.
**Built from**: 1 (debugging, not code quality; the pilot framing; not anti-AI), 2 (the 2am story, 38→61, the stack-trace reviews), 3 (staff engineer in the trenches, plain, firm ask to managers), 4 (story → number → brief pro-AI note → one rule).
**Strongest objection**: 38→61 is one number over six months with no control. If P2 volume, system complexity, or the on-call roster changed in the same window, someone will say so from the floor and the number does half the work against you. **Test**: before Friday, pull the P2 count and the top two or three causes for the same six months. If the mix is roughly flat, the number holds; if it isn't, say so yourself and lean on the story and the reviews instead.
**Other direction**: Make it a norm for everyone, not juniors only: one assistant-free debugging shift per on-call rotation, so seniors keep the muscle too.

---

## Outline (5:00)

**1. The 2am outage (0:00–0:50)**
Opening paragraph below. Story only, no moral yet.

**2. It isn't a one-off (0:50–1:40)**
- Over the last six months, our median time-to-resolve for P2 incidents went from 38 minutes to 61.
- What I see in reviews: more engineers who can't read a stack trace through code they wrote. The code is theirs in git. The understanding isn't.
- Flag the gap: same systems, same tools for building, slower at fixing.

**3. What this is not (1:40–2:10)**
- The code in that outage wasn't AI-written, and this isn't a talk about AI code being bad. Use the assistant for writing new code. I do. Keep doing it.
- The problem isn't what the assistant writes. It's what happens to us when something breaks and the assistant doesn't have the answer.

**4. Why debugging is different (2:10–3:10)**
- Writing with an assistant, you can check the result: tests pass, the feature works. Debugging is the case where the tool is guessing and you have to know it's guessing. Four confident wrong fixes look identical to one confident right one unless you can read the log yourself.
- Pilots: the autopilot flies better than they do most of the time, and they still train on manual flying, because the skill exists for the day the automation hands you the controls. 2am is that day for us.
- You don't build that skill while the assistant is answering for you.

**5. The rule (3:10–4:10)**
- Juniors do their first six months of debugging without an assistant.
- Concretely: when something breaks, read the log, read the trace, form a hypothesis, then fix it. The assistant is fine for writing the fix once you know what's wrong. It's off for finding out what's wrong.
- This is six months, not forever. After that, use whatever gets you to the answer; by then you'll know when the tool is bluffing.

**6. The ask (4:10–5:00)**
- To engineering managers: make this part of onboarding, in writing, this quarter. Not "encouraged." Expected.
- To everyone else: next time you're on call and the first fix doesn't work, open the log before you paste the error a second time.
- Close on the number: 38 to 61. I'd like to be back here in six months reading it the other way.

---

## Opening paragraph

> We had an outage at two in the morning. The engineer on call did what most of us would do now: pasted the error into the assistant. It came back with a fix. Confident, specific, and wrong. So they pasted it again, and again, and again: four times, four different fixes, every one of them just as sure of itself as the last. We were still down. I found the cause in about ten minutes by reading the log. I'm not telling you this to score a point off whoever was on call. At two in the morning, with a tool that answers in two seconds and never sounds unsure, reaching for it is the obvious move. I'm telling you because I run our incident reviews and do on-call, and that night wasn't an outlier. It's starting to look like the shape of our incidents.

---

**Before you use it**
- Section 5's definition of "debugging" (log, trace, hypothesis, then the assistant may write the fix) is my proposal, not something you said. Adjust it to the line you actually want managers to enforce.
- "This quarter" in the ask is a placeholder deadline; put in the real one or cut it.
- If you can name the system or the actual cause from the log in one clause, add it to the opening. It makes "ten minutes by reading the log" land harder.

**Distance from the default**: The whole piece is yours: a single rule about debugging and tenure, opened on a real incident, grounded in a real metric, with a direct ask to managers. All three default samples open by declaring "that's the wrong question," split the job into "typing vs thinking," walk through a pros-then-cons list, and land on "you own every line you merge." None of that is here. What it still shares: the samples mention "2am/3am incidents" as a hypothetical and "skill atrophy for juniors" as one bullet among six; yours is built on an actual 2am incident and makes atrophy the only point, so the overlap is in the topic, not the piece.