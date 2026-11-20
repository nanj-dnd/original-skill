**Angle**: Point the "measure and score" mechanic at a city's large buildings instead of its residents: a browser tool that ranks every reported building by how far its energy use sits above peers of the same type, so a retrofit officer sees the few hundred addresses that move the number.
**Built from**: 1c (planner working from public data), 2a (score behaviour), your constraints (solo frontend, 24h, no backend or hardware), 4a (technical judges, live demo).
**Strongest objection**: city benchmarking data is self-reported and a year or more old, so your "worst building" may be a data-entry error or a hospital filed as an office. **Test**: on Saturday night, take the top 10 your ranking produces and look each up on a map; if more than two are obviously misclassified, add a property-type filter and a visible "self-reported" tag before you pitch.
**Other direction**: urban-heat scoring of street segments from OpenStreetMap tree and building data, keyless via Overpass; stronger visuals, but the GIS work alone could eat the 24 hours.

---

## The idea: Retrofit Rank

Many large cities require big buildings to report their annual energy use, and publish the results on an open-data portal (New York's Local Law 84 data and Chicago's energy benchmarking are both on public portals with JSON endpoints that need no key). Planners mostly get this as a spreadsheet. Retrofit Rank turns it into the question a city energy office actually asks: *if we can fund 50 retrofits this year, which 50?*

It scores each building against the median of its own property type, converts the gap into reported tonnes of CO₂e, and ranks the city by "tonnes recoverable per building." Everything runs in the browser against the live portal, so the pitch is: no model, no backend, just the city's own numbers read properly.

## What you'd build (frontend only)

**Data layer.** Fetch the benchmarking dataset straight from the portal's JSON API, paged, into a Web Worker. Cache the parsed array in IndexedDB so reloads are instant and the demo survives bad Wi-Fi. Commit one JSON snapshot to the repo as the fallback.

**Scoring, in the worker.** For each property type, compute the median and quartiles of energy-use intensity. Each building's score is its distance above the type median, multiplied by floor area, expressed as the share of its reported emissions it would shed by reaching that median. A single "target" slider (median / top quartile / top decile) re-runs the scoring over the whole set in one pass, which is the moment that shows judges it's real computation, not a mock.

**Map.** MapLibre with a hexagon aggregation layer: colour by recoverable tonnes per hex, click a hex for its ranked buildings, click a building for its own card (type, area, reported intensity vs. peers, tonnes). A borough/area dropdown and a property-type filter; state lives in the URL so any view is a shareable link.

**Export.** One button that downloads the current ranked list as CSV. That's the thing a planner would actually take into a meeting.

**24-hour split.** Hours 1–3: confirm the endpoint, field names and CORS, get rows into the worker. Hours 3–8: scoring and a plain table (if nothing else ships, this is a demo). Hours 8–16: map and hex layer. Hours 16–20: slider, filters, URL state, CSV. Sleep. Last 4: snapshot fallback, demo rehearsal, kill anything flaky.

## Demo plan (3 minutes, live)

**0:00** Open on the full-city hex map already loaded. "This is every large building the city requires to report its energy use. Each hex is coloured by how many tonnes it would save if its buildings performed like the median of their type."

**0:30** Pick the hottest hex. The ranked list appears. "These eight addresses account for most of this neighbourhood's gap. The city already has this data; it just hasn't been sorted this way."

**1:10** Click the top building. Show its card: its intensity against its peers' distribution, its reported emissions, the recoverable share. Say what it is (you checked on Saturday night).

**1:40** Drag the target slider from median to top quartile. Watch the whole map recolour and the citywide total jump. "That re-scored every building in the dataset in your browser. No server."

**2:10** Filter to one property type (offices, say) and copy the URL into a new tab to show the state persists. Hit export; open the CSV. "This is the sheet the retrofit team starts Monday with."

**2:40** Close: "One frontend, one public dataset, no model. Any city publishing this data gets the same tool by changing one URL."

Rehearse against the committed snapshot once, so you know the demo works offline.

---

**Before you use it**: Confirm the exact dataset endpoint, field names (intensity, emissions, floor area, property type, coordinates), the API's page limit, and that it allows cross-origin requests from the browser; if it doesn't, a one-file proxy on a free host is your only backend. Floor-area thresholds and reporting years differ by city, so read the dataset's description before you quote anything on stage. Add your own city's name in the pitch if a judge is local.

**Distance from the default**: The user changed from a consumer to a city planner (1c) and the build collapsed to a pure frontend against a public portal (your constraints), which replaced the receipt-scanner and the grid-scheduler alike. It keeps the default's "score it and show the gap" mechanic because you chose 2a, and it shares one thing with two of the samples: a committed data snapshot as the demo fallback.