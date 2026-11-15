import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).parent))
import bench, bench_blog
X = Path(__file__).parent
SKILL2 = (X / "skill_body2.md").read_text()
def skillp(task): return "Follow these instructions for my task.\n\n--- INSTRUCTIONS ---\n" + SKILL2 + "\n--- END INSTRUCTIONS ---\n\nMy task: " + task
if __name__ == "__main__":
    import importlib
    importlib.reload(bench)  # restore the talk persona (bench_blog patched it on import)
    assert bench.persona.__module__ == 'bench'
    with ThreadPoolExecutor(4) as ex:
        for r in ex.map(lambda w: bench.two_turn("fable", X / "rerun/talk", "skill", w, skillp(bench.TASK)), bench.PERSONAS): print("talk", r, flush=True)
    # blog runs sequentially patch the persona function to the blog cards
    bench.persona = bench_blog.persona
    with ThreadPoolExecutor(4) as ex:
        for r in ex.map(lambda w: bench.two_turn("fable", X / "rerun/blog", "skill", w, skillp(bench_blog.TASK)), bench_blog.PERSONAS): print("blog", r, flush=True)
