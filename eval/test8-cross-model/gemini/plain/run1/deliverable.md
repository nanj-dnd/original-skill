## Opening Paragraph

"A year ago, half of us were ignoring AI coding assistants, and the other half were worried they were coming for our jobs. Today, the question isn't *whether* we use them, but whether we should be using them for *everything*. It’s tempting to let the AI write the boilerplate, refactor the legacy code, and maybe even design the architecture while we sip our coffee. But as we've integrated these tools into our daily workflow, a clear pattern has emerged: AI is an incredible co-pilot, but a terrible auto-pilot. For the next few minutes, I want to talk about where we should step on the gas with AI, and where we absolutely need to keep our hands on the steering wheel."

---

## 5-Minute Presentation Outline

**1. The Hook & The Current State (Minute 0:00 - 1:00)**

* Deliver the opening hook (above).
* Acknowledge the current landscape: Everyone is using these tools to some degree, and productivity metrics are generally up.
* State the core thesis: AI scales our typing, not our thinking.

**2. The "Green Light" Zone: Where to Use AI for Everything (Minute 1:00 - 2:30)**

* **Boilerplate & Scaffolding:** Generating standard CRUD operations, API wiring, and repetitive structural code.
* **Test Generation:** Writing unit tests for existing, well-defined functions.
* **Translation & Comprehension:** Explaining dense legacy code, translating between languages (e.g., Python to Go), or writing complex Regex.
* *Takeaway:* If the task is tedious but highly predictable, offload it completely.

**3. The "Red Light" Zone: Where Human Judgment is Non-Negotiable (Minute 2:30 - 4:00)**

* **System Architecture & Design:** AI lacks the context of the company's specific infrastructure, technical debt, and long-term business goals.
* **Complex Business Logic:** The AI doesn't know *why* a bizarre edge case exists for a specific enterprise client.
* **The "Illusion of Competence":** Address the danger of subtle hallucinations. AI code looks highly confident even when it introduces a security vulnerability or a silent logic bug.
* *Takeaway:* If the task requires deep context, domain knowledge, or architectural foresight, humans must drive.

**4. The Golden Rule & Wrap-Up (Minute 4:00 - 5:00)**

* **The Code Review Standard:** Introduce the mental model: *"Review AI-generated code exactly like you would review a PR from a fast, eager, but easily confused junior developer."*
* **Security Reminder:** A brief note on not pasting sensitive customer data or proprietary keys into public LLMs.
* **Call to Action:** Encourage the team to share their best AI prompts and worst AI fails in the engineering Slack channel to build collective intelligence.