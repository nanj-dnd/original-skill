1: Closest to b, but the guardrail I care about isn't really code quality. I'm fine with assistants for writing new code. My worry is skill atrophy in debugging. My actual position is that juniors should do their first six months of debugging without an assistant. It's the same reason pilots still train on manual flying even though the autopilot is better than they are most of the time: you need the skill for the day the automation hands you the controls. And please don't let it read as anti-AI. I'm not, and if it comes across as "old guy distrusts new tool," the point gets dismissed.

2: Not quite a, because the code wasn't AI-generated. It's two things from incident review:
- The number: over the last 6 months our median time-to-resolve for P2 incidents went from 38 to 61 minutes.
- The story: a 2am outage. The on-call engineer pasted the error into the assistant four times and got four different confident fixes. I found the cause in about 10 minutes by reading the log.

I'm also seeing more and more engineers in reviews who can't read a stack trace through code they "wrote."

3: Somewhere between a and b. I'm a staff engineer who runs the incident review and does on-call, so I'm speaking as someone in the trenches, not as management. But I do want engineering managers to walk away with a clear expectation about how juniors get onboarded. Plain and conversational, with a firm ask at the end. Not provocative for its own sake.

4: b. Open with the 2am story, use the 38→61 number to show it isn't a one-off, then land the one rule: no assistant for debugging in your first six months. Keep it brief that assistants are great for writing code, so nobody thinks I'm telling them to turn it off.