# AI assistants: mostly your call, except for one thing

*Tech division all-hands, 5 minutes (about 650 spoken words)*

## Outline

**1. Opening: the honest answer is the boring one (0:00 to 0:45)**
- Should we use AI coding assistants for everything? No, and where it stops is mostly a judgment call the people in this room are better placed to make than any rule.
- Signal the turn early: there's one part that isn't a judgment call, and that's what the back half is about.

**2. The judgment part: speed against quality (0:45 to 2:00)**
- Keep this short. Everyone here already has opinions and evidence from their own week.
- Where it pays: getting to a first working version fast, code you'd have written the same way anyway.
- Where it costs: diffs that take longer to review than they would have taken to write, rework when it's confidently wrong, review load landing on whoever gets the PR.
- The only rule here: you own what you merge, exactly as if you'd typed it. Beyond that, use it where it makes you faster without making the code worse, and keep arguing about where that is. That argument is healthy.

**3. The turn: the part that isn't a judgment call (2:00 to 3:30)**
- We keep coming close to the same mistake: someone almost pastes customer data or a production log into one of these tools.
- Name when it happens: not when people are careless, but when they're moving fast. A failing request in prod, an error you can't reproduce, a log excerpt you want explained right now. The same pull toward speed from section 2 is what puts real data on the clipboard.
- The kind of thing that slips through: a stack trace with a customer's email in it, query output with real rows, a log line with an account ID.
- Compliance already forbids this. The point isn't new policy; it's saying it out loud, in this room, in one sentence everyone can remember.

**4. The line (3:30 to 4:30, the minute that matters)**
- Say it plainly, then pause: **No customer data. No production logs. In any external tool.**
- "Any" means any: chat assistants, browser tabs, editor plugins that send what you give them to someone else's servers, the "just this once" paste during an incident.
- What to do instead: describe the error instead of pasting it, build a made-up example with the same shape, reproduce it locally with test data.
- If you're not sure whether something counts, it counts. Don't paste it; ask first.

**5. Close (4:30 to 5:00)**
- Everything in section 2: your call, keep experimenting, keep disagreeing.
- This one: not a call. Repeat the line word for word as the last thing you say.

## Opening paragraph

I was asked to talk about whether we should be using AI coding assistants for everything. My honest answer is the boring one: no, not for everything, and where exactly it stops is mostly a judgment call that the people in this room are better placed to make than any rule I could write. Some days it saves you an afternoon. Some days it hands you a diff that takes longer to review than it would have taken to write. I'm not going to settle that up here. But there is one part of this that isn't a judgment call at all, and we've come close to getting it wrong more than once, so that's what I want to spend the second half of my time on.
