"""python3 rerun4_judge.py build | claude | score"""
import json, random, re, sys, statistics as st
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).parent))
from bench import claude
from h2h import TASKS, STRIP
from score2 import card, p_abs, p_h2h
X = Path(__file__).parent; R4 = X / "rerun4b"; R4A = X / "rerun4"; R3 = X / "rerun3"; R = X / "rerun"
WHO = {"talk": ["priya", "marcus", "jo", "raj"], "blog": ["leah", "tomas", "max", "grace"]}
def src(c, t, w):
    return {"v4": R4 / t / "v4" / w, "v3": (R4A / "talk/v3" / w) if t == "talk" else (R3 / "blog/skill" / w), "chatgpt_asks": X / "chatgpt" / t / "asks" / w}[c]
SAMP = {"talk": X / "claude/plain", "blog": X / "blog/claude/plain"}
def build():
    old = {(i["task"], i["who"], i["c"]): i["piece"] for f in [R / "items.json", R3 / "items.json"] for i in json.loads(f.read_text())}
    items, todo = [], []
    for t in WHO:
        for w in WHO[t]:
            items.append({"task": t, "who": w, "c": "chatgpt_asks", "piece": old[(t, w, "chatgpt_asks")]})
            if t == "blog": items.append({"task": t, "who": w, "c": "v3", "piece": old[(t, w, "original_v3")]})
            else: todo.append((t, w, "v3"))
            todo.append((t, w, "v4"))
    def strip(a):
        t, w, c = a
        return {"task": t, "who": w, "c": c, "piece": claude(STRIP.replace("{task}", TASKS[t][0]) + (src(c, t, w) / "deliverable.md").read_text(), "opus")[0].strip()}
    with ThreadPoolExecutor(8) as ex: items += list(ex.map(strip, todo))
    rnd = random.Random(1118); rnd.shuffle(items)
    for n, i in enumerate(items, 701): i["id"] = n
    (R4 / "items.json").write_text(json.dumps(items, indent=1))
    piece = {(i["task"], i["c"], i["who"]): i["piece"] for i in items}
    cases = []
    for t in WHO:
        for w in WHO[t]:
            for opp in ("v3", "chatgpt_asks"):
                for a, b in (("v4", opp), (opp, "v4")):
                    cases.append({"task": t, "who": w, "opp": opp, "first": a, "second": b, "p1": piece[(t, a, w)], "p2": piece[(t, b, w)]})
    rnd.shuffle(cases)
    for n, c in enumerate(cases, 801): c["id"] = n
    (R4 / "h2h_cases.json").write_text(json.dumps(cases, indent=1))
    (R4 / "abs1.txt").write_text(p_abs(items[:12])); (R4 / "abs2.txt").write_text(p_abs(items[12:]))
    (R4 / "hh1.txt").write_text(p_h2h(cases[:16])); (R4 / "hh2.txt").write_text(p_h2h(cases[16:]))
    blocks = [f"=== PIECE {i['id']} ===\nTHE PERSON (their description):\n{card(i['task'], i['who'])}\n\nWHAT THEY TOLD THE ASSISTANT:\n{(src(i['c'], i['task'], i['who']) / 'answers.md').read_text().strip()}\n\nTHE PIECE:\n{i['piece']}" for i in items]
    ids = ", ".join(str(i["id"]) for i in items)
    audit = ("You are auditing written pieces for invented personal details, blind. Each piece was written for the person described, after they answered the assistant's questions. Their description plus their answers are EVERYTHING that is known about them.\n\n"
             "For each piece, list every statement it makes about the person, their life, family, work, company, colleagues, past attempts, habits, feelings or experiences that is supported by NEITHER the description NOR their answers. Quote the exact phrase. "
             "Count a detail as supported if it is stated in the description or the answers, or follows directly from them. Do not count: general advice, claims about people in general, rhetorical examples clearly framed as hypothetical, opinions that restate the views they gave, or the piece's structure and wording.\n\n"
             f"Reply with ONLY a JSON object covering pieces {ids}: {{\"<piece>\": {{\"invented\": [\"quoted phrase\", ...], \"count\": n}}, ...}}\n\n" + "\n\n".join(blocks))
    (R4 / "audit.txt").write_text(audit)
    ov = []
    for t in WHO:
        plain = "\n\n".join(f"--- PLAIN ANSWER {k} ---\n" + (R4A / "heldout" / t / f"run{k}/deliverable.md").read_text().strip() for k in (1, 2, 3))
        its = [i for i in items if i["task"] == t]
        ov.append(f"##### TASK: \"{TASKS[t][0]}\"\n\nTHREE PLAIN ANSWERS ANYONE GETS BY PASTING THIS REQUEST:\n{plain}\n\n" + "\n\n".join(f"=== PIECE {i['id']} ===\n{i['piece']}" for i in its))
    ids = ", ".join(str(i["id"]) for i in items)
    (R4 / "overlap.txt").write_text("Below are requests, three plain AI answers to each, and several pieces written for specific people. For each piece, count how many of these it shares with the plain answers: the main claim, the key examples, the overall structure, the opening move, stock phrases. "
        "Score shared (0-5, 0 = shares none of them, 5 = shares all). Also give one short phrase naming the biggest thing it shares, or \"none\".\n\n"
        f"Reply with ONLY a JSON object covering pieces {ids}: {{\"<piece>\": {{\"shared\": n, \"what\": \"...\"}}, ...}}\n\n" + "\n\n".join(ov))
    print(len(items), "items", len(cases), "cases", {f: len((R4 / f).read_text()) for f in ["abs1.txt", "abs2.txt", "hh1.txt", "hh2.txt", "audit.txt", "overlap.txt"]})
