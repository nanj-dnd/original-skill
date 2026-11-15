"""Re-run judging: python3 rerun_judge.py build | claude | score"""
import json, random, re, sys, statistics as st
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).parent))
from bench import claude
from h2h import TASKS, STRIP
from score2 import p_abs, p_h2h
X = Path(__file__).parent; R = X / "rerun"; R.mkdir(exist_ok=True)
def build():
    old = [i for i in json.loads((X / "score2/items.json").read_text()) if i["c"] in ("original", "chatgpt_asks")]
    todo = [(t, w, R / t / "skill" / w / "deliverable.md") for t, (_, _, people, _) in TASKS.items() for w in people]
    def strip(a):
        t, w, p = a
        return {"task": t, "who": w, "c": "original_v2", "piece": claude(STRIP.replace("{task}", TASKS[t][0]) + p.read_text(), "opus")[0].strip()}
    with ThreadPoolExecutor(8) as ex: new = list(ex.map(strip, todo))
    items = [{"task": i["task"], "who": i["who"], "c": i["c"], "piece": i["piece"]} for i in old] + new
    rnd = random.Random(1115); rnd.shuffle(items)
    for n, i in enumerate(items, 201): i["id"] = n
    (R / "items.json").write_text(json.dumps(items, indent=1))
    piece = {(i["task"], i["c"], i["who"]): i["piece"] for i in items}
    cases = []
    for t, (_, _, people, _) in TASKS.items():
        for w in people:
            for order in (0, 1):
                a, b = ("original_v2", "chatgpt_asks") if order == 0 else ("chatgpt_asks", "original_v2")
                cases.append({"task": t, "who": w, "opp": "chatgpt_asks", "first": a, "second": b, "p1": piece[(t, a, w)], "p2": piece[(t, b, w)]})
    rnd.shuffle(cases)
    for n, c in enumerate(cases, 301): c["id"] = n
    (R / "h2h_cases.json").write_text(json.dumps(cases, indent=1))
    (R / "abs1.txt").write_text(p_abs(items[:12])); (R / "abs2.txt").write_text(p_abs(items[12:]))
    (R / "hh1.txt").write_text(p_h2h(cases[:8])); (R / "hh2.txt").write_text(p_h2h(cases[8:]))
    print(len(items), "items", len(cases), "cases", [len((R / f).read_text()) for f in ["abs1.txt", "abs2.txt", "hh1.txt", "hh2.txt"]])
def run_claude():
    def one(n):
        t = claude((R / f"{n}.txt").read_text(), "opus")[0]
        d = json.loads(re.search(r"\{.*\}", t, re.S).group(0)); (R / f"claude_{n}.json").write_text(json.dumps(d, indent=1)); return n, len(d)
    with ThreadPoolExecutor(4) as ex:
        for r in ex.map(one, ["abs1", "abs2", "hh1", "hh2"]): print(r, flush=True)
def load(fs):
    d = {}
    for f in fs: d.update({re.sub(r"\D", "", k): v for k, v in json.loads(Path(f).read_text()).items()})
    return d
def score():
    items = {str(i["id"]): i for i in json.loads((R / "items.json").read_text())}
    cases = {str(c["id"]): c for c in json.loads((R / "h2h_cases.json").read_text())}
    judges = [j for j in ["claude", "gemini", "gpt"] if (R / f"{j}_abs2.json").exists()]
    M = ["use_as_is", "fit", "originality", "specificity", "tone", "writing", "invented", "unsupported_stats"]
    out = {"judges": judges, "scores": {}, "h2h": {}, "jo": {}}
    for c in ["original_v2", "original", "chatgpt_asks"]:
        ids = [k for k, i in items.items() if i["c"] == c]
        out["scores"][c] = {m: {j: round(st.mean(load([R / f"{j}_abs1.json", R / f"{j}_abs2.json"])[k][m] for k in ids), 2) for j in judges} for m in M}
        for m in M: out["scores"][c][m]["mean"] = round(st.mean(out["scores"][c][m][j] for j in judges), 2)
        jo = [k for k in ids if items[k]["who"] == "jo"]
        out["jo"][c] = {j: load([R / f"{j}_abs1.json", R / f"{j}_abs2.json"])[jo[0]]["use_as_is"] for j in judges}
    for j in judges:
        if not (R / f"{j}_hh2.json").exists(): continue
        v = load([R / f"{j}_hh1.json", R / f"{j}_hh2.json"]); m = defaultdict(list)
        for cid, c in cases.items():
            pos = 1 if c["first"] == "original_v2" else 2
            for q in ["prefer", "less_generic"]: m[(c["task"], c["who"], q)].append(int(v[cid][q]) == pos)
        for q in ["prefer", "less_generic"]:
            w = [sum(x) for k, x in m.items() if k[2] == q]; out["h2h"].setdefault(j, {})[q] = [w.count(2), w.count(1), w.count(0)]
    (R / "results.json").write_text(json.dumps(out, indent=1))
    for c, s in out["scores"].items(): print(c.ljust(13), {m: s[m]["mean"] for m in M}, "by judge use:", s["use_as_is"])
    print("Jo use_as_is:", out["jo"]); print("h2h new vs chatgpt_asks:", out["h2h"])
if __name__ == "__main__":
    {"build": build, "claude": run_claude, "score": score}[sys.argv[1]]()
