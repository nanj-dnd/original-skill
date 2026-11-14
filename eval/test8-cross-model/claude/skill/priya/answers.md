1d 2c 3b 4a

Incident: in August an AI-generated DB migration silently dropped a NOT NULL constraint. It caused a reconciliation mismatch that took three weeks to trace, and the engineer who merged it couldn't explain what the migration did.

Numbers: PR volume is up about 60% since spring. Review time for my two seniors went from ~4 to ~11 hours a week each. That's where the cost actually landed. Upside: new hires ramp about twice as fast now.

And please, no benefits-vs-risks structure. I'm proposing a rule: the author owns every line, "the AI wrote it" is never an excuse in a postmortem, and PRs over 400 changed lines get split. Half the room is sales/ops/compliance, so it has to make sense to them too.