**Path: specific answers, so I'm building directly (step 4).** You gave things I couldn't have guessed: P2 median time-to-resolve going from 38 to 61 minutes, the 2am outage where four pastes got four confident fixes, your seat running incident reviews, and a concrete rule for juniors. This is a talk, so here's the plan first. I'll write it once you've had a look.

**Angle:** Keep using assistants to write code, but treat debugging without one as a skill we have to keep training on purpose, the way pilots keep logging manual hours. Starting now, juniors do their first six months of debugging without an assistant.

**Built from:** 1 (the real issue is losing skills, not code quality, and you're not anti-AI), 2 (it's for engineers and the managers who train juniors, with a short version for everyone else), 3 (the 2am outage), 4 (staff engineer, on call, runs incident reviews), 5 (one concrete change starting Monday).

**Tension I'll use rather than smooth over:** you use these tools yourself and don't want to sound against them, but what you're asking for is a restriction. The talk handles that by saying it up front: "I use this every day. That's why I'm asking for this." The rule covers debugging only, for juniors only, for six months only.

**Strongest objection:** the jump from 38 to 61 minutes might not be about assistants at all. It could come from more new hires, new services, harder incidents or changes to the on-call rotation. Someone in the room will also say that if the tools keep getting better, debugging by hand is like learning long division.

**Test before Friday:** check whether the P2 slowdown follows assistant adoption or something else. If you can, split time-to-resolve by tenure, or by whether the responder used an assistant. If you can't split it, present the number as "this is what we're seeing," not "this is the cause." Your answer to the long-division point is the 2am outage: the assistant is exactly what you can't rely on at 2am.

**Other directions:**
- Make the change about incident reviews instead: add "could the responder have found this without the assistant?" as a standard review question.
- Frame it as an experiment: track resolve times for juniors with
