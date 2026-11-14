---
name: original
description: Gives a non-default answer to an open task. Writes what everyone would get, asks a few targeted questions, then builds from your answers. Use for /original or "not the generic answer".
---

# Original: get off the default answer

Two people who paste the same task into a model get the same ideas in different words. This moves the answer off that default by making it visible, asking only the questions whose answers would change it, and building from those answers.

The rules come from research on AI idea diversity and a pilot test of this skill. The reason behind each rule is in `references/why.md`; read it when a rule seems wrong for the task, or when the user asks why. Don't swap the rules for prompting tricks.

## 0. Split the task

- Fixed parts: facts, numbers, constraints, anything with one right answer. Never vary these; verify them. Any statistic or study you cite, check with a search if you can. If you can't, leave it out unless the argument needs it, and list it in the closing note as unchecked (step 4), not inside the text.
- Open parts: the claim, the angle, what to include, the structure, the assumed reader, which question to answer at all.

If the whole task is fixed, say so in one line, answer normally and stop. For coursework, vary ideas and positions only, and keep any rule the course sets.

## 1. Write the default

Under ten lines, headed "What everyone gets": the main claim a pasted prompt would get, in one or two sentences, then the 3 to 6 choices it made (thesis, angle, examples, structure, who it assumes is reading, what it leaves out).

## 2. Ask, once

Skip this if the user wrote "quick", and go to "Quick mode" below.

The questions do most of the work (see `references/pilot.md`); spend the care here.

- Every question targets one choice the default made and states that choice inside the question, so it makes sense on its own.
- Don't ask what the conversation, the files at hand, an earlier answer or a fair guess already settles.
- Choose which to ask: draft one possible question per default choice, then keep the ones whose different answers would change the deliverable most. Drop any where every answer leads to much the same piece. Do this silently.
- Usually 3 to 5 questions, never more than 8, all in one go. No second round.
- Each has 2 to 4 options plus room for the user's own words. If a tool for clickable questions is available, use it (a second call back to back only if one call takes fewer than you need). Otherwise put them in one message, numbered with lettered options, so the user can reply like `1b 2a 3c 4: <own words>`.
- Mix two kinds:
  - **Position**: options are the default's choice, its opposite, and one other real stance.
  - **Specifics**: the case, number, person or incident behind their view, with concrete options drawn from the task, the conversation and any files at hand. Word these so they hold whichever way the position answers go ("Is there a real case behind this?", not "Why do you disagree?"). Always include at least one, and make sure one option, or one question, asks for a number, a measure or data where the task could use one: in testing, a user's best material was a figure that no "real case" option had room for.

## 3. Build from the answers

Build directly from what they said, however much or little it is. Whatever they gave you (a case, a number, a role, an audience, a picked option) is more theirs than anything you could generate, so start from it. If their position matches the default, build from their specifics, not from a contrarian stance they don't hold. Say plainly, later in the distance section, when the answers were thin and the piece stays close to the default.

In a few lines before the deliverable:

- **Angle**: the claim, in one sentence. Not the default's main claim unless the user chose it.
- **Built from**: which answers it rests on, by number.
- **Strongest objection**, stated fairly, and a **test**: a fact it depends on, a rebuttal it must survive, or a check they can make before using it.
- **Other directions**: one or two alternatives, a line each.

Where two answers pull against each other, or a fixed fact sits badly with one of them, use that tension instead of smoothing it over.

If the deliverable runs longer than about a page, or is a talk, show this block and wait before writing: a go-ahead, a redirect, or anything they want worked in (a line, an example, how it ends). Shorter pieces go straight to step 4, with one line after the deliverable inviting anything to add.

## Quick mode: no answers

With nothing from the user to build on, variety has to come from generating. In one pass:

1. List 8 to 12 one-line candidates from at least three different starting points: an inverted default choice, a constraint in the task, the reader who would disagree, a fixed fact that sits badly with the default. Revise so no two are the same idea and none is the default reworded; ban exactly one thing, the default's main claim.
2. Pick the one that differs most from the default and still answers the task, say in one line why, and say plainly that without answers it isn't tailored to them.
3. Go to step 4. No shortlist, no wait. No personas, "be bold", example ideas to imitate, or rerolls.

If the idea's value depends on being new to the world (a research question, a product idea), search for prior work if you can and say what you found. Never score novelty yourself.

## 4. Develop

Write the deliverable from the chosen angle and verify the fixed parts. Make it ready to use as it stands: no brackets, placeholders or "[unchecked]" marks inside it. Use only facts the user gave about their own life and don't invent anecdotes; where the piece would be stronger with a real detail they didn't give, write it so it holds without one, and suggest the detail in the closing note.

Before showing it, reread the draft once as a demanding reader who doubts the angle: find where it goes thin, turns generic, or drifts back toward the default, and revise those parts. Keep the angle, don't show the critique, and don't judge how new the idea is. One pass only.
If it is prose going out under the user's name and a skill for their writing voice is installed (for example `anshul-voice`), hand the writing to it once the angle is settled; otherwise follow the tone they described.

After the deliverable, a short **Before you use it** note, only the items that apply: figures or studies you couldn't check; any small detail you added that they should confirm; one or two real details they could add and where. Then **Distance from the default**: 3 to 5 lines, each naming something the output has that the default didn't and which answer caused it, plus one line on what did not move. If little differs, say so plainly. Don't dress up a default answer.

## 5. Record and export

Offer to export the run. On yes, make a downloadable Markdown file (a PDF only if they ask; one Markdown block if you can't write files) in the format below.

Run record, sections in order:

- Title: the task in a few words.
- One line: date · answered or quick · angle chosen, or "not written".
- Task (as given; say if trimmed) · Fixed and open parts · What everyone gets · What they said (each default choice → their answer, in their own words; "quick run, no questions" if skipped) · Angle (and, in quick mode, the candidates) · Deliverable (in full) · Before you use it · Distance from the default · Prior work ("not searched" if none).

Write it from what was actually said. Don't tidy their answers into positions they didn't take.

## What this cannot do

It draws out what is distinct in the user's view; it can't manufacture one. Most of its effect comes from asking before writing: in testing, a plain model told to ask clarifying questions first did about as well, so what this adds is making the model ask, showing the default, the objection and test, and honest checks. If a run produces nothing the default didn't already have, report that as the result.
