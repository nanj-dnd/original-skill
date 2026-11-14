---
name: original
description: Gives a non-default answer to an open task (an essay angle, an argument, a strategy, a product or research idea, a talk). Writes what everyone would get, asks a few targeted questions, then builds the answer from what only this user knows. Use for /original, and whenever the user says something like "not the generic answer", "make this less generic", "everyone says the same thing", "give me a take nobody else has" or "what's an original angle on this". Not for tasks with one right answer.
---

# Original: get off the default answer

Two people who paste the same task into a model get the same ideas in different words. This moves the answer off that default by making it visible, asking only the questions whose answers would change it, and building from those answers. The rules come from research on AI idea diversity (`references/research.md`) and from a pilot test of this skill (`references/pilot.md`). Do not swap them for prompting tricks.

The pilot's main lesson shapes this version: **the questions do most of the work.** When a user's answers carried a real position or a specific case, a plain model given those answers reached the same idea as the full generate-and-shortlist process, every time. So the shortlist is kept for when it can help (thin answers, or no answers at all) and skipped when the answers already point somewhere.

## 0. Split the task

- Fixed parts: facts, numbers, constraints, anything with one right answer. Never vary these; verify them. If you can't verify a figure, say so next to it rather than presenting it as checked.
- Open parts: the claim, the angle, what to include, the structure, the assumed reader, which question to answer at all.

If the whole task is fixed, say so in one line, answer normally and stop. For coursework, vary ideas and positions only, and keep any rule the course sets.

## 1. Write the default

Under ten lines, headed "What everyone gets": the main claim a pasted prompt would get, in one or two sentences, then the 3 to 6 choices it made (thesis, angle, examples, structure, who it assumes is reading, what it leaves out).

## 2. Ask, once

Skip this if the user wrote "quick", and go to step 3 with no answers.

These questions are the most valuable part of the skill, so spend the care here.

- Every question targets one choice the default made, and states that choice inside the question.
- Don't ask what the conversation, an earlier answer or a fair guess already settles.
- Ask every question in one go: usually 3 to 5, never more than 8. Each has 2 to 4 options plus room for the user's own words. If a tool for clickable questions is available, use it (a second call back to back only if you truly need more than it takes at once). Otherwise put them in one message, numbered with lettered options, so the user can reply like `1b 2a 3c 4: <own words>`. No second round of follow-ups.
- Mix two kinds:
  - Position questions: options are the default's choice, its opposite, and one other real stance.
  - Specifics questions: the case, number, person or incident behind their view, with concrete options drawn from the task and the conversation. Word these so they hold whichever way the position answers go ("Is there a real case behind this?", not "Why do you disagree?"). Always include at least one; a real case was the single strongest ingredient in the pilot.

Fewer, sharper questions beat more. In the research, cutting an interview by 80% barely changed what the model knew, and long questionnaires got shorter, flatter answers.

## 3. Route on the answers

Read the answers and pick one path. Say in one line which path you're taking and why.

- **Specific answers → step 4.** The user gave at least one concrete thing the default didn't have: a real case, a number, a named audience, a hard constraint, or a stated position of their own. This is true even if their position matches the default; then build from the specifics, not from a contrarian stance they don't hold.
- **Thin answers → step 5.** Mostly picked letters with no specifics, "don't know", or "keep it general". There's not enough to build from, so generating candidates is where the variety has to come from.
- **Quick mode (no answers) → step 5.**

If the answers both match the default and are thin, the default may simply be their answer. Say so, and ask whether they want the default done well or a shortlist of alternatives. That is the only case where you stop to ask again.

## 4. Specific answers: build directly

Don't generate a long candidate list or wait for a pick. Instead, in a few lines before the deliverable:

- **Angle:** the claim you're building, in one sentence. It must not be the default's main claim unless the user chose that claim themselves.
- **Built from:** which answers it rests on, by number.
- **Strongest objection** and a **test** (a fact it depends on, a rebuttal it has to survive, or a check they can make before using it). Users took these seriously in the pilot and corrected their own claims because of them.
- **Other directions:** one or two alternatives in a line each, so the user can redirect if you misread them.

Where two answers pull against each other, or a fixed fact sits badly with one of them, use that tension rather than smoothing it over; it is usually the most distinctive thing on the page. Then go to step 6.

## 5. Thin answers or quick mode: generate, cut, shortlist

In one continuous pass:

1. List 12 to 15 one-line candidates for the open parts. Use at least three different starting points: a contradiction in their answers, an inverted default choice, a constraint they named, the reader who would disagree, a specific case they gave, a fixed fact that sits badly with the default. Different starting points produce pools that barely overlap, which is where the coverage comes from.
2. Revise so that no two are the same idea and none is the default reworded.
3. Add two or three that you would be unlikely to say, and mark them unlikely. This is about how probable the idea is coming from you, not a judgement of how new it is to the world.
4. Ban exactly one thing: the default's main claim. Don't stack bans; quality collapses after the first.

Don't add a persona, "be bold", example ideas to imitate, an analogy from an unrelated field by default, or rerolls. None of these moved idea diversity in the studies, and examples and far analogies made it worse. Two or three passes at most.

**Cut.** Drop near-duplicates, anything a fixed fact breaks, anything that is the default reworded, and anything the user already turned down in this chat (unless a new answer removes the reason). If the idea's value depends on being new to the world (a research question, a product idea), search the web for prior work if you can, and say what you found. Never score novelty yourself or show a novelty number; model judgements of novelty are unreliable and lean toward machine-sounding ideas. Then choose the 3 to 5 survivors that differ most from each other and from the default, even if that leaves out a strong idea that sits close to another one.

**Shortlist.** For each survivor:

- the idea in one or two sentences
- **Only yours because**: which of the user's answers it depends on, or "nothing; this is available to anyone"
- **Strongest objection**: one line, stated fairly
- **Test**: a fact it depends on, a rebuttal it has to survive, or a prediction that can be checked later

Recommend one and ask which to develop; combinations ("A with C's ending") are fine. In quick mode, don't wait: say which one you're developing and why, and say plainly that without answers it isn't tailored to them. Then go to step 6.

## 6. Develop

Write the deliverable from the chosen angle and verify the fixed parts. Use only the facts the user gave you about their own life; don't invent anecdotes, and flag any small detail you added so they can check it. If it is prose going out under the user's name and a skill for their writing voice is installed (for example `my-writing-style`), hand the writing to it once the angle is settled; otherwise follow any attached style guide or the tone they described. End with:

**Distance from the default**: 3 to 5 lines, each naming something in the output that the default did not have and which answer caused it. Include one line on what did not move, if anything. If little differs, say so plainly. Don't dress up a default answer.

## 7. Export

Offer to export the run. On yes, make a downloadable Markdown file (a PDF only if they ask; otherwise one Markdown block if you can't write files) with these sections in order: the task in a few words as the title; a line with the date, the path taken (direct, shortlist or quick) and the angle chosen; Task; Fixed and open parts; What everyone gets; What they said (each default choice, then their answer in their own words); Angle (direct path) or Candidates and Shortlist (shortlist path, with cuts and reasons); Deliverable (in full); Distance from the default; Prior work. Write it from what was actually said. Don't tidy their answers into positions they didn't take.

## What this cannot do

It draws out and sharpens what is distinct in the user's view; it can't manufacture a view they don't have. In the pilot, when users had a clear view and a real case, the answers carried the result; when they don't, the shortlist gives variety but not fit, because the ideas aren't built on anything of theirs. If a run produces nothing the default didn't already have, report that as the result.
