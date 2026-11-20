**Angle**: Build a repair-or-replace checker. The climate action most people can take this month is keeping what they already own, and the hard part of that product is research, not code, which is what a half-technical team can actually do in a weekend.
**Built from**: 2d (mixed team, some non-technical), 4a (working notes), 1a (consumers, kept).
**Strongest objection**: people decide repair vs replace on cost and hassle, not carbon, so a tool that only says "carbon says keep it" gets ignored. **Test**: before Saturday, ask five people outside the team what they'd do with a seven-year-old washing machine that's leaking, and whether a carbon number would change it. If nobody moves, lead with the cost figure and put carbon second.
**Other direction**: a "run it when the grid is clean" scheduler using a public carbon-intensity API. Good demo, but it's the idea two out of three plain models produce, and it leaves the non-technical half of the team watching.

---

**Working notes: Worth Fixing**

**What it is**
You tell it what's broken (type of thing, rough age, what's wrong). It tells you whether to repair or replace, in both money and carbon, and where to get it repaired near you. One page, no account.

Why this and not a footprint tracker: trackers need people to log things for weeks before they show anything. This gives an answer in thirty seconds to a question people already have, and the answer is usually "fix it", which is a climate win nobody argues with.

**Scope: cover five things, not fifty**
Washing machine, fridge, laptop, phone, vacuum. Everything else gets "we don't cover that yet". Five done well beats fifty guessed.

**Who does what**
Non-technical:
- Per item, find the embodied-carbon figure for making a new one and the typical running cost and energy use per year, old model vs current. Manufacturers' environmental reports are the first place to look (several big brands publish per-product sheets). Record the source next to every number; the tool shows the source on screen.
- Write the decision rule for each item in plain English: at what age and what fault does replacing beat repairing? Keep it to one short paragraph per item. The developers turn these into code, so make them unambiguous.
- Build the repair-shop list for our city for those five items: name, what they fix, rough price for the common faults. Phone calls are fine. Twenty entries is plenty.
- Write the on-screen copy and the pitch.

Technical:
- One form (item, age, fault from a short list, postcode), one results page (verdict, the two numbers behind it, the nearest two or three repairers, the source line).
- The rules live in one JSON file the non-technical side can edit without asking.
- No database, no login. Static site plus one small function if you want the repairer lookup to be live.

**Saturday**: numbers and rules for three items, form and results page working with those three.
**Sunday morning**: the other two items, repairer list, copy. **Sunday afternoon**: demo rehearsal, twice, with someone outside the team pressing the buttons.

**Demo**
1. Ask the room who has something broken at home right now. Most hands go up. Pick one person and use their item for the demo.
2. Run their case live. Read the verdict out, then the two numbers, then the repairer nearest them.
3. Run a second case where the answer is "replace", so the room sees it's not a guilt machine.
4. Hand round the phone (or put the link on the slide) and let a couple of people try it while someone closes.
5. Close on the point: the product doesn't ask anyone to change their habits, it answers a question they already had, and the climate benefit rides along.

Keep a pre-filled case ready in case the volunteer's item is one of the forty-five we don't cover.

**If it's going badly by Sunday lunchtime**
Drop the repairer lookup; keep the verdict and the numbers. The verdict is the product.

---

**Before you use it**: I haven't put any emissions or cost figures in because I couldn't check them here; the Saturday research task is where they come from, and every one should carry its source. Confirm the audience is local before building the repairer list for one city. If anyone on the team has a broken item right now, use that as the first case; it makes the pitch personal.

**Distance from the default**: The consumer target stays (1a). The product moved from a footprint tracker to a repair-or-replace checker because of 2d, which also drove the shape: a work split by technical and non-technical rather than core/stretch/stack. It still shares with the samples a named product, a cut list for when time runs out, and a backup case for the live demo.