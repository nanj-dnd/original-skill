import json, re, statistics as st
from pathlib import Path
from collections import defaultdict
X = Path(__file__).parent; S = X / "score2"; H = X / "h2h"; G = X / "gpt"
items = {str(i["id"]): i for i in json.loads((S / "items.json").read_text())}
M = ["use_as_is", "fit", "originality", "specificity", "tone", "writing", "invented", "unsupported_stats"]
def load(files):
    d = {}
    for f in files: d.update({re.sub(r"\D", "", k): v for k, v in json.loads(Path(f).read_text()).items()})
    return d
J = {"claude": load([S / f"claude_abs{n}.json" for n in range(1, 5)]), "gemini": load([S / f"gemini_abs{n}.json" for n in range(1, 5)]), "gpt": load([G / f"abs{n}.json" for n in range(1, 5)])}
for j, d in J.items(): assert len(d) == 48, (j, len(d))
C = ["original", "chatgpt_asks", "gemini_asks", "claude_plain", "gemini_plain", "chatgpt_plain"]
per = {}
for c in C:
    ids = [k for k, i in items.items() if i["c"] == c]
    per[c] = {m: {j: round(st.mean(J[j][k][m] for k in ids), 2) for j in J} for m in M}
    for m in M: per[c][m]["mean"] = round(st.mean(per[c][m][j] for j in J), 2)
corr = {f"{a}-{b}": round(st.correlation([J[a][k]["use_as_is"] for k in items], [J[b][k]["use_as_is"] for k in items]), 2) for a, b in [("claude", "gemini"), ("claude", "gpt"), ("gemini", "gpt")]}
def h2h(cases_file, judge_files):
    cases = {str(c["id"]): c for c in json.loads(Path(cases_file).read_text())}
    out = {}
    for j, fl in judge_files.items():
        v = load(fl)
        m = defaultdict(lambda: defaultdict(list))
        for cid, c in cases.items():
            pos = 1 if c["first"] == "original" else 2
            for q in ["prefer", "less_generic"]: m[c["opp"]][(c["task"], c["who"], q)].append(int(v[cid][q]) == pos)
        for opp, d in m.items():
            for q in ["prefer", "less_generic"]:
                w = [sum(x) for k, x in d.items() if k[2] == q]
                out.setdefault(opp, {}).setdefault(j, {})[q] = [w.count(2), w.count(1), w.count(0)]
    return out
old = h2h(H / "cases.json", {"claude": [H / f"claude_{n}.json" for n in range(1, 5)], "gemini": [H / f"gemini_{n}.json" for n in range(1, 5)], "gpt": [G / f"h2h{n}.json" for n in range(1, 5)]})
new = h2h(S / "h2h_cases.json", {"claude": [S / f"claude_hh{n}.json" for n in range(1, 4)], "gemini": [S / f"gemini_hh{n}.json" for n in range(1, 4)], "gpt": [G / f"hh{n}.json" for n in range(1, 4)]})
hh = {**old, **new}
tot = {j: [sum(hh[o][j]["prefer"][i] for o in hh) for i in range(3)] for j in ["claude", "gemini", "gpt"]}
gtot = {j: [sum(hh[o][j]["less_generic"][i] for o in hh) for i in range(3)] for j in ["claude", "gemini", "gpt"]}
out = {"per_contestant": per, "use_as_is_corr": corr, "head_to_head": hh, "prefer_totals": tot, "less_generic_totals": gtot}
(G / "results3.json").write_text(json.dumps(out, indent=1))
for m in M:
    print(m.ljust(18), "  ".join(f"{c[:12]}:{per[c][m]['claude']}/{per[c][m]['gemini']}/{per[c][m]['gpt']}={per[c][m]['mean']}" for c in C[:3]))
print("rest use_as_is mean:", {c: per[c]["use_as_is"]["mean"] for c in C[3:]})
print("corr:", corr)
for o, d in hh.items(): print("vs", o.ljust(14), {j: d[j]["prefer"] for j in d}, "| generic", {j: d[j]["less_generic"] for j in d})
print("prefer totals W/T/L:", tot, " less generic:", gtot)
