# Eval harness for the `original` skill

Measures whether the skill moves outputs off the default answer, and whether that comes from its questions or its generation step. Results of the first run: `pilot-results.md`.

## Layout
- `tasks.md`: the two open tasks and their expected defaults
- `personas/`: hand-written users with specific views (two mostly agree with the default)
- `prompts/`: run prompts per arm, the persona prompt, and the three judge prompts
- `scripts/prep_judging.py`: blinds outputs (random ids, true-vs-decoy persona pairs)
- `scripts/score.py`: same-idea spread, distinct ideas, distance from plain, fit, quality
- `scripts/embed_score.py`: embedding spread and distance (needs sentence-transformers and huggingface.co access)

## Run order
1. For each task × persona, run the arms `plain`, `quick`, `full` (full stops at questions; a persona agent answers; stops again at the shortlist; persona picks).
2. Build `plain_ctx/outputs/context.md` from each full run's questions (minus "What everyone gets") plus the answers, then run `plain_ctx`.
3. `python3 -I scripts/prep_judging.py <iteration_dir> <key_outside_workspace.json>`
4. Run the extract and fit judges per task, then the similarity judge on `extract.json`.
5. `python3 -I scripts/score.py <iteration_dir> <key.json>` and `<venv>/bin/python -I scripts/embed_score.py <iteration_dir>`

## Paths

The prompts and scripts were run in a cloud session where the skill lived at `/home/user/original/SKILL.md`, this folder at `/home/user/original-eval/`, and runs at `/home/user/original-workspace/`. Here those are `src/` (built with `build.py`), `eval/` and `eval/runs/`; adjust the paths in `prompts/` before rerunning. The judges' answer keys were kept outside the workspace and are not included.

## Rounds

- `runs/iteration-1/`: pilot of v1 (arms plain, plain_ctx, quick, full). Write-up: `pilot-results.md`, side by side: `pilot-viewer.html`.
- `runs/iteration-2/`: v2 check (plain, full, v2; plus vague personas Jo and Max). Write-up: `v2-results.md`.
- `runs/iteration-3/`: Test 3 (plain, plain_ctx, plain_asks, v2). Write-up: `test3-results.md`.
- `runs/skill-v1/`: the v1 skill as tested.
