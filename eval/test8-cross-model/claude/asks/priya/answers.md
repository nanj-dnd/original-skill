1. I have a stance. Use them, I'm not banning anything. But the cost moved from writing code to reviewing it, and nobody's talking about that. I want to propose a rule: the author owns every line, "the AI wrote it" is never an excuse in a postmortem, and PRs over 400 changed lines get split.

2. Engineering manager, 9 years here, I lead 7 engineers. I'm the one watching the review load pile up.

3. Whole company, about 40 people. Half are non-engineers: sales, ops, compliance.

4. Widely used, no real policy. That's why I want to propose the rule.

5. PR volume is up about 60% since spring. Review time for my two seniors went from about 4 to about 11 hours a week each. In August an AI-generated database migration silently dropped a NOT NULL constraint. It caused a reconciliation mismatch that took three weeks to trace, and the engineer who merged it couldn't explain what the migration did. On the plus side, new hires ramp about twice as fast now, and I'm glad about that.

6. Back the rule. And understand that "faster" isn't free. Someone pays for it in review.

7. Direct. Not provocative for its own sake, but definitely not balanced.

8. Please don't make it a pro/con talk. I find those useless. Haven't decided on slides yet.