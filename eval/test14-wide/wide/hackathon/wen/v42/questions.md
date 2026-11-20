**What everyone gets**

The main claim a pasted prompt returns: a personal carbon-footprint tracker (or a close cousin: a receipt-scanner that estimates emissions, a "greener alternatives" shopping browser extension, or an AI assistant that scores your meals/commute). The choices it makes:

- **Angle**: individual behaviour change; the user is the polluter who needs nudging.
- **Build**: mobile/web app + an LLM wrapper + a public emissions-factor dataset, with a dashboard of charts.
- **Structure**: idea → feature list → tech stack → "demo: walk through onboarding, log an item, show the chart".
- **Reader**: generic judges who reward polish and a sweeping impact slide.
- **Tone**: pitch-deck optimism ("empower users to make sustainable choices").

Four questions, reply like `1b 2a 3c 4a`:

**1. Who is the user?** The default picks an individual consumer tracking their own footprint.
a) Individual consumer (the default)
b) A business or operator: building manager, farmer, fleet owner, small factory
c) A city, utility, or public body working with grids, water, or planning data
d) Scientists, journalists, or activists who need to find or verify climate data

**2. What's the team's actual edge this weekend?** The default assumes a web app plus an LLM over a public dataset.
a) We're strong on hardware/sensors or embedded (can wire something physical in two days)
b) We're strong on data/ML (can train or fine-tune something, handle real datasets)
c) We're strong on front-end/product (polished UI, fast iteration)
d) Mixed or unsure; want something low-risk to ship

**3. Real material: what do you already have?** A dataset, device, API access, a domain contact, or a specific local problem (a river, a grid, a building you know). Also: team size and hours available. Anything here becomes the centre of the idea rather than a feature dropped in.
a) Nothing specific yet, pick for us
b) We have access to a specific dataset, API, or device: *tell me which*
c) One of us knows a domain (energy, agriculture, insurance, logistics, etc.): *tell me which*
d) There's a local problem we've noticed: *tell me what*

**4. What are the judges rewarding?** The default assumes polish plus an impact claim.
a) Technical ambition: judges are engineers, demo depth wins
b) Business viability: judges are VCs/sponsors, "who pays" matters
c) Measurable climate impact: judges care about tonnes avoided, not slides
d) Unknown or a typical mixed panel