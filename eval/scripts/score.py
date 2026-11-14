"""Score the pilot. Usage: python3 -I score.py <iteration_dir> <key_path>
Reads _judge/<task>/{extract.json,similarity.json,fit.json}; writes pilot_scores.md/json."""
import os, json, sys, pathlib, itertools, statistics as st
it = pathlib.Path(sys.argv[1]); KEYS = json.loads(pathlib.Path(sys.argv[2]).read_text())
ARMS = os.environ.get("ARMS", "plain,plain_ctx,quick,full").split(",")
out = {}; lines = ["# Pilot scores", "",
  "Similarity is 0 (different idea) to 3 (same idea and choices). Lower within-arm = more spread between users.", ""]
for task in ["talk", "resolutions"]:
    jd = it / "_judge" / task; key = KEYS[task]
    ext = json.loads((jd / "extract.json").read_text())
    sim = json.loads((jd / "similarity.json").read_text())
    fit = json.loads((jd / "fit.json").read_text())
    S = {}
    for p in sim["pairs"]:
        a, b = str(p["a"]), str(p["b"]); S[(a, b)] = S[(b, a)] = p["score"]
    clusters = {str(i): n for n, cl in enumerate(sim["clusters"]) for i in cl}
    by_arm = {a: [i for i, k in key.items() if k["task"] == task and k["arm"] == a] for a in ARMS}
    lines += [f"## {task}", "", "| arm | spread: mean within-arm similarity | distinct main ideas (of 4) | similarity to plain | fit accuracy | quality (1-5) |", "|---|---|---|---|---|---|"]
    out[task] = {}
    for a in ARMS:
        ids = by_arm[a]
        within = [S[(x, y)] for x, y in itertools.combinations(ids, 2) if (x, y) in S]
        to_plain = [S[(x, y)] for x in ids for y in by_arm["plain"] if x != y and (x, y) in S]
        distinct = len({clusters.get(x, x) for x in ids})
        fits = [fit[x] == key[x]["fit_true"] for x in ids if x in fit]
        qual = [ext[x]["quality"] for x in ids if x in ext]
        r = {"within": st.mean(within) if within else None, "distinct": distinct,
             "to_plain": st.mean(to_plain) if to_plain else None,
             "fit": sum(fits) / len(fits) if fits else None, "quality": st.mean(qual) if qual else None}
        out[task][a] = r
        f = lambda v, d=2: "n/a" if v is None else f"{v:.{d}f}"
        lines.append(f"| {a} | {f(r['within'])} | {distinct} | {f(r['to_plain'])} | {f(r['fit'])} | {f(r['quality'],1)} |")
    lines.append("")
(it / "pilot_scores.json").write_text(json.dumps(out, indent=2))
(it / "pilot_scores.md").write_text("\n".join(lines))
print("\n".join(lines))
