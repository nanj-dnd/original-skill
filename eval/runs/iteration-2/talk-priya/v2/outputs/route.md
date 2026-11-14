# Route

**Path: specific answers, so step 4 (build directly).** Your answers name a position (the author owns every line), an audience (the whole room, about half of it sales, ops and compliance), numbers (PR volume up about 60%, senior review time up from about 4 to about 11 hours a week) and a real incident (the August migration). There's enough here to build from, so there's no shortlist.

## Before the deliverable

**Angle:** AI didn't remove the cost of writing code. It moved that cost into *understanding* the code. Right now two seniors are paying it in review hours, and when it slips through, the rest of the room pays it in quiet failures like August's. So the rule isn't "use it for X but not Y". It's "if you merge it, you can explain it."

**Built from:** 1 (accountability: the author owns every line, "the AI wrote it" is no excuse), 3 (the cost moved to review and landed on two seniors, with the numbers), 5 (the August NOT NULL migration and the engineer who couldn't explain it), 2 (the whole room, especially sales, ops and compliance), 4 (you speak as the lead of 7 engineers, not as a neutral explainer).

**The tension I'm using:** in answer 1 the author owns every line. In answers 3 and 5, in practice, the *reviewers* have become the people who understand the code, and in August nobody did. Accountability has drifted from authors to your two seniors. The talk names that gap instead of smoothing it over.

**A number worth using (my arithmetic on your approximate figures, so please check it):** volume up about 1.6x while review time went up about 2.75x means each PR takes roughly 70% longer to review than it did in spring. Across two seniors, about 7 extra hours each is about 14 hours a week, close to two working days. So the code isn't only more plentiful. It's harder to understand.

**Strongest objection:** the review increase and the August bug might not be AI's fault. Team changes, harder work since spring, or an ordinary human mistake in a migration could explain either. A sceptic in the room can say "you're blaming a tool for a process gap."
**Test:** before Friday, check whether the rise in review hours tracks the share of AI-assisted PRs (or at least whether the biggest review loads came from AI-heavy PRs). Also ask whether the August engineer could have explained a migration they'd written by hand. If the answer to both is "not really", reframe it as "AI made an old process gap much bigger". That's still true, and harder to argue with.

**Other directions:**
- A leadership and capacity talk: your seniors are now the bottleneck, so review time needs to be budgeted and staffed like any other cost.
- The August incident told from the far side: the three weeks it took to trace the mismatch, as the people who chased it lived them, and what "quiet" failure costs non-engineers.
