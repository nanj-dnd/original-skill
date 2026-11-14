**Angle**: AI is fantastic for writing code, but to prevent critical skill atrophy, we need new engineers to spend their first six months debugging manually—just like pilots learning stick-and-rudder flying.
**Built from**: The 38-to-61-minute P2 metric, the 2am outage story, and the pilot analogy, using a direct, engineering-focused tone.
**Strongest objection**: Banning assistants for debugging will initially slow down onboarding and frustrate new hires. **Test**: Run a tabletop incident simulation with a new cohort using only raw logs versus an AI assistant, and compare their root-cause identification times.
**Other direction**: Focus purely on improving our incident runbooks and observability dashboards to make the AI's job easier.

---

I want to talk about AI coding assistants, and I’ll start by saying I love them. I want you using them to write new code, and not just for boilerplate. They make us faster, and the quality is mostly fine. But I’m looking at a worrying trend in our incident reviews. Over the last six months, our median time-to-resolve for P2 incidents has climbed from 38 minutes to 61 minutes. That is a massive jump. And the root cause isn't that the code we are shipping is worse. The root cause is that we are losing the ability to read a stack trace and reason through a failure in code we nominally wrote ourselves.

**Outline:**

* **The 2AM Reality Check**
* Share the recent outage story: The on-call engineer pasted the error into the AI four times, got four confident but wrong fixes, and spun their wheels.
* Contrast this with manual debugging: 10 minutes of just reading the raw logs revealed the issue.
* Clarify the intent: This isn't a dunk on that specific engineer. It's a systemic pattern popping up in our incident reviews. We are relying on AI to explain our own systems to us.


* **The Pilot Analogy: Stick-and-Rudder Skills**
* Commercial pilots fly with autopilot 90% of the time, but they still train relentlessly on stick-and-rudder manual flying.
* Why? Because when the automation hands you a mess at 2am in a storm, you have to be able to take over immediately.
* Debugging is our stick-and-rudder skill. If you don't build the manual reps, skill atrophy sets in, and you freeze when the AI guesses wrong.


* **The New Standard for Onboarding**
* Direct address to Engineering Managers: You own the culture on your teams.
* The new norm: For the first six months, junior engineers and new hires debug without an assistant.
* They can write code with it, but when the build fails or a bug is filed, they need to follow the execution path manually. We have to force them to build that muscle.


* **Closing**
* Reiterate: We are not pulling back on AI. We want the speed.
* But speed only matters if we maintain the resilience to fix things when they break. Use the tools, but don't let them blind you to how your own systems work.



---

**Before you use it**: Make absolutely sure the engineer from the 2am outage cannot be identified by the team, or ask their permission privately first. Also, verify if any major infrastructure changes happened in the last six months that could partially explain the P2 resolution spike.
**Distance from the default**: Massive shift. Instead of generic warnings about "sloppy AI code," this targets human skill atrophy, grounded in your real P2 metrics and a highly specific operational analogy.

*(Let me know if you’d like me to export this whole run—including your prompts, the default analysis, and this final piece—as a Markdown file or PDF for your records.)*