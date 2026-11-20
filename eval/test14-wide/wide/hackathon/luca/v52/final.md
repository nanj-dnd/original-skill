**Angle**: Point the "measure and score" mechanic at a city's large buildings instead of its residents: a browser tool that ranks every reported building by how far its energy use sits above peers of the same type, so a retrofit officer sees the few hundred addresses that move the number.
**Built from**: 1c (planner working from public data), 2a (score behaviour), your constraints (solo frontend developer, 24 hours, no hardware or specific dataset), 4a (short pitch and live demo).
**Strongest objection**: City benchmarking data is self-reported and often a year or more old. Your "worst building" may be a data-entry error or a hospital filed as an office. **Test**: On Saturday night, take the top 10 buildings your ranking produces and look each one up on a map. If more than two are obviously misclassified, add a property-type filter and a visible "self-reported" tag before you pitch.
**Other direction**: Score street segments for urban heat from OpenStreetMap tree and building data, which is keyless via Overpass. It has stronger visuals, but the GIS work alone could eat the 24 hours.

---

## The idea: Retrofit Rank

Many large cities require big buildings to report their annual energy use and publish the results on an open-data portal. New York's Local Law 84 data and Chicago's energy benchmarking are both on public portals with JSON endpoints that need no key. Planners mostly get this as a spreadsheet. Retrofit Rank turns it into the question a city energy office actually asks: *if we can fund 50 retrofits this year, which 50?*

It scores each building against the median of its own property type, converts the gap into reported tonnes of CO₂e, and ranks the city by "tonnes recoverable per building." Everything runs in the browser against the live portal. That keeps the build inside frontend skills, and it gives you the pitch: no model, no server, just the city's own numbers read properly.

## What you'd build (frontend only)

**Data layer.** Fetch the benchmarking dataset straight from the portal's JSON API, page by page, into a Web Worker. Cache the parsed array in IndexedDB so reloads are instant and the demo survives bad Wi-Fi. Commit one JSON snapshot to the repo as the fallback.

**Scoring, in the worker.** For each property type, compute the median and quartiles of energy-use intensity. Each building's score is its distance above the type median multiplied by floor area. Express it as the share of the building's reported emissions it would shed by reaching that median. A single "target" slider (median, top quartile, top decile) re-scores the whole set in one pass. That is the moment that shows it's real computation, not a mock.

**Map.** Use MapLibre with a hexagon aggregation layer:
- Colour each hex by recoverable tonnes.
- Click a hex to see its ranked buildings.
- Click a building to open its card: type, area, reported intensity against its peers, and tonnes.
- Add an area dropdown and a property-type filter.
- Keep state in the URL so any view is a shareable link.

**Export.** One button downloads the current ranked list as CSV. That's the thing a planner would actually take into a meeting.

**24-hour split.**
- **Hours 1–3:** Confirm the endpoint, field names and CORS, and get rows into the worker.
- **Hours 3–8:** Build the scoring and a plain table. If nothing else ships, this is still a demo.
- **Hours 8–16:** Build the map and hex layer.
- **Hours 16–20:** Add the slider, filters, URL state and CSV export.
- **Sleep.**
- **Last 4 hours:** Set up the snapshot fallback, rehearse the demo, and cut anything flaky.

## Demo plan (3 minutes, live)

**0:00** Open on the full-city hex map, already loaded. "This is every large building the city requires to report its energy use. Each hex is coloured by how many tonnes it would save if its buildings performed like the median of their type."

**0:30** Pick the hottest hex. The ranked list appears. "These eight addresses account for most of this neighbourhood's gap. The city already has this data; it just hasn't been sorted this way."

**1:10** Click the top building. Show its card: its intensity against its peers' distribution, its reported emissions, and the recoverable share. Say what the building is, which you'll know from the Saturday-night check.

**1:40** Drag the target slider from median to top quartile. The whole map recolours and the citywide total jumps. "That re-scored every building in the dataset in your browser. No server."

**2:10** Filter to one property type, offices for example. Copy the URL into a new tab to show the view persists. Hit export and open the CSV. "This is the sheet the retrofit team starts Monday with."

**2:40** Close: "One frontend, one public dataset, no model. Any city publishing this data gets the same tool by changing one URL."

Rehearse once against the committed snapshot so you know the demo works offline.

---

**Before you use it**:
- Confirm the exact dataset endpoint and its field names: intensity, emissions, floor area, property type and coordinates.
- Check the API's page limit.
- Check that the API allows cross-origin requests from the browser. If it doesn't, a one-file proxy on a free host is the only server-side piece you'd need.
- Floor-area thresholds and reporting years differ by city, so read the dataset's description before you quote anything on stage.
- If a judge is local, use your own city's name in the pitch.

**Distance from the default**: You moved the user from a consumer to a city planner (1c). Your constraints (solo frontend developer, 24 hours, no hardware or dataset) shrank the build to a browser app against a public portal. Together these replaced both the receipt scanner and the grid scheduler from the samples. The idea keeps the default's "score it and show the gap" mechanic because you chose 2a. It still shares one thing with two of the samples: a committed data snapshot as the demo fallback.