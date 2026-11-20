**Angle**: A flood warning system for apartment buildings wins only if it solves the midnight problem, so build the escalating wake-up call, not the dashboard.
**Built from**: 1b, 2b, 3b, 4c, and the December 2023 basement: 30 cars, nobody noticed after midnight.
**Strongest objection**: a ₹300 float switch wired to a siren already does this, so why software? **Test**: before Saturday, ask two people who live in buildings with basements whether a siren at 1 a.m. would reliably get the gate reached, the pump started and the owners called; if yes, cut the backend and build the siren.
**Other direction**: skip the building and do the street: a sensor on the storm drain outside, feeding a ward-level map so the corporation knows which drains are choked before the water reaches basements.

---

# Kaaval: the basement that calls you at 1 a.m.

## The night it's built for

In December 2023 the basement of an apartment building in Chennai filled overnight. Around thirty cars were damaged. Nobody did anything wrong in the usual sense; the water came up after midnight and everyone was asleep. By the time someone walked down in the morning the decision had been made for them.

That night is the spec. Not "monitor flooding", which is what a dashboard does, but: at 1 a.m., with the rain still coming, get a human awake, standing at the top of the ramp, with a number in their head for how long they have. Everything below exists to produce that moment, and the demo is that night replayed with the phone ringing.

## The idea in one line

A box of cheap water-level sensors in the basement, a small backend that turns rising water into a time estimate, and an alert chain that keeps calling people until one of them says "I'm on it".

Chennai is the right city to build this in. The 2015 floods and the December 2023 rains both put water into basements across the city, and apartment basements are where a building keeps its most expensive movable things. The building can't stop the water. It can buy itself forty minutes, and forty minutes at the right level is the difference between moving the cars up the ramp and claiming insurance.

## What you'd build, by person

**The sensor rig (the Arduino owner).** Three or four water-level sensors mounted at fixed heights on one post: floor, ankle, roughly the sill of a hatchback, roughly where the electricals sit. Multiple fixed heights rather than one continuous reading, because the question the system has to answer is "which line has the water crossed and how fast is it moving between lines", and discrete sensors answer that without calibration drama. The Arduino reports which sensors are wet, every few seconds, over USB serial to a laptop for the weekend. A Wi-Fi board can replace the cable later; don't spend Saturday on it.

**The backend (you).** Python, reading the serial line, keeping a short history, and doing the one calculation that matters: rate of rise between the last two lines crossed, projected forward to the next line. Output is not "level: 14 cm" but "water at ankle height, rising about 1 cm every 2 minutes, reaches car sills in roughly 35 minutes." Store a log so there's a replay. Then the alert chain:

1. Level one wet: a message to a group (Telegram bot is free and takes an hour; WhatsApp through Twilio's sandbox if you want it to look like what residents actually use).
2. Level two wet, or rate above a threshold: a phone call. An actual ringing phone, because messages don't wake people and this whole product is about people who are asleep. Twilio's trial tier can call numbers you've verified, which is enough for a demo.
3. No acknowledgement within a few minutes: call the next person on the list. Keep going. The acknowledgement is a keypress on the call or a reply in the chat, and it's the thing the dashboard shows most prominently: who is awake and on their way.

**The screen (the designer).** One page, meant to be glanced at on a phone in the dark: the post with its lines, which are wet, the countdown to the next line, and the call chain with ticks against the names as people acknowledge. Resist the map, the historical chart and the settings panel. The second screen worth having is the morning-after log: a timeline of when each line was crossed, when each call went out, who answered.

## Demo plan: replay the night

Set up a clear plastic tub with the sensor post standing in it, a jug of water, and a judge's phone number entered as the second person on the call chain.

1. Explain the December 2023 basement in three sentences. Thirty cars. After midnight. Nobody noticed. Then: "This is that night again."
2. Start pouring. Floor sensor goes wet; the Telegram group gets its first message in front of them.
3. Keep pouring faster. The screen shows the rate and the countdown to the sill line dropping from twelve minutes to four. Say nothing; let the countdown do the talking.
4. Sill line goes wet. The first phone on the chain rings (yours, and don't answer it). After the timeout, the judge's phone rings. That's the moment. Let them pick up and press a key.
5. The screen shows their name ticked as acknowledged, calls stop. Show the morning-after log: every event with a timestamp, in one glance.
6. Close on what it costs: a sensor post, a cable, a phone number list. Something a residents' association can put in over a weekend, which is also how long it took you.

Record the whole run on Friday night as a backup. Keep a pre-filled serial log so the backend can replay a flood without water if the Arduino misbehaves on stage. Put the judge's number in a few minutes before, not the night before.

## What climate-domain judges will push on, and the honest answers

*"This doesn't reduce flooding."* No. It's adaptation, not mitigation, and the theme allows for that. Chennai will keep getting these rains; the question is how much damage each one does.

*"Why not a float switch and a siren?"* Because a siren goes off in a basement nobody is in. The product is the chain of phone calls and the acknowledgement, and the time estimate that tells the person who picks up whether to run or walk.

*"Who buys it?"* Residents' associations, which in Chennai already pay for watchmen, generators and sump pumps. This sits beside the pump. The sensible stretch, if you finish early, is a relay that starts the pump at level one and reports in the log whether it kept up.

*"How do you know the sensor heights mean anything?"* Measure a real car on Friday: where the floor mat sits, where the sill is, where the fuse box is. Put those three numbers on the post and in the pitch.

---

**Before you use it**: confirm the December 2023 date against the Cyclone Michaung rains (3–4 December) if you want to name the storm on stage; check Twilio trial voice calling works to Indian mobile numbers from your account before relying on it, and keep the Telegram route as the fallback. Measure the car heights rather than trusting rough figures. If you're willing, saying on stage that the basement was your own building makes the pitch land harder than any slide.

**Distance from the default**: far. All three samples built consumer emissions tools (receipt carbon scanner, two grid-scheduling apps); this is an adaptation product for buildings, driven by your flooded basement and the Arduino sensors (1b, 2b, 3b). What it still shares with them: a physical thing happening live during the demo as the payoff, and the advice to record a backup and mock the data feed.