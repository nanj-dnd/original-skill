# Built on Day 1, Done on Day 7
*All-hands talk, 5 minutes, about 700 words spoken*

## Opening paragraph

> Quick vote before I say anything else, hands up, all twelve of you. Our Monday standup is at 9am, every week, set from here. You fly to Tokyo for a week. What time should the standup show up on your calendar? Hands up for "9am Tokyo time, obviously." Hands up for "still 9am *here*, whatever ungodly hour that works out to in Tokyo." Hands up for "it shouldn't show up at all, I'm travelling." *(Look at the room.)* Great, we don't agree. Hold on to that feeling, because last month a question exactly like that one cost us six days, and it's the best explanation I've got for what engineering is now.

## Outline

**1. The vote (0:00–0:45)**
- Opening paragraph above. Let the split land. Point at one person from each camp: "you're both right, and that's the problem."
- If the room *doesn't* split, use the fallback line: "OK, now imagine the person who set the meeting voted differently from you." *(Before Friday, test the question on a couple of people as planned. If it doesn't split cold, swap in a different recurring-event scenario.)*

**2. The reveal: there's no right answer, only a decision (0:45–1:15)**
- No setting is "correct." Someone has to *decide* what we mean and write it down. That's a spec.
- "This is the job now. Not typing code. Deciding what's right."

**3. The calendar sync story (1:15–2:30)**
- Engineers use AI for basically everything here, and that's settled. So for calendar sync we wrote **140 tests first**. A test is a written promise about what the product does, and the computer checks it for us.
- The AI agent wrote the code to pass all 140. The whole feature, in **one day**.
- Then recurring events across time zones broke it. No test covered that case, because nobody had decided what *should* happen. It took **six more days**.
- The line, said slowly: **"Built on day 1. Done on day 7."**
- The agent did exactly what we asked. We asked for the wrong thing.

**4. What this means if you're not an engineer (2:30–3:30)**
- The code is the cheap part now. The expensive part is the spec and the tests: deciding what's right and writing it down so a computer can check it.
- So when engineers spend all day on tests and arguing about specs, that's not a delay. That's the factory running.
- For sales especially: when you hear "it's built," that means **day 1**. Before you tell a customer anything, ask **"is it built, or is it done?"** Done means day 7.

**5. You're in engineering now: the ask (3:30–4:30)**
- The six-day bug was a *customer* question: what happens to my recurring meeting when I'm somewhere else? Support and sales hear questions like that every week. Engineers usually don't.
- The bottleneck isn't engineers typing. It's knowing the weird cases before we build.
- The ask: **one weird customer case a week**, from anyone outside engineering. Every one becomes a test. *(Name where to post it, e.g. a channel or doc, and who picks them up.)*

**6. Close: callback to the vote (4:30–5:00)**
- "Remember how we couldn't agree about the standup? Good. I want that argument on day 0, in this room, with you in it, not on day 6 with a customer waiting."
- Final line: "Built on day 1. Done on day 7. Help us make it day 2."
