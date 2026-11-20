**Angle**: For a solo frontend dev with no data of your own, build **Twins** — a dashboard over an open city building-energy dataset that finds a building's "twins" (same type, size, age) and shows judges how wildly they differ in energy use. The insight is in the data, not the code, so a static site is the whole product.
**Built from**: 1b (building operators), 2a (insight over action), 3d (no own data, so a public dataset carries it), 4a + solo / frontend / 24h / must finish.
**Strongest objection**: "That's a chart over someone else's CSV, not a product." **Test**: before writing any UI, open the dataset, filter one property type (say schools), sort by energy intensity, and compare the top and bottom quartile at similar floor area. If the spread isn't comfortably over 2×, the reveal is weak — switch property type or city before you commit.
**Other direction**: a grid-carbon-intensity dashboard that tells a building when its HVAC or EV chargers should run. Fits 1b and loves a chart, but depends on a live API and is what most of the room will bring.

---

## Twins — every building has a few, and some of them use five times the energy

### The idea

Cities like New York, Seattle and Chicago make large buildings report their energy use every year, and publish it. Each row is a building: type, floor area, year built, energy per square foot, and usually its CO₂e. Almost nobody outside the compliance office looks at it.

Twins is a single-page site where a building operator — a school facilities manager, a small landlord, an office tenant — enters three things (type, floor area, year built) and sees the buildings most like theirs, where they sit in that group, and what the gap between them and the median is worth in energy and carbon. No sensors, no account, no backend.

The point for judges is the one they didn't know: two buildings with the same use, size and age, on the same grid, in the same climate, can differ several-fold — and the cheap half of that gap is operations (schedules, setpoints, equipment left running), not retrofits.

### What you'd build

All of this is frontend. The data ships as a trimmed JSON file in the repo; the deployed site is static.

**1. Data prep (first 2–3 hours, do it once, do it early)**
Pick one city. Seattle's Building Energy Benchmarking dataset is the easiest — a single CSV per year with property type, floor area, year built, site EUI and total GHG emissions. NYC's Local Law 84 data is bigger and has the same fields. Load it in the browser with Papaparse, drop rows with missing EUI or zero floor area, keep the ten or so columns you need, and save the result as `buildings.json`. A few thousand to a few tens of thousands of rows is fine in memory; you don't need DuckDB.

**2. The distribution view**
Pick a property type from a dropdown. Show a strip plot or histogram of energy intensity for every building of that type, each dot a building, hover for name, size and year. This single chart is the product. Make it good: log scale if the tail is long, median marked, quartiles shaded.

**3. Twin finder**
Three inputs: type, floor area, year built. Compute the nearest 20–30 buildings by normalised distance on area and age, highlight them on the distribution, and place a "you" marker at whatever EUI the user enters (or at the median if they don't know theirs). Show a small ranked table of the twins: the three most efficient and the three least, with EUI and CO₂e side by side.

**4. The gap**
One number, computed live: if this building moved from its position to the median of its twins, how many kWh and tonnes CO₂e per year is that. Then the flip: a toggle that applies the same move to *every* building above median in the whole dataset and shows the citywide total. Use the dataset's own GHG column so you never have to defend an emissions factor.

**5. Polish (the last quarter of your time)**
Transitions when the twin set changes, a sensible empty state, a one-line source citation at the foot of every chart, and a shareable URL that encodes the inputs so a judge can open it on their own phone.

**Stack**: Vite + whatever framework you're fastest in, a charting library you already know (D3 or Observable Plot for the strip plot; Recharts if you want speed over control), Papaparse for the one-off prep, deploy to Vercel, Netlify or GitHub Pages. No keys, no rate limits, nothing to go down at hour 23.

**Rough clock for 24 hours solo**: 0–3 data prep and a hard-coded chart on screen; 3–9 distribution view done properly; 9–14 twin finder; 14–18 the gap numbers and citywide toggle; 18–21 polish and the URL state; 21–24 rehearse, fix what breaks, sleep an hour.

### Demo plan

Build the pitch around the chart, not around slides. Three screens, four minutes.

**Screen one — the dots.** Open on the distribution for schools (or whichever type passed the spread test). Don't explain the product yet. Say what the chart is: "Every public-school building in Seattle, one dot each, by energy per square foot. Same climate, same job." Let the judges see the spread themselves for a few seconds. Then point at the two ends: "This one and this one are about the same size and age."

**Screen two — the twins.** Type in a building: say 60,000 ft², built 1965, school. The twins light up. Walk down the table: "Her building's most efficient twin uses a third of the energy. Nothing exotic about it — same era, same size." Now type an EUI near the top of the pack and show the gap number: "If this building just reached the middle of its own twins, that's X tonnes a year." (X comes from the data on the night; don't pre-write it.)

**Screen three — the city.** Flip the toggle. The citywide figure appears: what it's worth if every above-median building reached the median. This is the line judges repeat afterwards. Close with who it's for: the facilities manager who has never seen this chart, who now has a list of three buildings to phone and ask what they're doing differently.

If there's time for a question, the one you'll get is "where does the data come from?" — the citation is already in the footer, so you point at it.

### Why it finishes

Every risky thing in a hackathon — OCR, live APIs, hardware, auth, a backend — is absent. The only thing that can fail is the data being dull, and the spread test on hour one tells you that before you've built anything. Everything after that is the thing you're good at.

---

**Before you use it**
- I couldn't run a search in this session, so confirm the exact column names in the Seattle (data.seattle.gov, "Building Energy Benchmarking") or NYC (NYC Open Data, "Local Law 84" energy and water disclosure) CSV before the hackathon — the fields I've described (property type, floor area, year built, site EUI, GHG emissions) are in both to my knowledge, but names vary by year.
- Run the spread test first. Don't quote a "5×" or "several-fold" figure on stage until the dataset has shown it to you.
- If the hackathon is outside the US, check your city for an equivalent (UK Display Energy Certificates are the nearest open dataset for public buildings) — the product is identical, only the JSON changes.

**Distance from the default**: Two of the three plain answers were the same grid-carbon scheduler (live intensity API, "kg CO₂ avoided" counter, smart-plug lamp as the money shot, Python backend, 3–4 people); the third was a receipt scanner. All three assumed a consumer, a backend and a team. This piece changed because of 1b (operators, not households), 2a (the demo proves a fact rather than performs an action) and your solo/frontend/24h constraint, which removed the API and backend entirely. What it still shares with them: a public dataset as the data source, a CO₂ figure on screen, and a demo that ends by scaling one case up to a city.