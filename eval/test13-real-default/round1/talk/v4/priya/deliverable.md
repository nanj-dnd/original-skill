**Angle**: The cost of AI-written code didn't go away, it moved from writing to reviewing and landed on two people; the rule puts it back on the author.
**Built from**: your position and three rules (1), the August migration and the two numbers (2a, 2c), the mixed room and no pro/con (3b), plain and direct (4a).
**Strongest objection**: "You're taxing the whole team because two seniors are overloaded; fix the review rotation instead." **Test**: before Friday, ask both seniors what share of their 11 hours is big AI-heavy PRs versus everything else. If it's under half, the 400-line rule won't move the number and you should lead with ownership only.
**Other direction**: Pitch it as a hiring/cost story (we're paying senior rates to proofread) and ask for a third senior reviewer rather than a rule change.

---

## Outline (5 minutes)

**1. August (0:00–1:00)**
- Tell the migration story straight, in words the ops and compliance people can follow: a database rule that says "this field can never be empty" got quietly removed; two systems that are supposed to agree stopped agreeing; three weeks to find out why.
- The detail to land on: the engineer who merged it couldn't explain what it did. Not a competence problem. A question nobody was asking.

**2. What actually changed (1:00–2:00)**
- The tools work. Nobody's writing code slowly any more. PR volume is up about 60% since spring.
- Writing got cheap. Checking didn't. Every line still has to be read by someone who understands it, and that someone is now reading a lot more lines they didn't write and weren't thinking about when they were written.
- The cost didn't disappear. It moved down the line.

**3. Who it landed on (2:00–2:45)**
- Our two senior engineers went from about 4 hours a week of review to about 11.
- That's the hours we most wanted on hard problems, spent proofreading. For non-engineers: it's the equivalent of your most experienced person doing everyone else's spell-check.
- August is what happens when that pile gets too tall to read carefully.

**4. The rule (2:45–4:15)** — three parts, say each one plainly
- **You own every line you merge.** Whoever or whatever typed it. If you can't explain it, you don't merge it. (The August test, applied before the fact.)
- **"The AI wrote it" is never a postmortem answer.** Not a blame rule; an ownership rule. Nobody gets to be a bystander to their own change.
- **Any PR over 400 changed lines gets split.** For non-engineers: a PR is a bundle of changes someone has to read and approve. Past a certain size it stops being read and starts being skimmed. 400 is where we draw the line.
- One sentence on what this is not: not a ban, not a slowdown on using the tools to write. A floor on how much we understand what we ship.

**5. What I'm asking (4:15–5:00)**
- Engineers: start the rule now, don't wait for a policy doc.
- Everyone else: when a change takes a day longer than it used to, this is why, and it's cheaper than three weeks.
- Close on the number you want to move: senior review hours. Say you'll report it back at a future all-hands.

---

## Opening paragraph

In August, one of our engineers merged a database change that had been written by an AI assistant. It looked fine. It was fine, mostly. Buried in it was a line that removed a rule saying a particular field could never be empty, and once that rule was gone, two systems that are supposed to agree with each other quietly stopped agreeing. It took us three weeks to find out why. When we finally traced it back, the engineer who merged it couldn't tell us what the change did. I'm not here to pick on that engineer, and I'm not here to tell you to stop using these tools. I use them. I'm here because that three weeks wasn't bad luck, it was a bill coming due, and I want to show you where the bill is being sent now and propose a rule that sends it back to the right place.

---

**Before you use it**
- The opening is about 40 seconds aloud; section 4 is the one that will run long, so decide in advance which rule gets the fewest words.
- "Two systems that are supposed to agree" is my plain gloss on "reconciliation mismatch." If you can say what the two systems are in one phrase without a confidentiality problem, do it. Same for who noticed the mismatch first.
- Confirm the 60% and the 4→11 hours are figures you're comfortable saying to compliance in the room, since someone may ask where they come from.
- Section 5 has you promising to report senior review hours back. Only say it if you'll actually track it.

**Distance from the default**: Far. All three samples open with "that's the wrong question," split the talk into where AI wins / where it breaks down, and resolve on a typing-versus-thinking line with skill atrophy and a 2am incident as the warnings. This version has none of that structure (your 3b: no pro/con), opens on your August incident (2a), and argues from your two numbers (2c) to the three rules you already hold (1). What it still shares with the samples: "author owns every line" and "the AI wrote it is never a postmortem answer" appear in two of them, but those are your rules, so they stay.