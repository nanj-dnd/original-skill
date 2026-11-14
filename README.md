# /original v2: source

One source, two builds: Claude Code (installed skill) and claude.ai (upload zip).

## Layout

- `src/core.md`: the skill. Blocks wrapped in `<!-- if code -->` … `<!-- end -->` appear
  only in the named targets (`code`, `claude-ai`; several allowed, no nesting).
- `src/references/`: `why.md` (the reason behind each rule), `research.md`, `pilot.md`.
  Shipped with every target.
- `src/export_pdf.py`: PDF exporter, Claude Code only.
- `build.py`: descriptions per target live at the top of this file.
- `dist/`: build output. Regenerated each time; don't edit.
- `v2-as-received/`: v2 exactly as it came from the claude.ai session, for reference.
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
