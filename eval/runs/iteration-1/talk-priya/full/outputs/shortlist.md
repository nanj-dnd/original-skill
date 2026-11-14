**Banned (the default's main claim):** "Powerful but not for everything: use it for the boring parts and keep humans in charge of the parts that matter."

**One check on your numbers before we start:** PR volume up ~60% and review time up from ~4 to ~11 hours (about 2.75x) means each PR now takes about **70% longer to review**, not just that there are more of them. Two seniors at +7 hours each is ~14 hours a week, about a third of a full-time engineer.

## Candidates

1. **Explain-it-or-don't-merge.** One rule: if you can't explain what your change does, line by line, you can't merge it, however it was written. *(from: your August case)*
2. **Accountability has drifted to the reviewers.** On paper the author owns every line. In practice my two seniors do, at 11 hours a week each. *(from: tension between your answers 1 and 3)*
3. **The half of the room that paid.** The August bug cost engineering a migration and cost ops and compliance three weeks of reconciliation. Accountability is something they're entitled to ask for. *(from: the reader the default ignored)*
4. **The bottleneck moved, it didn't disappear.** We didn't get faster; the queue moved from writing to reviewing, and two people now cap our throughput. *(from: inverting the default's "speed" assumption)*
5. **Use it for everything, if you could have written it yourself.** Full permission, with the authorship test as the only gate.
6. **Give the talk as a blameless postmortem of August**, ending with the one new rule: "the AI wrote it" is never a root cause. *(from: your case + your answer 1, inverting the default's pros/cons structure)*
7. **Review was never a safety net for code nobody understood.** It checks intent, and if the author has no intent there's nothing to check. *(from: the engineer in the room who'd say "that's what review is for")*
8. **Accountability needs a budget.** Count review as real work: 14 extra hours a week is a third of an engineer nobody hired or planned for. *(from: your numbers)*
9. **Treat AI output like vendor code:** nobody ships a vendor's work unexamined, and the author is the one signing for it.
10. *(unlikely)* **The tools made us more honest.** They showed that review was always the real gate and was underfunded even at 4 hours.
11. *(unlikely)* **The lead takes the first hit.** "I set up a team where shipping PRs was rewarded and reviewing them wasn't counted. The August migration is on me before it's on anyone else." Accountability runs upward too.
12. *(unlikely)* **Give non-engineers a job.** When something breaks, ask one question: "Who can explain this change?" Sales, ops and compliance become part of the accountability loop.
13. **Each PR got heavier, not just more numerous.** Per-PR review time is up ~70%, so AI changes are harder to check (large, plausible-looking diffs). The lever is change size.
14. **Redefine "author":** whoever can defend the change in a postmortem, regardless of who typed it.
15. **Draw the line at data:** AI everywhere except schema and data changes that money depends on.

## Cut

- **5:** the same idea as 1, with permission added on.
- **14:** a near-duplicate of 1 and 6.
- **15:** the default reworded (it still draws the line by task type).
- **9:** an outside analogy that adds nothing 1 doesn't already say.
- **7:** folded into 2. It's the rebuttal 2 has to survive, not a separate talk.
- **12:** folded into 3, as its ending.
- **4, 8, 10, 13:** good, but they all sit close to 2 (the review load). 2 survives as the strongest of that cluster; 8 and 13 become its supporting numbers.
- **1:** survives as the closing rule inside 6, not as a talk of its own.

## Shortlist

**A. The author owns it on paper; my seniors own it in practice** (2, with 8 and 13 as evidence)
The rule says the author owns every line. The numbers say otherwise: since spring, two seniors went from 4 to 11 hours of review a week, and each PR takes ~70% longer to check. Accountability isn't being enforced; it's being quietly absorbed. Ask: authors must be able to explain their change before it reaches review, and review hours get counted as real work.
- **Only yours because:** your accountability position (1c), your review numbers (3) and your two seniors (4b).
- **Strongest objection:** this is a team-management problem. Why air it in front of sales and compliance?
- **Test:** it has to survive "AI just makes more PRs, so of course review goes up." Your ~70% per-PR rise is the answer, so double-check that the 4h and 11h figures measure the same thing.

**B. The talk for the half of the room that paid** (3, ending with 12)
Talk to sales, ops and compliance first. The August migration was an engineering change, but its cost landed on them: three weeks of reconciliation mismatch. Accountability for AI-written code is something they're entitled to expect, and you give them one question to ask whenever something breaks: "Who can explain this change?"
- **Only yours because:** your read of the room (2: half sales, ops and compliance) and your August case (5a).
- **Strongest objection:** it may sound like engineering handing its quality problem to non-engineers to police.
- **Test:** whether ops and compliance actually felt those three weeks, and whether they'd say so in the room. Check with someone from that side before Friday.

**C. A five-minute blameless postmortem of August** (6, closing on 1)
Structure the whole talk as a postmortem: what happened (a NOT NULL constraint silently dropped), impact (three weeks to trace a reconciliation mismatch), contributing factors (the merger couldn't explain the migration; review was stretched thin), and one action item: "the AI wrote it" is never a root cause, and you don't merge what you can't explain.
- **Only yours because:** your August case (5a), your accountability rule (1c) and your review load (3).
- **Strongest objection:** however blameless you make it, the room may work out who merged it, and that engineer is sitting there.
- **Test:** the engineer involved, and ideally your seniors, should be fine with it being told. Ask them before Friday.

**D. *(unlikely)* The lead goes first** (11)
You open by owning it: "I ran a team where PR count was visible and review time wasn't. The August migration is on me before it's on anyone else." Then the author-owns-every-line rule applies all the way up: the engineer owns the change, and you own the system that lets an unexplained change through.
- **Only yours because:** your role as lead (4b), plus your case (5a) and accountability position (1c).
- **Strongest objection:** in five minutes it can read as a confession that blurs your own rule (author owns every line) or lets the author off.
- **Test:** whether your own manager or leadership would back you saying this publicly at an all-hands.

## Pick

**I'd recommend C.** It's the one shape that makes your strongest material, the August migration, legible to the whole room. Sales and compliance can follow a postmortem easily, it carries the review-load numbers as a contributing factor, and it ends on a rule as concrete as your position. Its main risk (the engineer in the room) can be fixed with one conversation before Friday.

Which should I develop? Reply with A, B, C or D, or a combination with a note (for example `C, with B's ending`).
