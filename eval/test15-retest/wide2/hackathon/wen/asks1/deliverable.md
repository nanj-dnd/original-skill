# Idea: **GreenHour**: "Know the cleanest time to plug in"

**The pitch:** The electricity grid gets cleaner or dirtier through the day depending on how much wind and solar is running. Running your dishwasher at 2pm instead of 6pm can cut its emissions significantly, and it costs you nothing. GreenHour tells you **when** to run your energy-hungry appliances so they use the cleanest power.

**Why it fits your situation:**
- **Easy to demo:** You enter a location, pick an appliance, and get a clear answer like "Run it at 1:30pm and save 40% CO₂." Judges get it in 10 seconds.
- **Low technical risk:** One free API, no hardware, no machine learning, and no backend required.
- **Beginner-friendly:** Mostly frontend work, so mixed skill levels can all contribute.
- **Real and actionable:** It's not another carbon footprint calculator. It asks for no sacrifice, just better timing.

---

## What You'd Build

### Data source
- **[UK Carbon Intensity API](https://carbonintensity.org.uk)** is free, needs no API key, provides a 48-hour forecast, and works by region or postcode. This is the easiest option.
- If you're outside the UK, look at **Electricity Maps** or **WattTime**. Both have free tiers but require signup, so check coverage for your region first. Even if you're not in the UK, demoing with UK data is perfectly fine for a hackathon.

### Core features (must-have, about 24 hours)
1. **Location input:** a postcode or region dropdown.
2. **Appliance picker:** dishwasher, washing machine, dryer, EV charging, and so on, each with an estimated energy use and run time.
3. **Forecast chart:** carbon intensity over the next 24 to 48 hours, with the cleanest window highlighted in green.
4. **The answer card:** "Best time: 1:30pm. Saves ~0.3 kg CO₂ (42%) vs. running now."
5. **"Remind me" button:** downloads a calendar event (.ics file) or triggers a browser notification. Both are easy to build.

### Stretch features (if you have 48 hours or finish early)
- An impact tracker: "This month you've saved 4.2 kg CO₂, equal to X km not driven."
- A shareable result card for social media.
- A household or friends leaderboard.
- A "cleanest hour today" home-screen widget view.

### Suggested stack
- **Frontend:** plain HTML/JS or React/Next.js, whatever your team knows best.
- **Charts:** Chart.js (simple and well documented).
- **Hosting:** Vercel or Netlify (free, and deploys in minutes).
- **Backend:** none needed. Call the API directly from the browser.

### Rough team split (for 3 to 5 people)
| Role | Tasks |
|---|---|
| Data person | Fetch the API, find the best window, calculate savings |
| Frontend person | Layout, inputs, results card |
| Chart person | Forecast chart with the highlighted window |
| Design/pitch person | Name, logo, colors, appliance energy estimates, slides, demo script |

Whoever finishes first picks up stretch features.

### Timeline (24-hour version)
- **Hours 0–2:** Agree on scope, set up a repo, get one API call working.
- **Hours 2–10:** Build the core features in parallel.
- **Hours 10–14:** Connect everything and deploy a working version early.
- **Hours 14–20:** Polish the UI, fix bugs, add one stretch feature.
- **Hours 20–24:** Freeze features, rehearse the demo, record a backup video.

---

## Demo Plan (about 2–3 minutes, live)

**1. Hook (20 sec)**
> "Quick question: does it matter *when* you run your dishwasher? Most people think no. But the grid's carbon intensity can change a lot within a single day, depending on wind and sun."

Show one slide with a real carbon intensity curve from today.

**2. Live demo (90 sec)**
- Open the deployed app on a phone or laptop.
- Enter a postcode and select "Dishwasher."
- The chart appears with the green window highlighted. Point to it.
- Read the answer card aloud: "Run it at 1:30pm and save 42%."
- Tap "Remind me" to show the calendar event appear.
- If you built it, show the impact tracker: "Over a year, this one habit saves..."

**3. Impact (30 sec)**
> "No new appliances, no cost, no sacrifice. Just timing. If 10,000 households shifted two loads a week, that's [your calculated number] tonnes of CO₂ a year."

Work out this number beforehand and keep it conservative and clearly labeled as an estimate.

**4. Close (15 sec)**
> "GreenHour: the cleanest time to plug in." Then mention what you'd build next, like smart plug integration that automatically runs appliances at the best time.

### Protect against demo failure
- **Cache a copy of the API response** and add a fallback so the app still works if the Wi-Fi or API fails.
- **Record a 60-second screen video** of the full flow as a last-resort backup.
- **Rehearse at least three times** and time it.

---

**Backup idea, if GreenHour doesn't excite your team:** *"Fridge Rescue,"* a web app where you list what's in your fridge and it suggests recipes that use the items expiring soonest, showing the food waste and CO₂ you avoided. It's similarly simple, but it depends on an AI or recipe API, which adds a little more risk.

Want me to sketch the API logic or a starter file structure for GreenHour?