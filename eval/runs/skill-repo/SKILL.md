---
name: original
description: Gives a non-default answer to an open task. Writes what everyone would get, asks a few targeted questions, then builds from your answers. Use for /original or "not the generic answer".
---

# Original: get off the default answer

Two people who paste the same task into a model get the same ideas in different words. This moves the answer off that default by making it visible, asking only the questions whose answers would change it, and building from those answers.

The rules come from research on AI idea diversity and a pilot test of this skill. The reason behind each rule is in `references/why.md`; read it when a rule seems wrong for the task, or when the user asks why. Don't swap the rules for prompting tricks.

## 0. Split the task

- Fixed parts: facts, numbers, constraints, anything with one right answer. Never vary these; verify them. Any statistic or study you cite, check with a search if you can; if you can't, mark it unchecked next to the figure.
- Open parts: the claim, the angle, what to include, the structure, the assumed reader, which question to answer at all.

If the whole task is fixed, say so in one line, answer normally and stop. For coursework, vary ideas and positions only, and keep any rule the course sets.

## 1. Write the default

Under ten lines, headed "What everyone gets": the main claim a pasted prompt would get, in one or two sentences, then the 3 to 6 choices it made (thesis, angle, examples, structure, who it assumes is reading, what it leaves out).

## 2. Ask, once

Skip this if the user wrote "quick", and go to step 3 with no answers.

The questions do most of the work (see `references/pilot.md`); spend the care here.

- Every question targets one choice the default made and states that choice inside the question, so it makes sense on its own.
- Don't ask what the conversation, the files at hand, an earlier answer or a fair guess already settles.
- Choose which to ask: draft one possible question per default choice, then keep the ones whose different answers would change the deliverable most. Drop any where every answer leads to much the same piece. Do this silently.
- Usually 3 to 5 questions, never more than 8, all in one go. No second round.
- Each has 2 to 4 options plus room for the user's own words. If a tool for clickable questions is available, use it (a second call back to back only if one call takes fewer than you need). Otherwise put them in one message, numbered with lettered options, so the user can reply like `1b 2a 3c 4: <own words>`.
- Mix two kinds:
  - **Position**: options are the default's choice, its opposite, and one other real stance.
  - **Specifics**: the case, number, person or incident behind their view, with concrete options drawn from the task, the conversation and any files at hand. Word these so they hold whichever way the position answers go ("Is there a real case behind this?", not "Why do you disagree?"). Always include at least one.

## 3. Route on the answers

Pick one path and say in one line which and why.

- **Specific answers → step 4.** The user said, in their own words, at least one thing you couldn't have guessed: a real case, a number, a named audience, a hard constraint, or a position they argued for. A picked option is a direction, not a specific, even when it states a position. Specific answers go here even if the position matches the default; then build from the specifics, not from a contrarian stance they don't hold.
- **Thin answers → step 5.** Mostly picked options, "don't know", "keep it general", or words anyone might type.
- **Quick mode (no answers) → step 5.**

If the answers both match the default and are thin, the default may simply be their answer. Say so, and ask whether they want the default done well or a shortlist of alternatives.

## 4. Specific answers: build directly

No long candidate list. In a few lines before the deliverable:

- **Angle**: the claim, in one sentence. Not the default's main claim unless the user chose it.
- **Built from**: which answers it rests on, by number.
- **Strongest objection**, stated fairly, and a **test**: a fact it depends on, a rebuttal it must survive, or a check they can make before using it.
- **Other directions**: one or two alternatives, a line each.

Where two answers pull against each other, or a fixed fact sits badly with one of them, use that tension instead of smoothing it over.

If the deliverable runs longer than about a page, or is a talk, show this block and wait before writing: a go-ahead, a redirect, or anything they want worked in (a line, an example, how it ends). Shorter pieces go straight to step 6, with one line after the deliverable inviting anything to add.

## 5. Thin answers or quick mode: generate, cut, shortlist

In one continuous pass:

1. List 12 to 15 one-line candidates for the open parts, from at least three different starting points: a contradiction in their answers, an inverted default choice, a constraint they named, the reader who would disagree, a case they gave, a fixed fact that sits badly with the default.
2. Revise so no two are the same idea and none is the default reworded.
3. Add two or three you would be unlikely to say, marked unlikely.
4. Ban exactly one thing: the default's main claim. No other bans.

Two or three passes at most. No personas, "be bold", example ideas to imitate, analogies from unrelated fields by default, or rerolls.

**Cut** near-duplicates, anything a fixed fact breaks, anything that is the default reworded, and anything the user already turned down in this conversation (unless a new answer removes the reason). If the idea's value depends on being new to the world (a research question, a product idea), search for prior work if you can and say what you found. Never score novelty yourself or show a novelty number. Keep the 3 to 5 survivors that differ most from each other and from the default, even if that drops a strong idea that sits close to another.

**Shortlist.** For each survivor:

- the idea in one or two sentences
- **Only yours because**: which answers it depends on, or "nothing; this is available to anyone"
- **Strongest objection**: one line, stated fairly
- **Test**: a fact it depends on, a rebuttal it must survive, or a prediction to check later

Recommend one and ask which to develop; combinations ("A with C's ending") are fine. In quick mode don't wait: say which one you're developing and why, and say plainly that without answers it isn't tailored to them.

## 6. Develop

Write the deliverable from the chosen angle and verify the fixed parts. Use only facts the user gave about their own life; don't invent anecdotes, and flag any small detail you added so they can check it. Where the piece needs a real detail they didn't give, leave a marked placeholder ("[your example here]") instead of making one up.

Before showing it, reread the draft once as a demanding reader who doubts the angle: find where it goes thin, turns generic, or drifts back toward the default, and revise those parts. Keep the angle, don't show the critique, and don't judge how new the idea is. One pass only.
If it is prose going out under the user's name and a skill for their writing voice is installed (for example `anshul-voice`), hand the writing to it once the angle is settled; otherwise follow the tone they described.

End with **Distance from the default**: 3 to 5 lines, each naming something the output has that the default didn't and which answer caused it, plus one line on what did not move. If little differs, say so plainly. Don't dress up a default answer.

## 7. Record and export

Offer to export the run. On yes, make a downloadable Markdown file (a PDF only if they ask; one Markdown block if you can't write files) in the format below.

Run record, sections in order:

- Title: the task in a few words.
- One line: date · path (direct, shortlist or quick) · angle chosen, or "not picked".
- Task (as given; say if trimmed) · Fixed and open parts · What everyone gets · What they said (each default choice → their answer, in their own words; "quick run, no questions" if skipped) · Angle (direct path) or Candidates, cuts with reasons, and Shortlist (shortlist path) · Deliverable (in full) · Distance from the default · Prior work ("not searched" if none).

Write it from what was actually said. Don't tidy their answers into positions they didn't take.

## What this cannot do

It draws out what is distinct in the user's view; it can't manufacture one. Without a clear view or a real case, the shortlist gives variety but not fit. If a run produces nothing the default didn't already have, report that as the result.
