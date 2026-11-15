"""python3 rerun3_judge.py build | claude | score"""
import json, random, re, sys, statistics as st
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).parent))
from bench import claude
from h2h import TASKS, STRIP
from score2 import card, p_abs
X = Path(__file__).parent; R3 = X / "rerun3"; R = X / "rerun"
ANS = {"original": X / "blog/claude/skill", "original_v2": R / "blog/skill", "original_v3": R3 / "blog/skill", "chatgpt_asks": X / "chatgpt/blog/asks"}
def build():
    prev = [i for i in json.loads((R / "items.json").read_text()) if i["task"] == "blog"]
    def strip(w):
        p = R3 / "blog/skill" / w / "deliverable.md"
        return {"task": "blog", "who": w, "c": "original_v3", "piece": claude(STRIP.replace("{task}", TASKS["blog"][0]) + p.read_text(), "opus")[0].strip()}
    with ThreadPoolExecutor(4) as ex: new = list(ex.map(strip, ["leah", "tomas", "max", "grace"]))
    items = [{k: i[k] for k in ("task", "who", "c", "piece")} for i in prev] + new
    random.Random(1116).shuffle(items)
    for n, i in enumerate(items, 401): i["id"] = n
    (R3 / "items.json").write_text(json.dumps(items, indent=1))
    blocks = [f"=== PIECE {i['id']} ===\nTHE PERSON (their description):\n{card('blog', i['who'])}\n\nWHAT THEY TOLD THE ASSISTANT (their answers to its questions):\n{(ANS[i['c']] / i['who'] / 'answers.md').read_text().strip()}\n\nTHE PIECE:\n{i['piece']}" for i in items]
    ids = ", ".join(str(i["id"]) for i in items)
    audit = ("You are auditing written pieces for invented personal details, blind. Each piece was written for the person described, after they answered the assistant's questions. "
             "Their description plus their answers are EVERYTHING that is known about them.\n\n"
             "For each piece, list every statement it makes about the person, their life, family, work, company, colleagues, past attempts, habits, feelings or experiences that is supported by NEITHER the description NOR their answers. "
             "Quote the exact phrase from the piece. Count a detail as supported if it is stated in the description or the answers, or follows directly from them (for example, 700 days is about two years). "
             "Do not count: general advice, claims about people in general, rhetorical examples clearly framed as hypothetical, or the piece's structure and wording.\n\n"
             f"Reply with ONLY a JSON object covering pieces {ids}: {{\"<piece>\": {{\"invented\": [\"quoted phrase\", ...], \"count\": n}}, ...}}\n\n" + "\n\n".join(blocks))
    (R3 / "audit.txt").write_text(audit); (R3 / "abs.txt").write_text(p_abs(items))
    print(len(items), "items;", len(audit), len((R3 / "abs.txt").read_text()))
def run_claude():
    def one(n):
        t = claude((R3 / f"{n}.txt").read_text(), "opus")[0]
        d = json.loads(re.search(r"\{.*\}", t, re.S).group(0)); (R3 / f"claude_{n}.json").write_text(json.dumps(d, indent=1)); return n, len(d)
    with ThreadPoolExecutor(2) as ex:
        for r in ex.map(one, ["audit", "abs"]): print(r, flush=True)
def load(f): return {re.sub(r"\D", "", k): v for k, v in json.loads(Path(f).read_text()).items()}
def score():
    items = {str(i["id"]): i for i in json.loads((R3 / "items.json").read_text())}
    out = {}
    for c in ["original", "original_v2", "original_v3", "chatgpt_asks"]:
        ks = [k for k, i in items.items() if i["c"] == c]; row = {}
        for j in ["claude", "gpt"]:
            f = R3 / f"{j}_audit.json"
            if f.exists(): d = load(f); row[f"invented_{j}"] = round(st.mean(len(d[k].get("invented", [])) for k in ks), 2)
        for j in ["claude", "gemini", "gpt"]:
            f = R3 / f"{j}_abs.json"
            if f.exists():
                d = load(f)
                for m in ["use_as_is", "fit", "originality", "specificity", "tone", "writing"]: row.setdefault(m, {})[j] = round(st.mean(d[k][m] for k in ks), 2)
        for m in ["use_as_is", "fit", "originality", "specificity", "tone", "writing"]:
            if m in row: row[m]["mean"] = round(st.mean(v for kk, v in row[m].items() if kk != "mean"), 2)
        out[c] = row; print(c.ljust(13), row)
    (R3 / "results.json").write_text(json.dumps(out, indent=1))
if __name__ == "__main__":
    {"build": build, "claude": run_claude, "score": score}[sys.argv[1]]()
