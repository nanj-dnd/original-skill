1. It's "it depends", and I know where the line goes. I'm not anti-AI. I use these tools myself, and for writing new code I think they're a net win. Please don't let the outline make me sound like a luddite yelling at clouds. I'm worried about skill atrophy, not code quality. My concrete line: junior engineers should do their first six months of debugging without an assistant. It's the same reason pilots still train on manual flying and hand-fly approaches when they have a perfectly good autopilot. The autopilot is great right up until it disconnects at the worst moment, and then you need someone in the seat who can actually fly the plane.

2. Mostly I want engineers and their managers to change how they work now, especially how juniors are onboarded and how we handle debugging and on-call. If it turns into a policy for the first six months, great, but I'd rather managers walk out agreeing with it than have a rule land on them. I don't need leadership to fund anything.

3. I'm a staff engineer. I'm on the on-call rotation and I run the incident review. We're about 300 people, a logistics company. It's a whole-company talk, so sales, ops and execs will be there, but the people I really need to reach are the engineers and their managers. Everyone else just needs to follow along.

4. Yes, engineers use assistants widely, for writing code and increasingly for debugging. There's no specific incident or debate behind the talk. It's a pattern I keep seeing in incident reviews: engineers who can't read a stack trace through code they supposedly "wrote".

5. Yes, two things:
- Metric: over the last six months our median time-to-resolve for P2 incidents went from 38 minutes to 61. I'm not claiming the assistants are the only cause, but the timing and what I see in reviews line up.
- Story: a 2am outage. The on-call engineer pasted the error into the assistant four times and got four different, confident fixes. I got pulled in, read the log, and found it in about 10 minutes. No heroics, I just read what the system was telling us. That's the story I'd like the talk built around.

6. Mostly just talking, with maybe a couple of slides for the 38 → 61 number. Serious and direct, but not doom and gloom. A little dry humor is fine, and I'll probably slip in an aviation line or two. It's really 5 minutes of me talking. Q&A, if there is any, comes after.
