# Idea: **"Since You Were Born"** — a personal climate story for any city

Type your hometown and birth year, and get a scrollable, shareable story of how that place's climate has changed over your lifetime — and where it's projected to be in 2050.

**Why this instead of a carbon footprint tracker:** Judges have seen dozens of footprint calculators, and they demo badly live (lots of form-filling before anything interesting appears). This flips it: one search box, instant visual payoff, and it's personal — you can ask a judge for *their* hometown on stage. It's also pure frontend with free, keyless APIs, so it's genuinely finishable solo in 24h with time left for polish.

---

## What you'd build

**Stack:** React + Vite, Tailwind, Recharts (charts), Framer Motion (scroll reveals), `html-to-image` (share card). No backend.

**Data (all free, no API key, CORS-enabled — Open-Meteo):**
- **Geocoding:** `geocoding-api.open-meteo.com/v1/search?name=Denver` → lat/lon
- **Historical:** `archive-api.open-meteo.com/v1/archive` — daily `temperature_2m_max`, `temperature_2m_min`, `precipitation_sum` from 1940 to today (ERA5 reanalysis)
- **Projections:** `climate-api.open-meteo.com/v1/climate` — daily values 1950–2050 from CMIP6 models (e.g. `EC_Earth3P_HR`, `MRI_AGCM3_2_S`). Double-check exact param names in their docs, but it's the same request style.

All the "analysis" is simple client-side aggregation over daily rows: annual means, count of days above a threshold, decade averages.

**The page (one scroll story, ~6 sections):**

1. **Hero** — "Since you were born in 1994, Denver has warmed **1.6°C**." Big number, animated count-up.
2. **Warming stripes** — one colored bar per year (the Ed Hawkins visual). Trivial to build with divs, instantly recognizable, looks great.
3. **Hot days** — bar chart of days above 32°C/90°F per year, with a line for your birth decade's average vs. the last 10 years.
4. **Your summers** — overlapping distribution of July–Aug daily highs, birth decade vs. now. Shows the whole curve shifting right.
5. **2050** — same stats from the projection model: "By 2050, Denver is projected to have ~X hot days a year — N× what it had when you were born."
6. **Share card** — one-tap export of a tidy PNG with the headline stat, city, and stripes. Gives judges a "what's next" vibe.

**Polish/safety details that matter for a solo build:**
- Cache every API response in `localStorage` keyed by lat/lon. Pre-load 4–5 demo cities during setup so the demo is instant.
- Bundle those cached responses as static JSON too — if venue wifi dies, the demo still works.
- Loading skeletons + a small "Powered by ERA5 / CMIP6 via Open-Meteo" footer (judges like seeing real data sources).
- °C/°F toggle, dark mode. Both are cheap and read as "finished product."

**Rough 24h split:** ~3h data fetching + aggregation functions, ~8h the six sections, ~4h animation/responsiveness/share card, ~3h caching/fallback/edge cases (cities with sparse data, ambiguous names), rest for sleep and rehearsing the demo.

**Stretch (only if ahead):** side-by-side comparison of two cities; "my parents' lifetime" mode (two birth years stacked).

---

## Demo plan — key beats (~3 min)

1. **Hook (20s):** "Climate change is usually a global number. This makes it personal." Ask a judge: "Where did you grow up, and what year were you born?"
2. **Live search (30s):** Type their city in. Headline number animates in. (If their city is obscure or the network is slow, you've got cached fallbacks — but a live hit lands much harder.)
3. **Scroll the story (60s):** Stripes → hot days → summer shift. Narrate one concrete line per section: "When you were a kid, this city got about 8 days over 90°F a year. Last decade: 23."
4. **2050 (30s):** Land on the projection. One sentence: "Same data sources, same city, 25 years out."
5. **Contrast + close (30s):** Switch to a pre-cached, very different city (e.g. Phoenix vs. Reykjavík) to show it's general, hit the share button, show the exported card. End: "Anyone, any city, one search."

Want me to sketch the aggregation functions or the component structure next?