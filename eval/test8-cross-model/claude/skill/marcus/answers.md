1b 2c 3: whole company will be there, but the people I actually need to reach are the engineers and their managers. Managers especially, because they're the ones who'd have to make room for juniors to debug the slow way. 4a

On 1, one important caveat: I'm not anti-AI, and I'll be irritated if this comes out sounding like I'm yelling at clouds. I use assistants and I'm fine with them for writing new code. My worry isn't code quality, it's skill atrophy. People are losing the ability to debug.

On 2, the specifics:
- Number: over the last six months our median time-to-resolve for P2 incidents went from 38 to 61 minutes. I run incident review, so I see this firsthand, and in those reviews I keep finding engineers who can't read a stack trace through code they supposedly wrote.
- Case: a 2am outage. The on-call engineer pasted the error into the assistant four times and got four different, confident fixes. I came in, read the log, and found it in about ten minutes.

The point I want to land: juniors should do their first six months of debugging without an assistant. It's the aviation thing. I fly privately, and even with excellent autopilots, pilots still train on manual flying first, because when the automation hands you the airplane at the worst moment, you need the stick-and-rudder skills to already be there. Autopilot is great. You just don't learn to fly on it.

Also, please drop the "future of engineering" rhetorical-question opener. I'd rather open with the 2am outage.