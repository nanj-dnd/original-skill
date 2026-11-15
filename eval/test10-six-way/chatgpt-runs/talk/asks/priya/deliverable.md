I'd build this around one central argument:

**AI hasn't eliminated the cost of engineering. It has moved the cost from writing code to reviewing, understanding, and owning code. And right now, we're not distributing that cost fairly.**

The August incident gives you a strong opening because it makes the issue tangible for engineers, ops, and compliance alike. I'd avoid making this an anti-AI speech. You're explicitly acknowledging the productivity gains while setting a higher standard for accountability.

## **5-minute all-hands outline**

**Title: AI Can Write the Code. Who Owns It?**

TARGET LENGTH · 5 MINUTES · APPROX. 600 WORDS

### **1. Opening: The August incident (0:00–0:50)**

- Start with the AI-generated database migration.
- It silently dropped a NOT NULL constraint.
- The result was a reconciliation mismatch that took three weeks to trace.
- The engineer who merged it couldn't explain what the migration actually did.
- Establish the point: the problem wasn't that AI wrote the code. It was that someone merged code they didn't understand.

### **2. The economics of AI-assisted engineering (0:50–1:45)**

Use your own numbers:

- PR volume has increased approximately 60% since spring.
- New hires are ramping up roughly twice as fast.
- That's genuinely good. AI is making us faster and more capable.
- But senior engineers' review time has increased from approximately 4 to 11 hours per week each.

**The key observation:** We have reduced the cost of producing code, but increased the cost of verifying it. That cost is disproportionately landing on two senior engineers.

### **3. The principle: You own every line (1:45–3:00)**

Make this the central message.

- It doesn't matter whether you wrote the code, Copilot wrote it, or Claude wrote it.
- If your name is on the PR, you own the code.
- "The AI wrote it" is never an acceptable explanation in a postmortem.
- You should be able to explain what your code does, why it does it, and what could go wrong.
- Generating code is not the same as engineering.

### **4. What changes from here (3:00–4:15)**

Keep this practical and specific.

Three expectations:

1. **Understand before you merge.** If you cannot explain a change, you aren't ready to approve it.
2. **Respect review capacity.** PRs exceeding 400 changed lines get split. Large AI-generated diffs aren't a shortcut around review.
3. **Don't outsource judgment.** AI can generate implementations, tests, migrations, and suggestions. The engineer remains responsible for correctness and consequences.

### **5. Closing: The standard we want (4:15–5:00)**

- We aren't going backwards. AI is here to stay.
- We want new hires ramping faster and engineers spending less time on repetitive work.
- But we cannot achieve that by transferring the burden to the people reviewing everyone else's output.
- The goal isn't to maximise lines of code or PR volume.
- The goal is to ship reliable software, faster, without sacrificing accountability.

End with:

**"Use AI as much as you want. Just never use it as an excuse for not knowing what you've shipped."**

## **Opening paragraph**

In August, we had a migration that was generated using AI. It silently dropped a NOT NULL constraint in our database. That eventually caused a reconciliation mismatch that took us three weeks to trace. And when we finally got to the engineer who had merged it, they couldn't explain what the migration actually did. Now, I want to be clear: the problem wasn't that they used AI. I'm glad we're using AI. It's helping us move faster, and our new hires are ramping up roughly twice as quickly as they used to. But that incident exposed something I think we need to talk about: **when AI writes the code, someone still has to understand it, review it, and take responsibility for it.** And increasingly, that someone is becoming one of our two senior engineers.

## **A few delivery recommendations**

- **Don't apologise for the position.** You're not arguing against AI, so don't spend time defending yourself against that interpretation.
- **Pause after the August incident.** Let the room absorb the three-week consequence, particularly ops and compliance.
- **Put the numbers on one slide:** +60% PR volume, 4 → 11 review hours per senior per week, 2× faster new-hire ramp-up.
- **Don't make the senior engineers sound like victims.** The issue is a structural imbalance in how work is distributed, not individual performance.
- **Avoid ending with a vague call to "use AI responsibly."** Your 400-line PR rule and ownership principle are much stronger because people can actually act on them.

One line I'd particularly emphasise during the talk:

**"We have made producing code cheaper. We haven't made being responsible for code cheaper."**

That's the thesis I'd want the 40 people in that room to remember.