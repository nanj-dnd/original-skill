1. In between. I'm not banning anything, the tools are fine. My point is that the cost didn't go away, it moved from writing code to reviewing it. I want to propose a rule: the author owns every line, "the AI wrote it" is never an excuse in a postmortem, and any PR over 400 changed lines gets split. Please don't make it a both-sides thing. I find pro/con talks useless.

2. I'm an eng manager with 7 engineers, 9 years here. It's a 40-person fintech and the whole company will be in the room. About half are non-engineers: sales, ops, compliance.

3. Review load has quietly piled up on my two senior engineers, and we had an incident. When I'm done I want people to back the ownership rule, and the non-engineers should understand why it matters to them too.

4. Yes, the team uses them a lot. PR volume is up about 60% since spring, and review time per senior went from about 4 to about 11 hours a week. In August an AI-generated database migration silently dropped a NOT NULL constraint. That caused a reconciliation mismatch that took three weeks to trace, and the engineer who merged it couldn't explain what the migration did. On the plus side, new hires ramp about twice as fast now, and I'm glad about that.

5. Probably a few slides, mostly me talking. Serious and to the point, with maybe one light moment. I don't want to name the engineer from the migration incident or make it sound like I'm blaming anyone.
