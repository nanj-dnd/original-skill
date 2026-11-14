1: none quite. Not pulling back, I'm not banning anything. The point is the cost moved from writing to reviewing and it landed on my two seniors. I want to propose a rule: the author owns every line, "the AI wrote it" is never an excuse in a postmortem, and PRs over 400 changed lines get split.

2b + 2c. In August an AI-generated migration silently dropped a NOT NULL constraint. It caused a reconciliation mismatch that took three weeks to trace, and the engineer who merged it couldn't explain what the migration did. Numbers: PR volume up ~60% since spring, and senior review time went from ~4 to ~11 hrs/week each.

3: direct, but it's the whole company. Half the room is sales, ops and compliance, so not too technical. And please no pro/con structure, I find those useless.