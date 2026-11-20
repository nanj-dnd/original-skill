# GridShift — "Run it when the grid is clean"

**One-liner:** A browser extension + tiny API that tells people (and apps) the cleanest hour to do energy-hungry things — charge the EV, run the dishwasher, kick off a big ML job — based on real-time grid carbon intensity.

## Why this works for a weekend
- **Real data, free APIs:** Electricity Maps, WattTime, UK Carbon Intensity, and ElectricityMap's forecast endpoints all give hourly gCO₂/kWh with forecasts. No data wrangling.
- **Tangible impact:** Shifting a load 3–4 hours can cut its emissions 30–60% in solar/wind-heavy grids. Easy to quantify on stage.
- **Small surface area:** One API wrapper, one UI, one integration. You can finish it.

## What you'd build

**1. Core service (Sat morning)**
- Node/Python service: `GET /best-window?region=CAISO&duration=2h&deadline=2026-11-17T08:00` → returns the lowest-carbon contiguous window before the deadline, plus % savings vs. "run now."
- Cache the upstream forecast every 15 min.

**2. Two consumer surfaces (Sat afternoon → Sun morning)**
- **Browser extension / PWA:** User sets region + a few recurring tasks ("laundry, 1.5h, done by 7am"). Shows a 24h bar chart colored by carbon intensity with a highlighted "do it now" window and push notifications.
- **Developer hook:** A GitHub Action / CLI (`gridshift run --max-delay 6h -- python train.py`) that delays a compute job until the clean window. This is the "wow" for a tech audience — carbon-aware CI/CD in 10 lines.

**3. Impact ledger (Sun afternoon polish)**
- Every shifted task logs "would've emitted X, actually emitted Y." Dashboard shows cumulative kg CO₂ avoided — equivalent in miles driven / trees. Judges love a number.

**Stack suggestion:** FastAPI or Express, SQLite, Vite + React for the UI, Recharts for the intensity graph, Plasmo for the extension if you go that route.

## Demo plan (5 minutes)

1. **Hook (30s):** "Right now in California, electricity is ~2× dirtier than it will be at 1pm. Most of us have no idea, and our devices don't care." Show the live intensity graph.
2. **Consumer flow (90s):** Add "charge EV, 3h, done by 8am." App returns the window, shows "47% less CO₂ than plugging in now." Trigger a notification live.
3. **Developer flow (90s):** Run `gridshift run --max-delay 4h -- ./train.sh` in a terminal. It prints the forecast, picks the window, and (for demo) you pass `--demo-fast` so it "waits" 5 seconds and runs. Show the GitHub Action YAML — 6 lines.
4. **Impact ledger (45s):** Dashboard with cumulative savings from your team's weekend of dogfooding. Extrapolate: "If 1% of US EV owners did this…"
5. **Close (30s):** Roadmap — smart plug integration (Kasa/Hue), Home Assistant plugin, cloud scheduler hooks (AWS Batch, k8s CronJobs).

**Demo-risk mitigations:** Record a fallback video of the full flow; cache a snapshot of the API response in case the venue wifi/API is down; hardcode a region with visible daily variation (CAISO, Germany, or UK are great).

## Stretch ideas if you're ahead
- Region auto-detect by IP
- A Slack bot: "☀️ Clean energy window starts in 20 min — good time to run your builds"
- Household mode: aggregate savings across roommates for friendly competition

Want me to scaffold the API and a starter UI in your scratchpad so you walk in with something running?