def run_claude():
    def one(n):
        t = claude((R4 / f"{n}.txt").read_text(), "opus")[0]
        d = json.loads(re.search(r"\{.*\}", t, re.S).group(0)); (R4 / f"claude_{n}.json").write_text(json.dumps(d, indent=1)); return n, len(d)
    with ThreadPoolExecutor(6) as ex:
        for r in ex.map(one, ["abs1", "abs2", "hh1", "hh2", "audit", "overlap"]): print(r, flush=True)
def load(fs):
    d = {}
    for f in fs:
        if Path(f).exists(): d.update({re.sub(r"\D", "", k): v for k, v in json.loads(Path(f).read_text()).items()})
    return d
def score():
    items = {str(i["id"]): i for i in json.loads((R4 / "items.json").read_text())}
    cases = {str(c["id"]): c for c in json.loads((R4 / "h2h_cases.json").read_text())}
    judges = [j for j in ["claude", "gemini", "gpt"] if (R4 / f"{j}_abs2.json").exists()]
    M = ["use_as_is", "fit", "originality", "specificity", "tone", "writing"]
    out = {"judges": judges, "scores": {}, "by_task": {}, "h2h": {}}
    for c in ["v4", "v3", "chatgpt_asks"]:
        row = {}
        for j in judges:
            a = load([R4 / f"{j}_abs1.json", R4 / f"{j}_abs2.json"])
            for m in M: row.setdefault(m, {})[j] = round(st.mean(a[k][m] for k, i in items.items() if i["c"] == c), 2)
            for t in WHO: out["by_task"].setdefault(t, {}).setdefault(c, {})[j] = {m: round(st.mean(a[k][m] for k, i in items.items() if i["c"] == c and i["task"] == t), 2) for m in ["use_as_is", "fit", "originality", "specificity"]}
        for m in M: row[m]["mean"] = round(st.mean(row[m][j] for j in judges), 2)
        for j in ["claude", "gpt"]:
            au = load([R4 / f"{j}_audit.json"])
            if au: row[f"invented_{j}"] = round(st.mean(len(au[k].get("invented", [])) for k, i in items.items() if i["c"] == c), 2)
            ov = load([R4 / f"{j}_overlap.json"])
            if ov: row[f"shared_{j}"] = round(st.mean(ov[k]["shared"] for k, i in items.items() if i["c"] == c), 2)
        out["scores"][c] = row
    for j in judges:
        v = load([R4 / f"{j}_hh1.json", R4 / f"{j}_hh2.json"])
        if len(v) < len(cases): continue
        m = defaultdict(list)
        for cid, c in cases.items():
            pos = 1 if c["first"] == "v4" else 2
            for q in ["prefer", "less_generic"]: m[(c["opp"], c["task"], c["who"], q)].append(int(v[cid][q]) == pos)
        for opp in ("v3", "chatgpt_asks"):
            for q in ["prefer", "less_generic"]:
                w = [sum(x) for k, x in m.items() if k[0] == opp and k[3] == q]
                out["h2h"].setdefault(j, {}).setdefault(opp, {})[q] = {"both_orders": w.count(2), "split": w.count(1), "lost_both": w.count(0)}
    (R4 / "results.json").write_text(json.dumps(out, indent=1))
    for c, s in out["scores"].items(): print(c.ljust(13), json.dumps(s))
    print(json.dumps(out["h2h"], indent=1)); print(json.dumps(out["by_task"]))
if __name__ == "__main__":
    {"build": build, "claude": run_claude, "score": score}[sys.argv[1]]()
