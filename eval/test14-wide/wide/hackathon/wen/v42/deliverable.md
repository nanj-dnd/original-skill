**Angle**: Build for the city's adaptation decision, not the resident's emissions: a map that tells a parks or transit department where to plant shade next, using data the city already publishes.
**Built from**: 1c (public body as user), 2d (low risk: no hardware, no live API at demo time, no backend), 3a (pick for you, so it uses open data any team can download Friday night), 4d (mixed panel: a clear buyer for the business judge, real geo work for the engineer, a heat story for the impact judge).
**Strongest objection**: adaptation projects don't produce a "tonnes avoided" figure, and some judges only know how to score that. **Test**: on Friday night, spend 30 minutes confirming one candidate city has a tree inventory with coordinates and bus stops in OpenStreetMap, then show the rough map to one person outside the team and ask "what should the city do?" If they can't answer in ten seconds, the map isn't carrying the argument and you should switch to the other direction below.
**Other direction**: same public-body user, mitigation instead of adaptation: a tool that ranks a city's own buildings (from its published energy-benchmarking disclosures) by retrofit payback, so the facilities department knows which roof to insulate first.

---

# Hot Stop: where should the city plant shade first?

## The idea

Cities are getting hotter, and the people most exposed are the ones standing at a bus stop in the afternoon with no tree over it. Most cities already publish two things that answer "where is that worst?": a street-tree inventory with coordinates (New York, San Francisco, Melbourne and others release theirs as open data) and a transit network that's in OpenStreetMap. Nobody has joined them. Hot Stop does: it scores every bus stop by how little shade it has and how many people use it, and gives the parks department a ranked list of where the next hundred trees do the most good.

The user is a city employee with a planting budget and no analyst. The output is the memo they'd otherwise take a month to write.

## What you'd build

Everything is precomputed into one GeoJSON file served as a static page. No backend, no API calls during the demo, nothing that can go down on stage.

**Saturday: data and score** (one or two people)
1. Download the tree inventory CSV for your chosen city. Keep latitude, longitude, and trunk diameter or canopy size if the column exists.
2. Pull bus stops for the same city from the Overpass API (one query, saved to disk). Keep the stop's coordinates and the number of routes serving it, which is in the OSM tags for most well-mapped cities.
3. For each stop, compute a shade score: number of trees within 25 metres, weighted by trunk diameter where you have it. Compute a demand proxy: routes serving the stop, or stop-level ridership if the transit agency publishes it. Priority = high demand, low shade.
4. Write the result out as GeoJSON with the score fields on each stop.

**Saturday: the map** (one or two people, in parallel)
1. A single Leaflet page. Stops drawn as circles, coloured from green (shaded) to red (exposed), sized by demand.
2. A side panel listing the top 20 priority stops with their street address.
3. Click a stop: panel shows trees nearby, routes served, and a link to Street View so the judge can see for themselves that it's a bare pavement.
4. A "plant here" control: add one to five trees of a chosen size at the selected stop and watch its score and rank update. This is the only interactive computation and it runs in the browser.

**Sunday morning, pick one if ahead**
- A neighbourhood view: aggregate stops by district so the map also says which part of the city is getting the least shade per rider.
- An export button that produces the top-50 list as a CSV, because that's the form a city actually consumes.

**Stack**: Python and pandas for the Saturday data step, plain HTML plus Leaflet for the page, no framework, no database. Deploy as a static site so the demo link works from any laptop.

## Demo plan (four minutes)

1. **Open on the map, already loaded** (20 seconds). Say the city's name. "Every dot is a bus stop. Red means someone waits there in full sun. We built this from two files the city already publishes."
2. **Zoom to the worst cluster** (40 seconds). Pick one red stop in a dense area. Open the panel: trees within 25 metres, routes served, Street View. Let the picture do the work. One sentence: "This stop has more routes than almost any in the city and not one tree."
3. **The ranked list** (40 seconds). Scroll the top-20 panel. "This is the list a parks department would spend a month producing. We produced it in a weekend from open data, and it updates when they update the tree inventory."
4. **Plant here** (40 seconds). Add three trees at the selected stop. Score changes, it drops down the ranking, the next-worst stop rises. "The budget question isn't 'should we plant', it's 'where first'. This answers it."
5. **Who uses it** (40 seconds). Name the buyer: the parks department and the transit agency, who split the cost of a shelter or a tree today without shared data. Mention that the same join works for any city with a tree inventory and an OSM network, and that the method extends to schools, clinics and playgrounds with no code change beyond the Overpass query.
6. **Close** (20 seconds). "Mitigation gets most of the hackathon ideas. The heat is already here. This is a tool for the people who have to deal with it on Monday."

**Demo insurance**: the page is static, so your only failure mode is the laptop. Keep a second copy on a phone and a screenshot deck as the last fallback. Rehearse the click sequence twice so step 2 lands on the same stop every time.

**Splitting a mixed team**: data person owns the score and the GeoJSON; map person owns the page; a third person owns the pitch, the Street View checks and the fallback deck, and tests the data person's output against five stops by hand on Saturday afternoon. If you are only two, drop the "plant here" control before anything else; the ranked list is the product.

---

**Before you use it**: confirm your chosen city's tree inventory actually includes coordinates and a diameter or canopy column (some only have addresses). Check whether the transit agency publishes stop-level ridership; if it does, use it instead of route count and say so on the slide, since it makes the demand side much harder to argue with. I haven't verified any one city's current file, so do that check Friday before committing.

**Distance from the default**: the three samples all build for an individual consumer and lead with a "kg CO₂ saved" counter, a live API or OCR step, and a scale-up slide; two of the three are the same carbon-aware scheduler with a smart-plug lamp. Your 1c moved the user to a public body and the problem from emissions to heat exposure; 2d removed the live dependencies and hardware. What it still shares with the samples: a must-have/stretch split, a timed demo with a single interactive reveal, and the advice to keep a fallback.