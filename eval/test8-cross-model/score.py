import json, itertools, statistics as st
from pathlib import Path
J = Path(__file__).parent / "judging"
items = json.loads((J / "items.json").read_text())
cases = json.loads((J / "fit_cases.json").read_text())
by_sim = {i["sim_id"]: i for i in items}
MARKERS = {"priya": ["60%", "11 hours", "~11", "11 hrs", "NOT NULL", "three weeks"], "marcus": ["38", "61"], "raj": ["9,000", "9000", "3 hours", "three hours"], "jo": []}
rows = []
for judge in ["claude", "gemini"]:
    ex = json.loads((J / f"{judge}_extract.json").read_text())
    sim = json.loads((J / f"{judge}_similarity.json").read_text())["pairs"]
    fit = json.loads((J / f"{judge}_fit.json").read_text())
    S = {}
    for p in sim:
        a, b = str(p["a"]), str(p["b"])
        S[frozenset((a, b))] = p["score"]
    for model in ["claude", "gemini"]:
        for arm in ["plain", "asks", "skill"]:
            grp = [i for i in items if i["model"] == model and i["arm"] == arm]
            plain = [i for i in items if i["model"] == model and i["arm"] == "plain"]
            q = st.mean(ex[i["qid"]]["quality"] for i in grp)
            spread = st.mean(S[frozenset((x["sim_id"], y["sim_id"]))] for x, y in itertools.combinations(grp, 2))
            dist = None if arm == "plain" else st.mean(S[frozenset((x["sim_id"], y["sim_id"]))] for x in grp for y in plain)
            fits = [fit[str(k)] == c["truth"] for k, c in enumerate(cases, 1) if next(i for i in items if i["qid"] == c["qid"]) in grp]
            f = None if arm == "plain" else sum(fits) / len(fits)
            rows.append(dict(judge=judge, model=model, arm=arm, quality=round(q, 2), spread=round(spread, 2), distance=None if dist is None else round(dist, 2), fit=f))
used = {}
for i in items:
    if i["arm"] == "plain" or not MARKERS[i["who"]]:
        continue
    hit = any(m in i["piece"] for m in MARKERS[i["who"]])
    used.setdefault((i["model"], i["arm"]), []).append((i["who"], hit))
# judge agreement on quality
qa = json.loads((J / "claude_extract.json").read_text()); qb = json.loads((J / "gemini_extract.json").read_text())
pairs = [(qa[k]["quality"], qb[k]["quality"]) for k in qa]
r = st.correlation([a for a, _ in pairs], [b for _, b in pairs])
fa = json.loads((J / "claude_fit.json").read_text()); fb = json.loads((J / "gemini_fit.json").read_text())
agree_fit = sum(fa[k] == fb[k] for k in fa) / len(fa)
out = {"rows": rows, "own_numbers_used": {f"{m}/{a}": v for (m, a), v in used.items()}, "quality_corr_between_judges": round(r, 2), "fit_agreement": agree_fit,
       "mean_quality_by_judge": {j: round(st.mean(v["quality"] for v in json.loads((J / f'{j}_extract.json').read_text()).values()), 2) for j in ["claude", "gemini"]}}
(J / "results.json").write_text(json.dumps(out, indent=1))
print(f"{'judge':7} {'model':7} {'arm':6} qual  spread dist  fit")
for x in rows:
    print(f"{x['judge']:7} {x['model']:7} {x['arm']:6} {x['quality']:<5} {x['spread']:<6} {str(x['distance']):<5} {x['fit']}")
print("own numbers used:", out["own_numbers_used"])
print("quality corr:", out["quality_corr_between_judges"], "fit agreement:", agree_fit, "mean q:", out["mean_quality_by_judge"])
