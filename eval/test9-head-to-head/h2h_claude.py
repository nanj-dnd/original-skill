import json, re, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).parent))
from bench import claude
H = Path(__file__).parent / "h2h"
def run(n):
    t = claude((H / f"prompt{n}.txt").read_text(), "opus")[0]
    d = json.loads(re.search(r"\{.*\}", t, re.S).group(0))
    (H / f"claude_{n}.json").write_text(json.dumps(d, indent=1)); return n, len(d)
with ThreadPoolExecutor(4) as ex:
    for r in ex.map(run, [1, 2, 3, 4]): print(r, flush=True)
