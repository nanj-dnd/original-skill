# Test 141: what AI actually changed about engineering

## Outline

**1. The question is already answered (0:00–0:45)**
- Should engineers use AI for everything? Here, they already do. It's just how we work.
- So skip the debate and talk about what it changed, because that explains things you see us do that look odd from the outside.
- Set up the story: calendar sync took one day. It also took seven.

**2. The calendar sync story (0:45–2:00)**
- Day one: we wrote 140 tests before any code existed. Each test is one sentence of "when this happens, the calendar should do that," written so a machine can check it.
- The agent wrote the code until all 140 passed. Whole feature, one day.
- Days two to seven: meetings that repeat every week, for people in different time zones. No test described that case, so nothing checked it, so the code didn't handle it.
- The punchline: the code was right. It did exactly what we asked. What we asked for was wrong.

**3. The job changed (2:00–3:00)**
- Writing code used to be the slow, expensive part. Now it's the cheap part.
- The expensive part is deciding exactly what "correct" means, every case, before anything gets built. The tests are where we write that down.
- So when engineers spend a whole day on tests, or an hour arguing about what a calendar invite should do, that isn't the warm-up before the work. That is the work.

**4. What this means for everyone else (3:00–4:15)**
- *"It took a day" means the first day.* The fast part is building what we already thought of. The rest of the week goes on what nobody thought of yet. When you plan around a launch, plan around the week.
- *A spec argument is good news.* Every argument we have before building is a bug we don't ship.
- *You know the weird cases before we do.* Sales and support hear what customers actually do, including the things nobody would think to write down. Those are exactly the tests we're missing. Bring them to us before we build, not after a customer finds them.

**5. Close: find test 141 (4:15–5:00)**
- Callback: 140 tests, and the one that mattered wasn't there.
- The agent will write whatever code we describe. It can't tell us what we forgot to describe.
- The ask: the most useful thing anyone in this room can do for engineering now is help us find test 141.

## Opening paragraph

The question for my five minutes is whether engineers should be using AI coding assistants for everything. Short answer: we already do. That ship has sailed, and honestly, an agent probably wrote the code for the sail. So I'm not going to argue about it. I want to tell you what it changed, because it explains a lot of things you see us do that probably look strange from the outside: why we spend whole days writing tests for code that doesn't exist yet, why we'll argue for an hour about what a calendar invite should do, and why, when I say a feature took a day, it still doesn't ship for a week. Last month we built calendar sync in one day. It also took seven. Let me tell you where the other six went.
