# Who Owns the Code? AI Assistants and Accountability
*All-hands talk, 5 minutes (about 650–700 words spoken)*

## Opening paragraph (word for word)

In August, a change went into one of our databases that quietly removed one rule. A field that was never allowed to be empty was suddenly allowed to be empty. Nothing crashed and no alarm went off. Instead, our numbers stopped reconciling, and it took three weeks to find out why. An AI coding assistant wrote that change. When we finally traced it, the engineer who merged it couldn't explain what it did. I'm not telling you this to point at anyone. The tools aren't the villain, and we're not banning them. I'm telling you because it answers the question I was asked to talk about, which is whether engineers should use AI for everything. I think that's the wrong question. The right one is: when something breaks, who owns it? My answer is the person whose name is on the change. That covers every line, whoever or whatever typed it.

---

## Outline

### 1. The August story (0:00–0:50)
- Deliver the opening paragraph above.
- Explain it in plain terms. Half the room isn't engineering, so "NOT NULL constraint" becomes "a rule that a field can't be left empty."
- Keep it blameless and don't name the engineer. The point is that our process allowed it, not that one person failed.

### 2. "Everything or not" is the wrong question (0:50–1:30)
- I lead seven engineers, and we use these tools. They're useful, and that isn't the debate.
- The rule: **the author owns every line.** "The AI wrote it" is never an answer in a postmortem.
- Ownership means you can explain what the code does, why it's right and what could go wrong. If you can't, it isn't ready to merge, no matter how it was written.

### 3. Where the cost actually went (1:30–2:45)
- AI made writing code cheap. It did not make checking code cheap.
- The numbers: pull requests (proposed changes) are up about 60% since spring. Review time for each of my two senior engineers went from about 4 hours a week to about 11.
- For non-engineers: review is the last human check before a change reaches the product you sell, support and report on. The extra volume landed on two people.
- When the last check is overloaded, things like August get through. AI didn't remove the cost of code. It moved the cost onto review.

### 4. Why this matters to everyone in the room (2:45–3:45)
- Sales, ops and compliance live with the fallout. You field the customer calls, rerun the reconciliations and answer the auditors.
- "We ship more" only helps you if what we ship can be trusted and explained.
- What you can expect from engineering: when something breaks, a person who can tell you what happened and why. "The tool did it" won't be the answer.
- What you can ask: when a change touches your data or your customers, ask who owns it and whether they can explain it.

### 5. What we're doing about it (3:45–4:30)
*Placeholders: keep only what you've actually committed to.*
- If you can't explain it, it doesn't merge. The author walks through the change, especially for AI-written code.
- Changes that touch data (database migrations, anything financial or compliance-related) get a stricter review.
- Treat review as real, scheduled work. Spread it beyond two people instead of letting it pile onto the seniors.
- Watch review load as closely as shipping speed.

### 6. Close (4:30–5:00)
- Go back to the opening: three weeks of chasing one missing rule.
- Closing line: "Use the tools for whatever helps. But put your name only on code you can explain, because the name on it is the one who owns it."
