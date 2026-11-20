**Angle**: A flood warning system for apartment buildings wins only if it solves the midnight problem, so build the escalating wake-up call, not the dashboard.
**Built from**: 1b, 2b, 3b, 4c, and the December 2023 basement: 30 cars, nobody noticed after midnight.
**Strongest objection**: a ₹300 float switch wired to a siren already does this, so why software? **Test**: before Saturday, ask two people who live in buildings with basements whether a siren at 1 a.m. would reliably get the gate reached, the pump started and the owners called. If yes, cut the backend and build the siren.
**Other direction**: skip the building and do the street: a sensor on the storm drain outside, feeding a ward-level map so the corporation knows which drains are choked before the water reaches basements.

---

# Kaaval: the basement that calls you at 1 a.m.

## The night it's built for

In December 2023 the basement of an apartment building in Chennai flooded overnight. Around thirty cars were damaged, because nobody noticed the water rising after midnight. That hour is the problem. Most people in any building are asleep then, and rising water makes no noise.

That night is the spec. "Monitor flooding" is what a dashboard does. The spec is this: at 1 a.m., with the rain still coming, get a human awake and standing at the top of the ramp, knowing how long they have. Everything below exists to produce that moment, and the demo replays that night with the phone ringing.

## The idea in one line

Kaaval is a set of cheap water-level sensors in the basement, a small backend that turns rising water into a time estimate, and an alert chain that keeps calling people until one of them says "I'm on it".

Chennai is the right city to build this in. The 2015 floods and the December 2023 rains both put water into basements across the city, and the basement is where a building keeps its most expensive movable things. The building can't stop the water. It can buy itself forty minutes, and forty minutes at the right level is the difference between moving the cars up the ramp and claiming insurance.

## What you'd build, by person

**The sensor rig (the Arduino owner).** Mount three or four water-level sensors at fixed heights on one post: floor, ankle, roughly the sill of a hatchback, and roughly where the electricals sit. Use discrete sensors at fixed heights rather than one continuous reading. The system has to answer which line the water has crossed and how fast it is moving between lines, and discrete sensors answer that without calibration drama. The Arduino reports which sensors are wet every few seconds, over USB serial to a laptop for the weekend. A Wi-Fi board can replace the cable later; don't spend Saturday on it.

**The backend (you).** Write Python that reads the serial line, keeps a short history and does the one calculation that matters: the rate of rise between the last two lines crossed, projected forward to the next line. The output is not "level: 14 cm" but "water at ankle height, rising about 1 cm every 2 minutes, reaches car sills in roughly 35 minutes." Store a log so you can replay a flood. Then build the alert chain:

1. **Level one wet:** send a message to a group. A Telegram bot is free and takes an hour. Use WhatsApp through Twilio's sandbox if you want it to look like what residents actually use.
2. **Level two wet, or rate above a threshold:** place a phone call. It has to be an actual ringing phone, because messages don't wake people and this product is for people who are asleep. Twilio's trial tier can call numbers you've verified, which is enough for a demo.
3. **No acknowledgement within a few minutes:** call the next person on the list, and keep going down it. The acknowledgement is a keypress on the call or a reply in the chat. It's the thing the dashboard shows most prominently: who is awake and on their way.

**The screen (the designer).** Build one page meant to be glanced at on a phone in the dark. It shows the post with its lines, which lines are wet, the countdown to the next line, and the call chain with ticks against the names as people acknowledge. Resist the map, the historical chart and the settings panel. The second screen worth having is the morning-after log: a timeline of when each line was crossed, when each call went out and who answered.

## Demo plan: replay the night

Set up a clear plastic tub with the sensor post standing in it and a jug of water. Enter a judge's phone number as the second person on the call chain.

1. Explain the December 2023 basement in three sentences: thirty cars, after midnight, nobody noticed. Then say: "This is that night again."
2. Start pouring. The floor sensor goes wet, and the Telegram group gets its first message in front of the judges.
3. Pour faster. The screen shows the rate and the countdown to the sill line, which drops from twelve minutes to four. Say nothing and let the countdown do the talking.
4. The sill line goes wet and the first phone on the chain rings. That phone is yours; don't answer it. After the timeout, the judge's phone rings. That's the moment. Let them pick up and press a key.
5. The screen ticks their name as acknowledged and the calls stop. Show the morning-after log: every event with a timestamp, in one glance.
6. Close on what it costs: a sensor post, a cable and a phone number list. A residents' association can put it in over a weekend, which is also how long it took you to build.

Record a full run on Friday night as a backup. Keep a pre-filled serial log so the backend can replay a flood without water if the Arduino misbehaves on stage. Enter the judge's number a few minutes before the demo, not the night before.

## What climate-domain judges will push on, and the honest answers

*"This doesn't reduce flooding."* No. It's adaptation, not mitigation, and the theme allows for that. Chennai will keep getting these rains; the question is how much damage each one does.

*"Why not a float switch and a siren?"* Because a siren goes off in a basement nobody is in. The product is the chain of phone calls and the acknowledgement. The time estimate also tells the person who picks up whether to run or walk.

*"Who buys it?"* Residents' associations, which in Chennai already pay for watchmen, generators and sump pumps. This sits beside the pump. If you finish early, the sensible stretch goal is a relay that starts the pump at level one and records in the log whether it kept up.

*"How do you know the sensor heights mean anything?"* Measure a real car on Friday: where the floor mat sits, where the sill is and where the fuse box is. Put those three numbers on the post and in the pitch.

---

**Before you use it**: If you want to name the storm on stage, confirm that your flood matches the Cyclone Michaung rains of 3–4 December 2023. Before relying on Twilio, check that trial voice calls reach Indian mobile numbers from your account, and keep the Telegram route as the fallback. Measure the car heights rather than trusting rough figures. Saying on stage that it was your own building's basement will land harder than any slide.

**Distance from the default**: far. All three samples built consumer emissions tools: a receipt carbon scanner and two grid-scheduling apps. This is an adaptation product for buildings, driven by your flooded basement and the Arduino sensors (1b, 2b, 3b). It still shares two things with them: a physical thing happening live as the demo's payoff, and the advice to record a backup and mock the data feed.