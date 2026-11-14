# Shortlist: 5-minute all-hands talk on AI coding assistants (quick mode)

Quick mode, so I asked no questions. Everything below comes from the task alone.

## Fixed and open parts

- **Fixed:** 5 minutes of speaking (about 650 to 700 words), a company all-hands next Friday (so the audience is mostly not engineers), and the topic: whether engineers should use AI coding assistants for everything. Any study cited has to be checked.
- **Open:** the claim, the angle, who the talk is really for, the structure, and whether "for everything" is even the right question.

## What everyone gets

Main claim: AI coding assistants are powerful but aren't right for everything. Use them for boilerplate, tests and docs, and keep humans in charge of architecture, security and judgment. It's a tool, not a replacement.

The choices it makes:
1. **Thesis:** "balance": a split by task type (good for X, bad for Y).
2. **Angle:** each engineer's tool choice, task by task.
3. **Examples:** a headline adoption stat ("X% of code is now AI-written"), then a list of pros and a list of cons.
4. **Structure:** hook stat, pros, cons, "tool not replacement", a vague call to action ("use it wisely").
5. **Assumed reader:** engineers, even though most of the room isn't.
6. **Leaves out:** what the company gets back, who decides, and whether anyone has measured anything.

## Candidates

Starting points used: an inverted default choice, a constraint in the task (all-hands, 5 minutes), the reader who would disagree, and a fixed fact that fits badly with the default. With no answers from you, I couldn't start from a contradiction in your answers or a case you gave.

1. **Writing got cheap, understanding didn't.** The limit isn't which tasks to hand over. It's how much code people can review and own at 3am, and that limit hasn't moved. (inverted default: split by reviewer capacity, not by task)
2. **Talk to the 80% of the room who aren't engineers.** Tell them what will change for them: faster prototypes, and the bottleneck moving to deciding what to build. (constraint: all-hands)
3. **Yes, for everything, by default.** Then the useful work is writing down the exceptions. (inverted position)
4. **No single company policy.** Each team picks and publishes its own rules, and the talk announces that the decision is local. (reader who disagrees: the engineer who resents mandates)
5. **Hear out the skeptic.** The engineer who won't use these tools knows something. Give them the floor. (reader who disagrees)
6. **The apprenticeship problem.** If juniors never write the boring code, how do they become seniors? (something the default leaves out)
7. **Use the 5 minutes to propose an experiment, not argue a position.** Run six weeks, measure named things, report back. (constraint: 5 minutes is too short to settle anything)
8. **Accountability can't be delegated.** Whoever ships the code owns it, whoever typed it. (inverted default: ownership, not tasks)
9. **"Should" is already moot.** People are using these tools whatever the policy says. The real question is what we pretend about it. (fixed fact sits badly: the debate lags behind what people actually do)
10. **The biggest gains are outside the editor.** Tickets, specs, incident write-ups, onboarding docs.
11. **A live 90-second demo** where the assistant fails, then succeeds, and the room judges. (constraint: 5 minutes)
12. *(unlikely)* **Use the slot to ask the whole company for one thing.** For example: "tell engineering where slow software hurts you." The question is the wrong one for an all-hands.
13. *(unlikely)* **The time has no owner.** If these tools save engineering time, nobody has decided where it goes (more features? fewer bugs? training juniors?). If they don't save time, we wouldn't know. That decision belongs to the whole company. (fixed fact: the 2025 METR trial, below, sits badly with the assumption that time is saved)
14. *(unlikely)* **Sameness is the risk.** If everyone uses the same assistants, our code and product drift toward everyone else's. Some work should stay deliberately hand-made because that's where we're different.
15. **A confession.** What I stopped doing by hand, and what I regret.

## Cuts

- **8:** near-duplicate of 1 (ownership and review capacity are the same limit). Merged into 1.
- **5:** sits too close to 4 (both start from the engineer who disagrees). 4 has the more concrete outcome.
- **3:** the default reworded. "Yes with exceptions" and "no except for these" end up as the same list of tasks.
- **10:** still a split by task type, just a wider one. Close to the default.
- **11:** a format, not an idea. A live demo also risks eating half of 5 minutes.
- **15:** depends on personal experience I don't have. I can't invent your view.
- **2:** good, but it's an audience choice rather than a claim, and the chosen idea already absorbs it.
- **7:** absorbed into 13 as its call to action.

## Shortlist (picked for spread)

### A. Writing got cheap, understanding didn't
The question isn't which tasks to give the assistant. It's how much code our people can actually read, review and stand behind, and that capacity didn't grow when typing got faster.
- **Only yours because:** nothing. Anyone could make this argument.
- **Strongest objection:** assistants also help with reading and review, so the limit may move too.
- **Test:** is review time per PR, or the revert/rework rate, rising on teams that use assistants heavily? You can check this in your own repos.

### B. The apprenticeship problem
"For everything" also covers the tasks juniors learn on. If juniors skip the grind, we need another route to seniority, or in five years we'll have no seniors.
- **Only yours because:** nothing. Anyone could make this argument.
- **Strongest objection:** every abstraction (compilers, frameworks, Stack Overflow) raised the same fear, and people still learned.
- **Test:** can a junior who mostly used an assistant debug an unfamiliar failure without it? You could try that in a real onboarding exercise.

### C. The time has no owner *(unlikely; recommended, and developed below)*
Engineers argue about whether to use AI for everything, but the result that matters is a company result. If it saves time, that time went somewhere (more scope, more bugs to fix, slack) and nobody chose where. If it doesn't, we have no way to tell. The talk hands that decision to the whole room.
- **Only yours because:** the fact that it's an all-hands. The argument only works for a mixed audience. Otherwise nothing from you specifically.
- **Strongest objection:** this dodges the question asked. People came to hear "should engineers use it or not".
- **Test:** the 2025 METR randomized trial found experienced open-source developers took about 19% longer on tasks with AI tools, while believing they'd been about 20% faster. Check those numbers before Friday. The talk survives either way: its point is that we don't know our own number.

### D. "Should" is already moot
Many engineers are using these tools no matter what anyone decides. Arguing "should" lets us skip the honest question: what are we already relying on, and what have we never checked?
- **Only yours because:** nothing. It rests on a fair guess about how people at your company behave, which you can confirm or reject.
- **Strongest objection:** if usage at your company is actually low or controlled, the premise falls apart.
- **Test:** an anonymous one-question poll of engineers before the talk.

### E. Sameness is the risk *(unlikely)*
If everyone writes code with the same assistants, products converge. Some work should stay deliberately hand-made, because that's where we're different.
- **Only yours because:** nothing. Anyone could make this argument.
- **Strongest objection:** customers judge the product, not the code. Convergence in boilerplate costs nothing.
- **Test:** name one part of your product where your edge comes from doing it differently from others in your market. If you can't, drop this angle.

## Developing: C

Quick mode, so I didn't wait for a pick. I'm developing **C** because it's the only one that uses the fact that this is an all-hands. A, B and E are engineering talks given to a mostly non-engineering room. C gives everyone in the room a stake and ends with a concrete ask instead of "use it wisely". It also takes in the strongest parts of 7 (measure, don't argue) and 2 (talk to the non-engineers).
