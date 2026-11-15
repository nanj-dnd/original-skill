import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).parent))
import bench, bench_blog
X = Path(__file__).parent
SKILL3 = (X / "skill_body3.md").read_text()
P = "Follow these instructions for my task.\n\n--- INSTRUCTIONS ---\n" + SKILL3 + "\n--- END INSTRUCTIONS ---\n\nMy task: " + bench_blog.TASK
bench.persona = bench_blog.persona
with ThreadPoolExecutor(4) as ex:
    for r in ex.map(lambda w: bench.two_turn("fable", X / "rerun3/blog", "skill", w, P), bench_blog.PERSONAS): print(r, flush=True)
