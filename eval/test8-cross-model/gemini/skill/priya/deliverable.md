**Angle:** AI hasn't eliminated engineering work; it has shifted the bottleneck from writing to reviewing, meaning engineers must take absolute ownership of every generated line so our senior reviewers aren't crushed by the volume.
**Built from:** Your custom stance on ownership/rules, the August migration incident and metrics (60% volume spike, 4 to 11 hours review time), and a direct, company-wide tone.
**Strongest objection:** Splitting code updates and demanding deep comprehension of AI-written code will slow down our shipment velocity, negating the speed benefits the AI gave us in the first place.
**Test:** Look at the last major code change you approved—could you explain every single line of it on a whiteboard without looking at the AI prompt?
**Other direction:** Focus purely on the financial cost of the three-week reconciliation mismatch to justify heavily investing in automated testing software instead of changing team behavior.

---

### Opening Paragraph

In August, a tiny piece of code quietly slipped into our system. It was written by an AI, and it accidentally dropped a single database rule. That omission caused a data mismatch that took us three weeks to untangle—and the engineer who approved it couldn't explain what the code actually did. I’m not bringing this up to ban AI. Since spring, these tools have helped us push out 60% more code, and that velocity is a massive win for our business. But this speed has a hidden cost. We haven't actually eliminated the hard work of engineering; we’ve just moved the heavy lifting from writing the code to reviewing it. Right now, that massive wave of new code is crashing directly onto our senior engineers, and we are going to change how we operate before they drown.

### Talk Outline (5 Minutes)

**1. The Illusion of "Free" Speed (1 min)**

* Start with the August incident (the dropped `NOT NULL` constraint and the 3-week cleanup).
* Acknowledge the win: We are generating 60% more code (Pull Requests) since spring. AI is working.
* The pivot: Writing code got faster, but reading and verifying it didn't.

**2. The Hidden Tax on Seniors (1 min)**

* Explain the bottleneck: The cost of AI isn't the software subscription; it's the review time.
* Share the numbers: Senior engineering review time has jumped from 4 hours to 11 hours a week per person.
* The impact on the whole company: When seniors spend two days a week just reading AI-generated code, they aren't architecting the big features sales and ops need next quarter.

**3. The New Standard: Absolute Ownership (1.5 mins)**

* Introduce the core cultural rule: The author owns every line.
* "The AI wrote it" is permanently retired as an excuse in postmortems.
* If you cannot explain how a block of code works, you are not allowed to merge it into our product. AI is a ghostwriter; you are the author on the cover.

**4. The 400-Line Speed Limit (1 min)**

* Introduce the operational rule: Any code change over 400 lines must be split up.
* Explain why in plain English: Reviewing 1,000 lines of AI code at once causes fatigue, which is exactly how database constraints get dropped. Smaller chunks protect the reviewers.

**5. Moving Faster, Safely (30 sec)**

* Closing takeaway: We aren't pumping the brakes. We are putting down guardrails so we can safely keep our foot on the gas without burning out our best people or breaking the product.

---

**Before you use it:** Since half the room is sales and ops, consider briefly defining a "PR" when you first say it (e.g., "a PR, or a proposed code update") so they understand what the 60% volume spike actually means.

**Distance from the default:** Complete departure. Instead of a generic HR-style "pros and cons of AI" memo, this is a firm, metric-driven policy drop anchored by a real failure and a specific operational bottleneck.

*(Let me know if you want me to export this run as a Markdown or PDF file for your records!)*