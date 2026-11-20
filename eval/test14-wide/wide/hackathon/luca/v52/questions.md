**What everyone gets**

A pasted prompt returns a "personal carbon footprint tracker" (or its cousin: an AI that scans your receipt/photo and estimates emissions, then nudges you with green alternatives). Its choices:

- **Angle**: individual behaviour change; the user is the polluter who needs a gentle nudge.
- **What's built**: mobile/web app, LLM wrapper over a public emissions-factor dataset, a dashboard with a score.
- **Examples**: grocery receipts, commute choices, flights.
- **Demo**: scan a receipt live, watch the number appear, show a "swap this for that" suggestion, close on a badge or leaderboard.
- **Tone**: upbeat, "every small action counts".

Four questions, answer like `1b 2a 3c 4a`:

**1. Who's the user?** The default picks a consumer nudging themselves.
a) An individual consumer (the default)
b) A small operator who makes decisions with money on the line: a farmer, building manager, fleet owner, restaurant
c) A city, utility or planner working from public data
d) Developers or other teams: a tool/API rather than an end-user app

**2. What's the core mechanic?** The default is "measure, score, nudge".
a) Measure and score behaviour (the default)
b) Predict or forecast something physical (heat, flood, grid carbon intensity, crop stress) and act on the prediction
c) Match or market: connect surplus to need (energy, food, materials, repair)
d) Verify or audit: catch greenwashing, check offsets, reconcile claims against data

**3. What does your team actually have?** This decides what's buildable in a weekend. Tell me roughly: how many people, your strong skills (web / ML / hardware / data / design), and anything real you can plug in: a sensor, a dataset you already have, an API key, a domain one of you knows (someone's family farm, a building you can get meter data for, a local problem you've seen).

**4. How is it judged, and what's the demo setting?**
a) Judges score technical difficulty; demo is a 3-minute pitch with slides and a live run
b) Judges score impact/story; demo is a video or stage walkthrough
c) Peer vote or ship-it bar: it must actually work end to end for someone in the room
d) Not sure / mixed

If you'd rather skip, say so and I'll pick the one non-default direction the climate theme best supports and write it without team-specific details.