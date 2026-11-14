#!/usr/bin/env python3
"""Cross-model benchmark, Claude side. Usage: bench.py <model-alias> <outdir>"""
import json, subprocess, sys, os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

HERE = Path(__file__).parent
EVAL = Path.home() / "Downloads/original-v2/eval"
TASK = ("I've got 5 minutes at our company all-hands next Friday to talk about whether engineers "
        "should be using AI coding assistants for everything. Can you write me an outline and the opening paragraph?")
SKILL = (HERE / "skill_body.md").read_text()
PERSONA_TMPL = (EVAL / "prompts/persona.md").read_text()
PERSONAS = ["priya", "marcus", "jo", "raj"]
ASKS = ("Before you write anything, ask me whatever clarifying questions would help you do this well. "
        "Just ask the questions now; I'll answer, then you write.\n\n" + TASK)
SKILLP = "Follow these instructions for my task.\n\n--- INSTRUCTIONS ---\n" + SKILL + "\n--- END INSTRUCTIONS ---\n\nMy task: " + TASK

def claude(prompt, model, resume=None):
    cmd = ["claude", "-p", "--model", model, "--setting-sources", "", "--strict-mcp-config",
           "--disable-slash-commands", "--exclude-dynamic-system-prompt-sections",
           "--system-prompt", "You are a helpful AI assistant.", "--tools", "", "--output-format", "json"]
    if resume:
        cmd += ["--resume", resume]
    r = subprocess.run(cmd + [prompt], capture_output=True, text=True, cwd=HERE, timeout=900)
    t = r.stdout
    d = json.loads(t[t.index("{"):])
    if d.get("is_error"):
        raise RuntimeError(d.get("result"))
    return d["result"], d["session_id"], list((d.get("modelUsage") or {}).keys())

def persona(name, msg):
    card = (EVAL / f"personas/talk-{name}.md").read_text()
    p = PERSONA_TMPL.replace("{CARD}", card).replace("{MSG}", msg)
    return claude(p, "opus")[0]

def two_turn(model, out, arm, name, first):
    d = out / arm / name
    d.mkdir(parents=True, exist_ok=True)
    q, sid, used = claude(first, model)
    (d / "questions.md").write_text(q)
    a = persona(name, q)
    (d / "answers.md").write_text(a)
    piece, _, used2 = claude(a, model, resume=sid)
    (d / "deliverable.md").write_text(piece)
    (d / "model.txt").write_text(", ".join(sorted(set(used + used2))))
    return f"{arm}/{name} done"

def plain(model, out, i):
    d = out / "plain" / f"run{i}"
    d.mkdir(parents=True, exist_ok=True)
    piece, _, used = claude(TASK, model)
    (d / "deliverable.md").write_text(piece)
    (d / "model.txt").write_text(", ".join(used))
    return f"plain/run{i} done"

if __name__ == "__main__":
    model, out = sys.argv[1], Path(sys.argv[2])
    jobs = []
    with ThreadPoolExecutor(max_workers=6) as ex:
        for i in range(1, 5):
            jobs.append(ex.submit(plain, model, out, i))
        for n in PERSONAS:
            jobs.append(ex.submit(two_turn, model, out, "asks", n, ASKS))
            jobs.append(ex.submit(two_turn, model, out, "skill", n, SKILLP))
        for j in jobs:
            try:
                print(j.result(), flush=True)
            except Exception as e:
                print("FAILED:", e, flush=True)
