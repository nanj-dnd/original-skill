# What everyone gets

**Claim:** a carbon-reduction app that shifts or scores everyday behaviour.

- **Angle:** individual households cutting emissions, with mitigation as the only frame.
- **Examples:** grid carbon intensity and smart plugs (two of three samples were "GridShift"), or grocery receipts.
- **Build:** a public API or OCR, a Python scheduler, and a React dashboard.
- **Demo:** hook, then problem, then a live task, then a smart-plug lamp clicking on, then an "if 10% of homes…" scale slide, then a roadmap.
- **Tone:** startup pitch.

---

**Angle:** Your basement didn't flood because water is unstoppable. It flooded because nobody knew in time. So build an alarm that spots water *rising* (not just present), predicts when it reaches car level, and keeps escalating until a human acknowledges it.
**Built from:** 1c (local climate impact), your December 2023 flood and the roughly 30 cars, 3d (Python, design, Arduino plus water-level sensors, 36 h), and 4a/4c (technical judges, a live demo in 3 minutes).
**Strongest objection:** cheap Wi-Fi leak detectors already exist, so judges may see this as a solved problem. **Test:** by hour 6, pour water past your sensor three times and check that the predicted time-to-car-level settles within a few seconds and doesn't jump around. If it can't, rate-of-rise prediction is not your edge, and you should lead with escalation and failure-detection instead. Either way, have one sentence ready: "Leak detectors beep at one person when water touches them. This warns a whole building before it gets deep, and won't stop until someone answers."
**Other direction:** the same sensors mounted at street drains or underpasses, feeding a live neighbourhood flood map.

---

# Tidemark: a basement flood alarm that won't let a building sleep through it

## The idea
In December 2023 your apartment basement flooded and around 30 cars were damaged, because nobody noticed the water rising overnight. Tidemark is a sensor and server that watches basement water level continuously. It works out how fast the water is rising and when it will reach tyre height. It alerts residents early, then escalates from a group message to a phone call to the next person on the list, until someone confirms they're on it.

The engineering that technical judges can probe:

1. **Rate, not threshold.** A fixed "water detected" trigger fires too late. Tidemark fits a slope to the last N readings and projects the time until the car line is reached.
2. **Silence is a failure, not an all-clear.** If the sensor stops reporting, that gets alerted too. A dead sensor at 3am is the same failure as nobody watching.
3. **Escalation with acknowledgement.** An alert isn't "sent" until a person confirms it.

## What you'd build

**Hardware (your hardware teammate)**
- Two water-level sensors at different heights in a clear container, with the "floor" and "tyre line" marked on the side. Two sensors give redundancy and a plausibility cross-check: if the upper one reads wet and the lower one dry, it's a fault, not a flood.
- The Arduino streams JSON lines over USB serial at 2 Hz, for example `{"s1": 512, "s2": 0, "t": 18234}`. The laptop acts as the building gateway. That's simpler and more reliable on demo day than Wi-Fi.
- Calibration: dip each sensor to 4 or 5 depths measured with a ruler and record the raw values. The backend interpolates between those points, because cheap resistive sensors aren't linear.

**Backend (you, Python)**
- **Serial reader → smoother → estimator.** Use an exponential moving average on raw readings, then linear regression over a sliding window to get the slope in cm/min. Compute an ETA to the car line only when the slope is clearly positive and the fit is decent. This keeps sensor jitter from setting off false alarms.
- **State machine:** `NORMAL → RISING → ALERT → ACKNOWLEDGED`, plus `SENSOR_FAULT` (no reading for X seconds, or the two sensors disagree).
- **Escalation ladder:**
  1. A Telegram group message with an "I'm on it" inline button.
  2. No acknowledgement within the timeout triggers a Twilio voice call that asks the person to press 1 to confirm.
  3. No answer moves the call to the next person on the list.
- **FastAPI plus a WebSocket** pushes live state to the dashboard. SQLite logs every reading and event.
- **Replay mode:** record one real pour as a CSV on Saturday. Replaying it through the same pipeline gives you repeatable tests and a fallback if the hardware fails on stage.
- **Demo scaling:** make thresholds and timeouts config values, so the jar's 15 cm and a 3-minute pitch stand in for a real basement and a real night. Tell the judges this openly.

