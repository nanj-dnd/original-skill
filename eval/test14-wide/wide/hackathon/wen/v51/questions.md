**What everyone gets**

The main claim a pasted prompt gets: a personal carbon-footprint tracker — an app that scans your receipts, bank transactions or photos, estimates the CO₂ behind each purchase, and nudges you toward lower-carbon swaps.

Choices it makes:
- **Angle**: individual consumer behaviour, guilt-reduction via gamified nudges.
- **Examples**: "swap beef for lentils", "this flight = X trees", a leaderboard with friends.
- **Structure**: Idea → Tech stack (LLM + emissions-factor API + React/Flutter) → Demo as a 3-minute scripted walkthrough ending on a "total CO₂ saved" counter.
- **Reader**: generic judges who reward polish and a feel-good narrative.
- **Tone**: upbeat pitch, "empower users", "make sustainability effortless".

Four questions before I write (reply like `1b 2a 3c 4b`):

**1. Who is the product for?** (default: an individual tracking their own consumption)
- a) Individuals — keep the consumer angle
- b) A specific operator — a building manager, small restaurant, farm, fleet, school
- c) A community or city — neighbours, a council, a campus
- d) Other builders — a dev tool or dataset other climate projects could use

**2. What does your team actually have to build with?** (default assumes a full-stack web team with API access and no hardware). Tell me: how many people, main skills, and anything real you can plug in — a sensor, a dataset you have access to, a local utility's data, a domain someone on the team knows first-hand.
- a) 2–3 people, mostly software, no hardware
- b) 4+ people, mixed software + design
- c) We have hardware (Raspberry Pi / ESP32 / sensors) and someone who can wire it
- d) Someone on the team has a real dataset or domain knowledge — I'll describe it

**3. What do the judges reward?** (default: polish and a feel-good story)
- a) Technical ambition — hard problem, impressive under the hood
- b) Demo polish — looks finished, smooth 3 minutes
- c) Measurable impact — a number that shows it would actually cut emissions
- d) Novelty — something they haven't seen pitched before

**4. How should the write-up sound?** (default: upbeat startup pitch)
- a) Blunt internal plan for the team — what we build, hour by hour
- b) Judge-facing pitch — polished, persuasive
- c) Both: a team plan plus a short pitch script

If you'd rather skip the questions, say "just write it" and I'll pick the single non-default choice the brief best supports.