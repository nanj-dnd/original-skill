**Angle**: For individuals, the climate product worth a weekend isn't another tool that measures their guilt. It's one that helps them on the day the climate actually touches them: a walking router that finds the shadiest route during a heatwave.
**Built from**: 1a (individuals, kept), 2a (2–3 software people, no hardware, so a map-and-data product with no device stunts), 3b (judges reward polish, and moving shadows on a map sell themselves without a slide), 4b (judge-facing).
**Strongest objection**: It's adaptation, not mitigation. If the judges read "climate" as "cut emissions", a shade router looks off-theme. **Test**: read the brief and rubric now. If either says "reduce emissions", or the last winners were all mitigation plays, drop it for the other direction below. Second test, Friday night: pull the OpenStreetMap buildings for the 2 km around the venue and check what share have a height or levels tag. If it's under about a third, you'll be guessing heights for most of the map.
**Other direction**: A browser extension that, on any flight-booking page, shows the rail alternative with time, price and emissions side by side. The lower-carbon choice becomes visible at the one moment it's actually made.

---

# Shadeway: the shadiest way to walk there

## What the judges will see

The screen shows a map of the streets outside this venue, with the clock set to 2 pm, 15 July. The usual fastest route from the door to a nearby landmark is drawn in orange, with its share of the walk in full sun shown beside it. One tap, and a second route appears in blue. It takes different streets, picked because the building shadows fall across them at that hour, and comes with its own extra walking time and shade share.

Then the presenter drags the time slider. The building shadows sweep across the map as the afternoon moves, and the shaded route re-draws itself, taking different streets at 11 am and different again at 4 pm.

That's the pitch. No slides are needed until the last thirty seconds.

## The idea

Record heat is now a routine part of summer. Cities respond with cooling plans, tree budgets and heat-health warnings, but none of that helps the person who has to walk twenty minutes across town at two in the afternoon. Every maps app will give you the fastest route. None will give you the coolest one, even though the data to compute it is public and deterministic: building footprints, building heights, and where the sun is.

Shadeway routes pedestrians by sun exposure instead of distance:
1. You pick a start, an end and a time.
2. It computes where the building shadows fall at that minute and scores every street segment by how much of it is shaded.
3. It returns two routes: the fastest, and the shadiest within a time budget you set (default: up to five minutes longer).
4. Each route comes with plain figures: length, walking time, and the share of the walk in shade.

It works anywhere OpenStreetMap has buildings, which covers most cities. It needs no sensors, no accounts and no user data.

## What we build

There are three tracks, all covering one neighbourhood. Everything is precomputed so the demo never touches the network. With three people, take one track each. With two, one person does shadows and routing in sequence, and the other owns the map from the first hour.

**Track 1: Shadows (data).** Saturday.
- Pull building footprints for a ~2 km box around the venue from the Overpass API.
- Take height from the `height` tag. If that's missing, use `building:levels` × 3 m, and failing that, a default by building type.
- For a given timestamp, get the sun's azimuth and elevation with the `pysolar` or `suncalc` libraries.
- Project each footprint along the shadow vector by height ÷ tan(elevation), and union the footprint with its projection to get the shadow polygon (Shapely).
- Precompute the merged shadow layer for every 30 minutes of a single July day and save it as GeoJSON.

**Track 2: Routing.** Saturday into Sunday morning.
- Load the walking network with `osmnx`.
- For each edge and each timestamp, compute the fraction of the edge's length that lies inside the shadow union.
- Set edge cost = length × (1 + w × sun fraction), where w is the user's "how much longer am I willing to walk" setting.
- Run Dijkstra twice: w = 0 for the fastest route, the user's w for the shadiest. Return both with length, time and shade share.
- Wrap it in a small FastAPI service that reads only the precomputed files.

**Track 3: The map.** Saturday through Sunday.
- Use MapLibre or Leaflet. Draw shadows as a translucent dark layer and the two routes in orange and blue.
- Add a time slider across the bottom, click-to-set start and end, and a side panel with the two routes' numbers.
- Spend Sunday making it look finished, since polish is what's being judged:
  - smooth shadow transitions as the slider moves
  - a sun-exposure bar that fills as you drag
  - a second precomputed neighbourhood, so you can show it isn't a one-block trick

**Deliberately out of scope**: trees (no reliable height data), live weather, a mobile app, user accounts. Say so if asked. It reads as judgement, not omission.

## Demo script (3 minutes)

- **0:00**: Open on the map, with no title slide. "This is the walk from this room to [the landmark you chose], at two o'clock on a July afternoon." The fastest route appears with its shade share.
- **0:25**: "Here's the same walk, if you'd rather not be in the sun." The shadiest route appears beside it. Read the two numbers off the panel.
- **0:50**: Drag the slider from 10 am to 5 pm. Let the shadows move and the route re-draw. Don't talk over the first few seconds of this.
- **1:30**: One line on why. Cities are spending on heat plans and maps apps optimise for time, but nobody has built the layer in between. The inputs are open data and geometry, so it runs anywhere.
- **2:00**: Switch to the second precomputed neighbourhood. Same thing, different streets. "Any city with OpenStreetMap buildings."
- **2:30**: One slide on who ships this: a "cool route" toggle in any maps product, a widget for city heat-warning pages, transport authorities routing people to shaded stops. Then the roadmap: trees, awnings, live heat data.
- **2:50**: Back to the map, slider at 2 pm, the shaded route lit up. Stop there.

**Safety**:
- All data is local and precomputed, so Wi-Fi can't kill the demo.
- Record the whole flow on Saturday night as a backup video.
- Show the July date clearly on screen. It's November, and a judge will otherwise ask why the shadows look like summer.

## Why this wins a polish round

It's visual before it's explained. It answers a question the judge has personally had on a hot day. It does one thing completely instead of five things partly. The maths behind it is simple, so there's nothing to hand-wave when someone asks how the shadows are computed.

---

**Before you use it**
- Run the real routes before writing the opening line. The fastest-versus-shadiest gap depends on your streets. If it's small at 2 pm, open on the time of day where the difference is starkest, or pick a different landmark.
- The pitch has no "shade makes it feel X degrees cooler" figure, because I couldn't verify one. If you want it on the closing slide, find a citable figure from urban-climate research on mean radiant temperature in shade and put the citation on screen.
- Check OSM building-height coverage for your venue's area before committing (the Friday test above). If it's thin, label heights as estimates in the panel rather than hiding it.
- Swap in the real landmark at 0:00. A hot-day walk someone on the team has actually made would land harder still.

**Distance from the default**: This moves from a consumer footprint tracker (emissions, nudges, a CO₂-saved counter) to a heat-adaptation router. Two answers drove that. 3b (polish over an impact number) favours a visual demo, and 2a (no hardware) ruled out the smart-plug stunt. The three samples all converged on either a receipt scanner or a carbon-aware scheduler with a "kg CO₂ avoided" counter and a lamp switching on, and none of that is here. It still shares some things with them: an individual-facing web app, a timed demo script with a backup video, and a build split into tracks with a weekend timeline.