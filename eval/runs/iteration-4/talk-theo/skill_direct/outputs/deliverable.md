## Outline: "Yes, for everything. Here's the catch, and how we find out." (5 min, about 700 words)

**1. Opening: my answer, and why you should care if you don't code (0:00 to 0:45)**
- Straight answer: yes, for everything.
- Two admissions: I'm an engineer, so I have a stake in this. And I have no proof, only a view.
- To the non-engineers: you get the call when something we ship breaks, so this is your question too.

**2. "Which tasks?" is the wrong question (0:45 to 1:45)**
- The usual answer splits the work: AI for the routine stuff, humans for the judgment calls.
- That line doesn't hold. Judgment calls hide inside routine-looking code: a default value, an error message, a retry loop.
- A list of approved tasks goes stale every few months as the tools change. Nobody checks it, so it stops being a rule.
- The question that lasts is who owns the result, not who typed it.

**3. The rule I'd propose: if you can't explain it, it doesn't ship (1:45 to 2:45)**
- Whoever's name is on a change answers for every line in it, the same as if they'd typed it themselves.
- In review, "the AI wrote that part" is never an answer. The author explains it or rewrites it.
- For the rest of the company: [an example from your own team's work, e.g. a proposal or a support macro built from a template still goes out under one person's name, and that person answers for it].
- So the risk moves from writing to reviewing. That's where the trial in section 5 should look.

**4. The honest part: none of us knows yet (2:45 to 3:20)**
- Nothing has happened here, good or bad, that settles this.
- There are studies pointing both ways. I'm not going to quote one, because it wouldn't be about us.
- So instead of arguing, let's measure.

**5. The experiment (3:20 to 4:30)**
- [Team or volunteers] use AI assistants for everything for [N] weeks, starting [date].
- One rule: the one in section 3.
- Two measures against the [N] weeks before: [review time per change] and [issues found after release].
- What would prove me wrong: if issues after release go up. If they do, we scale it back and I'll say so here.
- Report back at [the next all-hands / date].

**6. Close: the ask (4:30 to 5:00)**
- Engineers: [volunteer for the trial / tell me what you'd measure instead].
- [Whoever has to approve the trial]: [the decision you need from them].
- Everyone else: if something we ship during the trial breaks, tell us. You're part of the measurement.
- Last line: [your closing line, e.g. "Ask me in [N] weeks whether I was right."]

## Opening paragraph

I was asked whether engineers should use AI coding assistants for everything. My answer is yes. Everything. Before you decide I've lost it, two admissions. First, I'm an engineer, so I'm not neutral here. Second, I don't have proof. Nothing has happened at this company, good or bad, that settles the question, and anyone who stands up here sounding certain is guessing. That includes me. So in the next five minutes I want to do three things: tell you why "which tasks should the AI do?" is the wrong question, give you the one I'd ask instead, and propose how we find out in [N] weeks whether I'm wrong. And if you don't write code, stay with me. When something we ship breaks, you're the people who get the call.
