import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).parent))
import bench
from bench import claude, EVAL, SKILL
TASK = "Write me a ~400-word blog post on why most New Year's resolutions fail. It's for my personal blog."
SKILLP = "Follow these instructions for my task.\n\n--- INSTRUCTIONS ---\n" + SKILL + "\n--- END INSTRUCTIONS ---\n\nMy task: " + TASK
PERSONAS = ["leah", "tomas", "max", "grace"]
def persona(name, msg):
    card = (EVAL / f"personas/resolutions-{name}.md").read_text()
    return claude(bench.PERSONA_TMPL.replace("{CARD}", card).replace("{MSG}", msg), "opus")[0]
bench.persona = persona
if __name__ == "__main__":
    out = Path(sys.argv[1])
    with ThreadPoolExecutor(max_workers=6) as ex:
        jobs = [ex.submit(bench.plain.__wrapped__ if hasattr(bench.plain, "__wrapped__") else None, None)] if False else []
        def plain(i):
            d = out / "plain" / f"run{i}"; d.mkdir(parents=True, exist_ok=True)
            p, _, used = claude(TASK, "fable"); (d / "deliverable.md").write_text(p); (d / "model.txt").write_text(", ".join(used)); return f"plain/run{i}"
        jobs = [ex.submit(plain, i) for i in range(1, 5)] + [ex.submit(bench.two_turn, "fable", out, "skill", n, SKILLP) for n in PERSONAS]
        for j in jobs:
            try: print(j.result(), flush=True)
            except Exception as e: print("FAILED", e, flush=True)
