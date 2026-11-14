# Shortlist (quick mode)

Quick mode: no questions asked, worked from the task alone. Nothing below depends on answers the user gave, because there were none; "Only yours because" points at the task's own constraints where it can.

## Fixed and open parts

- **Fixed:** 5 minutes of speaking time (about 650 to 750 words at a normal speaking pace); a company all-hands, so the room includes non-engineers; the question as posed ("should engineers use AI coding assistants for everything?"); an outline plus one opening paragraph. No statistics will go in unless they can be verified, so the draft avoids them.
- **Open:** the claim, the angle, the structure, which part of the room it speaks to, and whether to answer the question as asked at all.

## What everyone gets

Main claim: "AI coding assistants are powerful productivity tools, but not for everything. Use them for the routine work and keep humans in charge of the judgment calls: augment, don't replace."

Choices it made:
1. **Thesis:** a balanced middle ("great tool, use it wisely"), with the split drawn by task type: boilerplate, tests and docs yes; architecture, security and novel problems no.
2. **Reason for the line:** risk and quality (hallucinations, bugs, security holes, licensing).
3. **Structure:** a hook stat about adoption or productivity, then pros, cons, guidelines and a call to action.
4. **Reader:** assumes the room is engineers, even though it is an all-hands.
5. **Examples:** generic ones like writing unit tests, a hallucinated API and a security vulnerability.
6. **Leaves out:** what the company sells and why that would change the answer; anyone who isn't an engineer.

## Candidates

Starting points used: an inverted default choice, a constraint the user named (all-hands, 5 minutes, the word "everything"), and the reader who would disagree (the skeptical senior engineer, the enthusiast, the customer).

1. *(constraint: all-hands)* Speak to the non-engineers: give sales, support and product the three questions they should be able to ask engineering about AI-written code.
2. *(inverted thesis)* Yes, everything, with one condition: you can explain every line you ship. The line is drawn by whether you can defend the code, not by task type.
3. *(constraint: "everything")* Writing code is no longer the slow part; reading it is. Set the policy by review capacity, not by what the tool is used for.
4. *(reader who disagrees: skeptical senior)* Take the apprenticeship point seriously: the struggle that turns juniors into seniors is what gets automated, so who are our senior engineers in five years?
5. *(reader who disagrees: enthusiast)* The cost lands at 2am: on-call for code nobody remembers writing.
6. *(inverted structure)* No pros and cons. Make three checkable predictions about our own codebase and commit to revisiting them at an all-hands a year from now.
7. *(inverted: policy to measurement)* Nobody in the room knows yet, so run it as a stated experiment with a metric instead of a policy.
8. *(constraint: 5 minutes)* Draw the line by reversibility: use it freely where mistakes are cheap to undo, carefully where they aren't.
9. The real question is what the saved hours are for. Decide that before deciding on tool usage.
10. *(unlikely)* Mandates ("use AI for everything") and bans both signal distrust of engineers. The policy should be: engineers decide, and say what they used.
11. *(reader who disagrees: the customer)* Customers don't care how the code was written. Measure outcomes, not tool usage, because counting usage gets you usage.
12. *(unlikely)* Confession format: one real week of the speaker's own work, covering what went to the assistant and what they took back. No general claims.
13. *(unlikely)* Assistants give the most likely answer, and every competitor has the same assistant. Use it for everything that should be the same as everyone else's, and keep it off the places where we're paid to be different.
14. What does "an engineer" mean here in two years, and what do we hire for?
15. Use the tool to argue with the code, not to write it: critique mode over draft mode.

Banned (one thing only): the default's main claim, "use it for routine work but not everything, and keep humans in the loop."

## Cuts

- **8 (reversibility):** the default reworded. It is still a "where to use it" rule split by risk.
- **9 (what saved hours are for):** "frees you up for higher-value work" is a stock line in the default.
- **5 (2am on-call):** too close to 3. Both say the cost moves downstream of writing; 3 is the broader version.
- **14 (what we hire for):** too close to 4.
- **12 (confession week):** depends on the user's own week, which quick mode doesn't have. It would be strong in full mode.
- **15 (critique mode):** a tactic, not a thesis. Folded into 13's closing ask.
- **6 and 7 (predictions, experiment):** close to each other, and both sit close to 11's "measure it" stance. Left out for spread.
- **10 (trust and disclosure):** a strong one, but it sits near 2 (the individual engineer decides and owns it). Left out for spread.

## Shortlist

**A. The bottleneck moved (3).** Generating code is now cheap and reading it is not. Whether engineers use AI for "everything" matters less than whether we have budgeted the review time that everything now needs.
- **Only yours because:** nothing; this is available to anyone. It leans on the word "everything" in the task.
- **Strongest objection:** for most of the room this is an engineering-process point, so it is a hard sell at an all-hands.
- **Test:** whether review queue time and PR size have actually grown on our teams since the assistants arrived. Engineering can check this.

**B. Who becomes senior? (4).** The work assistants absorb first is the work that used to train juniors. The question for the company is how people learn judgment here when the struggle is optional.
- **Only yours because:** nothing; this is available to anyone.
- **Strongest objection:** every new tool (compilers, Stack Overflow) drew the same worry, and engineers still learned.
- **Test:** it has to survive the rebuttal "juniors learn faster by reading and fixing generated code". Is there evidence either way in our own onboarding?

**C. The all-hands question (1).** The talk is for the people who aren't engineers: what sales, support and product should be able to ask engineering about AI-written code, and why the answer is theirs to care about.
- **Only yours because:** it follows from the setting the user named (an all-hands, not an engineering meeting).
- **Strongest objection:** it sidesteps the question that was asked. Engineers in the room may hear it as a dodge.
- **Test:** whether non-engineers in the room actually have a stake they can act on. If they don't, it is filler.

**D. Same as everyone, on purpose (13, unlikely).** Assistants are built to give the most likely answer, and every competitor has the same ones. So use them for everything that should be the same as everyone else's, which is most code. Keep them off the few places where we are paid to be different.
- **Only yours because:** it uses the all-hands setting, since every function in the company knows where we differ, and the literal word "everything" in the question.
- **Strongest objection:** what makes a company different usually lives in product decisions, not in lines of code, and assistants can be pushed off the obvious answer.
- **Test:** can each team name two or three places in its code that are deliberately not what a competitor would write? If no team can, the talk's premise fails for this company.

## Picked: D

Quick mode, so no waiting for a pick. I'm developing **D**. It is the only candidate that answers the yes-or-no question directly ("yes, for nearly everything") but draws the line for a reason the default never uses: being distinctive, not risk. It also speaks to the whole all-hands room, because sales, product and support know where the company is different as well as engineering does. A and C are good fallbacks: A if the room is mostly engineers, C if leadership wants a talk aimed at the non-engineers.
