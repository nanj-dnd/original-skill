# "It took a day" — 5-minute all-hands talk

**Target: ~5 min spoken, about 650–750 words.**

## Outline

**0:00–0:45 — Open: the question's already answered**
- The question I was given: should engineers use AI for everything? Here, they already do. It's just how we work.
- So the better question is what that changed. Hook: calendar sync. The code took one day and the feature took seven.

**0:45–2:00 — The calendar sync story**
- We wrote 140 tests first, describing everything the feature should do. Then the agent wrote the code. All 140 passed. One day.
- Then recurring events across time zones broke it. The spec was wrong about them, and no test covered it. Six more days.
- *[Add one plain-language example of the bug that non-engineers can picture, e.g. what happened to a weekly meeting. I've left it to you so it's the real one.]*

**2:00–3:15 — What the job is now**
- Code is the cheap part. The expensive part is deciding what "correct" means in every weird case, then writing that down as tests the AI has to pass.
- That's why engineers spend all day on tests and arguing about specs. The arguing *is* the engineering.
- The twist: 140 green tests and it was still wrong. Tests only check the questions you thought to ask. The hard part is thinking of the question.

**3:15–4:20 — What this means for everyone else in the room**
- Decoding "it took a day": the code took a day. The question to ask is whether we know what "right" looks like yet.
- Why estimates look strange now. The code is fast, but finding out what's true about the world isn't.
- *[Optional, to check: you hear what customers actually do. The weird cases often reach sales and support first, so tell us. Keep this only if it matches how your team works.]*

**4:20–5:00 — Close**
- Callback: the code took a day, and figuring out what "right" meant took six.
- Closing line: "So next time an engineer tells you something took a day, ask them: which day?"

## Opening paragraph

> I was asked to talk about whether engineers should be using AI coding assistants for everything. Good news: this is the shortest debate of the day, because we already do. Pretty much everything. It's just how we work now. So I want to talk about something more useful, which is what that changed. It explains a thing that probably drives some of you a little crazy: an engineer says "it took a day," and then it doesn't ship for a week. Last month we built calendar sync. The code took one day. The feature took seven. Those six extra days aren't a delay. They're the job now, and I want to show you why.
