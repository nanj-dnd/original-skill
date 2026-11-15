#!/usr/bin/env python3
"""Sample the real default for /original: plain answers to the bare task, in parallel.

    python3 sample_default.py "<the task, as the user pasted it>" [n]
    python3 sample_default.py - [n] <<'EOF'      (task on stdin; safe for quotes and $)

Runs `claude -p` n times (default 3) with no skills, no tools, no project settings and a
neutral system prompt, so each answer is what a pasted prompt gets. Writes them to one
Markdown file in the temp folder and prints its path. Prints "unavailable: <reason>" and
exits 0 if the CLI is missing or every sample fails, so the skill can carry on without it.
"""
import json
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

CMD = ["claude", "-p", "--setting-sources", "", "--strict-mcp-config", "--disable-slash-commands",
       "--exclude-dynamic-system-prompt-sections", "--system-prompt", "You are a helpful AI assistant.",
       "--tools", "", "--output-format", "json"]


def one(task: str) -> str:
    r = subprocess.run(CMD + [task], capture_output=True, text=True, timeout=300,
                       cwd=tempfile.gettempdir())
    out = r.stdout
    d = json.loads(out[out.index("{"):])
    if d.get("is_error"):
        raise RuntimeError(str(d.get("result"))[:200])
    return d["result"].strip()


def main() -> None:
    if len(sys.argv) < 2 or not sys.argv[1].strip():
        sys.exit("usage: sample_default.py \"<task>\" [n]")
    task = sys.stdin.read().strip() if sys.argv[1] == "-" else sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    if not task:
        sys.exit("empty task")
    if not shutil.which("claude"):
        print("unavailable: claude CLI not found")
        return
    answers, errors = [], []
    with ThreadPoolExecutor(n) as ex:
        for f in [ex.submit(one, task) for _ in range(n)]:
            try:
                answers.append(f.result())
            except Exception as e:  # one failed sample shouldn't sink the rest
                errors.append(str(e)[:200])
    if not answers:
        print("unavailable: " + "; ".join(errors))
        return
    path = Path(tempfile.gettempdir()) / f"original-default-{time.strftime('%Y%m%d-%H%M%S')}.md"
    body = [f"# Plain answers to the task ({len(answers)} of {n})", "", f"Task: {task}", ""]
    for i, a in enumerate(answers, 1):
        body += [f"## Sample {i}", "", a, ""]
    path.write_text("\n".join(body), encoding="utf-8")
    print(path)


if __name__ == "__main__":
    main()
