**Angle**: The hard problem isn't detecting water in a basement, it's waking the right person at 1am and escalating when they don't answer — so build the alert chain as the product and treat the sensor as the trigger.
**Built from**: 1b (building operator), 2c (Arduino kit + water-level sensors, Python backend, designer), 3c (your basement, December 2023, ~30 cars, nobody noticed after midnight), 4a (technical judges, plain language).
**Strongest objection**: a float switch wired to a siren does this for a few hundred rupees with no backend; the software is decoration. **Test**: before Friday, ask your apartment association who would have acted at 1am that night if a siren had gone off. If the answer is "nobody was awake to hear it", the call chain is the product. If "the security guard", scope down to siren plus a log and spend the weekend on reliability instead.
**Other direction**: skip the building and go city-scale — a cheap sensor any apartment can install, all reporting to one Chennai map that the corporation and insurers can see.

---

# Wake Call: a basement flood alarm that phones people until someone answers

## Why this one

In December 2023 your own basement flooded overnight and around thirty cars were damaged. The water wasn't the failure. The failure was that it rose after midnight and nobody noticed. Every building that flooded that week probably had the same story: someone would have moved the cars if someone had been awake.

So the pitch to technical judges is narrow and honest: a sensor on the basement floor is trivial; a system that reliably gets a sleeping human to act at 1am, and keeps trying if the first person doesn't pick up, is the actual engineering. That's what you'll show working.

## What you'd build

**The trigger (Arduino, your third member)**
Two or three water-level sensors from the kit, mounted at different heights on a strip — floor, ankle, car-sill. Reading more than one height gives you rate of rise, not just "wet / dry", and rate is what turns a reading into a time estimate: "at this pace the sills go under in about 40 minutes." The Arduino streams readings over serial to the laptop running the backend. Going wireless (GSM or Wi-Fi board, battery backup) is the obvious next step but not a weekend goal; say so on the slide rather than fake it.

**The brain (Python, you)**
Three pieces, all small:
1. *Debounce.* A splash, a leak from a pipe, a mop bucket — none of these should wake the whole building. Require the lowest sensor to stay wet for a set window, and only escalate severity when the next sensor up gets wet too.
2. *Escalation chain.* An ordered list of phone numbers with a timeout each: on-duty security first, then two designated residents, then everyone with a car in the basement. Each step is a real phone call with a spoken message (Twilio voice does this from Python in a few lines), not a push notification. A phone call at 1am wakes people; a notification doesn't. If the call isn't answered or a key isn't pressed to acknowledge, the next number fires.
3. *Event log.* Every reading, call, and acknowledgement timestamped. Afterward the association can see exactly when the water started and who responded when. That log is also your demo's receipt.

**The face (designer)**
One screen, built for a phone at night: current water height, estimated minutes until car-sill level, who has been called, who has acknowledged. Big text, high contrast, one button: "I'm on it." Resist a dashboard; the person looking at this is half-asleep in a stairwell.

**Stretch, only if Saturday goes well**
A resident-facing SMS at the end: "Water reached 12 cm at 01:47, security acknowledged at 01:51." Closing the loop is what makes people trust the thing enough to keep it plugged in.

## Demo plan: re-run that night in four minutes

Set the sensor strip in a clear plastic tub on the table. Put two team phones in the chain, on the table, screens up, and before you start, ask a judge for their number and add it as the third contact. Then pour.

- *Water touches the floor sensor.* The screen shows a reading but nothing happens. Say why: one wet sensor for a few seconds is a splash, not a flood. This is the moment that tells technical judges you thought about false alarms.
- *It stays wet, then the second sensor goes.* Severity jumps, the rate-of-rise estimate appears, and the first phone rings on the table. Let it ring out. Nobody answers — that's the point. Say: "This is what happened to us in December 2023."
- *Timeout expires.* The second phone rings. The teammate answers, hears the spoken message, presses 1. The screen flips to "acknowledged" with their name and the time.
- *Pull the acknowledgement.* Mark it unanswered in the admin view, and the judge's phone rings. Let them pick up and hear it. Nobody forgets a demo that calls them.
- *Show the log.* Scroll through the timestamped events from the last three minutes. Then one line: "Around thirty cars in our basement. This chain would have fired an hour before the water reached them."

Keep a recorded serial feed on disk so that if the sensor misbehaves, the backend can replay the pour and the calls still go out live.

---

**Before you use it**: check what sensors are actually in the kit — the common Arduino water-level module is a short resistive strip (a few centimetres of range), so you may need to stagger three of them rather than rely on one tall one. Twilio trial accounts can only call verified numbers, so verify the judge's number in advance or use a paid credit. If judges ask, confirm the exact date of your flood; if it was during Cyclone Michaung that's worth naming, but only if it's true. A real number worth adding: what one damaged car cost someone in your building to repair — it makes the price of three sensors obvious.

**Distance from the default**: completely different product. The default was a consumer carbon-footprint tracker; this is a building-operator flood alarm because of 1b, built around your hardware (2c) and your own basement (3c), with the escalation chain as the technical centre because of 4a. What it still shares with the plain samples: a named product, a core/stretch split, and a physical prop that does something live during the demo.