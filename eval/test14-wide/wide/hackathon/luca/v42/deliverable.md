**Angle**: Instead of tracking what the user does, show what has already happened to a place they know, in their own lifetime: type a city and a birth year, get a personalised, shareable climate card built live from 85 years of public weather data.
**Built from**: 1a (consumer), 2d (public dataset: Open-Meteo's free historical archive), 3a plus your note (solo, frontend only, 24h, so no backend, no OCR, no ML, no hardware), 4c (plan plus pitch).
**Strongest objection**: it's a visualisation, not a product; judges may ask "and then what?" **Test**: on Friday night, pull three cities you'd actually demo and check the numbers move visibly (the hot-day count should at least double between birth year and last year). If they don't, the emotional hit isn't there and you should switch cities or stat before building the UI.
**Other direction**: a frontend-only "run it when the grid is clean" scheduler on the keyless UK Carbon Intensity API. Solid, but it's the idea everyone else in the room will have.

---

# Since You Were Born

**One line:** You type your hometown and your birth year. It shows you the weather you were born into, the weather there now, and the gap in between, as a card you can share.

## Why this one, for you

- One keyless, CORS-friendly API (Open-Meteo), so the whole thing runs in the browser. No server to build or keep alive at demo time.
- The data is the product. The work is in the visuals, which is where your strength is.
- It has a reveal. The number animates up and people reach for their own city. That's the demo.

## What you build

**Data (one fetch per city).**
Geocode the city with `geocoding-api.open-meteo.com/v1/search?name=…`, then pull daily max and mean temperature from `archive-api.open-meteo.com/v1/archive` from 1940-01-01 to last month. That's roughly 31,000 daily values in one JSON response. Compute per year: mean temperature, hottest day, and count of "very hot days". Define very hot relative to the city, not a fixed 35°C, so it works for Oslo and Chennai alike: any day hotter than 90% of days in the 1961–1990 baseline. That's the standard reference period climate services use, and it keeps the "unfair comparison" question off the table.

**Screen 1: the ask.** City field with autocomplete, year picker. Nothing else. Three preset chips (your demo cities) so judges can click instead of type.

**Screen 2: the card.**
- Warming stripes for that city, 1940 to now, one thin bar per year coloured by annual mean. The birth year gets a marker: "you".
- Two big numbers side by side: very hot days in the birth year, very hot days last year. Count-up animation.
- One sentence under them, templated from the data: "Your hometown now has about N more very hot days a year than when you were born."
- Hottest day ever recorded in the dataset, with the date.

**Screen 3: share.** Render the card to a PNG (html2canvas or draw it on a canvas directly), Web Share API on mobile, download on desktop. State lives in the URL (`?city=…&year=…`) so a link reproduces the card. Credit Ed Hawkins' warming stripes in the footer; it's the visual language people recognise and judges will ask.

**Stack:** Vite + React (or Svelte if you're faster there), SVG for stripes, CSS or Framer Motion for the count-up. localStorage cache of API responses keyed by city.

## 24-hour build order

| Hours | Do | Done when |
|---|---|---|
| 0–2 | Scaffold, geocode + archive fetch, log the yearly stats to console | You can see mean temp per year for one city |
| 2–5 | Stripes component from real data | Stripes render and look like the real thing |
| 5–10 | Card layout, two numbers, templated sentence, count-up | The reveal works end to end |
| 10–13 | Screen 1 with autocomplete and presets, URL state | Someone else can use it without you |
| 13–16 | Share to PNG, mobile layout | A card lands in someone's camera roll |
| 16–19 | Polish: loading skeleton, colour scale, type, empty states | It looks finished on a projector |
| 19–21 | Bundle the three demo cities' JSON into the build as fallback | Demo works with Wi-Fi off |
| 21–24 | Rehearse twice, screenshots, README, sleep an hour | — |

Cut order if you fall behind: share → autocomplete → hottest-day line. Never cut the count-up; it's the demo.

## Demo plan (3 minutes)

1. **Open on the blank screen (10s).** Ask the judge nearest you where they grew up and what year. Type it. If they're shy, use preset one.
2. **The reveal (40s).** Say nothing while the stripes draw and the numbers count up. Then read the sentence off the screen.
3. **Second city (30s).** Click preset two, somewhere with a different climate, to show it isn't tuned to one place. Point out the "you" marker moving.
4. **Share (20s).** Hit share, show the PNG on your phone. "This is the bit that travels."
5. **How it works (30s).** One sentence: open reanalysis data, 85 years, computed in the browser, nothing stored. Mention the baseline so the method sounds honest.
6. **Close (20s).** The 60-second pitch below, compressed to its last three lines.

Safety: fallback JSON bundled, Wi-Fi off during rehearsal, screenshots of all three cities in a folder.

## 60-second pitch

Every climate app asks you to do something: log a meal, scan a receipt, change a habit. Most of us close it by day three.

This one asks for two things you already know: where you grew up, and when.

Here's Delhi, 1998. The stripes are every year since 1940, coloured by how warm it was. The marker is the year you were born. These two numbers are the count of very hot days, defined against the city's own climate, in your birth year and last year. Watch them.

That's not a projection. That's the record. Those days already happened, in a place you can picture.

It runs on open reanalysis data, in the browser, with nothing stored. And it ends with a card you can send to the people who grew up there with you.

We don't tell you what to do. We show you what's already changed where you're from, and let you decide what that's worth.

---

**Before you use it**
- Confirm in hour one that the Open-Meteo archive endpoint returns from 1940 for your demo cities and that the browser fetch isn't blocked by CORS; both are true in my experience but check before building on them.
- Pick demo cities where the signal is strong. Run the Friday-night test above before committing to the card layout.
- The pitch uses Delhi and 1998 as an example; swap in a city and year that mean something to you or the room.

**Distance from the default**: the default (and two of the three samples) builds a consumer tool around *doing* something: footprint from receipts, or shifting loads to clean grid hours. This flips to *seeing* what has already happened, because 3a plus "solo, frontend, 24h" rules out OCR, backends and hardware, and 2d asked me to pick the data. It still shares with the samples the core/cut-order plan, a timed demo script with a Wi-Fi fallback, and a share card as the viral hook.