**Angle:** Build HangTime, a single-purpose phone web app that answers one daily question with real forecast data: *"Will my washing dry outside today, and when do I bring it in?"* It saves tumble-dryer runs by making line-drying a safe bet.

**Built from:** 1a (one action by individuals: drying laundry), 2c (pure web, no hardware, free keyless API), 3a (narrow, works end to end on live data), 4c (story-led around one person's laundry on stage).

**Strongest objection and test:** People can look out the window, and weather apps already exist, so HangTime may not solve a real problem. **Test before Saturday:** ask five people who own a dryer when they last line-dried and why they didn't more often. If most say "I can tell myself," switch to the other direction below. If they say "it rained on it once" or "I never know if it'll be dry by evening," you have your problem.

**Other direction:** a "pre-warm or wait" heating nudge that uses the same forecast data to time home heating around the cheapest or cleanest hours.

---

# HangTime: will it dry today?

## The idea

A dryer is one of the most energy-hungry appliances in a home. People reach for it on doubtful days because they don't trust the sky. The worry is rarely "is it sunny." It's "will this be dry before it rains, or before I get home?"

HangTime gives one answer, not a weather report:

- **"Hang it out by 10:00, it'll be dry by 14:30."**
- **"Rain likely from 15:00: bring it in by 14:30."**
- **"Not today. Next good drying window: Tuesday morning."**

Drying depends less on sunshine than people think. It is driven by how dry the air is, by wind, and by warmth. A grey, breezy, low-humidity day can beat a still, muggy, sunny one. That gap between what people assume and what actually dries clothes is the insight your pitch rests on.

## What you'd build

The stack is a single-page web app, installable on a phone home screen as a progressive web app. It has no backend beyond static hosting, no accounts, and no hardware.

**Data:** the Open-Meteo forecast API, which is free and needs no key. You pull hourly values for your location:
- temperature
- relative humidity
- wind speed
- precipitation probability
- shortwave radiation
- vapour pressure deficit, a direct measure of how "thirsty" the air is

**The drying model:**
1. Each hour gets a drying rate from vapour pressure deficit and wind, plus a small bonus for sun.
2. You add hourly rates until a load counts as "dry." The user picks one of three load types (light cottons, mixed, towels and jeans), which sets the threshold.
3. The model looks for a window in daylight hours that finishes before any hour with high rain probability.
4. It outputs a hang-out time, a bring-in time, and a confidence level.

**The real data that makes it credible: a towel test.** All weekend, hang a wet towel near the venue and weigh it every 30 to 60 minutes on a kitchen scale. Wet weight minus dry weight is the water still in it. Log it next to the forecast for those hours. This calibrates your model and gives you a measured drying curve to show judges. If it rains all weekend, the test still works: you recorded HangTime saying "not today" and being right.

**Two small features that close the loop:**
- **Bring-in reminder:** one tap adds a calendar event (`.ics` download) at the bring-in time. This is simpler and more reliable than web push for a weekend build.
- **Saved-runs counter:** the user enters their dryer's kWh per cycle once, from the energy label or manual. Each "I hung it out" tap adds a load to a running total of kWh and money not spent. All figures come from the user's own appliance, so no estimate is pulled from thin air.

## Build plan

**Friday night**
- Fetch and render the hourly Open-Meteo data for the venue's coordinates.
- Hang the first towel and start the weigh-in log in a shared spreadsheet.
- Agree on the three answer screens: hang now, bring in by, not today.

**Saturday**
- Write the drying-rate function and the window search. Tune the "dry" threshold against the towel log as data comes in.
- Build the main screen: one big answer and a simple timeline bar showing the hang-out time, the predicted dry time, and any rain.
- Add the load-type picker and browser geolocation.

**Sunday morning**
- Add the calendar reminder and the saved-runs counter.
- Build the "why" view: forecast drying rate plotted against the measured towel curve.
- Cache a forecast JSON locally as a demo fallback, then rehearse twice.

Scope stop rule: if the model isn't calibrated by Saturday evening, ship the window search on a simpler rule (no rain, humidity under a threshold, some wind). Show the towel data as "how we'll tune it next."

## Demo plan (about 3 minutes, story-led)

**0:00 The person.** Hold up a damp towel. Introduce one person with a load just out of the washer, a grey sky, and a dryer one button away. "This is the moment the dryer usually wins. Not because they don't care, but because they don't want to come home to wet washing."

**0:30 The answer.** Open HangTime on a phone, mirrored to the screen. The live forecast for this room's location shows one plain sentence: hang out by this time, dry by that time.

**1:00 Why you can trust it.** Switch to the "why" view. "We've been drying this towel since Friday night." Show predicted drying against the weighed curve, including any hours where the model was off. Being honest about the misses makes the rest believable.

**1:45 The rain case.** Pick a day in the forecast with rain coming. HangTime says "bring it in by 14:30." Tap the reminder and show the calendar event appear. This is the fear that keeps people on the dryer, handled.

**2:15 What it adds up to.** Show the saved-runs counter for the person's loads this weekend, in kWh and money, using their dryer's own label figure.

**2:40 Close on the person.** "They hung it out." Fold the towel, now dry or nearly so. End there, not on a market-size slide.

**Fallbacks:**
- If venue wifi drops, load the cached forecast.
- If the towel test went badly, show it anyway as calibration data. That is a stronger story than a perfect chart.

---

**Before you use it**
- Check that Open-Meteo's hourly variables (vapour pressure deficit, shortwave radiation) and its free-use terms suit your hackathon before you build on them.
- Get the dryer kWh figure from a real appliance label rather than an online average.
- The story works best with a real teammate who actually uses a dryer and their real reason for it. Swap that in for the generic person.
- I didn't know your team size. The plan assumes 3 to 4 web developers. With two, drop the calendar reminder first.

**Distance from the default:** The plain answers converged on a grid-timing scheduler ("GridShift") demoed with a smart plug and a lamp, and closed on a "10% of households" scale slide. Your 1a, 2c and 4c answers moved this to one domestic action, no hardware, and a person-and-towel story with measured data. It still shares two moves with those samples: showing a live forecast on stage, and keeping a cached fallback.