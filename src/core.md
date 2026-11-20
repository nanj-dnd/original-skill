# Original: get off the default answer

Two people who paste the same task into a model get the same ideas. This shows the user that default, asks a few questions before writing, and builds from their answers. Asking before writing does most of the work; the reason for each rule is in `references/why.md`.

<!-- if code -->
Files: `runs/` (a record per run, for export), `export_pdf.py`, `sample_default.py`, `stats.py`, `references/`. This file is built from `~/Downloads/original-v2/src/core.md` by `build.py`; change the source and rebuild, since edits here are overwritten on install.

If the task is `export` or `stats`, skip to "Export".

<!-- end -->
## 1. Default

If the task has one right answer (a fact, a calculation), say so in one line and just answer it.

Otherwise write, under eight lines, headed "What everyone gets": the main claim a pasted prompt would get, then the 3 to 5 choices it made (angle, examples, structure, reader, tone).
<!-- if code -->

At the same time, sample the real default: run `python3 ~/.claude/skills/original/sample_default.py -` with the task as they pasted it on stdin (a quoted heredoc), using Bash in the background (about 10 to 60 seconds) and carry on. It prints a file of 3 plain answers, or "unavailable", in which case go on without it.
<!-- end -->

If it is coursework, work on ideas and angle only, and follow any rule the user has set for that course.

## 2. Ask

3 or 4 questions, all at once, no second round.
<!-- if code -->
Use one AskUserQuestion call; each question has 2 to 4 options, and the free-text option covers the rest.
<!-- end -->
<!-- if claude-ai -->
Each has 2 to 4 options. Use a clickable question tool if there is one; otherwise number them with lettered options so the user can reply like `1b 2a 3c`.
<!-- end -->

- Draft one question per default choice and keep the ones whose answers would change the piece most. Each states the default's choice inside it, so it reads on its own.
- One asks for their real material: a case, and a number or measure where the task could use one. If the piece is written as them, ask for one real moment instead: something that happened, a number, or a line someone said.
- One asks how it should sound for this reader (plain or formal, whose name is on it), unless that is already settled.
- Don't ask what the conversation or a fair guess already settles. Where the conversation or their files hold material (a draft, notes, figures), put it in the options so one click carries it.
- If the piece can't go out without facts only they know (names, who signs it, the exact ask, a word, time or format limit, things to avoid), make sure a question collects them; it can share the material question, since the free-text option takes both.
- If they say skip or "just write it", don't ask again: pick the one non-default choice the task itself best supports, write without personal details, and say in the distance line that it stays close to the default.

## 3. Angle

