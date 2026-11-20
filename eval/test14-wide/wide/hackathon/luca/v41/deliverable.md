**Angle**: Make the unit the year, not the trip: a frontend-only dashboard where a judge clicks their own commute on a map and sees it repeated 220 times, so one habit becomes one big number they can argue with.
**Built from**: 1a (one daily habit), 2a (solo, frontend, 24h, no backend to babysit), 4b (judges drive it on a laptop), "polished over complicated".
**Strongest objection**: it's still a carbon calculator, and judges have seen those. **Test**: on Saturday morning, hand it to one person for 60 seconds with no explanation. If they don't say a number out loud or change their mode to see what happens, the reveal isn't landing and you should tighten the first screen before adding anything else.
**Other direction**: same shape, different habit: a drag-things-onto-a-plate food dashboard using the Poore & Nemecek food-emissions table, also fully static.

---

# Repeat — your commute, 220 times

## The idea

Nobody changes a habit because of one trip's number; a single drive to work is a few kilos of CO₂ and feels like nothing. The same trip happens about 220 working days a year, and that is the number people don't have in their heads. Repeat is a single-page dashboard: you click where you live and where you work, pick how you get there, and the page draws the year — one cell per working day, sized by that day's emissions — next to the same year by train, bus, bike or car-share. The pitch is one sentence: "One trip is noise. Here's the year."

It fits the brief because the habit is genuinely daily, the swap is one decision (mode), and the whole thing is browser-side: a map, a routing call, a bundled table of emission factors, and good charts. No accounts, no database, no OCR, no device to wire up.

## What you'd build

One page, four panels, all client-side:

**Map (top left).** Leaflet with OpenStreetMap tiles. The user clicks two points; the route line comes from the public OSRM demo server. If that call fails or is slow, fall back silently to straight-line distance × 1.3 and draw a dashed line. Bundle three pre-computed routes (short city, suburban, long) as demo presets so the page works with no network at all.

**Mode picker (top right).** Five tiles: car (solo), car (shared, 2 people), bus, train, bike / e-bike. Each tile shows kg per day for this route. Selecting one is the only interaction that matters; everything else recalculates on change. A working-days slider (default 220) and a "round trip" toggle sit under it.

**The year (bottom, full width).** A grid of 220 cells in a GitHub-contribution layout, cell area proportional to that day's emissions, filling left to right with a 1.5-second animation when the mode changes. This is the panel that does the work: switching from car to train should visibly shrink the grid, not just change a label.

**Side-by-side year (right rail).** Total kg per year for every mode on this route, as horizontal bars, with the current pick highlighted and an equivalence under the biggest bar expressed in something concrete you have a source for (kilometres driven, or kWh), not trees.

**Data.** Emission factors come from the UK government's published greenhouse-gas conversion factors (free annual spreadsheet; US teams can use EPA's equivalents). Put the five factors you use in a JSON file in the repo, show the source and year in the page footer, and make the "how we calculate" link a real modal with the arithmetic. Nothing else lives outside the repo.

**Stack.** Vite + React (or plain TypeScript if you're faster that way), Leaflet, one chart library you already know. Deploy to Vercel or GitHub Pages so the demo URL works on any laptop, including a judge's.

### A 24-hour plan for one person

- **Hours 0–2**: factors JSON, the arithmetic, a plain text output. Get the numbers right before anything is pretty.
- **Hours 2–6**: map, two-click route, OSRM with the straight-line fallback, three presets.
- **Hours 6–10**: the year grid, animated. Stop when a mode switch makes you say "oh."
- **Hours 10–13**: mode tiles, slider, side-by-side bars.
- **Hours 13–16**: sleep. Seriously.
- **Hours 16–20**: polish pass: typography, empty state, mobile width, the "how we calculate" modal, the footer source line.
- **Hours 20–22**: deploy, test on a laptop that isn't yours, test with Wi-Fi off.
- **Hours 22–24**: rehearse the judge flow below three times, fix whatever you tripped on.

If you're running late, cut the side-by-side bars first, then the slider. Never cut the fallback routes or the footer source.

## Demo plan

Because judges use it themselves, the plan is a 90-second guided flow rather than a pitch, with you talking only to steer.

1. **Hand over the laptop, already open on the page.** Say: "Click where you live, then where you work." Don't explain anything else. If they don't have a commute, click one of the three presets for them.
2. **Let them pick their real mode.** The grid fills. Say nothing until they react; the number on screen is the pitch. If they read the number out loud, that's the moment.
3. **Say: "Now try the train."** The grid shrinks. This is the only line you need: "That gap is one decision, made 220 times."
4. **Point at the footer.** "Those are the official UK factors; the arithmetic is behind that link." Judges who are sceptical of calculators want to see this; judges who aren't won't mind.
5. **Close with scope, honestly.** "It's one habit on purpose. The next habit is a new preset, not a new app."

Have a second laptop or your phone open on the deployed URL as a backup, and the three presets ready in case a judge's route makes the public routing server stall. Keep the whole thing under two minutes so the panel can pass it along; a dashboard that three judges each touched beats one you narrated.

---

**Before you use it**: I couldn't verify the current year's conversion factors or the exact per-mode figures, so take them from the published spreadsheet when you build the JSON rather than from memory. Working days per year varies by country (around 220–230 in the UK, closer to 250 in the US); pick your hackathon's country and say so on the slider. Check the OSRM public demo server is up the night before; it's free but unreliable.

**Distance from the default**: The three plain samples all assumed a team, a Python backend, a live external API at demo time, a physical prop or OCR step, and a five-minute narrated pitch; two of the three converged on the same carbon-aware scheduler. Your answers removed all of that: solo and frontend-only pushed it to bundled data and a fallback that works offline, "judges on a laptop" turned the demo into a hand-over flow, and "polished over complicated" made the year-grid visual the product instead of a feature list. It still shares the samples' use of government emission factors and a before/after number as the reveal, which is the honest core of any climate dashboard.