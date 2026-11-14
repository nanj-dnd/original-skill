**Angle**: AI didn't make our code worse, it quietly moved the work of understanding code from the person who wrote it to the person reviewing it — and the rule exists to move it back.

**Built from**: 1d (accountability, not yes/no), the migration incident and the 4→11 hour review number (2c), the mixed room (3b), lunch-table tone (4a).

**Strongest objection**: "You're taxing the fast engineers to protect against one bad merge. The 60% PR volume and 2x ramp are real gains; a 400-line cap and an ownership rule will slow the people who are using the tool well." **Test**: before Friday, pull last month's PRs and sort by size. If the ones over 400 lines are mostly from people who could explain them cold, the cap is the wrong lever and you should lead with the ownership rule only. If they're where the review hours are going, you have your proof.

**Other direction**: make it the reviewers' problem instead — add review capacity, rotate the senior load, and say nothing about authorship. Cheaper politically, but it treats the symptom.

---

## Outline (5 minutes, ~650 words spoken)

**0:00 — Open on the August migration** *(opening paragraph below)*
One story, told plainly. Constraint dropped, three weeks to trace, author couldn't explain the change. Land on the line: nobody did anything wrong by the rules we had. That's the problem.

**0:50 — Say what this talk is not**
"I'm not here to tell you AI coding tools are good or bad. They're staying. New hires ramp in about half the time they used to. Pull requests are up sixty percent since spring. The question isn't whether we use them. It's who is responsible for what they produce."

**1:20 — Where the cost actually landed**
The number for the whole room: two senior engineers went from about four hours a week reviewing code to about eleven. That's nearly a day each, every week, reading code someone else generated and didn't fully read themselves. Translate it for sales/ops/compliance: *imagine your contract volume went up sixty percent, and every contract now needs legal to read it twice because the person who sent it can't tell you what's in clause 9.* The work didn't disappear. It moved — to the most expensive people in the room.

**2:20 — The rule, in three parts**
State it as a policy they could repeat back:
1. **The author owns every line.** If you merge it, you can explain it. Not "the tool suggested it" — what it does and why.
2. **"The AI wrote it" is never an answer in a postmortem.** Same as "the intern wrote it" never was. You reviewed it, you shipped it, it's yours.
3. **PRs over 400 changed lines get split.** Not because small is virtuous, but because nobody — not the author, not the reviewer — can actually hold 400 lines in their head. The August migration would have been caught in a PR you could read in one sitting.

**3:30 — Why this is good for the engineers, not just the reviewers**
Pre-empt the objection. This isn't a speed limit. If you're using the tool well, you already own your lines and this rule costs you nothing. It only bites when someone's shipping code they haven't read — and that person is going to get bitten eventually anyway, in a postmortem, at 2am. Better to make it the rule now than discover it the hard way again.

**4:10 — Why the rest of the room should care**
For compliance and ops: this is the same principle as any controlled process. Output is fine. Unaccountable output isn't. For sales: three weeks of reconciliation mismatch is three weeks of customers seeing wrong numbers.

**4:40 — Close**
"Use the tool for everything you want. Just don't ask it to be responsible for you. That part's still your job." Ask for the rule to go into the engineering handbook; invite objections after.

---

## Opening paragraph

In August, one of our engineers merged a database migration. It looked fine. It passed review. What nobody noticed was that it quietly dropped a constraint — a rule that says a certain field can't be empty — and once that rule was gone, records started slipping through with blanks in them. It took three weeks to figure out why our reconciliation numbers didn't match. When we finally traced it back to that migration and asked the engineer who merged it what the change did, the honest answer was: I don't know. The AI wrote it. And here's the thing I want you to sit with. Under the rules we had at the time, that engineer did nothing wrong. They used the tool we gave them, they opened a pull request, a reviewer approved it. Every step was followed. The code just didn't have an owner. That's what I want to fix.

---

**Before you use it**
- The 400-line threshold shows up in code review research as roughly where defect detection falls off, but I couldn't verify a specific study from here. Don't cite a source unless you've checked one; the number stands fine on its own as your policy.
- Run the test above. If the big PRs turn out to be fine, drop rule 3 from the talk and keep it as a handbook note.
- Confirm "about a day each" matches how your seniors actually count hours (11 hours ≈ 1.4 days).
- Check the migration engineer is okay being referenced, even anonymously. Half the room will guess.

**Distance from the default**: Far. The default would have been a benefits-vs-risks talk ending in "use judgment." Your answers 1d and 2c turned it into one incident, one cost number, and a rule — and the senior review hours became the spine of the argument rather than a bullet under "risks."

Want me to export this run as a Markdown file (task, defaults, your answers, angle, outline, opening, notes)?