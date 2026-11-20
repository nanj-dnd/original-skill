**Angle**: Make the room the demo. A Wordle-shaped daily check-in ("what did you eat today?") that friends answer together. The audience plays it live during your pitch, and the same daily-with-friends loop is the reason anyone opens it a second day.
**Built from**: 1a (consumers, but opened twice), 2a (web + API only), 3c (no dataset, so the data is whatever the room types), 4a (live demo, wow moment), and that you joined with friends.
**Strongest objection**: underneath, it's still a food-carbon calculator, and free-text answers give rough numbers a sharp judge can poke at. **Test**: Friday night, have everyone on the team type what they actually ate. If the category and figure that come back are ones you'd say out loud without wincing, ship it. If not, show categories and rankings, not kilograms.
**Other direction**: a paste-a-product-link tool ("here's the lower-carbon version of this"). Same stack, works solo, no audience needed.

---

# Forkcast: one question a day, answered with your friends

## The moment you're building toward

A QR code goes up on the projector with the question "What did you have for lunch?" Judges and the audience type their answers into their phones, things like "chicken wrap", "leftover pasta" or "two slices of pepperoni". Within thirty seconds the screen fills up. Each answer lands as a tile, sized by its footprint. The big tiles are obviously beef and cheese. Then one line appears: *If this room's six beef lunches had been chicken, that would have saved more than every other swap here combined.*

Nobody downloaded anything. Nobody logged a week of meals. The product's whole point just happened to the people judging it.

## Why it gets opened a second time

Carbon trackers die because they're solo and they ask for effort. This one asks one question a day and takes ten seconds. The payoff is social: you see what your friends ate, who had the lightest day, and the one swap that would have mattered most. It's the Wordle shape, a shared daily prompt with a result you compare, applied to food, which is the biggest climate lever most people touch every day.

You don't need to prove retention in a weekend. You need to show the loop: today's prompt, yesterday's results, a streak, a group.

## What you'd build

One web app, no install. Three screens and one API call.

1. **Answer screen (phone)**: today's question, a text box, a submit button. You join a group with a 4-letter code or the QR link.
2. **Classifier**: send the free text to an LLM with a fixed list of about 40 food categories. Ask it for the category, a rough portion and a confidence. Look the category up in a small emissions table you keep in the repo. Poore & Nemecek 2018 is the standard source, and its per-kg figures are on Our World in Data. If confidence is low, show the answer as "unsure, not counted". Honest beats precise.
3. **Group screen (projector or everyone's phone)**: live tiles sized by footprint, the group total, the single biggest-lever line, and a small "yesterday" strip with a streak counter.
4. **Daily prompt**: a cron or a hard-coded schedule that rotates the question: lunch, dinner, "what did you drink today", "what did you snack on".

Keep it to one small server with a realtime push (Supabase realtime, Firebase, or a plain websocket) and a single-page front end. Seed every group with a few made-up answers from "the team" so the screen is never blank when someone joins.

**If it's Saturday night and you're behind, cut in this order**: streaks and yesterday first, then the biggest-lever line, then live updates (fall back to a refresh button). The tiles and the QR must survive.

**If you're ahead**: add a "swap it" tap on your own tile that shows what a different choice would have done, and a share card for the group's day.

## Demo run-sheet (about 3 minutes)

- **0:00**: QR on screen. "What did you have for lunch? Phones out." No slide, no stat. Let them type.
- **0:30**: Turn around to the screen as the tiles land. Name the biggest one out loud. Let the biggest-lever line appear and read it.
- **1:15**: Swipe to the phone view and walk through it: this is what a user sees, this is yesterday, this is the streak. "This is the whole app. One question, ten seconds, with the people you already eat with."
- **2:00**: Say what you didn't build: no camera, no barcode, no diary. Then give the numbers' source in one line and explain how you handle "unsure".
- **2:40**: Close on the room's total and one sentence about where it goes next: house groups, offices, a school's year group.

Rehearse with the room empty. Have whoever's on the team answer on their phones while one person drives the screen. Time it, because the live typing always takes longer than you think.

---

**Before you use it**
- Check the figures in your emissions table against Our World in Data before the demo. I'm confident in the source but didn't verify the exact per-kg numbers here. The one you'll be quoting is the rough ratio of beef at around ten times chicken per kg.
- Pick a different name if "Forkcast" collides with something that already exists.
- Once you know your team size, decide whether the "if you're ahead" items are realistic.

**Distance from the default**: the three plain answers built either a grid-carbon scheduler (twice, both with a smart-plug lamp) or a receipt scanner. All of them were individual tools with a stage-managed "money shot". This one became a group daily prompt because of 1a (opened twice) and 4a (wow moment), and it drops hardware because of 2a. It still shares the food-emissions lookup and the "show unsure rather than guess" rule with the receipt sample, and the timed run-sheet with all three.