**Dashboard and alerts (your designer)**
- One screen with:
  - a large water-level gauge with the tyre line drawn on it
  - the current rise rate and a countdown such as "reaches cars in 1:40"
  - the escalation timeline, showing who was messaged, who was called, and who acknowledged
  - a sensor-health light
- **Alert wording for someone woken at night:** short, specific, and actionable. For example: "Basement water rising 2 cm/min. Reaches car level in about 12 min. Move cars now. Tap if you're handling it."
- **A QR card** that adds judges to the Telegram alert group.

## 36-hour plan

| Hours | Hardware | Backend (you) | Design |
|---|---|---|---|
| 0–6 | Wire both sensors, serial output, first calibration | Serial reader, smoothing, slope and ETA; **run the pour test** | Dashboard layout, alert wording |
| 6–18 | Mount sensors in the container, mark lines, repeat pours | State machine, Telegram bot with ack button, WebSocket | Build the dashboard against fake data |
| 18–30 | Make it robust: secure the wiring, dry the sensors between runs | Twilio call with keypress ack, fault detection, replay mode, SQLite log | Connect to the live feed, QR card, one architecture slide |
| 30–36 | **Feature freeze.** Full rehearsals with real water | Tune thresholds for the jar | Rehearse, record a backup video |

**If you fall behind,** cut in this order: the second sensor, then the Twilio call (keep Telegram), then the database log. Never cut fault detection. It's your strongest technical moment.

## 3-minute demo

Skip the problem slide. The water is the problem slide.

- **0:00–0:20.** The container is on the table and the dashboard is on screen. One person speaks: "In December 2023 our apartment basement flooded. About 30 cars were damaged, because nobody noticed the water rising overnight. We built the thing that would have noticed."
- **0:20–0:40.** "Scan this to join our building's alert group." The judges scan the QR card.
- **0:40–1:20.** Start pouring slowly. The gauge rises, the rate appears, and the countdown to the tyre line starts. "Notice it's predicting *when*, not just reporting *that*."
- **1:20–1:40.** The alert fires while the water is still well below the line, and the judges' phones buzz. Nobody taps "I'm on it."
- **1:40–2:10.** The timeout expires and the phone on the table rings. A teammate answers and presses 1. The dashboard shows "Acknowledged by Anshul, 1:58."
- **2:10–2:40.** The judge-bait moment. Unplug the sensor. Within seconds: "SENSOR OFFLINE. Basement unmonitored." "A silent sensor is the same failure as nobody watching, so we treat it as an emergency."
- **2:40–3:00.** Show the architecture slide (sensor → gateway → estimator → escalation) and close: "That night, the water rose for hours with nobody watching. Tidemark would have had someone moving cars in minutes."

**Stage safety:** run the dashboard on localhost so venue Wi-Fi only matters for the alerts. Have the replay CSV loaded behind a single keypress in case the hardware fails. Keep a towel and a tray under the container.

---

**Before you use it**
- Twilio trial accounts can only call phone numbers you've verified in advance. The ringing call should go to a team phone. The judges get the Telegram message, not the call.
- In a real deployment, a phone call is more likely than a message to get through silent mode. iPhone's "Allow Repeated Calls" setting lets a second call within three minutes ring through Do Not Disturb. Check the current iOS and Android behaviour before claiming it on stage.
- Check your sensors' real measuring range. Many kit water-level strips only cover about 4 cm. If that's true of yours, scale the container and the marked lines to match.
- Check the hackathon rules on pre-written code and hardware, and on whether you need an organiser's permission to use water in the venue.

**Distance from the default:** you moved the idea from carbon-cutting apps to local flood alerting (1c and your basement flood). The build follows your hardware teammate's Arduino kit (3d). The emphasis on rate, faults and escalation, and the demo with no problem slide, come from 4a/4c. It still shares two things with the samples: a FastAPI-plus-dashboard stack, and a physical object reacting live on stage.