Over the last six months, our median time to resolve P2 incidents has climbed from 38 minutes to 61 minutes. When I look through our recent incident reviews, a distinct pattern emerges: we are shipping features faster than ever, but when systems break, the authors frequently struggle to follow a stack trace through code they supposedly just wrote. I am not here to take away your AI coding assistants—they are incredible force multipliers for generating new work, and you should absolutely keep using them to build. But there is a critical difference between knowing how to fly the airplane and knowing how to program the autopilot. Today, I want to talk about why we need our junior engineers to spend their first six months hand-flying our codebase when things break, and why building raw debugging muscle is the only way to ensure we can still land the plane when the autopilot disconnects in production.

**Talk Outline (5 Minutes)**

**I. The Reality of Our Current Metrics (1 Minute)**

* **The Data Point:** State the P2 median time-to-resolve increase (38 min to 61 min) directly.
* **The Paradox:** Acknowledge that while velocity on the front end (shipping new code) has increased thanks to AI, our operational velocity on the back end (fixing broken code) has degraded.
* **The Observation:** Share insights from recent incident reviews. Engineers are trusting the assistant's output without building a mental model of the underlying architecture, leading to deer-in-the-headlights moments during on-call rotation.

**II. Generation vs. Investigation (1.5 Minutes)**

* **The Value of AI:** Reiterate that you are pro-AI. Writing boilerplate and scaffolding is low-value work; AI handles this beautifully.
* **The Danger of Abstraction:** Explain that debugging is fundamentally different from writing. Debugging requires an internal, systemic map of how components interact.
* **Skill Atrophy:** Highlight the risk of outsourcing our investigative skills. If the AI writes the bug and the AI fails to find the bug, the engineer is left without the necessary tools to intervene.

**III. The Aviation Analogy (1 Minute)**

* **The Autopilot:** Modern commercial jets can fly a route and land automatically.
* **The Requirement:** Despite this, pilots are still required to accumulate hundreds of hours of manual hand-flying.
* **The "Why":** Because when sensors fail, weather shifts unexpectedly, or the autopilot disconnects, the pilot has seconds to rely on pure muscle memory and situational awareness. Debugging a live production outage is our equivalent of a disconnected autopilot.

**IV. The Proposal: 6 Months of "Hand-Flying" (1 Minute)**

* **The Pitch to Managers and Seniors:** We need to protect our junior engineers from long-term skill atrophy by forcing the reps early.
* **The Rule:** For their first six months, junior engineers can use AI to build and ship, but debugging—especially during incidents and deep investigative work—must be done manually.
* **The Expectation:** Managers need to create the psychological safety and timeline padding for juniors to read stack traces, parse logs, and step through debuggers without an AI crutch.

**V. Closing (30 Seconds)**

* **Summary Thought:** AI makes us remarkably fast builders, but deep, manual reps make us reliable operators.
* **Call to Action:** Let's keep using the tools to accelerate our output, but let's make sure we still know how to read the instruments when the screens go dark.