Build from whatever they gave you, even picked options. If they agree with the default or want the usual thing done well (they pick the default's options or give little), keep its claim and shape and make it specific and well made; don't steer it away. Build from their specifics, not a contrarian stance they don't hold. If their answers are thin or their view is mild, keep the stance as measured as theirs: make the piece specific and well made, not more opinionated than they are. Before the piece, in four lines:

- **Angle**: the claim in one sentence; not the default's unless they chose it.
- **Built from**: which answers.
- **Strongest objection**, stated fairly, and a **test** they can run before using it.
- **Other direction**: one alternative, in a line.

## 4. Write

<!-- if code -->
- If the default samples came back, read them first and note what at least two of them share: the examples, the structure, the opening move, stock phrases. Replace those with the user's own material and a different shape. The samples never move the stance: if their claim is the user's view too, keep it and make it theirs through specifics.
<!-- end -->
- Verify the facts. Check any statistic or study with a search if you can; otherwise leave it out unless the argument needs it.
- Limits they gave (length, time, the exact ask, words to avoid) beat everything else, distance from the default included. For ideas and plans, pick the most original option their time, team and skills can actually deliver.
- Make it ready to use: no brackets, placeholders or "[unchecked]" marks inside it. Keep to the length and format they asked for (within about a tenth of a word count, without printing the count) and the platform's conventions.
- Their real material is the centre of the piece, not an example dropped into the default's frame: open with it or build the argument on it.
- Every fact about the user, their life, their work or their past must come from their answers or the conversation. In first-person pieces that includes small colour: past attempts, other habits, how they felt, what someone said. If they didn't give it, write around the gap instead of filling it with a plausible detail.
- First-person pieces (written as the user): their memories, experiences, feelings, opinions, timelines, counts and quotes may only be ones they gave you. Where the piece wants colour, write it about people in general ("most of us", "it's easy to") or to the reader ("you"), not as the user's own memory.
- Use the tone they chose. Hand it to a voice skill (such as `anshul-voice`) only if they asked for their own voice.
- Before showing it, reread it once as a reader who doubts the angle: fix where it goes thin or generic, and cut any personal detail you can't trace to an answer. In a first-person piece, go through every I, my and me sentence, including what they do, use or believe, and keep it only if their answers support it; rewrite the rest in general terms or delete it.
<!-- if code -->
- Then have a fresh reader check it. Launch one subagent (Agent tool, general-purpose) and give it only the piece, their answers in their words, and anything else they told you or shared in this conversation, with this job: list every statement the piece makes about the user (their life, work, past, habits, feelings, numbers, quotes, what they do or believe) that the material does not support, quoting each phrase; general claims about people and advice don't count. Fix or cut each phrase it lists, unless you can name the answer that supports it. If you can't launch a subagent, do the same check yourself as a separate pass: write each claim about the user next to the answer it came from, and cut the ones with none.
<!-- end -->
<!-- if claude-ai -->
- Then check it as a separate pass: list each statement the piece makes about the user next to the answer it came from, and cut or rewrite the ones with none.
<!-- end -->

After it, only if something applies, **Before you use it**: figures you couldn't check, details to confirm, a real detail worth adding. Then one line of **Distance from the default**: what changed and which answer caused it, or that little did.
<!-- if code -->
If the samples came back, the distance line also names anything the piece still shares with them.
<!-- end -->

If they ask for changes afterwards, the same rules hold (no invented details, their tone, their length), and the record is updated.
<!-- if code -->

Then ask one AskUserQuestion, "Would you use this?", with options As is, With edits, Not using. On every fifth run (count the files in `runs/`), if the samples came back, add a second question to the same call: "Which would you rather use?", with options A and B, each showing one full piece in its preview (yours and the first sample, in random order), plus "Skip". Don't say which is which until they answer.
<!-- end -->

## 5. Record

<!-- if code -->
Save the run to `runs/<YYYY-MM-DD>-<slug>.md` and tell the user `/original export` makes a PDF of it.
<!-- end -->
<!-- if claude-ai -->
Offer to export the run as a Markdown file (PDF if they ask).
<!-- end -->
The record holds: the task, What everyone gets, each question with their answer in their words, the angle block, the piece, the note and the distance line.
<!-- if code -->
End the record with `Would use: as is | with edits | not using` and, if a blind pick was asked, `Blind pick: original | plain | skipped`.
<!-- end -->

<!-- if code -->
## Export

`/original export` makes a PDF in `~/Downloads/originals/` from this conversation's run, or the newest file in `runs/`, or one named by topic or date (ask with AskUserQuestion if several match). Update the record first if the piece changed. Run `python3 ~/.claude/skills/original/export_pdf.py ~/.claude/skills/original/runs/<file>.md` (needs Chrome), send the PDF with SendUserFile, and give the path in one line.

`/original stats` runs `python3 ~/.claude/skills/original/stats.py` and reports what it prints in two or three lines: how often runs were used as is, and how blind picks went.

<!-- end -->
## Limits

In testing, a plain model told to ask first did about as well, and in the one real blind test the user picked the plain version. What this adds is making sure the questions get asked, showing the default, and the objection and test. If the result is close to the default, say so.
