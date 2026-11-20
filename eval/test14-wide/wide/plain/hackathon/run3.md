# Hackathon Idea: **GridShift** — a "run it when the grid is clean" scheduler

## The idea
Electricity isn't equally dirty all day. Depending on your region, carbon intensity (gCO₂/kWh) can swing 2–3× between noon (solar-heavy) and evening (gas peakers). Most flexible loads — dishwashers, EV charging, laundry, batch compute jobs, bulk downloads — don't care *when* they run. GridShift tells you (and your devices) the cleanest window to run them, and quantifies the CO₂ you avoided.

**Why it's a good hackathon pick:** real public data, a clear before/after number, a tangible demo, and a scope you can finish in a weekend.

## What you'd build

**Core (must-have, ~Saturday)**
1. **Carbon intensity feed** — pull live + 24h forecast from a public API (Electricity Maps has a free tier; UK Carbon Intensity API and WattTime are alternatives). Cache it so you're not blocked by rate limits during the demo.
2. **Scheduler engine** — input: task duration, deadline, energy draw (kWh). Output: the window that minimizes CO₂ before the deadline. Simple sliding-window min over the forecast; add a "comfort" penalty for late-night slots.
3. **Web dashboard** — one page: a 24h intensity chart with the recommended window highlighted, a list of your queued tasks, and a running "kg CO₂ avoided" counter with an equivalence ("= 12 km not driven").

**Stretch (Sunday, pick one)**
- **Real device hook** — control a smart plug (TP-Link Kasa / Tapo via `python-kasa`, or a Home Assistant webhook) to actually switch a load on in the clean window.
- **CI/compute hook** — a GitHub Action or CLI wrapper (`gridshift run -- python train.py --deadline 6h`) that delays non-urgent jobs. Judges love "we carbon-aware'd our own build pipeline."
- **Browser notification** — "Clean window opens in 40 min — plug in your EV."

**Stack suggestion:** Python/FastAPI backend, React or plain HTML + Chart.js frontend, SQLite for task queue. Nothing exotic.

## Demo plan (5 minutes)

1. **Hook (30s)** — Show a live intensity chart for your region. "Right now the grid is 420 gCO₂/kWh. At 1pm it'll be 180. Same electrons, less than half the carbon."
2. **The problem (30s)** — "Most of what we plug in doesn't care when it runs. Nobody acts on this because nobody can see it."
3. **Schedule a task (1 min)** — Add "Charge EV, 3h, 20 kWh, done by 7am." Watch the window snap to the forecast's trough. Show the avoided-CO₂ figure update.
4. **Physical payoff (1 min)** — If you did the smart plug: have a lamp or fan on the plug. Set a demo deadline of "now + 2 min" with a spoofed forecast so it visibly switches on mid-pitch. Props win hackathons.
5. **Scale the story (1 min)** — Dashboard "if 10,000 households shifted their dishwasher" slide using real average loads. Also show the CLI/CI hook if you built it: "We ran our own test suite this way during the hackathon."
6. **Close (30s)** — Roadmap: utility partnerships, demand-response credits, open API for appliance makers.

**Demo safety tips:** record a backup video, mock the API response locally so Wi-Fi can't kill you, and have a fake "fast-forward" clock so you don't wait 6 hours for a window to open.

## Pitch line
*"GridShift: the same power, a third of the carbon — just by changing when you press start."*

Want me to sketch out the repo structure or a task breakdown for a team of 3–4?