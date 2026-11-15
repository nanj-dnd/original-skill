**Angle**: The problem isn't how much AI the engineers use; it's that since spring, "who can explain this code" has quietly become nobody, and three rules put a name back on every change.
**Built from**: 1d (your rule), 2b and 2c (the August migration, the 60%, the 4→11 hours), 3b (mixed room, no jargon), 4a (leave with a policy).
**Strongest objection**: the 400-line cap probably wouldn't have caught August. A migration that drops one constraint is a handful of lines; the first two rules do the safety work, and the third is really about your seniors' review hours. **Test**: pull up the August PR and check its size, then pull last month's PRs over 400 lines and ask the two seniors how many they'd have caught something in if split. If August was small, say so in the talk and present rule three honestly as a review-load rule, not a safety rule.
**Other direction**: skip the line cap and instead require every PR description to say, in plain words, what the change does and what it could break, written by the author. It's the exact sentence the August engineer couldn't give, demanded up front.

---

## Outline (5 minutes)

**1. August (0:00–1:10)**
The opening paragraph below. One story, told plainly, ending on the sentence the engineer couldn't say.

**2. What changed since spring (1:10–2:10)**
- This isn't a story about one person. Since spring, the amount of code going in for review is up about 60%.
- Translate for the room: more code, written faster, by people who increasingly didn't type it themselves.
- Two senior engineers went from about 4 hours a week checking other people's work to about 11. Say it as a fraction: nearly a third of their week, up from a tenth.
- The point: those two are the people best placed to catch August, and they now have less time per change to catch it. The tools made writing cheap. They did not make understanding cheap. August lives in that gap.

**3. The rule, three lines, one slide (2:10–3:50)**
Say each once, then the reason.
- *You own every line you merge.* Not "you ran the checks"; you can explain it. If someone asks what a change does and the person who merged it can't answer, it isn't ready.
- *"The AI wrote it" is never an excuse in a postmortem.* (Gloss for the room: a postmortem is the write-up after something breaks.) In August that sentence was true and useless. The rule exists so nobody needs to say it again.
- *Any change over 400 lines gets split.* A change too big to read carefully is a change nobody read carefully. This one is as much for the reviewers' 11 hours as for safety.
- Say what the rule is not: it is not "use less AI." Volume can stay up 60%. It's that every line arrives with a human who can explain it.

**4. What this asks of everyone else in the room (3:50–4:30)**
- Non-engineers: "what does this do?" is a fair question to ask engineering, and you should get a plain answer. This rule makes that answer required.
- Anyone waiting on features: splitting big changes means some things land in pieces. That's the rule working, not engineering slowing down.

**5. Close (4:30–5:00)**
- Back to August: three weeks to find, one question to answer, and the answer was "I don't know." Three rules so that answer never comes back.
- Say when the rule starts and where the written version lives.

---

## Opening paragraph

In August, a change went into our database. It was small, it was written by an AI assistant, and it went in the way changes go in. What it did, and nobody noticed at the time, was quietly remove a rule that said one particular field could never be left empty. That's it. One safety check, gone. For the next three weeks, numbers that were supposed to match stopped matching, and it took that long to trace it back to that one change. When we did, we asked the engineer who'd merged it what the change did. And they couldn't say. I'm not telling you this to point at anyone. I'm telling you because I think that sentence, "I can't say what it did," is the real problem, and it has very little to do with how much AI our engineers are using. So I'm not going to spend five minutes on pros and cons. I'm going to tell you what's changed since the spring, and then ask you to back three rules.

---

**Before you use it**
- The opening runs about 70 seconds spoken; cut the "I'm not telling you this to point at anyone" line if you need it under a minute.
- Check whether the engineer from August is in the room and knows the story is being told; the paragraph keeps them anonymous, but the company may not.
- Confirm you're happy saying the 60% and the 4→11 hours company-wide.
- Run the test above on the August PR's size before you present rule three as a safety measure.

**Distance from the default**: the samples all open by declaring "that's the wrong question," then run a benefits-then-risks structure and close on a generic "human in the loop"; this drops the reframe and the pros-and-cons (your instruction), builds the whole talk on August and your two numbers (2b, 2c), and glosses every technical term for the mixed room (3b). What it still shares with the samples is the wording "you own every line you merge" and "the AI wrote it is never an excuse in a postmortem", which appeared in all three, but those are your rule verbatim, so they stay.