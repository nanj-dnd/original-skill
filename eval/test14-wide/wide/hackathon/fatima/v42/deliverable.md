**Angle**: The city already knows when it rains; what nobody watches is the two hours between water entering a private basement at 1am and thirty ruined cars — so build a basement-level sensor node that turns rate-of-rise into "minutes until damage", wakes the right people, and gives the utility ground truth it doesn't have.
**Built from**: 3a (the December 2023 car park), 1b (building operator), 2b (Arduino + water-level sensors), 4d (3 people, 3-minute live demo, utility engineer judging).
**Strongest objection**: a ₹200 float switch wired to a buzzer detects the same thing — why software? **Test**: before Friday, ask three neighbours whether a siren in the basement at 1am would have woken them, and ask the utility judge during Q&A whether the city receives any readings from private basements today. If both answers are "no", the software layer (reaching people, aggregating buildings) is the product; if the siren would do, pivot to the cheapest possible hardware and make the utility feed the whole pitch.
**Other direction**: skip the utility layer and spend the hours on a resident-only product — sensor, group alerts, a "move your car" workflow — tighter, but it hands the judge nothing.

---

# Basement Watch

## The gap

In December 2023 your building's basement car park flooded overnight and about thirty cars were damaged, because nobody noticed the water rising after midnight. Nothing about that night was undetectable. Rain was forecast, the drains were backing up, the water came up over hours, not seconds. What was missing was a sensor in the one place the city's instruments don't reach — a private basement — and a chain that gets the reading to a person who can move a car.

That's the product: a water-level node for underground car parks that reports level and rate of rise, predicts how long until water reaches the cars, escalates through residents → building security → a utility feed, and, once a few buildings run it, shows the city where its storm drains are backing up before the streets flood.

## What you build (one piece each)

**Hardware (Arduino kit).** One node: the water-level sensor from the kit at the low point of the ramp or sump, a piezo buzzer, and a serial link to the backend. For 36 hours, use USB serial to the laptop, not Wi-Fi — nothing to pair, nothing to drop mid-demo. If the kit has a Wi-Fi board, make it the Sunday-morning stretch, not the base. Sample every second, send `timestamp, level_mm` as a plain line. If the kit's sensor is the resistive strip type, calibrate it in a jug with a ruler on Friday night and store the mapping as a lookup table; it's non-linear and judges will ask.

**Backend (Python).** Four jobs:
1. Read serial (pyserial), store readings in SQLite.
2. Fit a line over the last 60 seconds of readings → rate of rise in mm/min → ETA to three thresholds: tyre, door sill, dashboard. Thresholds are configurable per building; for the demo they're scaled to the tub.
3. Escalation ladder, each step logged with the time it fired: ETA under 60 min → message the residents who have cars in the basement; ETA under 30 min → message the security desk and sound the buzzer; level above sill → fire the utility report.
4. A `/utility` endpoint that publishes building location, current level, rate, and status — one JSON object, the thing the judge can picture ingesting.

For messages, use a Telegram bot: free, no approval queue, works in ten minutes, and a phone pinging on stage is the whole demo. Try Twilio WhatsApp only if Telegram is already working.

**Design.** Two screens, no more.
- *Building screen*: a vertical gauge of the car park with the water line drawn on it, the three thresholds marked, the ETA in large type ("Water reaches tyre height in 4 min"), and the escalation log underneath. This screen's job is to be readable from the back of the room.
- *Utility screen*: a map of Chennai with your building as a live pin and a handful of others clearly labelled **simulated**, each showing level and rate. When several pins in one neighbourhood rise together, the map draws a highlighted zone and the caption "Drainage backing up — probable blocked outfall." That caption is the sentence you want the utility engineer to remember.

## The 3-minute live demo

Props: a clear tub, the sensor clipped inside, a jug with water, a laptop on the projector, the designer holding a phone with the Telegram chat open and the volume up.

**0:00–0:20** — One slide: a photo of a flooded basement car park if you have one, otherwise just the text "December 2023. Our building. ~30 cars. Nobody noticed until morning." Say it in two sentences.

**0:20–1:30** — Start pouring at a steady rate. Building screen on the projector: water line climbs, ETA counts down. Say what's happening in the maths: "It's not watching the level, it's watching the rate." At the first threshold the phone pings — the designer holds it up: *"Basement Watch: water at ramp low point, rising 12 mm/min, reaches tyre height in ~4 min. Move your car."* Keep pouring. Second threshold: buzzer goes off on the Arduino. Stop pouring.

**1:30–2:20** — Switch to the utility screen. Your building is a live pin. Say plainly: "The other pins are simulated — here's what a real network looks like." Replay a scripted 20-second sequence: three nearby pins rise within minutes of each other, the zone highlights. Turn to the judge: "This is a reading the city doesn't get today. Street gauges tell you the road is flooding; basements tell you the drain failed twenty minutes earlier."

**2:20–3:00** — What's real and what isn't, in one breath: one real node, real rate-of-rise maths, real messages; the city map is simulated. Then the cost of a node from the kit's parts, and the ask: which drain catchments the utility would want instrumented first. Stop. Leave 30 seconds for the question that'll come.

**Rehearsal rules.** Time the pour on Saturday night so the first threshold fires within 40 seconds and the second within 70 — mark the jug. Run the whole three minutes five times. Put a `--replay` flag on the backend that feeds a recorded Saturday run into the same pipeline, so if the sensor dies on stage you flip a flag, not a plan. Charge the demo phone.

## 36 hours

- **Friday evening (4h):** Hardware: sensor wired, calibrated, printing serial. Backend: serial reader + SQLite + the rate-of-rise function with a unit test on a fake ramp. Designer: both screens on paper, agree thresholds and the message wording.
- **Saturday (14h):** Morning — escalation ladder, Telegram bot, building screen live on real readings. Afternoon — utility endpoint, map screen, simulated-pin script. Evening — first full run-through with the tub; fix whatever makes the ETA jitter (probably sensor noise: median-filter the last five readings).
- **Sunday morning (6h):** Replay flag, slide, five rehearsals, no new features after 10am. If there's slack: a second node on the ramp entrance to show the backend handling two readings from one building.

## For the utility engineer

Expect three questions. *Why not a float switch?* Because a float switch tells you water is there; the rate tells you how long you have, and the building is at a lot more risk at 1am than at 1pm. *Who maintains the node?* The building's security desk — the dashboard shows "last reading 3s ago" and nags when it stops. *What would the utility do with it?* Treat basements as the earliest upstream sensors on the drainage network, and prioritise crews by which catchments are backing up — ask them whether that's how they'd use it; their answer is worth more than yours.

---

**Before you use it**: confirm which water-level sensor is actually in the kit (resistive strip, float, or ultrasonic — the calibration step differs); confirm whether the venue projector takes HDMI from your laptop; check Telegram isn't blocked on the venue Wi-Fi, otherwise tether. If anyone can confirm which storm-drain outfall serves your building, name it on the map — that one detail makes the utility screen land.

**Distance from the default**: the default was a consumer carbon tracker, and two of the three plain samples converged on a grid-carbon scheduler with a public API, a smart plug, a "scale the story" slide and a roadmap of utility partnerships. This is a building-operator flood node built on your December 2023 car park (3a, 1b) and your Arduino kit (2b), with the demo and the 36-hour plan shaped to three people and a utility judge (4d). What it still shares with the samples: a timed demo script, a physical prop that fires on stage, and a replay fallback — those are hackathon basics, not the samples' idea.