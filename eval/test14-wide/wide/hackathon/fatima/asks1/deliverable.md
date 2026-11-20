Here's the idea, shaped around your December 2023 basement flood — which should be the opening line of your pitch.

## The idea: **Sentinel** — early-warning flood intelligence for shared basements and garages

A low-cost sensor + forecasting system that tells a building manager *hours before* a basement floods, not after 30 cars are underwater. It fuses two signals that are usually separate:

1. **Live water-level sensors** in the garage/basement (your Arduino kit)
2. **Public weather and rainfall forecasts** for the building's location

The core insight: a sensor alone only tells you water is already there. A forecast alone doesn't know your building's drainage. Sentinel learns the relationship between rainfall and your basement's actual water response, so it can warn *before* the first sensor trips — and escalate aggressively once it does.

Why this fits your judges: it's genuinely adaptation (not mitigation), it has a real, specific incident behind it, and a water-utility engineer will immediately recognize the problem of "sewer surcharge + combined systems + nobody monitoring private basements." It's not a carbon calculator.

---

## What you'd build (36 hours, 3 people)

### Hardware (your hardware person)
- Arduino with 2–3 water-level sensors mounted at different heights on a vertical rail (e.g., 5 cm, 15 cm, 30 cm) — this gives you *rate of rise*, not just presence. Rate of rise is the thing that matters for "do I have 3 hours or 20 minutes."
- Serial/WiFi out to the backend (ESP32 if you have one; otherwise Arduino → USB → laptop acting as gateway is fine for the demo).
- Build a **demo rig**: a clear plastic tub, the sensor rail, and a jug or small pump. This is your live-demo prop — see below.
- Stretch: a buzzer/LED strip on the rig as the "building alarm."

### Backend (you)
- Python service (FastAPI) that ingests sensor readings, stores a time series, and computes:
  - Current level, rate of rise (cm/min), and projected time-to-threshold (e.g., "water reaches vehicle sill height in ~45 min at current rate")
  - Risk score from forecast: pull hourly precipitation from a public API (Open-Meteo is free, no key, has forecast + historical; NWS API if you're US). Weight by short-horizon rainfall intensity (mm/hr over next 3–6 hrs).
  - Combined alert state: **Watch** (forecast-driven, no water yet) → **Warning** (water detected, slow rise) → **Emergency** (fast rise or threshold crossed)
- Alerting: SMS via Twilio (or just a push to the dashboard + a simulated phone screen if you'd rather not deal with credits). Escalation ladder: notify manager → if unacknowledged in N minutes, notify residents with cars in the garage.
- A simple "building profile": sill height of lowest parked car, sump pump present Y/N, number of vehicles. This is what makes it feel like a product, not a sensor demo.
- Technical-depth hook for the utility engineer: use historical rainfall from Open-Meteo to pull the actual December 2023 storm and show what Sentinel *would have* flagged that night. Even a crude threshold model becomes compelling when it's run against the real event.

### Frontend (your designer)
- One dashboard view: building status, live water-level graph, rate of rise, time-to-threshold countdown, forecast strip for the next 12 hours, and an incident log.
- A mobile-sized "manager phone" view showing the alert and an Acknowledge button. This can literally be a browser tab at phone width on a second screen or a real phone.
- Keep it to two screens. Resist adding a map, a settings page, or a marketplace.

### Division of the 36 hours
- **Hours 0–4:** Agree on sensor data format (JSON over serial), alert thresholds, and the two screens. Hardware person wires sensors; you stub the API with fake data; designer mocks screens.
- **Hours 4–16:** Hardware streams real readings. You build ingestion, rate-of-rise, forecast pull, alert state machine. Designer builds the dashboard against your stub.
- **Hours 16–26:** Integrate. Build the physical demo rig. Wire SMS/notification. Run the December 2023 backtest.
- **Hours 26–32:** Rehearse the demo end-to-end at least 5 times. Fix whatever breaks.
- **Hours 32–36:** Sleep, polish, buffer. Do not add features here.

---

## The 3-minute live demo

**0:00–0:25 — The hook.** "In December 2023, our apartment's basement flooded overnight. Thirty cars were destroyed. Nobody knew until morning. The sensor that would have prevented it costs eight dollars." Show one photo if you have one.

**0:25–0:50 — The forecast layer.** Dashboard open. Show the building at Watch status because of incoming rain in the forecast. Point to the historical backtest: "Here's what Sentinel saw the night of our actual flood — it would have raised a Watch at 9 PM and a Warning by 11."

**0:50–2:15 — The live sensor demo.** This is the whole pitch. Pour water into the rig. Audience watches the level graph climb in real time. First sensor trips → status flips to Warning, the manager's phone buzzes on screen. Keep pouring → rate-of-rise jumps, time-to-threshold countdown drops from "2 hrs" to "12 min" → Emergency, buzzer on the rig fires, escalation to residents triggers. Press Acknowledge on the phone. Pouring water in front of judges is memorable and proves it's not a mock.

**2:15–2:45 — Why it's real.** Bill of materials under $40 per building. Works with any sump/garage. Point out the hardware person's rail design and the rate-of-rise logic — that's your technical-depth moment. Mention the utility angle directly to the judge: aggregated anonymized basement data could give the city a real-time map of where the sewer system is surcharging, something they currently can't see.

**2:45–3:00 — Close.** "Thirty cars. One sensor. We're not building a dashboard — we're building the thing that wakes someone up." Stop talking.

---

## Risks and how to de-risk them

- **Serial/WiFi flakiness during demo:** Have a "replay" mode that feeds pre-recorded sensor data into the same pipeline. Switch to it silently if the hardware stalls. Still pour the water for theater.
- **Weather API down at demo time:** Cache the forecast response locally the morning of.
- **SMS not arriving on stage:** Show the manager-phone view on screen and treat the real SMS as a bonus.
- **Scope creep:** The thing most likely to sink this is building a third screen. Two screens, one rig, one alert ladder.

If you want, I can sketch the sensor JSON schema and the alert state machine next so you and the hardware person can start in parallel immediately.