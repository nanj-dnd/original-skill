## Angle

- **Angle:** A solo frontend dev wins a storytelling-judged room by putting the judges' own lives into the data, not by building a backend. Build a scroll story that turns any hometown and birth year into "how many hot days your life has had, and will have."
- **Built from:** 1d (consumer-wide audience, as in the default), 2c (solo, frontend, 24h means no backend, no hardware, no OCR), 3c (polish and a 3-minute story means one emotional reveal), 4d (easiest and impressive means free public climate data, mostly charts).
- **Strongest objection:** It's awareness, not action. A judge may ask "nice chart, but what does it *change*?" **Test:** Show a rough version to three people on Saturday night and ask what they'd do after seeing it. If nobody says "share it" or "look up my parents' town," the hook is weak. Strengthen the share card before you polish anything else.
- **Other direction:** A carbon-aware scheduler (the obvious pick, and what most teams with a backend will build). Avoid it so you're not the third grid app on stage.

---

# Lifetime Heat
*Type your hometown and the year you were born. Watch your life on a thermometer.*

## The idea
Climate numbers are global and abstract: "+1.5°C" means nothing at a dinner table. Lifetime Heat makes one number personal: **how many unusually hot days your town had the year you were born, how many it has now, and how many it's projected to have when you're older.** It's a short, scroll-driven story that ends in a shareable card ("Kolkata: 31 hot days the year I was born, 58 projected by 2050").

It's consumer-wide, needs no login, and the input is something every person can give in five seconds.

## What you'd build (frontend only, 24 hours)

**Data: all free, keyless, callable from the browser (confirm before starting)**
- **Open-Meteo Geocoding API** turns a typed town into latitude and longitude.
- **Open-Meteo Climate API** gives daily max temperature per location from about 1950 to 2050 using CMIP6 climate models.
- Use the climate model's own series for the whole line, past and future, so you don't stitch observed data onto projections. One consistent line is easier to defend when a judge pokes at it.

**The one clever bit: a fair "hot day" for every town**
A fixed threshold like 35°C makes Oslo look fine and Phoenix look permanently on fire. Instead, define a hot day *relative to that place*: hotter than the 90th percentile of its 1961–1990 days. You compute this in a few lines of JavaScript, and it lets a judge from anywhere get a meaningful result. It's also the answer when someone asks "hot compared to what?"

**Screens (one page, scroll-driven)**
1. **Input:** town and birth year, one big button.
2. **Scene 1, "The year you were born":** a single number, large, with the town name.
3. **Scene 2, "Today":** the number animates up and a year-by-year bar chart draws itself from birth year to now.
4. **Scene 3, "When you're [age in 2050]":** the chart continues into a shaded projection band (min to max across two or three models, so you show uncertainty instead of hiding it).
5. **Scene 4, the share card:** a clean image with town, three numbers and a sparkline, plus download and copy-link buttons. The URL holds the town and year, so links open straight to that person's story.

**Stack:** your usual framework (React, Svelte or plain Vite), Observable Plot or D3 for the chart, Scrollama or IntersectionObserver for the scroll triggers, and html-to-image for the card. Deploy on Vercel or Netlify so judges can open it on their phones.

**What to cut if time runs short:** multi-model bands (use one model), the share card (keep the URL) and mobile layout polish. Never cut the relative threshold; it's what makes the live demo safe for any town.

## 24-hour plan
| Hours | Work |
|---|---|
| 0–3 | Call both APIs from a scratch page. Get one town's 1950–2050 daily series into an array. Compute the baseline percentile and hot-day counts per year. |
| 3–8 | Bar chart with birth-year and "today" markers. Projection band. |
| 8–13 | Scroll story: four scenes, number animations, typography. This is where the demo is won. |
| 13–16 | Share card and URL state. Deploy. |
| 16–18 | Sleep, seriously. |
| 18–21 | Pre-fetch and cache JSON for 10–15 likely towns (big cities near the venue, plus judges' hometowns if you can find them). Fall back to the cache if the API is slow. |
| 21–24 | Rehearse the 3-minute script five times. Fix only what breaks during rehearsal. |

## Demo plan (3 minutes)

**0:00–0:20: Start with a person.**
"Before I show you anything, can one of the judges tell me where you grew up and roughly what year you were born?" Type it in live. Don't explain the product yet.

**0:20–1:20: Let the story play.**
Scroll through it on the big screen. Read their numbers out loud: "The year you were born, your town had this many unusually hot days. This year, this many." Pause on the chart drawing itself. Let the room react; this is the moment.

**1:20–1:50: The projection, honestly.**
Scroll into 2050. "This band is the range across climate models, not a forecast for any single day." Saying that unprompted earns credibility with technical judges.

**1:50–2:20: How it works, briefly.**
One slide or a quick toggle: "Hot means hot *for that town*, compared with its own 1961–1990 days. That's why this works for Oslo and for Chennai." Mention it's fully client-side public climate data, built solo in 24 hours.

**2:20–2:50: The product, not just the chart.**
Show the share card. Open the link on your phone to show it lands on the same story. "Climate data spreads when it's about your town and your age. This is built to be sent to your parents."

**2:50–3:00: Close on their number.**
Go back to the judge's card on screen. "That's your town. Everyone in this room has one."

**If the live input fails:** switch to a cached town without comment ("let's try the city we're in"). That's why you pre-fetch.

---

**Before you use it**
- Confirm the Open-Meteo Climate API's current date range, model list and terms (it's free for non-commercial use as far as I know, but check the docs Friday night before committing).
- Check the projected counts for two towns you know against intuition. If a number looks absurd, check your percentile code before your story.

**Distance from the default:** This moves from "track your own emissions" to "see your own town's heat over your lifetime." That comes from 2c (no backend or hardware), 3c (the demo is built around one judge's live reveal) and 4d (free public data, mostly charts). 1d keeps the same consumer-wide audience as the default. Compared with the samples, it drops the grid-scheduler idea two of them chose, the smart-plug prop, and the "if 10,000 households" scale slide with its utility-partnership roadmap. It still shares their practical advice to cache data and plan a fallback so the demo can't die on Wi-Fi.