# Use it to write. Learn to debug without it.

**5 minutes, about 650 spoken words**

## Outline

**1. The 2am outage (0:00–1:00)**
- The opening paragraph below.
- The on-call engineer stays anonymous. What they did is what anyone would do at 2am with that tool in hand.

**2. It's not one person. It's all of us (1:00–1:45)**
- "I run our incident reviews, and I'm on the rotation. I keep seeing the same thing: people who can't follow a stack trace through code they shipped. I've caught myself doing it too."
- The number: over the last six months, our median time to resolve a P2 incident went from 38 minutes to 61. That's 23 minutes longer, roughly 60% slower.
- For everyone outside engineering, in one line: when something breaks for a customer, it's taking us longer to fix it.
- Say plainly: this isn't about code quality. It's about a skill we're losing.

**3. Why debugging is the line (1:45–3:00)**
- An assistant is built to give you a plausible answer. For writing new code, that's exactly what you want, because there are many good-enough ways to write a function. "I use it for that every day, and I'm not going to stop."
- Debugging is the opposite kind of problem. A bug has one cause. A tool that makes plausible answers will give you plausible causes, each one stated with total confidence.
- So four different fixes that night wasn't the tool breaking. It was the tool doing its job on the wrong kind of question. Only reading the system tells you which answer is true.
- The answer to "should we use it for everything?" is that it's not about how much we use it. It's about which kind of problem we hand it.

**4. The change (3:00–4:00)**
- The rule: for their first six months, junior engineers debug without an assistant. They keep using it to write code, just not to debug.
- The aviation parallel: pilots log hours flying by hand before they lean on the autopilot. Autopilot is great, but when it drops out, you have to be able to fly.
- To the managers: you own how juniors get trained. The struggle that used to teach debugging is gone by default now, so we have to put it back on purpose.
- To the engineers: when you're on call, read the log first, before you ask the assistant.

**5. Close: this is how we lean harder on AI safely (4:00–5:00)**
- Turn it around: this isn't me taking the tools away. The more code we write with assistants, the more code exists that no human typed. That makes the ability to debug it rarer and more valuable, not less.
- Airlines faced this. As cockpits got more automated, regulators pushed for more manual-flying practice, not less. *(Check before Friday: the FAA's 2013 safety alert for operators, SAFO 13002 "Manual Flight Operations," encouraged airlines to give pilots more manual flying time after automation-dependence findings.)*
- Last line, roughly: "So use it. Use it more. Just make sure that at two in the morning, when it gives you four confident answers, someone in the room can read the log."

## Opening paragraph

"We had an outage at two in the morning. The engineer on call did exactly what I would have done, and what most of you would have done: they pasted the error into the assistant. It came back with a fix, stated with total confidence. The fix didn't work, so they pasted the error again. They got a different fix, with the same confidence. They did that four times and got four different answers, each one completely sure of itself. When I joined the call, I opened the log, read it top to bottom, and found the cause in about ten minutes. I'm not telling you this because someone got it wrong. They didn't do anything I haven't done. I'm telling you because that night is the clearest picture I have of something happening to all of us, me included. It's the thing I want to spend the next five minutes on."
