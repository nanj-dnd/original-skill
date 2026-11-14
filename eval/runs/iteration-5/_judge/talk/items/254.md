# "Who owns this change?": a five-minute postmortem

**Format:** a blameless postmortem of the August migration, given to the whole all-hands. About 700 spoken words.

## Outline

**1. What happened (0:00–0:50)**: the opening paragraph below.
- An AI-generated database migration silently dropped a NOT NULL constraint.
- Nothing crashed and no alert fired. The reconciliation numbers just stopped matching.

**2. Impact (0:50–1:40)**: speak to the half of the room that isn't engineering.
- It took three weeks to trace the mismatch back to that one migration.
- Say who paid for those three weeks outside engineering: ops and compliance, chasing numbers that didn't add up. *(Name the team, or a person if they agree, and check the description with them before Friday.)*
- Line: "That's what an engineering mistake costs: the time of the people who have to live with it, not just a bug ticket."

**3. Root cause (1:40–2:20)**
- Not the tool. AI assistants write migrations all the time, and most are fine.
- The root cause: a change got merged that nobody could explain. The engineer who merged it couldn't say what it did, and nothing in our process asked them to.
- Keep it blameless: describe the gap in the process, not the person.

**4. Contributing factor: review is where the cost moved (2:20–3:20)**
- Since spring, our PR volume is up about 60%.
- Our two senior engineers carry most of the review. Each went from about 4 hours a week of review to about 11.
- That's more than the extra volume explains: each PR now takes roughly 70% longer to review. AI-written changes are bigger, and they look plausible.
- Together that's about 14 extra hours a week, roughly a third of an engineer we never hired.
- Line: "A constraint quietly disappearing from a migration is exactly what you miss in your eleventh hour of review that week."

**5. So: should engineers use AI for everything? (3:20–3:45)**
- The answer to the all-hands question: we're not banning them, and they're fine to use.
- The question that matters isn't which tool typed the code. It's who owns the result.

**6. Action items: the rule, in three parts (3:45–4:40)**
1. **The author owns every line.** If your name is on the PR, you can explain what each line does before it goes to review, whoever or whatever wrote it.
2. **"The AI wrote it" is never an excuse.** Not in review, and not in a postmortem. It isn't a root cause; it's a description of how the code was typed.
3. **PRs over 400 changed lines get split.** Review is where the cost moved, so we protect it. Smaller changes are ones a reviewer can actually check, and one an author can actually explain.

**7. Close (4:40–5:00)**
- Go back to the opening. With these three rules, the August migration either gets explained before review or gets caught in a PR small enough to read. Either way it doesn't cost three weeks.
- Last line: "Use whatever tools make you fast. Just make sure that when someone asks 'who owns this change?', the answer is a person who can explain it."

## Opening paragraph

In August, we shipped a database migration that did something nobody asked it to do. It quietly removed a rule saying one particular field could never be empty. Nothing crashed. No alert went off. Our reconciliation numbers just stopped matching, and it took us three weeks to find out why. When we finally traced it back, we found the migration had been written by an AI assistant, and the engineer who merged it couldn't tell us what it did. In fairness, nothing in our process asked them to. So I'm not going to give you the pros and cons of AI coding tools today. I'm going to give you a five-minute postmortem. "Should engineers use AI for everything?" has a more useful question underneath it: when they do, who owns the result?
