## Angle

**Angle:** Use AI coding assistants for as much as you like, but whoever merges a change must be able to explain every line of it, because when "the AI wrote it" becomes acceptable the cost doesn't disappear: it moves onto two senior reviewers and onto the sales, ops and compliance people who live with the fallout.

**Built from:** 1 (accountability, not a ban), 2 (the whole room, half of it non-engineering), 3 (review cost moved to two seniors; ~60% more PRs; ~4 to ~11 hours a week), 4 (you lead 7 engineers), 5 (the August migration).

**Where the answers pull against each other:** answer 1 says the author owns every line, but answers 3 and 5 show that in practice ownership has been sliding to the reviewers, since the August author couldn't explain the change and review hours nearly tripled. The talk uses that gap as its middle section instead of smoothing it over.

**Strongest objection:** "If every engineer has to understand AI output as well as if they'd written it, you've thrown away most of the speed. And one bad migration is an anecdote: people wrote bad migrations before AI too." A fair listener could also say the extra review time simply reflects 60% more work shipping, which might be a good trade.

**Test:** before Friday, check whether the August migration was approved by one of your seniors. If it was, someone will ask "where was the reviewer?", and the honest answer (review was overloaded) supports section 3, but you need to have it ready rather than discover it on stage. Also be ready to say whether the extra PR volume has meant more shipped, or mostly more churn.

**Other directions:**
- A leadership-facing version: the hidden cost of AI coding is senior review time, so plan and staff for it.
- A policy talk built entirely around one rule, "if you can't explain it, you can't merge it", with how you'd enforce it.

## Before you use it

- **Your figures:** the ~60% and the ~4 to ~11 hours are yours and are said as "about" in the talk. The "roughly 14 extra hours a week between two people, close to two working days" is my arithmetic from them (7 extra hours each, two seniors). Check it matches what you mean.
- **The August engineer:** the talk keeps them unnamed and doesn't blame them. They may well be in the room; consider telling them beforehand.
- **Lines I added that you should confirm:** "From me, as the lead: my job is to stop the review bill landing on the same two people" (section 5) is a commitment; keep it only if you'll back it with something. Likewise the ask to non-engineers ("ask who can explain it") is my suggestion, not something you said.
- **Details that would make it stronger:**
  - In section 4, what the reconciliation mismatch actually touched (which team spent those three weeks, or whether a report, a customer or an audit was involved). One concrete sentence there will land harder with sales, ops and compliance than the general version.
  - In section 5, one practical step you're actually taking (for example, authors walking reviewers through AI-written changes, or spreading review beyond the two seniors), if you have one.

## Distance from the default

- **Thesis:** the default draws a line by task type (boilerplate yes, architecture no). This draws no line by task; it says use it for anything, and makes the merging author accountable. From answer 1.
- **Who it talks to:** the default addresses engineers. This gives a whole section and a direct ask to the non-engineering half of the room. From answer 2.
- **Stakes:** the default's worry is generic quality and security. This is about where the cost went, with your numbers: review hours moving onto two seniors. From answer 3.
- **Speaker and opening:** the default is a neutral explainer opening on an industry statistic. This is a lead of seven opening on your own August incident, with a commitment of your own in the ask. From answers 4 and 5.
- **What didn't move:** at its core this still lands near the default's "keep a human responsible". It sharpens that to a named person who can explain the change rather than replacing it, and the structure (story, problem, cost, ask) is still a familiar one.
