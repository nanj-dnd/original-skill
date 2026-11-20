**Angle**: For individuals, the climate product worth a weekend isn't another tool that measures their guilt — it's one that helps them on the day the climate actually touches them: a walking router that finds the shadiest route during a heatwave.
**Built from**: 1a (individuals, kept), 2a (2–3 software people, no hardware → a map-and-data product, no device stunts), 3b (judges reward polish → the demo is moving shadows on a map, which sells itself without a slide), 4b (judge-facing).
**Strongest objection**: It's adaptation, not mitigation. If the judges read "climate" as "cut emissions", a shade router looks off-theme. **Test**: read the brief and rubric now; if either says "reduce emissions" or the last winners were all mitigation plays, drop it for the other direction below. Second test, Friday night: pull the OpenStreetMap buildings for the 2 km around the venue and check what share have a height or levels tag — under about a third and you'll be guessing heights for most of the map.
**Other direction**: A decision-point tool rather than a tracker — a browser extension that, on any flight-booking page, shows the rail alternative with time, price and emissions side by side, so the lower-carbon choice is visible at the one moment it's actually made.

---

# Shadeway — the shadiest way to walk there

## What the judges will see

A map of the streets outside this venue. The clock on screen says 2 pm, 15 July. The usual fastest route from the door to the station is drawn in orange: almost all of it in full sun. One tap, and a second route appears, two streets over, running along the shaded side of the tall blocks and under the covered arcade. It's a couple of minutes longer and most of it is out of the sun.

Then the presenter drags the time slider. The building shadows sweep across the map as the afternoon moves, and the shaded route re-draws itself — different streets at 11 am, different again at 4 pm.

That's the pitch. No slides needed until the last thirty seconds.

## The idea

Record heat is now a routine part of summer, and cities respond with cooling plans, tree budgets and heat-health warnings. None of that helps the person who has to walk twenty minutes across town at two in the afternoon. Every maps app will give you the fastest route; none will give you the coolest one, even though the data to compute it — building footprints, building heights, and where the sun is — is public and deterministic.

Shadeway routes pedestrians by sun exposure instead of distance. You pick a start, an end, and a time. It computes where the building shadows fall at that minute, scores every street segment by how much of it is shaded, and returns two routes: the fastest, and the shadiest within a time budget you set (default: up to five minutes longer). Each comes with a plain figure — length, walking time, and the share of the walk in shade.

It works anywhere OpenStreetMap has buildings, which is most cities, and it needs no sensors, no accounts and no user data.

## What we build

Three parallel tracks, one neighbourhood, everything precomputed so the demo never touches the network.

**Track 1 — Shadows (data).** Pull building footprints for a ~2 km box around the venue from the Overpass API. Height comes from the `height` tag, else `building:levels` × 3 m, else a default by building type. For a given timestamp, get the sun's azimuth and elevation (the `pysolar` or `suncalc` libraries), project each footprint along the shadow vector by height ÷ tan(elevation), and union the footprint with its projection to get the shadow polygon (Shapely). Precompute the merged shadow layer for every 30 minutes of a single July day and save as GeoJSON. One person, Saturday.

**Track 2 — Routing.** Load the walking network with `osmnx`. For each edge and each timestamp, compute the fraction of the edge's length that lies inside the shadow union. Edge cost = length × (1 + w × sun fraction), where w is the user's "how much longer am I willing to walk" setting. Run Dijkstra twice — w = 0 for fastest, user's w for shadiest — and return both with length, time and shade share. Wrap it in a small FastAPI service that reads only the precomputed files. One person, Saturday into Sunday morning.

**Track 3 — The map.** MapLibre or Leaflet. Shadows drawn as a translucent dark layer; the two routes in orange and blue; a time slider across the bottom; click-to-set start and end; a side panel with the two routes' numbers. Sunday is for making this look finished: smooth shadow transitions as the slider moves, a sun-exposure bar that fills as you drag, and a second precomputed neighbourhood so you can show it isn't a one-block trick. One person throughout, since polish is what's being judged.

**Deliberately out of scope**: trees (no reliable height data), live weather, mobile app, user accounts. Say so if asked — it reads as judgement, not omission.

## Demo script (3 minutes)

- **0:00** — Open on the map, no title slide. "This is the walk from this room to the station, at two o'clock on a July afternoon." Fastest route appears with its shade share.
- **0:25** — "Here's the same walk, if you'd rather not be in the sun." Shadiest route appears beside it; read the two numbers off the panel.
- **0:50** — Drag the slider from 10 am to 5 pm. Let the shadows move and the route re-draw. Don't talk over this for the first few seconds.
- **1:30** — One line of why: cities are spending on heat plans, maps apps optimise for time, nobody has built the layer in between — and the inputs are open data and geometry, so it runs anywhere.
- **2:00** — Type a different neighbourhood (the second precomputed one). Same thing, different streets. "Any city with OpenStreetMap buildings."
- **2:30** — One slide: who ships this. A "cool route" toggle in any maps product; a widget for city heat-warning pages; transport authorities routing people to shaded stops. Roadmap in three words each: trees, awnings, live heat.
- **2:50** — Back to the map, slider at 2 pm, the shaded route lit up. Stop there.

**Safety**: all data is local and precomputed, so Wi-Fi can't kill it. Record the whole flow Saturday night as a backup video. Set the demo clock to July explicitly on screen — it's November, and a judge will otherwise ask why there are shadows at all.

## Why this wins a polish round

It's visual before it's explained, it answers a question the judge has personally had on a hot day, and it does one thing completely instead of five things partly. The underlying maths is simple enough that there's nothing to hand-wave when someone asks how the shadows are computed.

---

**Before you use it**
- The pitch avoids a "shade makes it feel X degrees cooler" number because I couldn't verify one here. If you want it on the closing slide, find a citable figure from urban-climate research (ASU's work on mean radiant temperature in shade is the usual source) and put the citation on screen.
- Check OSM building-height coverage for your venue's area before committing (the Friday test above). If it's thin, say "estimated heights" in the panel rather than hiding it.
- Add a real detail if you have one: a hot-day walk someone on the team actually made, or the venue's actual nearest station, makes the opening land harder than a generic "the station".

**Distance from the default**: Moved from a consumer footprint tracker (emissions, nudges, a CO₂-saved counter) to a heat-adaptation router — driven by 3b (polish over an impact number favours a visual demo) and 2a (no hardware ruled out the smart-plug stunt). The three samples all converged on either a receipt scanner or a carbon-aware scheduler with a "kg CO₂ avoided" counter and a lamp switching on; none of that is here. What this still shares with them: it's an individual-facing web app, it's a timed demo script with a backup video, and the build is split into core and stretch.