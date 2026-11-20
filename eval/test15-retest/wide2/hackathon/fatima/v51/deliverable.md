## Angle

- **Angle:** Flood sensors are cheap and already exist. What failed in your basement was waking someone up in time, so build a system that predicts when water will reach the cars and keeps escalating until a human answers.
- **Built from:** 1c (adaptation), 2a (the December 2023 flood: about 30 cars, unnoticed after midnight), 2c (3 people, Python, design, hardware, Arduino and water-level sensors, 36 hours), 3b (physical live demo), 4c (technical but straightforward).
- **Strongest objection:** Water leak alarms are a cheap, solved product, and large buildings already have building-management systems with flood inputs, so judges may see a sensor with a phone attached. **Test:** Before Saturday, ask your building manager what was installed in December 2023 and who it would have alerted. Then look up two commercial parking-garage flood monitors and check whether they do rate-of-rise prediction and escalation with acknowledgement. If they do, your pitch becomes "the low-cost version for residential buildings."
- **Other direction:** A shared map where residents across a city log garage and basement flooding, so buildings can see their risk before the first storm.

---

# Wakeline: a basement flood alarm that won't let everyone sleep through it

## The idea

In December 2023 our apartment basement flooded overnight. Around 30 cars were damaged, and nobody noticed the water rising after midnight.

Detecting the water wasn't the hard part. A wet sensor costs a few dollars. The hard part is that at 1am the water rises in an empty room while everyone who could act is asleep upstairs. A beeping alarm in the basement reaches no one, and a single push notification is easy to sleep through.

Wakeline handles the gap between detection and action. It does three things.

1. **Measures how fast the water is rising**, not just whether it is there.
2. **Turns that rate into a deadline:** the minutes left until water reaches the height where car damage starts.
3. **Escalates until a human acknowledges it.** It calls a phone, waits, then calls the next person and the next, getting more urgent as the deadline gets closer.

The climate link is direct. Heavier downpours are a well-documented effect of warming, and underground parking is where that water collects. This is adaptation for a building that has already flooded once.

## What we'd build

**Hardware (your hardware person)**
- Mount the water-level sensors at several fixed heights on a vertical stick inside the "basement." The heights could be floor level, a few centimetres up, and your car-damage threshold. Discrete heights are more robust than one cheap analog strip. Each sensor that trips gives a clean timestamp, and the time between trips gives you the rate.
- The Arduino reads the sensors and streams JSON lines over USB serial. If your board has Wi-Fi, it can post over HTTP instead, but serial removes venue Wi-Fi from the hardware path.
- Add a local buzzer and LED on the Arduino as a last-resort alarm if the network dies.

**Backend (Python)**
- **Ingest:** A serial reader using `pyserial` debounces readings. A sensor must stay wet for a few consecutive reads before it counts, so a splash doesn't trigger a 1am call.
- **Rate and deadline:** For each pair of trip events, compute rate = Δheight / Δtime, then deadline = (threshold height − current height) / rate. Severity is set by the deadline, not the level. Water at 2 cm rising fast is more urgent than water at 4 cm sitting still.
- **Escalation engine:** A small state machine.
  - Tier 1 calls the on-duty resident.
  - If no one presses 1 within N minutes, Tier 2 calls the building manager and texts everyone with a car on that level.
  - When the deadline drops below a set number of minutes, everyone gets called at once.
  - Use Twilio for voice and SMS. A voice call with "press 1 to acknowledge" is the core of the product, because ringing is what wakes people. Every event and acknowledgement is logged with a timestamp.
- **API:** A FastAPI app that serves the live state to the screen.

**Screen (your designer)**
- One page with three parts: the water height on a live line, a large countdown ("Water reaches car level in 11 min"), and the escalation ladder showing who has been called, who answered, and who is next.
- Design for the person half-awake on their phone at 1am, not for a judge.

**Stretch, only if Sunday morning is free**
- Pull a rainfall forecast from Open-Meteo (free, no key) to put the system on high alert on heavy-rain nights: lower thresholds and a heads-up text at bedtime.

### 36-hour split
- **First 12 hours:** Hardware gets sensors reading reliably over serial. Backend builds the rate and deadline logic against fake serial data. The designer builds the screen against a mocked API.
- **Next 12 hours:** Connect the real sensors, add Twilio calls and the escalation timer, and run the first full pour test.
- **Last 12 hours:** Tune debounce and thresholds by pouring water repeatedly. Build the demo rig, run the demo five times, and fix whatever breaks. Freeze features well before judging.

## Demo plan: replay the night

The demo is your flood, replayed at table scale, with the beats keyed to water height instead of a slide deck.

**The rig:** a clear plastic tub as the basement, the sensor stick at one end, and a row of toy cars on the floor. Mark a line on the side at "car damage." Use a jug of water, or a small pump if your hardware person wants a steady, repeatable rise. The laptop screen is mirrored to the projector, and one team member's phone is face-up on the table with the volume on.

1. **The setup (one sentence):** "December 2023, our basement flooded overnight and damaged around 30 cars because nobody noticed the water rising after midnight. This is that basement, and it's now 1am."
2. **The water starts:** Pour slowly. The first sensor trips and the screen shows water detected, with the rate still being calculated. Nothing rings yet. Point out that a splash wouldn't have triggered this, because of the debounce.
3. **The rate appears:** The second sensor trips. The deadline locks in ("car level in N minutes") and the phone on the table rings out loud. Let it ring and don't answer. That is the 1am scenario.
4. **The escalation:** After the timeout, the ladder moves. A second phone rings and the texts go out. Pour faster, and the room watches the deadline shrink and the severity jump.
5. **The acknowledgement:** A teammate answers and presses 1. The ladder shows who acknowledged it and when. Say what would happen next in the building: someone goes down and moves the cars.
6. **The technical point (30 seconds):** Show the rate-to-deadline calculation and the escalation state machine on one slide. That is the hard part, and it's why this isn't just a leak beeper.

**Make it survive the room**
- Set demo timeouts to about 20 seconds, so escalation happens on stage instead of after a 10-minute wait.
- If Twilio or the Wi-Fi fails, the Arduino buzzer and LED still fire and the screen still shows the ladder. Say so out loud, because that fallback is a real feature.
- Pre-wet nothing. Dry the sensors with a cloth between runs, and practise the pour speed so the deadline lands in a believable range.

---

**Before you use it**
- Check which Arduino board you have. If it has no Wi-Fi, keep the USB-serial setup described above.
- Twilio trial accounts can only call and text numbers you have verified, so verify every team phone before the event.
- Measure where water reaches a car's sills in your actual garage, and use that as the threshold in the pitch. It's a real number from your building.
- If you know what caused the December 2023 flood (rain, drainage, a burst pipe), add it to the opening line. Don't guess.

**Distance from the default:** All three default answers built mitigation apps (two grid-carbon schedulers and a receipt carbon tracker). This one is adaptation, built on your flood and your Arduino sensors, because of 1c, 2a and 2c. The demo is a replay of one night rather than a timed hook-problem-scale-close pitch, because of 3b. What it still shares with the samples: a Python/FastAPI backend, a live chart on screen, a physical prop, and a "have a fallback" plan.