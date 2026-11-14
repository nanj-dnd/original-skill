# "Who can explain this?": 5 minutes at the all-hands

About 700 words spoken. Rough timings are in brackets.

## Outline

**1. Open with August (0:00 to 0:50)**
- The NOT NULL constraint the migration dropped, the three-week reconciliation hunt, and the engineer who couldn't explain what the migration did. (See the opening paragraph below.)
- Say up front: this is not a talk about banning AI tools.

**2. What actually changed (0:50 to 1:50)**
- AI made code cheap to write. It didn't make it cheap to understand.
- Since spring, PR volume is up about 60%. Review time for each of our two senior engineers went from about 4 hours a week to about 11.
- Put it plainly: that's roughly 14 extra hours a week, close to two working days, landing on two people. Review time grew faster than volume, so each change is also harder to review, not just more frequent. *(Check this arithmetic against your real figures.)*
- The cost didn't go away. It moved, and it moved onto the people who are best at catching problems.

**3. Why this is everyone's problem, not just engineering's (1:50 to 2:50)**
- Talk straight to sales, ops and compliance, about half the room.
- AI-assisted mistakes rarely crash anything. They fail quietly, as numbers that don't match and records that don't reconcile. August didn't page an engineer. It turned into weeks of somebody chasing a discrepancy. *[Fill in: which teams spent the three weeks, so the room recognises itself.]*
- For compliance: when an auditor or a customer asks why a change was made, "the AI wrote it" isn't an answer we can give.

**4. The position: wrong question, right rule (2:50 to 3:50)**
- "Should engineers use AI for everything?" is the wrong question. Use it as much as you like.
- The rule is that the author owns every line. "The AI wrote it" never appears in a postmortem as an explanation.
- Be honest about the gap: in practice, accountability has been drifting from the people who write the code to the people who review it. That isn't fair to our seniors, and August shows it doesn't even work.
- In one line: if you merge it, you can explain it.

**5. The ask, one for each part of the room (3:50 to 4:40)** *(these specific mechanics are my suggestions, so change them to match what you'll actually commit to)*
- Engineers: for every change, and especially anything that touches data or migrations, write in the PR, in your own words, what it does and what could go wrong. If you can't write that, it isn't ready.
- Leadership: count review hours as a real cost, and stop treating them as free capacity that happens to belong to two people.
- Everyone else: when something breaks or looks off, ask "who can explain this change?" There should always be a name.

**6. Close (4:40 to 5:00)**
- Go back to August. The question that would have saved three weeks wasn't "did an AI write this?" It was "can anyone tell me what this does?"
- End on the rule: use the tools for everything you like, but never merge what you can't explain.

## Opening paragraph

In August, one of our database migrations quietly dropped a single constraint, a NOT NULL on one column. Nothing visibly broke that day. What we got instead was a reconciliation mismatch that took three weeks to trace. When we finally found the cause, the engineer who'd merged that migration couldn't tell us what it did, because they hadn't written it. An AI assistant had. I lead a team of seven engineers, and I'm not up here to tell you we should stop using these tools. I'm up here because that story is the real answer to "should engineers be using AI for everything?" The question was never how much code the AI writes. It's whether someone can explain it. Right now, when nobody can, the cost lands on two people on my team, and on a lot of people in this room.

*Details I added that you should check: "Nothing visibly broke that day" is my reading of "quietly", and "because they hadn't written it" assumes the whole migration was AI-generated rather than partly edited. All the numbers are your approximations, used as you gave them.*
