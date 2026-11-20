# Hackathon Idea: **GridShift** — Carbon-Aware Scheduling for Everyday Devices

## The Idea
Electricity carbon intensity varies hugely throughout the day — at 2pm on a sunny day the grid might be 80% solar, while at 7pm it's mostly gas. Most flexible loads (EV charging, dishwashers, laundry, home batteries, even laptop charging) don't need to run *right now*. **GridShift** tells you (and your devices) the cleanest hour to run things, and automates it where possible.

The pitch: *"Cut your home's carbon footprint 15–30% without changing what you use — just when you use it."*

## What We'd Build (48 hours)

**Core (must-have):**
1. **Carbon forecast engine** — Pull real-time + 24hr forecast grid carbon intensity from a public API (Electricity Maps, WattTime, or the UK Carbon Intensity API — the UK one is free and needs no key, which is ideal for a hackathon). Normalize into a per-hour "clean score."
2. **Task scheduler** — User enters a flexible task ("charge EV, needs 3 hours, done by 7am"). The engine finds the lowest-carbon window that satisfies constraints and shows CO₂ saved vs. running immediately.
3. **Web dashboard** — A simple timeline: green/yellow/red hours for the next 24h, your scheduled tasks overlaid, and a running "kg CO₂ avoided" counter.

**Stretch (if time allows):**
- **Smart plug integration** — Control a TP-Link Kasa or Tapo plug via its local API to actually switch a load on/off at the optimal time. One real device makes the demo 10x more convincing.
- **Household leaderboard** — Gamify avoided emissions across friends/neighbors.
- **Push notifications** — "Grid is 70% renewable right now — good time to run the dishwasher."

**Suggested stack:** Python/FastAPI backend (carbon API + scheduler), React or plain HTML+Chart.js frontend, SQLite for tasks, optional `python-kasa` for plug control. All buildable by 3–4 people in a weekend.

## Demo Plan (5 minutes)

1. **Hook (30s):** Show a live chart of today's grid carbon intensity. Point out the peak vs. trough — "Same kWh, 3x the emissions depending on when you use it."
2. **Problem (30s):** "Nobody looks at this. Your dishwasher certainly doesn't."
3. **Live product (2.5 min):**
   - Add a task: "Charge laptop, 2 hours, by 9am tomorrow."
   - Show GridShift pick the window and display "saves 0.4 kg CO₂ vs. charging now."
   - Add a second task with a tight deadline — show it correctly picks a less-ideal but valid window.
   - **The money shot:** Trigger a "simulated time jump" to the scheduled hour and have a real smart plug + lamp click on live on stage. (Pre-record a backup video in case Wi-Fi fails.)
4. **Impact (1 min):** Scale the math — "If 10% of UK homes shifted just EV charging, that's ~X tonnes/year." Show the leaderboard screen for the community angle.
5. **Close (30s):** Roadmap — utility partnerships, direct integration with Tesla/Nest/Home Assistant APIs.

## Why This Wins
- **Real data, real action** — not just a dashboard; it does something.
- **Demo-able physically** — a lamp turning on is memorable.
- **Low API risk** — free, keyless data source means you won't get blocked at hour 40.
- **Clear impact story** judges can quantify.

Want me to scaffold the backend (carbon API fetcher + scheduler logic) so you have a head start?