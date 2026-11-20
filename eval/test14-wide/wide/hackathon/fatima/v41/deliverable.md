**Angle**: A ₹2,000 retrofit that watches a basement car park overnight and tells the people who can act (the guard, the association) how many minutes they have before the water reaches the cars.
**Built from**: 1b (adaptation), 2b (a building operator, here a resident association), 3b (Arduino + water-level sensors, Python backend, a designer), 4a (technical judges, live in three minutes), and the December 2023 night.
**Strongest objection**: Water sensors and flood alarms already exist, so a judge may ask what's new. Your answer has to be the time-to-damage estimate and the alert chain, not the sensor. **Test**: before Saturday, pour water into a bucket with two sensors at different heights and log the readings; if the rise rate you compute predicts the second sensor's trigger within ~20%, the pitch holds. If it doesn't, you still have a working alarm, but drop the ETA claim.
**Other direction**: Point the same kit at the street instead of the basement: a sensor on a stormwater drain grate that reports which drains are blocked before the rain starts.

---

## The idea

In December 2023 your basement car park flooded after midnight and about thirty cars were written off because nobody saw the water coming. The damage wasn't caused by the rain; it was caused by six hours of nobody knowing. Every car could have been driven up the ramp in ten minutes if someone had been woken at 1 a.m.

Build that wake-up call. Two or three water-level sensors on the basement floor, an Arduino reading them, a Python service that computes how fast the water is rising and how long until it reaches bumper height, and an alert that goes to the security guard and the association committee with one line: *"Basement water at 4 cm, rising 3 cm/min, reaches cars in ~9 minutes. Move them."* Chennai gets this kind of night more often now; the building can't be rebuilt, but it can be fitted with ₹2,000 of parts in an afternoon.

The user is the apartment association, not a resident with an app. They already have a guard on duty and a WhatsApp group; the system just has to feed both.

## What we'd build, by person

**Hardware (Arduino person).** Three sensors at three heights on one vertical strip: floor level (water present), 5 cm (warning), and bumper height, around 25 cm (damage). If the kit's sensors are the analog strip type, one sensor gives a continuous level and the other two become confirmation; if they're float switches, three thresholds is enough for the rate calculation. Arduino reads every second and writes `timestamp,level_mm` over USB serial. Nothing on the board needs to be smart. Also build the demo rig: a clear plastic tub, the sensor strip taped to the inside wall, a toy car at bumper height, and a 2-litre bottle.

**Backend (you).** A Python process reading the serial line into SQLite. Three jobs:
1. *Rate of rise*: linear fit over the last 60 seconds of readings, giving mm/min.
2. *ETA to damage*: (damage_height − current_level) / rate, recomputed every reading, with a floor so a noisy reading never shows "ETA 0".
3. *Alert ladder*: water detected → one message; ETA under 15 minutes → message plus phone call to the guard; damage height reached → message to everyone. Each tier fires once, with a cooldown, so a sloshing sensor doesn't send forty messages. Use a Telegram bot for the demo (free, no approval, works over mobile data); say on stage that production uses WhatsApp Business API, which is what the association actually reads.

Add a `/simulate` endpoint that replays a logged rise at any speed. You'll use it for development and as the fallback if the tub leaks on stage.

**Design (third person).** One screen, meant for a guard's phone at 1 a.m., not a dashboard: current level as a big number, a bar showing where the cars are, the ETA in minutes, and a "mark cars moved" button that silences the ladder. Also the alert message text itself — that's a design problem, since the person reading it is half asleep. And a printed one-page install sheet: where to screw the strip, how to run the wire, which number to put in the config.

Skip anything that needs the internet beyond the Telegram call. No cloud, no login, no map.

## Three-minute demo, scripted

Setup before you're called: tub on the table, empty; laptop screen mirrored; one judge's phone (or yours, held up) in the Telegram group.

**0:00–0:20** — You, one sentence: "December 2023, our basement, thirty cars, nobody awake. Here's the thing that wakes someone." Hold up the sensor strip. No slides.

**0:20–1:10** — Hardware person starts pouring, slowly and steadily. The screen shows the level climbing live from the serial feed. At floor contact the first Telegram message arrives on the phone; show it. Then point at the rate figure settling in and the ETA counting down. Say the number out loud: "Rising 2 cm a minute, nine minutes to the cars." That's the part the judges score: a live fit on noisy sensor data producing a usable number.

**1:10–1:50** — Pour faster. ETA drops, the warning tier fires, and the guard's phone rings. Let it ring; silence is fine for five seconds. Designer presses "cars moved" and the ladder stops.

**1:50–2:30** — Keep pouring to bumper height, toy car gets wet, final-tier message arrives. Then the technical close: show the raw serial log and the fit window side by side, say what the sensors cost and how the install sheet works. If a judge asks about false triggers from a mop bucket, the answer is the rate: standing water doesn't rise.

**2:30–3:00** — Stop. "Three sensors, one Arduino, a Python script, a Telegram bot. Parts under ₹2,000 per basement. Every building in Chennai with a ramp can have this before next November." Take questions.

If the sensors misbehave, hit `/simulate` with the real pour you logged on Saturday and say so; a replayed real log is still honest.

**Before you use it**
- I didn't check whether your kit's sensors are analog strips or float switches; the rate calculation differs slightly, so settle that first.
- Chennai's December 2023 flooding was Cyclone Michaung's week (early December); if your night was that one, say so on stage, since judges will know it.
- The ₹2,000 parts figure is my estimate; price your actual sensors, Arduino and wire and use that number.
- If the association has a real guard name or the actual car count from the insurance claim, use the real one.

**Distance from the default**: The default was an individual footprint app; this moved to a physical adaptation device for a building operator because of 1b, 2b and your own basement. The three samples never touched flooding, but they share a shape I avoided: a bold product name as the header, a "core / stretch" build list, a timed demo with a "money shot" and a scale-the-story slide. What stays shared with them is the pattern of one physical prop reacting live on stage and a pre-logged fallback if hardware fails; both are just good hackathon practice.