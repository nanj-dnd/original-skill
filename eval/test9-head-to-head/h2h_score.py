import json
from pathlib import Path
from collections import defaultdict
H = Path(__file__).parent / "h2h"
cases = {str(c["id"]): c for c in json.loads((H / "cases.json").read_text())}
out = {}
for judge in ["claude", "gemini"]:
    v = {}
    for n in range(1, 5): v.update(json.loads((H / f"{judge}_{n}.json").read_text()))
    assert len(v) == 48, (judge, len(v))
    # per match (task, who, opp): did /original win in each order?
    m = defaultdict(lambda: {"prefer": [], "less_generic": []})
    for cid, c in cases.items():
        orig_pos = 1 if c["first"] == "original" else 2
        for q in ["prefer", "less_generic"]:
            m[(c["task"], c["who"], c["opp"])][q].append(int(v[cid][q]) == orig_pos)
    res = defaultdict(lambda: {"prefer": [0, 0, 0], "less_generic": [0, 0, 0]})  # win, tie(split), loss
    pos_bias = sum(int(x["prefer"]) == 1 for x in v.values()) / 48
    for (task, who, opp), r in m.items():
        for q in ["prefer", "less_generic"]:
            w = sum(r[q]); idx = 0 if w == 2 else 1 if w == 1 else 2
            res[opp][q][idx] += 1; res[f"{opp}|{task}"][q][idx] += 1
    out[judge] = {"by_opponent": {k: v2 for k, v2 in res.items()}, "first_position_rate": round(pos_bias, 2)}
for judge in out:
    print(f"== {judge} judge (picked piece 1 in {out[judge]['first_position_rate']:.0%} of cases)")
    for k, r in sorted(out[judge]["by_opponent"].items()):
        p, g = r["prefer"], r["less_generic"]
        print(f"  /original vs {k:22} prefer W/T/L {p}   less generic W/T/L {g}")
(H / "results.json").write_text(json.dumps(out, indent=1))
