# Idea: **CleanHour**: "When should I plug in?"

**Pitch:** The grid's carbon intensity swings a lot during the day depending on how much wind, solar, and gas is running. CleanHour tells you **the cleanest time in the next 48 hours** to run your dishwasher, laundry, or EV charger, and shows how much CO₂ you save by waiting.

**Why it fits you:**
- **Frontend-heavy.** The core is a timeline chart and a clean UI, with no backend required.
- **Free, keyless data.** The [UK Carbon Intensity API](https://carbonintensity.org.uk) gives a 48-hour forecast in 30-minute slots, nationally or by postcode. You don't need credits or a dataset.
- **No LLM needed.** The core logic is simple math, so the demo can't be broken by an AI call.
- **Easy to explain.** Everyone understands "run it at 2am instead of 6pm."

*Not UK-focused?* Electricity Maps has a free tier with a signup key that covers many countries. Swap the data layer and keep everything else.

---

## What you'd build

**Core (must-have):**
1. **Location input:** a postcode, or "use national average."
2. **Appliance picker:** cards for dishwasher, washing machine, dryer, EV charge, and custom. Each has an editable default energy use and run time (e.g., dishwasher ~1.2 kWh over 2h, dryer ~3 kWh over 1.5h).
3. **48-hour carbon timeline:** an area chart color-graded green to red, with "now" marked and the **best window highlighted**.
4. **Recommendation card:** "Start at **01:30**. Saves **~410 g CO₂** vs. now (≈ X km of driving)."
5. **Add to calendar:** generate a `.ics` file entirely in the browser.

**Window logic:** slide a window the length of the run time across the forecast slots, average the intensity in each, and pick the minimum.
`saving = kWh × (intensity_now − intensity_best)`

**Polish (if time allows):**
- A "your week" tracker stored in `localStorage` that tallies total CO₂ saved, with a little streak or leaf badge.
- A "Why is it cleaner?" tooltip showing the generation mix (the API provides it).
- A shareable result card.

**Stretch (only if everything else is done):** a plain-English one-liner such as "Windy tonight, so the grid is cleanest after midnight." You can generate it from the mix data with templates, so you don't need an LLM.

**Stack:** React or Next.js with Vite, Recharts or Chart.js, and Tailwind. Deploy to Vercel or Netlify.

**Safety net:** save a snapshot of the API response as `fallback.json` early on. If the live call fails during the demo, the app loads the snapshot silently.

---

## 24-hour build plan

| Hours | Goal |
|---|---|
| 0–2 | Scaffold, fetch the API, log data, save `fallback.json` |
| 2–6 | Timeline chart with now marker and gradient |
| 6–9 | Appliance picker, window algorithm, recommendation card |
| 9–10 | **Deploy.** You now have a working MVP |
| 10–16 | Visual polish, mobile layout, loading and error states, `.ics` export |
| 16–19 | Savings tracker and generation-mix tooltip |
| 19–21 | Rehearse the demo and fix rough edges |
| 21–24 | Buffer and sleep. Don't add features now |

---

## 3-minute demo script

**0:00–0:30, the hook.** "The same load of laundry can have double the carbon footprint depending on *when* you run it. The grid changes every half hour, but nobody can see that. CleanHour makes it visible."

**0:30–1:45, the live flow.**
- Enter a postcode and the chart animates in. Point out the clean dip: "Look, the grid gets much greener overnight because of wind."
- Tap **Dishwasher**. The best window lights up: "Start at 1:30am, save 410g of CO₂."
- Switch to **EV charge** to show the bigger number: "That's like skipping a 20km drive."
- Click **Add to calendar** and show the event appear.

**1:45–2:30, the impact.** Open the tracker: "One user doing this for a month saves about ___ kg." Then scale it up: "If 10,000 households shifted just their dishwasher…" Calculate these figures beforehand.

**2:30–3:00, the close.** "It's free, uses open data, needs no smart home and no signup. Next steps: more countries, and smart-plug integration to schedule appliances automatically."

**Demo tips:** pre-load the tab, bookmark a postcode with an interesting curve, and know that `fallback.json` will cover you if the Wi-Fi dies.

Want me to scaffold the project or write the window-finding function and API fetch code to get you started?