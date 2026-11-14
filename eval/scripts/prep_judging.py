"""Blind deliverables for judging. Usage: python3 -I prep_judging.py <iteration_dir> <key_path> [talk,resolutions]
The key is saved as {task: {id: {...}}}; keep it outside the workspace so judges can't read it."""
import os, json, random, sys, pathlib
it = pathlib.Path(sys.argv[1]); key_path = pathlib.Path(sys.argv[2])
cards = pathlib.Path(__file__).resolve().parent.parent / "personas"
random.seed(7)
ARMS = os.environ.get("ARMS", "plain,plain_ctx,quick,full").split(",")

TASKS = sys.argv[3].split(",") if len(sys.argv) > 3 else ["talk", "resolutions"]
key = json.loads(key_path.read_text()) if key_path.exists() else {}
for task in TASKS:
    cases = sorted(p.name for p in it.iterdir() if p.is_dir() and p.name.startswith(task + "-") and all((p / a / "outputs" / "deliverable.md").exists() for a in ARMS))
    items = [(c, a) for c in cases for a in ARMS]
    ids = random.sample(sorted(set(range(100, 1000)) - {int(k) for t in key.values() for k in t}), len(items))  # never reuse an id from an earlier task
    key[task] = {}; jd = it / "_judge" / task; (jd / "items").mkdir(parents=True, exist_ok=True); (jd / "fit").mkdir(exist_ok=True)
    for (c, a), i in zip(items, ids):
        src = it / c / a / "outputs" / "deliverable.md"
        (jd / "items" / f"{i}.md").write_text(src.read_text())
        decoy = random.choice([x for x in cases if x != c])
        pair = [c, decoy]; random.shuffle(pair)
        fit = f"# Output {i}\n\n{src.read_text()}\n\n# Person A\n\n{(cards / (pair[0] + '.md')).read_text()}\n\n# Person B\n\n{(cards / (pair[1] + '.md')).read_text()}\n"
        (jd / "fit" / f"{i}.md").write_text(fit)
        key[task][str(i)] = {"task": task, "case": c, "arm": a, "fit_true": "A" if pair[0] == c else "B"}
key_path.write_text(json.dumps(key, indent=2))
print("ok", {t: len(v) for t, v in key.items()})
