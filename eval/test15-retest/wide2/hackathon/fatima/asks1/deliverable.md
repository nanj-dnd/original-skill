# Tideline: Basement Flood Early Warning for Apartment Buildings

## The idea

Tideline is a low-cost sensor network and alert system for apartment basements and parking garages. It doesn't just say "there's water." It measures **how fast the water is rising**, estimates **how long until cars are damaged**, and alerts **the right residents** in time to move their cars.

Your December 2023 flood is the pitch. The water rose overnight, nobody noticed, and 30 cars were damaged. Even a 30-minute warning would likely have saved most of them.

**Why it fits your judging criteria:**
- **Technical depth:** real hardware, signal smoothing, rate-of-rise prediction, rainfall forecast data, and alerts that escalate in stages.
- **Real-world impact:** a clear victim, a clear cost, and a clear fix. Each node costs roughly $15–30 in parts, compared with thousands per damaged car.
- **Continuable:** your own building is the first pilot site.

---

## What you'd build

### 1. Hardware (hardware person)
- **2–3 sensor nodes** placed at different points: the ramp entrance, the drain or sump, and the lowest parking bay.
- Arduino plus your water-level sensors. If you have an ESP32, use it for Wi-Fi. If not, send the readings over USB serial to a laptop acting as the "building gateway."
- **A local buzzer and LED on the node** that sounds even if the internet is down. Judges care about this kind of failure handling.
- **A physical model:** a clear plastic tub laid out as a mini parking garage, with numbered bays and toy cars.

*Note:* cheap resistive sensors corrode and only cover a few centimeters. They're fine for the demo, but mention that a real deployment would use waterproof ultrasonic sensors (e.g., JSN-SR04T).

### 2. Backend (you, Python)
- **FastAPI service** that receives readings and stores them in SQLite.
- **Prediction:** smooth the readings, then fit a linear regression over a sliding window to get the rise rate (cm/min). From that, calculate the **time until each danger level**:
  - ~10 cm: water at tire level (warning)
  - ~15 cm: exhaust pipes at risk
  - ~25–30 cm: water reaches door sills and floor electronics (critical)
- **Noise filtering:** require a sustained rise across several readings, and cross-check sensors against each other, so a mopped floor doesn't trigger an alarm.
- **Rainfall data:** pull the forecast from the free **Open-Meteo API** (no API key needed). If heavy rain is forecast, send a "pre-alert" before any water appears.
- **Staged alerts through a Telegram bot.** Telegram is free and instant, with no approval process like SMS.
  1. Building manager: "Water detected at ramp, rising 0.8 cm/min"
  2. Residents parked in affected bays: "Your car in B-12 is at risk in ~18 min"
  3. Everyone: critical alert
- **A "✅ I moved my car" button** in each alert, so the dashboard tracks which cars are still at risk.
- **Replay mode:** feed in recorded or synthetic sensor data. This is your backup if the hardware fails during the demo, and it also lets you replay a storm like December 2023.

### 3. Dashboard and brand (designer)
- A live **parking map** where bays shift from green to amber to red as water reaches them, and turn gray once the owner confirms the car is moved.
- A large level gauge, the rise rate, and a **countdown to critical**. This number is the emotional center of the demo.
- The Telegram alert copy. It should be calm, specific, and actionable.
- The pitch visuals: one slide on the 2023 flood and one on the path forward.
- Simplest tech choice: a plain HTML/JS page polling FastAPI, or Streamlit if the designer prefers to lay out components.

---

## 36-hour plan

| Hours | Hardware | Backend (you) | Designer |
|---|---|---|---|
| 0–3 | Wire sensors, get raw readings over serial | FastAPI skeleton, data model | Dashboard wireframes, name and brand |
| 3–10 | Calibrate readings to cm, build the tub model | Ingestion, smoothing, rise rate and countdown | Build the parking-map UI |
| 10–16 | Buzzer/LED local alarm, second node | Telegram bot, staged alerts, "moved" button | Wire the dashboard to the live API |
| 16–22 | **Sleep in shifts.** Don't skip this. | | |
| 22–28 | Make it rugged: mounting, tidy cables | Open-Meteo pre-alert, replay mode, noise filtering | Alert copy, pitch slides |
| 28–32 | **Full end-to-end runs with real water**, 5+ times | Fix bugs found in runs | Polish |
| 32–35 | Record the backup demo video, rehearse the pitch 5+ times | | |
| 35–36 | Buffer. Stop coding. | | |

**Cut order if behind:** rainfall pre-alert, then second node, then the "moved" button. Never cut the countdown or the phone alert.

---

## 3-minute demo plan

**0:00–0:30 · The story** (whoever tells it best)
> "December 2023. Our building's basement flooded overnight. By morning, 30 cars were ruined. The water didn't rise in an instant. It took hours. Nobody knew."

**0:30–0:50 · The setup**
Show the tub garage, the sensor nodes, and the live dashboard (all green). Say once that the demo runs on **compressed time**: real floods rise over hours, so the thresholds are scaled. Judges respect that honesty.

**0:50–2:00 · The live moment**
- Slowly pour water into the tub, or use a small pump for a steadier rise.
- The dashboard updates live: level rising, rate shown, **"Critical in 3:40"** counting down.
- Phones buzz. Hold one up, or project it: *"Your car in B-12 is at risk in ~3 min."*
- A teammate taps **"I moved my car."** That bay turns gray on the map.
- Optional but memorable: put a QR code on screen so judges can join the Telegram alert channel and get the alert on their own phones. Only do this if it worked smoothly in rehearsal.
- Briefly unplug the network: **the buzzer still sounds.** "It works even when the Wi-Fi doesn't."

**2:00–2:20 · The technical depth**
One quick slide or verbal summary: rise-rate prediction, noise filtering, rainfall pre-alerts from forecasts, staged alerts.

**2:20–3:00 · Impact and what's next**
> "About $25 per node, compared with thousands per damaged car. We're piloting it in our own building next month. After that: housing societies, then a shared street-level flood map built from every building on the network."

**Demo insurance:**
- Measure the exact pour amount and pour speed in rehearsal.
- Keep replay mode one keypress away if a sensor misbehaves.
- Have the backup video ready on a second laptop.
- Bring towels. Seriously.

---

## After the hackathon
1. **Pilot in your building.** You already know the failure point and the residents.
2. **Upgrade the hardware:** ultrasonic sensors, battery backup, LoRa radios for basements without Wi-Fi.
3. **Grow the network:** each building adds data to a shared neighborhood flood map, which becomes useful to cities and emergency services.
4. **Business paths:** subscriptions for housing societies, partnerships with insurers (who have a direct incentive to prevent claims), and integration with building management companies.

Do you want me to sketch the FastAPI and prediction code, or the Arduino-to-backend data format, so you can start on hour one?