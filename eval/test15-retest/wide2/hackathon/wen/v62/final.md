**This is an idea, not a single right answer, so here is the full process.**

**Angle:** Make a climate page for one person. Someone types their hometown and birth year, and the page shows how much hotter that place has become in their lifetime, using real weather records. In the demo, the judges' own hometowns are the data.

**Built from:** 1a (consumer-facing), 2d (open data, no material of your own), 3d (a few friends, unknown skills, keep it small), 4a (general judges, short pitch).

**Strongest objection:** It shows people the problem but doesn't help them reduce emissions. Judges who score "impact" may rank it below a tool that changes behaviour. It also looks a lot like the NYT's 2018 hometown-heat interactive and Ed Hawkins' warming stripes. **Test:** By Saturday lunch, run three very different towns. Check that the change is clearly visible and isn't just noise. Then show it to two people outside your team. If neither asks to try their own town, switch ideas.

**Other direction:** A one-page "should I fly or take the train?" comparison using the UK government's public emission conversion factors.

---

# Born Hotter

## The idea

You type the town you grew up in and the year you were born. The page answers one question: how much hotter is that place now than when you were born?

It pulls real temperature records for that spot going back to 1940 and shows three things:

- One big number: the town's recent average year compared with the decade you were born in, for example "+1.4°C".
- A warming-stripes chart: one coloured bar per year from 1940 to now, blue for cool years and red for hot ones, with your birth year marked.
- A look forward: the projected temperature for that town in the year you turn 60, from climate model data.

Most climate apps ask you to log things, and beginners can't build a convincing footprint calculator in a weekend. This app asks for two inputs and gives an answer about a place the user cares about. Because everyone has a hometown, the demo is personal for every judge in the room.

## What you'd build

The whole thing is one web page with no backend, no database and no login. It uses three free Open-Meteo services that need no API key:

1. **Find the town.** The Open-Meteo geocoding API turns "Pune" or "Leeds" into latitude and longitude.
2. **Get the past.** The Open-Meteo historical weather API returns daily temperatures from 1940 to now for that point. Average them by year.
3. **Get the future.** The Open-Meteo climate API returns model projections for the same point up to 2050.
4. **Show it.** Display the big number, the stripes and the projection on one screen, using plain HTML, CSS and JavaScript with Chart.js. A "Share my card" button saves the screen as an image.

Two design choices will make it trustworthy:

- **Compare decades, not single years.** One hot year can be a fluke. Comparing "the 1990s average" with "the last 10 years" is honest and still dramatic.
- **Say "around your town", not "your street".** The historical data is on a grid roughly 25 km across, so it describes the area, not one neighbourhood. Put that in one line at the bottom. Judges trust a team that states its limits.

**Splitting it among a few friends:**

- One person gets the API calls working and logs the numbers to the console. This is the riskiest part, so do it first.
- One person builds the page layout and the big-number card using fake numbers.
- One person builds the stripes chart.
- Whoever is free prepares the demo and the backup recording.

If all of that works by Saturday evening, everything else is a bonus. Possible stretch goals, in order:

1. The share card.
2. A "compare two towns" view for where you were born versus where you live now.
3. A line counting how many days last year were hotter than the hottest day in your birth year.

## Weekend plan

- **Friday night:** Everyone opens the three API links in a browser and confirms data comes back for one town. Pick names and colours. Stop there.
- **Saturday morning:** Get the APIs to produce a real big number for one hardcoded town.
- **Saturday afternoon:** Add the town and birth-year input and the stripes chart. Run the three-town test from above.
- **Saturday evening:** Add the projection and do styling. Save the full data for six or seven towns as files so the demo works without Wi-Fi.
- **Sunday morning:** Freeze features. Rehearse the demo three times and record the backup video.
- **Sunday afternoon:** Make only small fixes.

## Demo plan

The demo works by turning the judges into users.

**Before you start talking:** Ask one judge, "Where did you grow up, and roughly what year were you born?" Write it down. If they'd rather not say, use a teammate's hometown.

**Then:**

1. Say one sentence: "Everyone's heard the world is warming. We wanted to know how much it's warmed for you."
2. Type the judge's town and year live. Let the big number appear, then pause and say nothing for a second.
3. Point to the stripes chart and to the bar for their birth year. Show how the red increases toward the right.
4. Scroll to the projection: "And here's that town in the year you turn 60."
5. Run it on a very different town, such as somewhere much hotter or colder, to show it works everywhere and the pattern repeats.
6. Close with one line on why it matters. Abstract global averages are easy to ignore, but your own hometown is hard to ignore. Finish by pressing "Share my card".

If the judges' time limit is tight, skip step 5.

**Safety net:** If the live API is slow, switch to your cached towns ("let me show you one we prepared earlier"). If the laptop fails completely, play the recorded video.

---

**Before you use it**
- I couldn't check the Open-Meteo details live: historical data from 1940, projections to 2050, and roughly a 25 km grid. Confirm them on open-meteo.com on Friday night, and adjust the "year you turn 60" step if the projections end earlier than that.
- Check whether the hackathon allows or rewards public data, and find the actual pitch time limit. The demo plan is sized for about three minutes.
- If a judge mentions the NYT interactive or warming stripes, credit them openly. Your additions are the live lookup for any town, the forward projection and the share card.

**Distance from the default:** This replaces the footprint tracker and the two samples' grid-scheduler and receipt-scanner ideas with a "your hometown is warming" page. It also makes the judges the demo's input instead of a scripted walkthrough. Your answers 1a and 3d kept it consumer-facing and small enough for one page. It still shares the samples' reliance on a free public API, a backup recording, and the idea / what to build / demo layout you asked for.