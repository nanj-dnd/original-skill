# Original: get off the default answer

Two people who paste the same task into a model get the same ideas. This shows the user that default, asks a few questions before writing, and builds from their answers. Asking before writing does most of the work; the reason for each rule is in `references/why.md`.

## 1. Default

If the task has one right answer (a fact, a calculation), say so in one line and just answer it.

Otherwise write, under eight lines, headed "What everyone gets": the main claim a pasted prompt would get, then the 3 to 5 choices it made (angle, examples, structure, reader, tone).

Three plain answers to the same task (the real default) will be given to you together with the user's answers.

If it is coursework, work on ideas and angle only, and follow any rule the user has set for that course.

## 2. Ask

3 or 4 questions, all at once, no second round.
Each has 2 to 4 options. Number them with lettered options so the user can reply like `1b 2a 3c`.

- Draft one question per default choice and keep the ones whose answers would change the piece most. Each states the default's choice inside it, so it reads on its own.
- One asks for their real material: a case, and a number or measure where the task could use one. If the piece is written as them, ask for one real moment instead: something that happened, a number, or a line someone said.
- One asks how it should sound for this reader (plain or formal, whose name is on it), unless that is already settled.
- Don't ask what the conversation or a fair guess already settles. Where the conversation or their files hold material (a draft, notes, figures), put it in the options so one click carries it.
- If they say skip or "just write it", don't ask again: pick the one non-default choice the task itself best supports, write without personal details, and say in the distance line that it stays close to the default.

## 3. Angle

Build from whatever they gave you, even picked options. If they agree with the default, build from their specifics, not a contrarian stance they don't hold. If their answers are thin or their view is mild, keep the stance as measured as theirs: make the piece specific and well made, not more opinionated than they are. Before the piece, in four lines:

- **Angle**: the claim in one sentence; not the default's unless they chose it.
- **Built from**: which answers.
- **Strongest objection**, stated fairly, and a **test** they can run before using it.
- **Other direction**: one alternative, in a line.

## 4. Write

- If the default samples came back, read them first and note what at least two of them share: the main claim, the examples, the structure, the opening move, stock phrases. Keep those out of the piece unless the user chose them.
- Verify the facts. Check any statistic or study with a search if you can; otherwise leave it out unless the argument needs it.
- Make it ready to use: no brackets, placeholders or "[unchecked]" marks inside it. Keep to the length and format they asked for (within about a tenth of a word count) and the platform's conventions.
- Their real material is the centre of the piece, not an example dropped into the default's frame: open with it or build the argument on it.
- Every fact about the user, their life, their work or their past must come from their answers or the conversation. In first-person pieces that includes small colour: past attempts, other habits, how they felt, what someone said. If they didn't give it, write around the gap instead of filling it with a plausible detail.
- First-person pieces (written as the user): their memories, experiences, feelings, opinions, timelines, counts and quotes may only be ones they gave you. Where the piece wants colour, write it about people in general ("most of us", "it's easy to") or to the reader ("you"), not as the user's own memory.
- Use the tone they chose. Hand it to a voice skill (such as `anshul-voice`) only if they asked for their own voice.
- Before showing it, reread it once as a reader who doubts the angle: fix where it goes thin or generic, and cut any personal detail you can't trace to an answer. In a first-person piece, go through every I, my and me sentence and keep it only if their answers support it; rewrite the rest in general terms or delete it.

After it, only if something applies, **Before you use it**: figures you couldn't check, details to confirm, a real detail worth adding. Then one line of **Distance from the default**: what changed and which answer caused it, or that little did.
If the samples came back, the distance line also names anything the piece still shares with them.

If they ask for changes afterwards, the same rules hold (no invented details, their tone, their length), and the record is updated.

## Limits

In testing, a plain model told to ask first did about as well, and in the one real blind test the user picked the plain version. What this adds is making sure the questions get asked, showing the default, and the objection and test. If the result is close to the default, say so.
