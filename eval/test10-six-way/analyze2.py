import json, re, math, itertools, statistics as st
from pathlib import Path
from collections import defaultdict, Counter
X = Path(__file__).parent; S = X / "score2"
import sys; sys.path.insert(0, str(X))
from score2 import CONTESTANTS, LABEL, MARKERS, CLICHES
items = {str(i["id"]): i for i in json.loads((S / "items.json").read_text())}
M = ["use_as_is", "fit", "originality", "specificity", "tone", "writing", "invented", "unsupported_stats"]
judged = {}
for j in ["claude", "gemini"]:
    d = {}
    for n in range(1, 5): d.update({re.sub(r"\D", "", k): v for k, v in json.loads((S / f"{j}_abs{n}.json").read_text()).items()})
    assert len(d) == 48, (j, len(d)); judged[j] = d
STOP = set("the a an and or of to in is it that for on with as are be this we you i your our at by not but they have was from can will more if what so do just about it's don't".split())
def vec(t):
    w = [x for x in re.findall(r"[a-z']+", t.lower()) if x not in STOP and len(x) > 2]
    return Counter(w)
def cos(a, b):
    num = sum(a[k] * b[k] for k in a if k in b); return num / (math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values())))
res = {}
for c in CONTESTANTS:
    its = [i for i in items.values() if i["c"] == c]
    r = {}
    for m in M:
        vals = [judged[j][str(i["id"])][m] for j in judged for i in its]
        r[m] = round(st.mean(vals), 2)
        r[m + "_by_judge"] = {j: round(st.mean(judged[j][str(i["id"])][m] for i in its), 2) for j in judged}
    with_markers = [i for i in its if MARKERS[i["who"]]]
    r["own_material"] = f"{sum(any(k in i['piece'] for k in MARKERS[i['who']]) for i in with_markers)}/{len(with_markers)}"
    r["cliches"] = round(st.mean(sum(i["piece"].lower().count(k.lower()) for k in CLICHES) for i in its), 2)
    r["placeholders"] = sum(len(re.findall(r"\[[^\]]{2,40}\]", i["piece"])) for i in its)
    blog = [len(i["piece"].split()) for i in its if i["task"] == "blog"]
    r["blog_words"] = round(st.mean(blog)); r["blog_len_err"] = round(st.mean(abs(w - 400) / 400 for w in blog), 2)
    r["talk_words"] = round(st.mean(len(i["piece"].split()) for i in its if i["task"] == "talk"))
    sims = []
    for t in ["talk", "blog"]:
        vs = [vec(i["piece"]) for i in its if i["task"] == t]
        sims += [cos(a, b) for a, b in itertools.combinations(vs, 2)]
    r["lexical_similarity_across_users"] = round(st.mean(sims), 2)
    res[c] = r
# questions asked (arms that ask)
def nq(p):
    t = p.read_text(); return len(re.findall(r"^\s*(?:\*\*)?\d+[.)]", t, re.M)) or t.count("?")
qa = {"original": [*(X / "claude/skill").glob("*/questions.md"), *(X / "blog/claude/skill").glob("*/questions.md")],
      "gemini_asks": [*(X / "gemini/asks").glob("*/questions.md"), *(X / "blog/gemini/asks").glob("*/questions.md")],
      "chatgpt_asks": [*(X / "chatgpt/talk/asks").glob("*/questions.md"), *(X / "chatgpt/blog/asks").glob("*/questions.md")]}
for c, fs in qa.items(): res[c]["questions_asked"] = round(st.mean(nq(f) for f in fs), 1)
# judge agreement
a = [judged["claude"][k]["use_as_is"] for k in items]; b = [judged["gemini"][k]["use_as_is"] for k in items]
agree = round(st.correlation(a, b), 2)
# head-to-head: earlier + new
def h2h(cases_file, files):
    cases = {str(c["id"]): c for c in json.loads(Path(cases_file).read_text())}
    out = {}
    for j, fl in files.items():
        v = {}
        for f in fl: v.update({re.sub(r"\D", "", k): x for k, x in json.loads(Path(f).read_text()).items()})
        m = defaultdict(lambda: defaultdict(list))
        for cid, c in cases.items():
            pos = 1 if c["first"] == "original" else 2
            for q in ["prefer", "less_generic"]: m[c["opp"]][(c["task"], c["who"], q)].append(int(v[cid][q]) == pos)
        for opp, d in m.items():
            for q in ["prefer", "less_generic"]:
                w = [sum(x) for k, x in d.items() if k[2] == q]
                out.setdefault(opp, {}).setdefault(j, {})[q] = [w.count(2), w.count(1), w.count(0)]
    return out
H = X / "h2h"
old = h2h(H / "cases.json", {j: [H / f"{j}_{n}.json" for n in range(1, 5)] for j in ["claude", "gemini"]})
new = h2h(S / "h2h_cases.json", {j: [S / f"{j}_hh{n}.json" for n in range(1, 4)] for j in ["claude", "gemini"]})
hh = {**old, **new}
out = {"per_contestant": res, "use_as_is_judge_corr": agree, "head_to_head": hh}
(S / "results.json").write_text(json.dumps(out, indent=1))
cols = ["use_as_is", "fit", "originality", "specificity", "tone", "writing", "invented", "unsupported_stats", "own_material", "cliches", "placeholders", "blog_words", "talk_words", "lexical_similarity_across_users", "questions_asked"]
print("contestant".ljust(22) + " ".join(c[:8].rjust(8) for c in cols))
for c in CONTESTANTS:
    print(LABEL[c][:22].ljust(22) + " ".join(str(res[c].get(k, "-"))[:8].rjust(8) for k in cols))
print("judge corr on use_as_is:", agree)
for opp, d in hh.items(): print("vs", opp.ljust(14), {j: d[j] for j in d})
