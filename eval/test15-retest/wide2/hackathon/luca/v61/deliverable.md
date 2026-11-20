## Angle

- **Angle:** Keep the personal carbon tracker, but make it practical: answer eight questions once instead of logging daily, see which two or three changes would matter most for you, then check in weekly with a few taps.
- **Built from:** 1a (individuals), 2a (web app), 3c (solo frontend dev, about 24 hours, no APIs or hardware, the usual idea is fine if practical), 4c (polished live demo with strong visuals).
- **Strongest objection:** Judges have seen many carbon calculators, so polish alone may not stand out. **Test:** By hour 16, show the what-if screen to two people for 30 seconds and ask which single change they'd make. If they can't answer immediately, the visual isn't working yet, and that matters more than any extra feature.
- **Other direction:** A trip comparer (train vs flight vs car for one journey) built on the same static data. It's narrower and quicker to build, but less of a tracker.

---

# Tally: a carbon tracker you set up once

## The idea

Most footprint apps fail on logging. Nobody records every meal and bus ride for more than a week. Tally swaps logging for a plan:

1. **Set up once (2 minutes).** About eight questions with sensible defaults: commute mode and distance, flights per year, heating type, rough electricity use, and how often you eat beef or lamb, other meat, and dairy.
2. **See your shape.** An annual footprint split by category, so the big blocks are obvious.
3. **Play with what-ifs.** Toggle realistic changes (two remote days a week, one fewer return flight, swap beef for chicken twice a week, a heat pump instead of gas) and watch the total fall. Ranking the changes by impact for *your* answers is the core of the product.
4. **Track the plan, not your life.** Pick two or three changes. Each week Tally asks one question per change ("Did you do your remote days?") and plots actual savings against the plan.

Everything runs in the browser. Emission factors live in a JSON file in the repo, state lives in localStorage, and there is no backend, login, or network call. That fits your constraints, and it also means venue Wi-Fi can't break your demo.

## What you'd build

**Data (do this first, about an hour).** Build one `factors.json` with around 15 to 20 entries. Each entry has a value, a unit, a source name and a year. Good free sources:

- UK government greenhouse gas conversion factors (DESNZ, published annually) for transport, fuels and electricity.
- Our World in Data's food emissions figures, based on Poore & Nemecek (2018), for food.

If your audience isn't in the UK, use your country's grid factor.

**Screens:**

| Screen | Visual | Why it carries the demo |
|---|---|---|
| Setup | One question per card, with defaults pre-filled so you can tap through in 30 seconds | Shows that the setup is easy |
| Your footprint | A treemap by category and sub-item, with the total counting up | The big blocks are obvious at a glance |
| What-if | A horizontal bar per change, sorted by kg saved. Toggling one animates the total down and shrinks the matching treemap block | This is the moment judges remember |
| Plan & check-in | A weekly tap card, then a line chart of planned vs actual savings | Shows it's a tracker, not a one-off calculator |
| Methodology | Click any number to see its factor, formula and source in a side panel | Answers "where's that number from?" before anyone asks |

**Stack:** Use whatever framework you're fastest in, with Vite and React or Svelte. For charts, D3 (or visx) gives you treemap transitions with full control. ECharts is faster if you'd rather not hand-build animations. Deploy as a static site on Netlify, Vercel or GitHub Pages so judges can open it on their phones.

**Two demo helpers to build early:**

- A **"Load demo person"** button that fills in a realistic profile you've rehearsed.
- A **"Reset"** button that clears localStorage.

## 24-hour plan (solo)

- **Hours 0–2:** Build `factors.json`, scaffold the app, and write the calculation functions as plain code with a few unit tests. These are what judges will question.
- **Hours 2–6:** Setup flow with defaults.
- **Hours 6–11:** Footprint treemap with the animated total.
- **Hours 11–16:** What-if bars, linked to the treemap. Spend the most polish time here.
- **Cut line at hour 14:** If you're behind, drop the weekly check-in and present the what-if screen as the product.
- **Hours 16–19:** Weekly check-in and planned-vs-actual chart. Seed six weeks of demo history so the line has a shape.
- **Hours 19–21:** Methodology panel, demo person, reset, and a QR code to the deployed URL.
- **Hours 21–24:** Visual polish (one accent colour, consistent easing, readable at projector size), deploy, and rehearse the demo three times out loud.

## Demo plan (about 3 minutes, all live)

1. **Open on a judge's numbers (60s).** Show the QR code and ask one judge to scan it and tap through setup on their phone while you narrate. If nobody volunteers, hit "Load demo person." Either way, the treemap builds on screen. Line: "That's 30 seconds of setup. Most trackers want that every day."
2. **The what-if (60s).** Switch to your laptop with the demo person loaded. Toggle the top-ranked change and let the bars and treemap animate. Then toggle a popular but low-impact change and show it barely moves the total. That contrast is your argument: the tool tells you *which* change matters for you.
3. **Tracking (30s).** Commit to two changes, tap through one weekly check-in, and show the six-week planned-vs-actual line.
4. **Credibility (20s).** Click the biggest number and open the methodology panel with factor, formula and source. "Every figure traces back to a published dataset."
5. **Close on the engineering (10s).** "No backend, no account, no network. It runs offline in the browser, and your data never leaves your device."

**Safety:** Rehearse with Wi-Fi off. Keep the laptop version as the main screen so a judge's phone is a bonus, not a dependency. Keep a 60-second screen recording ready in case the projector misbehaves.

**Pitch line:** *"Tally doesn't make you log your life. It shows you the two changes that matter for you, and checks in once a week."*

---

**Before you use it**
- Pull the factor values yourself from the current DESNZ release and the Our World in Data food page, and note the year in `factors.json`. I haven't included specific figures because I couldn't check them here.
- Check that your hackathon allows pre-made datasets and UI libraries. Most do, but some require everything to be built on site.

**Distance from the default:** The core claim stays the default's, a personal carbon tracker web app, because you chose 1a and 2a and said the usual idea is fine. What changed: setup once instead of daily logging (from "practical" in 3c), a ranked what-if simulator and a methodology panel as the centrepiece (4c), and a frontend-only, offline build with no APIs (3c). Unlike the samples, it drops OCR, LLMs, grid APIs, smart plugs and the "imagine it at scale" close. It still shares an on-screen data citation and a backup-recording safety plan with them.