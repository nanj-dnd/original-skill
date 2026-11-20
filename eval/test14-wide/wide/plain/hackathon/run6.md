# Hackathon Idea: **GridWise** — a "when to use power" assistant

## The idea
Electricity isn't equally clean all day. Depending on the hour, your local grid might be 70% solar/wind or 70% gas/coal. Most people have no idea, and shifting flexible loads (laundry, EV charging, dishwasher, batch compute jobs) by a few hours can cut their real carbon footprint meaningfully — with zero lifestyle sacrifice.

**GridWise** tells you *the best times today to use electricity* based on your location's live grid carbon intensity, and can automatically schedule flexible tasks into those windows.

## Why it works for a hackathon
- **Real data, free APIs:** Electricity Maps, WattTime, and (for the UK) Carbon Intensity API all expose live and forecast carbon intensity. No fake data needed.
- **Clear, demoable outcome:** "You saved X kg CO₂ this week" is a number judges understand instantly.
- **Scopes down cleanly:** core loop is small; extras are optional.
- **Differentiated angle:** most climate hackathon projects are carbon *calculators*. This one takes *action*.

## What you'd build (48-hour scope)

**Core (must-have, ~day 1)**
1. **Backend** (Python/FastAPI or Node): poll a carbon-intensity API for the user's region, cache the 24-hour forecast.
2. **"Clean windows" engine:** rank the next 24 hours into green / neutral / dirty blocks; given a task duration (e.g. "2-hour laundry"), return the lowest-carbon slot before a user deadline.
3. **Web dashboard** (React/Next.js or just Svelte): a timeline bar colored by intensity, "right now" indicator, and a simple "Add flexible task" form.

**Stretch (day 2, pick 1–2)**
- **Smart-plug integration** (Kasa/TP-Link or Home Assistant) — actually switch a device on in the green window. Huge demo payoff.
- **Push/Slack notification:** "Grid is 80% renewable for the next 3 hours — good time to charge."
- **Impact tracker:** compare carbon of chosen slot vs. "if you'd run it now" and accumulate savings.
- **Dev-focused twist:** a GitHub Action / CLI that delays CI jobs, model training, or backups to green windows ("carbon-aware cron").

**Tech stack suggestion:** FastAPI + SQLite + React/Tailwind. One API key, one deploy (Vercel + Fly/Railway). Avoid auth entirely — use a hard-coded demo user.

## Demo plan (5 minutes)

1. **Hook (30s):** Show two screenshots of the same grid at 2 PM vs. 9 PM — "same kettle, 3× the emissions." Ask the room: does anyone know what their grid looks like right now?
2. **Live dashboard (90s):** Open GridWise on your actual location. Show today's intensity timeline, the "now" marker, and the next green window.
3. **Schedule a task (60s):** Add "EV charge, 3 hours, done by 7 AM." Watch it snap to the cleanest slot and show "saves 1.2 kg CO₂ vs. charging now."
4. **Physical payoff (60s):** Smart plug with a lamp on the table. Fast-forward the clock (fake "now" via a demo toggle) — lamp turns on when the green window hits. This is the moment people remember.
5. **Scale the story (30s):** Impact screen: "If 10,000 households shifted one load per day → X tonnes/year." Close with the carbon-aware cron angle for dev teams.
6. **Q&A buffer (30s).**

**Demo safety tips:** cache a known-good forecast response in case the venue wifi dies, build a "demo mode" clock override from the start, and rehearse the smart-plug moment at least three times.

## Team split (3–4 people)
- One on API ingestion + scheduling engine
- One on frontend timeline/dashboard
- One on hardware/notifications integration
- Everyone shares pitch deck + impact math in the last 3 hours

Want me to sketch the data model and scheduling algorithm, or draft the pitch slides?