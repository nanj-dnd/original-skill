**Angle**: The hard problem isn't detecting water in a basement. It's waking the right person at 1am and escalating when they don't answer. So the alert chain is the product, and the sensor is the trigger.
**Built from**: 1b (building operator), 2c (Arduino kit and water-level sensors, Python backend, designer), 3c (your basement, December 2023, around 30 cars, nobody noticed after midnight), 4a (technical judges, plain language).
**Strongest objection**: A float switch wired to a siren does this for a few hundred rupees with no backend, which makes the software decoration. **Test**: Before Friday, ask your apartment association who would have acted at 1am that night if a siren had gone off. If the answer is "nobody was awake to hear it", the call chain is the product. If it's "the security guard", scope down to a siren and a log, and spend the weekend on reliability instead.
**Other direction**: Go city-scale instead: a cheap sensor any apartment can install, all reporting to one Chennai map that the corporation and insurers can see.

---

# Wake Call: a basement flood alarm that phones people until someone answers

## Why this one

In December 2023 your own basement flooded overnight and around thirty cars were damaged. The water rose after midnight and nobody noticed. Basement floods at night tend to share that shape: the problem is often less the water than the hours when nobody is watching it.

So the pitch to technical judges is narrow and honest. A sensor on the basement floor is trivial. The real engineering is a system that reliably gets a sleeping person to act at 1am and keeps trying if the first person doesn't pick up. That's what you'll show working.

## What you'd build

**The trigger (Arduino, your third member)**
Mount two or three water-level sensors from the kit on a strip at different heights: floor, ankle and car sill. Several heights give you a rate of rise, not just wet or dry. The rate turns a reading into a time estimate, such as "at this pace the sills go under in about 40 minutes." The Arduino streams readings over serial to the laptop running the backend.

Going wireless with a GSM or Wi-Fi board and battery backup is the obvious next step, but it isn't a weekend goal. Say so on the slide rather than fake it.

**The brain (Python, you)**
Three pieces, all small:
1. *Debounce.* A splash, a dripping pipe or a mop bucket shouldn't wake the whole building. Require the lowest sensor to stay wet for a set window, and raise the severity only when the next sensor up gets wet too.
2. *Escalation chain.* Keep an ordered list of phone numbers with a timeout for each: on-duty security first, then two designated residents, then everyone with a car in the basement. Each step is a real phone call with a spoken message, which Twilio's voice API does from Python in a few lines. A push notification won't do here, because a phone call wakes people at 1am and a notification doesn't. If a call goes unanswered, or nobody presses a key to acknowledge it, the next number fires.
3. *Event log.* Timestamp every reading, call and acknowledgement. Afterwards the association can see exactly when the water started and who responded when. The log is also your demo's receipt.

**The face (designer)**
Build one screen for a phone at night. It shows the current water height, the estimated minutes until car-sill level, who has been called and who has acknowledged. Use big text, high contrast and a single button: "I'm on it." Resist building a dashboard, because the person looking at this is half-asleep in a stairwell.

**Stretch, only if Saturday goes well**
Send residents a closing SMS, such as "Water reached 12 cm at 01:47, security acknowledged at 01:51." Closing the loop is what makes people trust the system enough to keep it plugged in.

## Demo plan: re-run that night in four minutes

Set the sensor strip in a clear plastic tub on the table. Put two team phones in the chain and lay them on the table, screens up. Before you start, ask a judge for their number and add it as the third contact. Then pour.

1. *Water touches the floor sensor.* The screen shows a reading, but nothing else happens. Explain why: one sensor wet for a few seconds is a splash, not a flood. This tells technical judges you thought about false alarms.
2. *It stays wet, then the second sensor goes.* The severity jumps, the rate-of-rise estimate appears and the first phone rings on the table. Let it ring out. Nobody answering is the point. Say: "This is what happened to us in December 2023."
3. *The timeout expires.* The second phone rings. The teammate answers, hears the spoken message and presses 1. The screen flips to "acknowledged" with their name and the time.
4. *Pull the acknowledgement.* Mark it unanswered in the admin view, and the judge's phone rings. Let them pick up and hear it. Nobody forgets a demo that calls them.
5. *Show the log.* Scroll through the timestamped events from the last three minutes. Then close with one line: "Around thirty cars in our basement, and nobody knew until morning. This chain starts calling the moment the water stays on the floor."

Keep a recorded serial feed on disk. If the sensor misbehaves, the backend can replay the pour and the calls still go out live.

---

**Before you use it**
- **Sensor range**: Check which sensors are actually in the kit. The common Arduino water-level module is a short resistive strip with a few centimetres of range, so you may need to stagger three of them rather than rely on one tall one.
- **Twilio limits**: Trial accounts can only call verified numbers. Verify the judge's number in advance, or add paid credit.
- **Flood date**: Confirm the exact date. If it was during Cyclone Michaung, that's worth naming, but only if it's true.
- **A number worth adding**: Find out how long the water took to reach the cars that night, if anyone knows. You could then say how much warning the chain would have given, which is a stronger line than any estimate I can write for you.
- **Repair cost**: What one damaged car cost someone in your building to repair would make the price of three sensors look obvious.

**Distance from the default**: This is a completely different product. The default was a consumer carbon-footprint tracker. This is a flood alarm for building operators because of 1b, built around your hardware (2c) and your own basement (3c), with the escalation chain at the technical centre because of 4a. It still shares three things with the plain samples: a named product, a core/stretch split and a physical prop that does something live during the demo.