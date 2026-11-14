"""Embedding-based spread and distance from default.
Usage: <venv>/bin/python -I embed_score.py <iteration_dir>
Each deliverable is split into chunks of ~200 words (the model truncates long input),
chunk embeddings are averaged, then cosine similarity is computed."""
import os, sys, pathlib, itertools, json
import numpy as np
from sentence_transformers import SentenceTransformer
it = pathlib.Path(sys.argv[1]); ARMS = os.environ.get("ARMS", "plain,plain_ctx,quick,full").split(",")
m = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
def emb(text):
    w = text.split(); chunks = [" ".join(w[i:i+200]) for i in range(0, len(w), 200)] or [""]
    v = m.encode(chunks, normalize_embeddings=True).mean(0); return v / np.linalg.norm(v)
out = {}; lines = ["# Embedding scores (cosine, all-mpnet-base-v2)", "",
  "within = mean pairwise cosine inside an arm (lower = more spread between users); to_plain = mean cosine to the plain arm's outputs (lower = further from the default).", ""]
for task in ["talk", "resolutions"]:
    cases = sorted(p.name for p in it.iterdir() if p.is_dir() and p.name.startswith(task + "-") and all((p / a / "outputs" / "deliverable.md").exists() for a in ARMS))
    E = {(c, a): emb((it / c / a / "outputs" / "deliverable.md").read_text()) for c in cases for a in ARMS}
    lines += [f"## {task}", "", "| arm | within | to_plain |", "|---|---|---|"]; out[task] = {}
    for a in ARMS:
        within = [float(E[(x, a)] @ E[(y, a)]) for x, y in itertools.combinations(cases, 2)]
        to_plain = [float(E[(x, a)] @ E[(y, "plain")]) for x in cases for y in cases if (a != "plain" or x != y)]
        out[task][a] = {"within": np.mean(within), "to_plain": np.mean(to_plain)}
        lines.append(f"| {a} | {np.mean(within):.3f} | {np.mean(to_plain):.3f} |")
    lines.append("")
(it / "embed_scores.json").write_text(json.dumps(out, indent=2, default=float))
(it / "embed_scores.md").write_text("\n".join(lines)); print("\n".join(lines))
