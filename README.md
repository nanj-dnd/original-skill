# /original

A skill for Claude that gets you off the default answer. Paste an open task (an essay
angle, a pitch, a post, a talk, a product idea) and it shows you what everyone would get,
asks you three or four questions, then writes from your answers: your case, your numbers,
your limits.

## What it does

1. **Default.** Shows the answer a pasted prompt gets. In Claude Code it also samples
   three real plain answers in the background.
2. **Ask.** Three or four clickable questions: your real material, the must-haves (names,
   the exact ask, limits), and how it should sound.
3. **Angle.** The claim, what it's built from, the strongest objection and a test.
4. **Write.** A ready-to-use piece. A separate reader then checks every claim about you
   against your answers and anything unsupported is cut.

## Results

Fifteen rounds of blind tests, judged by Claude and ChatGPT. The users were simulated,
so read these as direction, not proof. Write-ups are in `src/references/pilot.md`.

- Against plain Claude, ChatGPT and Gemini: won 71 of 80 judged matchups (Tests 8 to 10),
  and 12 of 12 against plain Claude on four new kinds of writing (Test 14).
- Against Claude told to ask questions first, the strongest rival: preferred 61% of the
  time by the Claude judge and 62% by the ChatGPT judge, and less generic in 89% and 79%
  of matchups (Test 15).
- Made-up details about the user: 0.5 per piece, against 1.17 for Claude asking first.
- Overlap with the generic answer: 1.6 out of 5, against 3.2.
- In the one real-user test so far, the user picked the plain version. The skill now asks
  about tone because of it.

## Install

Claude Code:

```bash
git clone https://github.com/nanj-dnd/original-skill && cd original-skill && python3 build.py --install
```

Then type `/original` followed by your task. claude.ai: run `python3 build.py` and upload
`dist/claude-ai/original-skill.zip` under Settings, Capabilities, Skills.

## Source

One source, two builds: Claude Code (installed skill) and claude.ai (upload zip).

## Layout

- `src/core.md`: the skill. Blocks wrapped in `<!-- if code -->` … `<!-- end -->` appear
  only in the named targets (`code`, `claude-ai`; several allowed, no nesting).
- `src/references/`: `why.md` (the reason behind each rule), `research.md`, `pilot.md`.
  Shipped with every target.
- `src/export_pdf.py`: PDF exporter, Claude Code only.
- `src/stats.py`: counts "would use" answers and blind picks from runs/ for `/original stats`, Claude Code only.
- `src/sample_default.py`: samples 3 plain answers to the task so the skill can see the real default, Claude Code only.
- `build.py`: descriptions per target live at the top of this file.
- `dist/`: build output. Regenerated each time; don't edit.
- `eval/`: the evaluation harness (tasks, personas, prompts, scripts), the three write-ups
  (`pilot-results.md`, `v2-results.md`, `test3-results.md`) and every run's outputs in `eval/runs/`.

## Build and install

```bash
python3 build.py
```

```bash
python3 build.py --install
```

`--install` replaces `~/.claude/skills/original/` with the Code build, keeping `runs/`.

The build stops with an error if the claude.ai description is over 200 characters,
a description would break the YAML header, or an `if` block is malformed.

## What goes where after a build

- claude.ai: upload `dist/claude-ai/original-skill.zip`.
