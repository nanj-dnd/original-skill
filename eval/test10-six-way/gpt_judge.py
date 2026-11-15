import json, re, subprocess, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
X = Path(__file__).parent; G = X / "gpt"
JOBS = {f"abs{n}": X / "score2" / f"abs{n}.txt" for n in range(1, 5)}
JOBS.update({f"hh{n}": X / "score2" / f"hh{n}.txt" for n in range(1, 4)})
JOBS.update({f"h2h{n}": X / "h2h" / f"prompt{n}.txt" for n in range(1, 5)})
def run(name):
    out = G / f"{name}.txt"
    if (G / f"{name}.json").exists(): return name, "cached"
    for attempt in range(2):
        r = subprocess.run(["codex", "exec", "--skip-git-repo-check", "-s", "read-only", "-c", "model_reasoning_effort=\"low\"", "-o", str(out), "-"],
                           input=JOBS[name].read_text() + "\n\nDo not run any commands or read any files; everything you need is above. Reply with the JSON only.",
                           capture_output=True, text=True, cwd=G, timeout=1800)
        try:
            d = json.loads(re.search(r"\{.*\}", out.read_text(), re.S).group(0))
            (G / f"{name}.json").write_text(json.dumps(d, indent=1)); return name, len(d)
        except Exception as e:
            err = (r.stderr or "")[-300:]
    return name, f"FAILED {err}"
for name in JOBS:
    res = run(name); print(res, flush=True)
    if "usage limit" in str(res[1]): print("stopping: usage limit", flush=True); break
