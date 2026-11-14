# Route

**Path: specific answers → step 4 (build directly).** Your answers carry things I couldn't have guessed: review hours going from ~4 to ~11 a week on your two seniors, the August migration that dropped a NOT NULL constraint, and an argued position (the author owns every line).

Since this is a talk, here's the plan before I write anything.

**Angle:** "Use AI for everything" is the wrong fight. The rule that matters is that whoever merges a line owns it, and right now we aren't living by it: the work moved from writing code to checking it, and it landed on two people, not on the authors.

**Built from:** 1 (accountability, not a ban), 2 (half the room is sales, ops and compliance, who absorb the fallout), 3 (the 60% / 4→11 hours shift onto two seniors), 4 (you lead 7 engineers, so it's your team), 5 (the August migration).

**A tension I'd use, not smooth over:** your rule says the author owns every line, but your numbers say the reviewers are carrying it. In August both failed together: the author couldn't explain the migration, and review didn't catch it. So the talk isn't "remember to own your code". It says ownership has drifted onto two people, and here's how to give it back. Your figures also show more than extra volume. PRs are up ~1.6x but senior review time is up ~2.75x, so each PR takes about 70% longer to review. That's consistent with AI code being harder to check, not just more of it.

**Strongest objection:** "60% more PRs means we're shipping more. One bad migration is an anecdote, and people dropped constraints before AI." That's fair, and someone from leadership may say it.
**Test before Friday:** (a) check whether shipped output (tickets closed, features released) rose along with PR volume, or only the PR count did. If it rose, say so and own the trade-off. (b) Make sure you're fine telling the August story at an all-hands in a blameless way, without naming the engineer. (c) Check that the ~4 and ~11 hour figures will hold up if one of your seniors is asked in the room.

**Other directions:**
- A capacity talk for leadership: review is the new bottleneck, and here is what it costs in senior hours.
- A talk for compliance and ops: what "the AI wrote it" means for the audit trail, and why they should care who can explain a change.

**Before I write it**, a go-ahead or a redirect, plus anything you want worked in. In particular:
1. **The ask at the end.** One concrete rule, for example "if you can't explain it line by line, you don't merge it", or a change to how review is shared? Or leave the ending to me?
2. **Your two seniors:** name them, thank them, or keep them anonymous?
3. **Anything for the non-engineers:** one thing you want sales, ops and compliance to do or ask after the talk?

---

# After the go-ahead (shown after the deliverable)

User approved the angle and added: the three closing rules, the seniors kept anonymous, the "who can explain this change?" ask for non-engineers, one line on new hires ramping about twice as fast, and "answer the objection, don't debate it". Deliverable written to deliverable.md.

**Flags:**
- "About 70% longer per PR" comes from your approximate figures: 11/4 = 2.75x review time against 1.6x PRs, which is about 1.7x. It assumes the seniors review roughly the same share of PRs as they did in spring.
- "Nearly an extra working day each week" is my framing of +7 hours each.
- "A customer you can't give an answer to, an audit question" in section 5 are examples I added of fallout for those teams. Swap in real ones if you have them.
- [shipped-output figure] is a placeholder until you've checked the numbers.

**Distance from the default:**
- The thesis is accountability (who can explain the change), not "good for boilerplate, bad for architecture". That came from answer 1.
- The audience is the whole room, with a specific ask for sales, ops and compliance, instead of a talk to engineers. That came from answer 2 and your go-ahead.
- The stakes are where the cost landed (review load on two seniors, about 70% longer per PR), not generic hallucination and security risk. That came from answer 3.
- It opens on your own August incident instead of an industry statistic, told by the lead of the team. That came from answers 4 and 5.
- It ends on three hard rules instead of "use it wisely". That came from your go-ahead.
- What did not move: like the default, it doesn't oppose AI. It still says to use the tools, as the default did.
