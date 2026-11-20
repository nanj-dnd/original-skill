# Hackathon Idea: **Dispatch** — a "cleanest hour" assistant for home energy use

## The idea

Grid carbon intensity swings 2–5x over a single day depending on how much solar/wind is online. Most people have at least a few flexible loads — EV charging, dishwasher, laundry, water heater, batch cooking — but no idea *when* running them actually matters. Dispatch tells you the cleanest windows in your area today, lets you "schedule" loads with one tap, and shows the CO₂ you avoided over time. It's behavior change with zero hardware.

Why it works for a weekend: the data is free and public, the core logic is a small optimization problem, and the demo is visual and immediately legible to judges.

## What you'd build

**Data layer**
- Pull hourly carbon-intensity forecasts from a free API (Electricity Maps has a free tier; WattTime has a free "signal" endpoint; UK has carbonintensity.org.uk with no key). Pick one region as the primary demo and fall back to cached data so the demo never depends on live network.
- Optional: a utility TOU price table for the same region so you can show cost *and* carbon.

**Core logic (the "brain")**
- User enters a load: name, duration (e.g., EV = 3h), deadline (e.g., "by 7am").
- Scheduler finds the contiguous window within the deadline that minimizes integrated carbon intensity (simple sliding window over the forecast — ~20 lines).
- Output: best window, the CO₂ saved vs. "run it now," and a plain-English reason ("Wind picks up after 11pm").

**App (web, mobile-first)**
- Screen 1: a 24-hour "cleanliness strip" — color-coded hour bar, green to red, with a "now" marker.
- Screen 2: add a load, see the recommended slot drop onto the strip.
- Screen 3: a simple ledger — "This week you shifted 4 loads and avoided 2.1 kg CO₂."
- Notifications: a push/SMS when a scheduled window opens ("Clean window starts in 10 min — plug in the car"). Twilio or a browser notification is enough.

**Stretch goals (only if ahead of schedule)**
- Household mode: multiple people, shared ledger, friendly leaderboard.
- Smart-plug integration via a Kasa/TP-Link or Home Assistant API — flip a real outlet on stage.
- "Explain it" button that uses an LLM to turn the forecast into a two-sentence narrative.

**Suggested stack:** Next.js or SvelteKit + Tailwind for the UI, a tiny Python/FastAPI or Node service for the scheduler, SQLite for the ledger. Deploy to Vercel/Fly so judges can open it on their phones.

**Team split (4 people):** one on data ingestion + caching, one on the scheduler + API, two on the frontend, with everyone converging on the demo path by Saturday night.

## Demo plan (aim for 3 minutes)

1. **Hook (20s):** "Right now in [region], electricity is X g CO₂/kWh. At 1am it'll be a third of that. Nobody knows this, and nobody can act on it. We fixed both."
2. **Show the strip (30s):** Open the app on a phone. Walk through today's color bar — point out the dirty evening peak and the clean overnight trough. Keep it visual, no numbers yet.
3. **Schedule a load (45s):** Add "Charge EV, 3 hours, done by 7am." Watch the slot snap into the cleanest window. Show the delta: "Running now: 1.9 kg. Running at 1am: 0.6 kg. Saved: 1.3 kg — about the same as a 5-mile drive."
4. **The moment (30s):** Trigger the notification live (fake the clock or have a "demo: jump to window" button). If you got the smart-plug stretch done, a lamp or fan on the table turns on. This is the thing judges remember.
5. **Ledger + scale (30s):** Flip to the week view showing cumulative savings. Then one slide: "If 10% of households in [region] shifted one load a day, that's ~X tonnes/year" — do the back-of-envelope math beforehand and cite your source.
6. **Close (15s):** "No hardware, no utility partnership, works today in any region with a public grid API. Next step: utility co-marketing and demand-response credits."

**Demo-risk hygiene:** bake the forecast data into the repo so the demo works offline, pre-seed the ledger with plausible history, and rehearse the full path at least three times. Have a second phone as a backup.

If you want a different flavor within the same theme, two alternates that also fit a weekend: a **receipt-to-footprint** scanner (photo a grocery receipt, get a carbon breakdown and swaps) or a **heat-risk checker** for renters (address → tree cover, surface temperature, and cooling resources nearby, using NASA/Landsat open data). Happy to flesh out either if Dispatch isn't the right fit.