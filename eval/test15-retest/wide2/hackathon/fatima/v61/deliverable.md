## Angle

- **Angle:** Build an overnight flood warning for basement car parks. A cheap sensor watches how fast the water is rising and wakes the right people early enough to move cars. The idea is climate adaptation (protecting people from the effects) rather than cutting emissions.
- **Built from:** 1c, which points at a physical place rather than individuals. 2a, your December 2023 flood: 30 cars lost because nobody saw the water after midnight. 3b, a team that can handle backend, data and hardware. 4a, a 3-minute live demo with a water utility engineer on the panel.
- **Strongest objection:** Water alarms already cost very little. A building could stick one on the floor and be done, and a system that rings phones at 2am will be muted after its first false alarm. **Test:** Before Saturday, show a neighbour or your building manager the one-line pitch and ask two questions: "Would a beep in the basement have saved the cars?" and "Would you answer a 2am call from this?" Then run the sensor in a bucket for an hour with no water and confirm it never fires.
- **Other direction:** A street-level version that crowdsources drain blockages for the utility, built from residents' photos instead of sensors.

---

# Waterline: a flood watch for the car park nobody checks at night

## The idea

The cars weren't lost because the flood was unstoppable. They were lost because the water rose after midnight and nobody knew.

Waterline puts a sensor in the basement and pays attention to *rate*, not just level. When the water starts rising, it estimates how many minutes remain before it reaches the cars. It then calls people in order (a phone call, because a 1am text gets slept through) until someone confirms they're on it.

Every alert is also a timestamped record of a basement taking on water, matched with the rainfall at that moment. That is the part for the engineer on your panel. A utility knows its pipes. It probably doesn't know which basements fill, or at what rainfall. Ask the engineer that question during your close.

## What you'd build

Five parts, one owner each. That matches a team of 3 to 5; double up if you're three.

1. **Sensor node (hardware).** An ESP32 with a waterproof ultrasonic distance sensor (JSN-SR04T) mounted above the floor, plus a float switch as a backup that confirms there is really water. It publishes the water depth every few seconds over MQTT.
2. **Rise engine (backend).** This turns readings into decisions:
   - It smooths out noise.
   - It calculates the rate of rise.
   - It projects the time until the water reaches a depth the building sets, such as the bottom of the lowest car's doors.
   - It needs two signals to agree before alarming: ultrasonic plus float, or a sustained rise across several readings. This is your answer to the false-alarm objection, so make it visible in the demo.
3. **Forecast arming (data).** Pull rainfall forecasts from Open-Meteo, which is free and needs no key. When heavy rain is due overnight, the system moves into "watch" mode: more frequent readings and lower thresholds. On dry nights it stays quiet.
4. **Escalation (backend).** A Twilio voice call reads out the depth, the rate and the minutes left. It goes down a call list, building manager first, then residents, until someone presses 1 to acknowledge. A Telegram bot posts the same alert to the residents' group, so people know to move their cars.
5. **Two dashboards (frontend).**
   - **The building view:** a live depth chart, the projected time to the threshold, and who has acknowledged.
   - **The utility view:** a map showing basement flood events against rainfall intensity. Build it by replaying a synthetic multi-building dataset through the real pipeline, and label it "simulated" on screen. An engineer will respect the label and will distrust it if it's missing.

**Cut first if you run short:** the utility map, then the forecast arming. The sensor, the rise engine and the phone call are the product.

## Demo plan (3 minutes, live)

**The prop:** a clear plastic storage box as the basement, a few toy cars inside, and the sensor mounted on the lid. Put tape on the side of the box at your threshold. A small aquarium pump feeds water from a second container, so you control the rise and don't have to pour by hand. Rehearse the pump timing until the threshold falls about 90 seconds into the run.

| Time | What happens |
|---|---|
| 0:00–0:20 | No slides. "December 2023. Our apartment's basement car park flooded overnight. Around 30 cars were damaged, because nobody noticed the water rising after midnight." Point at the box: "This is that car park." |
| 0:20–0:40 | Building dashboard. It is already in watch mode because of an overnight rain forecast (seed this so it's guaranteed). Say what armed it and why it stays quiet on dry nights. |
| 0:40–1:30 | Start the pump. The depth chart climbs live. Narrate the two-signal check as the float trips. The projection appears: "threshold in ~N minutes." |
| 1:30–2:00 | A teammate's phone on stage rings. Put it on speaker so the judges hear the call read out depth, rate and minutes left. The teammate doesn't answer, so the second phone rings. That phone presses 1. The Telegram group lights up with the acknowledgment. |
| 2:00–2:40 | Stop the pump. Switch to the utility view and replay the simulated multi-building data. Point out that events cluster at particular rainfall intensities. Name the design choice: every alert is a data point the drainage network doesn't currently produce. |
| 2:40–3:00 | Close on the engineer. "Would basement-level flood timing be useful to your team, and what would it need to look like for you to use it?" That turns your last 20 seconds into a conversation with the judge most likely to care. |

**Demo safety:**
- Twilio trial accounts can only call verified numbers, so verify both stage phones on Friday.
- Have a local replay of a recorded sensor run ready in case Wi-Fi drops. The call can still fire from the replayed data.
- Bring towels.

---

**Before you use it**
- Mount the ultrasonic sensor high enough. It has a minimum sensing distance of roughly 20–25 cm, so a shallow box lid may be too close. Check this with your actual box on Friday.
- If you know when the water was found in 2023 and how deep it got, put it in the opening line. A real time and a real depth will land harder with the utility engineer than "overnight."

**Distance from the default:** The default and all three samples are about personal emissions (receipt scanning, scheduling power for when the grid is cleanest). Waterline is adaptation, built on your 2023 flood (2a) and aimed at the utility judge (4a). It still shares two things with two of the samples: a physical prop on stage, and the warning to keep a local fallback for flaky Wi-Fi.