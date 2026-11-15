# Original: get off the default answer

Two people who paste the same task into a model get the same ideas. This shows the user that default, asks a few questions before writing, and builds from their answers. Asking before writing does most of the work; the reason for each rule is in `references/why.md`.

<!-- if code -->
Files: `runs/` (a record per run, for export), `export_pdf.py`, `references/`. This file is built from `~/Downloads/original-v2/src/core.md` by `build.py`; change the source and rebuild, since edits here are overwritten on install.

If the task is `export`, skip to "Export".

<!-- end -->
## 1. Default

If the task has one right answer (a fact, a calculation), say so in one line and just answer it.

Otherwise write, under eight lines, headed "What everyone gets": the main claim a pasted prompt would get, then the 3 to 5 choices it made (angle, examples, structure, reader, tone).

## 2. Ask

3 or 4 questions, all at once, no second round.
<!-- if code -->
Use one AskUserQuestion call; each question has 2 to 4 options, and the free-text option covers the rest.
<!-- end -->
<!-- if claude-ai -->
Each has 2 to 4 options. Use a clickable question tool if there is one; otherwise number them with lettered options so the user can reply like `1b 2a 3c`.
<!-- end -->

- Draft one question per default choice and keep the ones whose answers would change the piece most. Each states the default's choice inside it, so it reads on its own.
- One asks for their real material: a case, and a number or measure where the task could use one.
- One asks how it should sound for this reader (plain or formal, whose name is on it), unless that is already settled.
- Don't ask what the conversation or a fair guess already settles.

## 3. Angle

Build from whatever they gave you, even picked options. If they agree with the default, build from their specifics, not a contrarian stance they don't hold. If their answers are thin or their view is mild, keep the stance as measured as theirs: make the piece specific and well made, not more opinionated than they are. Before the piece, in four lines:

- **Angle**: the claim in one sentence; not the default's unless they chose it.
- **Built from**: which answers.
- **Strongest objection**, stated fairly, and a **test** they can run before using it.
- **Other direction**: one alternative, in a line.

## 4. Write

- Verify the facts. Check any statistic or study with a search if you can; otherwise leave it out unless the argument needs it.
- Make it ready to use: no brackets, placeholders or "[unchecked]" marks inside it.
- Every fact about the user, their life, their work or their past must come from their answers or the conversation. In first-person pieces that includes small colour: past attempts, other habits, how they felt, what someone said. If they didn't give it, write around the gap instead of filling it with a plausible detail.
- Use the tone they chose. Hand it to a voice skill (such as `anshul-voice`) only if they asked for their own voice.
- Before showing it, reread it once as a reader who doubts the angle: fix where it goes thin or generic, and cut any personal detail you can't trace to an answer.

After it, only if something applies, **Before you use it**: figures you couldn't check, details to confirm, a real detail worth adding. Then one line of **Distance from the default**: what changed and which answer caused it, or that little did.

## 5. Record

<!-- if code -->
Save the run to `runs/<YYYY-MM-DD>-<slug>.md` and tell the user `/original export` makes a PDF of it.
<!-- end -->
<!-- if claude-ai -->
Offer to export the run as a Markdown file (PDF if they ask).
<!-- end -->
The record holds: the task, What everyone gets, each question with their answer in their words, the angle block, the piece, the note and the distance line.

<!-- if code -->
## Export

`/original export` makes a PDF in `~/Downloads/originals/` from this conversation's run, or the newest file in `runs/`, or one named by topic or date (ask with AskUserQuestion if several match). Update the record first if the piece changed. Run `python3 ~/.claude/skills/original/export_pdf.py ~/.claude/skills/original/runs/<file>.md` (needs Chrome), send the PDF with SendUserFile, and give the path in one line.

<!-- end -->
## Limits

In testing, a plain model told to ask first did about as well, and in the one real blind test the user picked the plain version. What this adds is making sure the questions get asked, showing the default, and the objection and test. If the result is close to the default, say so.
