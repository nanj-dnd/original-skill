# Can We Still Fly the Plane?

*5 minutes, about 650 spoken words. Timings are a guide.*

## Outline

**1. The 2am outage (0:00 to 0:50, about 120 words)**
- Tell the story plainly: outage at 2am, the on-call engineer pastes the error into an assistant four times, gets four different fixes, each one stated with total confidence. You read the log and find the cause in about ten minutes.
- Say straight away that this isn't about blaming anyone and isn't an anti-AI talk. You use these tools yourself to write code.
- Turn the question: "AI for everything or not" is the wrong question. The real one is whether we can still work when the assistant is wrong.

**2. The autopilot (0:50 to 1:40, about 110 words)**
- Autopilot is very good, and nobody in aviation wants to remove it. Pilots still train on hand-flying, because the moment it drops out is the moment they most need the skill.
- Our version of "drops out" is the assistant being confidently wrong, and that tends to happen on the hard problems at the worst hours. Four confident answers at 2am is what that looks like.
- One line for everyone outside engineering: this isn't about how fast we write features. It's about what happens when something breaks.

**3. What I'm seeing (1:40 to 2:50, about 150 words)**
- The number: over the last six months, our median time to resolve a P2 incident went from 38 minutes to 61. That's 23 minutes more, a rise of more than half. For sales and support: that's the stretch between something breaking and it being fixed.
- The pattern from incident reviews: engineers who can't follow a stack trace through code they wrote themselves.
- Be straight about the limits: one number doesn't prove one cause. But it fits what you see in the reviews every week, and that's why you're raising it now.

**4. Why debugging is the skill to protect (2:50 to 3:40, about 110 words)**
- Writing code with an assistant is fine. The output gets reviewed, tested and shipped, and you can check it.
- Debugging is different: it's how you learn how a system really works, and you only learn it by doing it. If the assistant does the digging, the engineer never builds the skill, and it isn't there at 2am.
- Name the tension openly: if people can't trace through code they wrote with help, then debugging is exactly where that understanding has to get built. It's the one place we can't hand over.

**5. The change, starting Monday (3:40 to 4:30, about 110 words)**
- Speak to managers and the people who decide how juniors are trained.
- The rule: for their first six months, junior engineers debug without an assistant. They keep using it to write code. Debugging they do by hand.
- Same idea as pilots logging manual hours before they lean on the automation.
- Be honest about the cost: some debugging will feel slower at first. That slowness is the training.

**6. Close (4:30 to 5:00, about 50 words)**
- Go back to 2am: four confident answers, and ten minutes with the log.
- End on the plane: the assistant can fly most of the trip. The point is that everyone on call can still land it when it can't.

## Opening paragraph

We had an outage at 2am. The engineer on call did what a lot of us would do: pasted the error into an AI assistant. Then pasted it again. Four times, four different fixes, and every one of them stated with total confidence. I read the log and found the cause in about ten minutes. I'm not telling you this to embarrass anyone, and I'm not here to tell you to stop using these tools. I use them myself to write code. I'm telling you because I'm on call, I run our incident reviews, and that night wasn't a one-off. The question for these five minutes is whether engineers should use AI assistants for everything. I think that's the wrong question. The right one is this: when the assistant is wrong at 2am, can we still fly the plane ourselves?
