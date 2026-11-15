import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).parent))
import bench
TALK_PERSONA = bench.persona
import bench_blog
X = Path(__file__).parent; R4 = X / "rerun4b"
def P(body, task): return "Follow these instructions for my task.\n\n--- INSTRUCTIONS ---\n" + (X / body).read_text() + "\n--- END INSTRUCTIONS ---\n\nMy task: " + task
SAMP = {"talk": X / "claude/plain", "blog": X / "blog/claude/plain"}
def samples(t): return "\n\n".join(f"--- PLAIN SAMPLE {k} ---\n" + (SAMP[t] / f"run{k}/deliverable.md").read_text().strip() for k in (1, 2, 3))
PERS = {"talk": TALK_PERSONA, "blog": bench_blog.persona}
TASK = {"talk": bench.TASK, "blog": bench_blog.TASK}
WHO = {"talk": bench.PERSONAS, "blog": bench_blog.PERSONAS}
def run(arm, t, w):
    d = R4 / t / arm / w; d.mkdir(parents=True, exist_ok=True)
    body = {"v4": "skill_body4b.md", "v3": "skill_body3.md"}[arm]
    q, sid, _ = bench.claude(P(body, TASK[t]), "fable"); (d / "questions.md").write_text(q)
    a = PERS[t](w, q); (d / "answers.md").write_text(a)
    msg = a + ("\n\n[The sampling step returned these three plain answers to the same task. The user has not seen them.]\n\n" + samples(t) if arm == "v4" else "")
    piece, _, _ = bench.claude(msg, "fable", resume=sid); (d / "deliverable.md").write_text(piece)
    return f"{arm}/{t}/{w}"
jobs = [("v4", t, w) for t in ("talk", "blog") for w in WHO[t]]
with ThreadPoolExecutor(6) as ex:
    for r in ex.map(lambda j: run(*j), jobs): print(r, flush=True)
