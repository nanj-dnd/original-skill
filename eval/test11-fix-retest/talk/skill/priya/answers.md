1: None quite fit. I'm not anti-AI and I'm not banning it; new hires ramp about twice as fast now. The problem is that the cost moved from writing code to reviewing it, and it landed on my two seniors. I want to propose a rule: the author owns every line, "the AI wrote it" is never an excuse in a postmortem, and PRs over 400 changed lines get split.

2a: PR volume is up about 60% since spring. Review time per senior went from ~4 to ~11 hours a week. In August an AI-generated migration silently dropped a NOT NULL constraint. That caused a reconciliation mismatch that took three weeks to trace, and the engineer who merged it couldn't explain what the migration did.

3: Engineers are heavy users. The other half of the company (sales, ops, compliance) mostly doesn't see the review cost at all.

4a: Plain and blunt, but no jargon, since half the room isn't technical. And please, not a pro/con talk.