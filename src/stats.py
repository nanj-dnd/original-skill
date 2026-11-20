#!/usr/bin/env python3
"""Usage stats for /original from the run records in runs/.

    python3 stats.py [runs-dir]

Reads the `Would use:` and `Blind pick:` lines that each record ends with and prints
counts. Records written before tracking existed are counted as untracked.
"""
import re
import sys
from collections import Counter
from pathlib import Path

runs = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / "runs"
files = sorted(runs.glob("*.md")) if runs.is_dir() else []
use, pick, untracked = Counter(), Counter(), 0
for f in files:
    text = f.read_text(encoding="utf-8", errors="replace")
    u = re.findall(r"(?im)^\W*would use\W*:\W*(as is|with edits|not using)", text)
    p = re.findall(r"(?im)^\W*blind pick\W*:\W*(original|plain|skipped)", text)
    if u:
        use[u[-1].lower()] += 1
    else:
        untracked += 1
    if p:
        pick[p[-1].lower()] += 1

tracked = sum(use.values())
print(f"runs: {len(files)} ({tracked} tracked, {untracked} from before tracking or unanswered)")
if tracked:
    print("would use: " + ", ".join(f"{k} {use[k]} ({use[k] * 100 // tracked}%)" for k in ("as is", "with edits", "not using")))
decided = pick["original"] + pick["plain"]
if decided or pick["skipped"]:
    print(f"blind picks: original {pick['original']}, plain {pick['plain']}, skipped {pick['skipped']}"
          + (f" (original won {pick['original'] * 100 // decided}% of decided picks)" if decided else ""))
if not files:
    print("no runs yet")
