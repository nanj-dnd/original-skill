---
name: original
description: Gives a non-default answer to an open task (an essay angle, an argument, a strategy, a product or research idea, a talk). Writes what everyone would get, asks a few targeted questions, then generates against it. Use for /original, and whenever the user says something like "not the generic answer", "make this less generic", "everyone says the same thing", "give me a take nobody else has" or "what's an original angle on this". Not for tasks with one right answer.
---

# Original: get off the default answer

Two people who paste the same task into a model get the same ideas in different words. This moves the answer off that default by making it visible, asking only the questions whose answers would change it, and generating against it. The rules come from research on AI idea diversity (`references/research.md` in this skill). Do not swap them for prompting tricks.

## 0. Split the task

- Fixed parts: facts, numbers, constraints, anything with one right answer. Never vary these; verify them.
- Open parts: the claim, the angle, what to include, the structure, the assumed reader, which question to answer at all.

If the whole task is fixed, say so in one line, answer normally and stop. For coursework, vary ideas and positions only, and keep any rule the course sets.

## 1. Write the default

Under ten lines, headed "What everyone gets": the main claim a pasted prompt would get, in one or two sentences, then the 3 to 6 choices it made (thesis, angle, examples, structure, who it assumes is reading, what it leaves out).

## 2. Ask, once

Skip this if the user wrote "quick", and work from the task and the conversation alone. In quick mode, also skip waiting for a pick in step 5: show the shortlist, say which one you're developing and why, and go straight to step 6. Quick should cost the user no extra turns.

- Every question targets one choice the default made, and states that choice inside the question.
- Don't ask what the conversation, an earlier answer or a fair guess already settles.
- Ask every question in one go: usually 3 to 5, never more than 8. Each has 2 to 4 options plus room for the user's own words. If a tool for clickable questions is available, use it (a second call back to back only if you truly need more than it takes at once). Otherwise put them in one message, numbered with lettered options, so the user can reply like `1b 2a 3c 4: <own words>`. No second round of follow-ups.
- Mix two kinds:
  - Position questions: options are the default's choice, its opposite, and one other real stance.
  - Specifics questions: the case, number, person or incident behind their view, with concrete options drawn from the task and the conversation. Word these so they hold whichever way the position answers go ("Is there a real case behind this?", not "Why do you disagree?").

Fewer, sharper questions beat more. In the research, cutting an interview by 80% barely changed what the model knew, and long questionnaires got shorter, flatter answers.

If the answers mostly pick the default's choices, that is a real result, not a failure: the user agrees with the default. Say so in one line. Then either give the default done well (if that's what they want) or generate only from the specifics and constraints they named, and say which you're doing.

## 3. Generate against the default

In one continuous pass:

1. List 12 to 15 one-line candidates for the open parts. Start from the tensions: where the answers contradict the default, where two answers pull against each other, where a fixed fact sits badly with the default's claim.
2. Revise so that no two are the same idea and none is the default reworded.
3. Add two or three that you would be unlikely to say, and mark them unlikely. This is about how probable the idea is coming from you, not a judgement of how new it is to the world (step 4 says why you shouldn't make that one).
4. Ban exactly one thing: the default's main claim. Don't stack bans; quality collapses after the first.

Vary the starting point across candidates, and use at least three of these: a contradiction in their answers, an inverted default choice, a constraint they named, the reader who would disagree, a specific case they gave. Different starting points produce pools that barely overlap, which is where the coverage comes from. Two or three passes at most.

Don't add a persona, "be bold", example ideas to imitate, an analogy from an unrelated field by default, or rerolls. None of these moved idea diversity in the studies, and examples and far analogies made it worse.

## 4. Cut

Drop near-duplicates, anything a fixed fact breaks, anything that is the default reworded, and anything the user already turned down in this chat (unless a new answer removes the reason). If the idea's value depends on being new to the world (a research question, a product idea), search the web for prior work if you can, and say what you found. Never score novelty yourself or show a novelty number; model judgements of novelty are unreliable and lean toward machine-sounding ideas.

Then choose the shortlist for spread, not just strength: pick the 3 to 5 survivors that differ most from each other and from the default, even if that means leaving out a strong idea that sits close to another one. In the research, picking the most different ideas from a pool afterwards beat every prompting method.

## 5. Shortlist, and the user picks

Show the 3 to 5 survivors. For each:

- the idea in one or two sentences
- **Only yours because**: which of the user's answers it depends on, or "nothing; this is available to anyone"
- **Strongest objection**: one line, stated fairly
- **Test**: a fact it depends on, a rebuttal it has to survive, or a prediction that can be checked later

Recommend one, then ask which to develop. The choice is theirs.

## 6. Develop

Write the deliverable from the chosen idea and verify the fixed parts. If it is prose going out under the user's name and a skill for their writing voice is installed (for example `my-writing-style`), hand the writing to it once the idea is settled; otherwise follow any attached style guide. End with:

**Distance from the default**: 3 to 5 lines, each naming something in the output that the default did not have and which answer caused it. If little differs, say so plainly. Don't dress up a default answer.

## 7. Export

Offer to export the run. On yes, make a downloadable Markdown file (a PDF only if they ask; otherwise one Markdown block if you can't write files) and present it with these sections in order: the task in a few words as the title; a line with the date, full or quick, and which idea was picked; Task; Fixed and open parts; What everyone gets; What they said (each default choice, then their answer in their own words); Candidates (all of them, unlikely ones marked, then each cut with its reason); Shortlist (with only-yours, objection and test); Picked; Deliverable (in full); Distance from the default; Prior work. Write it from what was actually said. Don't tidy their answers into positions they didn't take.

## What this cannot do

It draws out and sharpens what is distinct in the user's view; it can't manufacture a view they don't have. Whether personal context makes ideas more original, and not just better fitted to the person, is untested. If a run produces nothing the default didn't already have, report that as the result.
