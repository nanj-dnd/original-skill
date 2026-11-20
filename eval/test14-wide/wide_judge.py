"""python3 wide_judge.py build | claude | gpt_prompts | score"""
import json, random, re, sys, statistics as st
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).parent))
from bench import claude
from h2h import STRIP
from wide import TASKS, WHO, card, W
J = W / "judge"; J.mkdir(exist_ok=True)
C = ["v5", "v5pre", "v4", "asks", "plain"]
def src(t, w, c, r):
    if c == "plain": return W / f"plain/{t}/run{WHO[t].index(w) + 4}.md"
    if c == "v5pre": return W / t / w / f"v5{r}" / "deliverable.md"
    f = "final.md" if c == "v5" else "deliverable.md"
    return W / t / w / f"{c}{r}" / f
def build():
    todo = [(t, w, c, r) for t in TASKS for w in WHO[t] for c, n in (("v5", 2), ("v5pre", 2), ("v4", 2), ("asks", 1), ("plain", 1)) for r in range(1, n + 1)]
    def strip(a):
        t, w, c, r = a
        return {"task": t, "who": w, "c": c, "r": r, "piece": claude(STRIP.replace("{task}", TASKS[t]) + src(*a).read_text(), "opus")[0].strip()}
    with ThreadPoolExecutor(8) as ex: items = list(ex.map(strip, todo))
    rnd = random.Random(1119); rnd.shuffle(items)
    for n, i in enumerate(items, 1001): i["id"] = n
    (J / "items.json").write_text(json.dumps(items, indent=1))
    pre = [i for i in items if i["c"] == "v5pre"]; items = [i for i in items if i["c"] != "v5pre"]
    P = {(i["task"], i["who"], i["c"], i["r"]): i["piece"] for i in items}
    cases = []
    for t in TASKS:
        for w in WHO[t]:
            pairs = [(("v5", 1), ("v4", 1)), (("v5", 2), ("v4", 2)), (("v5", 1), ("asks", 1)), (("v5", 2), ("plain", 1))]
            for a, b in pairs:
                for x, y in ((a, b), (b, a)):
                    cases.append({"task": t, "who": w, "opp": b[0], "first": x, "second": y, "p1": P[(t, w) + x], "p2": P[(t, w) + y]})
    rnd.shuffle(cases)
    for n, c in enumerate(cases, 2001): c["id"] = n
    (J / "cases.json").write_text(json.dumps(cases, indent=1))
    for n in range(6): (J / f"abs{n + 1}.txt").write_text(p_abs(items[n * 12:(n + 1) * 12]))
    for n in range(6): (J / f"hh{n + 1}.txt").write_text(p_h2h(cases[n * 16:(n + 1) * 16]))
    ask = [i for i in items if i["c"] != "plain"]
    for n in range(5): (J / f"audit{n + 1}.txt").write_text(p_audit(ask[n * 12:(n + 1) * 12]))
    for n in range(2): (J / f"audit{n + 6}.txt").write_text(p_audit(pre[n * 12:(n + 1) * 12]))
    (J / "overlap.txt").write_text(p_overlap(items))
    print(len(items), "items", len(cases), "cases")
def p_abs(chunk):
    blocks = [f"=== PIECE {i['id']} ===\nTHE PERSON:\n{card(i['task'], i['who'])}\n\nWHAT THEY ASKED FOR: \"{TASKS[i['task']]}\"\n\nTHE PIECE:\n{i['piece']}" for i in chunk]
    ids = ", ".join(str(i["id"]) for i in chunk)
    return ("You are scoring written pieces, blind. Each was produced by an AI assistant for the person described. You see the person's real situation, views, material and audience; the assistant may or may not have known them.\n\n"
            "Score each piece:\n- use_as_is (1-5): would this person be glad to use it as is?\n- fit (1-5): does it reflect THIS person's views, cases, numbers, audience and constraints?\n"
            "- originality (1-5): how far is it from the answer anyone would get by pasting the same request into an AI? 1 = the stock answer.\n- specificity (1-5): concrete details, examples and numbers vs vague general claims.\n"
            "- tone (1-5): does the voice suit this person and their readers as described?\n- writing (1-5): clear, well structured, engaging, right length for the request.\n\n"
            f"Reply with ONLY a JSON object covering pieces {ids}: {{\"<piece>\": {{\"use_as_is\": n, \"fit\": n, \"originality\": n, \"specificity\": n, \"tone\": n, \"writing\": n}}, ...}}\n\n" + "\n\n".join(blocks))
def p_h2h(chunk):
    blocks = [f"=== CASE {c['id']} ===\nTHE PERSON:\n{card(c['task'], c['who'])}\n\nWHAT THEY ASKED FOR: \"{TASKS[c['task']]}\"\n\nPIECE 1:\n{c['p1']}\n\nPIECE 2:\n{c['p2']}" for c in chunk]
    ids = ", ".join(str(c["id"]) for c in chunk)
    return ("You are judging pairs of written pieces, blind. In each case below, one person asked for a piece of writing, and two different assistants produced PIECE 1 and PIECE 2. You see the person's real situation, views and audience.\n\n"
            "For each case answer two questions:\n- prefer: which piece would this person rather use as is? Weigh fit to their views, situation, material and audience, and how good and ready to use it is.\n"
            "- less_generic: which piece is further from the answer anyone would get by pasting the same request into an AI?\nAnswer 1 or 2 for each; no ties. Add a one-line reason for prefer.\n\n"
            f"Reply with ONLY a JSON object covering cases {ids}: {{\"<case>\": {{\"prefer\": 1 or 2, \"less_generic\": 1 or 2, \"reason\": \"...\"}}, ...}}\n\n" + "\n\n".join(blocks))
def ans(i): return (W / i["task"] / i["who"] / f"{i['c'].replace('pre', '')}{i['r']}" / "answers.md").read_text().strip()
def p_audit(chunk):
    blocks = [f"=== PIECE {i['id']} ===\nTHE PERSON (their description):\n{card(i['task'], i['who'])}\n\nWHAT THEY TOLD THE ASSISTANT:\n{ans(i)}\n\nTHE PIECE:\n{i['piece']}" for i in chunk]
    ids = ", ".join(str(i["id"]) for i in chunk)
    return ("You are auditing written pieces for invented details about the person, blind. Each piece was written for the person described, after they answered the assistant's questions. Their description plus their answers are EVERYTHING that is known about them.\n\n"
            "For each piece, list every statement it makes about the person, their life, work, company, product, customers, team, past, habits, feelings or experiences that is supported by NEITHER the description NOR their answers. Quote the exact phrase. "
            "Count a detail as supported if it is stated in the description or the answers, or follows directly from them. Do not count: general advice, claims about people in general, rhetorical examples clearly framed as hypothetical, opinions that restate the views they gave, or the piece's structure and wording.\n\n"
            f"Reply with ONLY a JSON object covering pieces {ids}: {{\"<piece>\": {{\"invented\": [\"quoted phrase\", ...]}}, ...}}\n\n" + "\n\n".join(blocks))
def p_overlap(items):
    ov = []
    for t in TASKS:
        plain = "\n\n".join(f"--- PLAIN ANSWER {k} ---\n" + (W / f"plain/{t}/run{k}.md").read_text().strip() for k in (4, 5, 6))
        ov.append(f"##### TASK: \"{TASKS[t]}\"\n\nTHREE PLAIN ANSWERS ANYONE GETS BY PASTING THIS REQUEST:\n{plain}\n\n" + "\n\n".join(f"=== PIECE {i['id']} ===\n{i['piece']}" for i in items if i["task"] == t and i["c"] != "plain"))
    ids = ", ".join(str(i["id"]) for i in items if i["c"] != "plain")
    return ("Below are requests, three plain AI answers to each, and several pieces written for specific people. For each piece, count how many of these it shares with the plain answers: the main claim, the key examples, the overall structure, the opening move, stock phrases. "
            "Score shared (0-5, 0 = shares none of them, 5 = shares all).\n\n" f"Reply with ONLY a JSON object covering pieces {ids}: {{\"<piece>\": {{\"shared\": n}}, ...}}\n\n" + "\n\n".join(ov))
def run_claude():
    names = [p.stem for p in sorted(J.glob("*.txt")) if not p.stem.startswith("g_") and not (J / f"claude_{p.stem}.json").exists()]
    def one(n):
        try:
            t = claude((J / f"{n}.txt").read_text(), "opus")[0]
            d = json.loads(re.search(r"\{.*\}", t, re.S).group(0)); (J / f"claude_{n}.json").write_text(json.dumps(d, indent=1)); return n, len(d)
        except Exception as e: return n, "FAILED " + str(e)[:100]
    with ThreadPoolExecutor(6) as ex:
        for r in ex.map(one, names): print(r, flush=True)
def gpt_prompts():
    cases = [c for c in json.loads((J / "cases.json").read_text()) if c["opp"] in ("v4", "asks")]
    for n in range(0, len(cases), 8): (J / f"g_hh{n // 8 + 1}.txt").write_text(p_h2h(cases[n:n + 8]))
    items = [i for i in json.loads((J / "items.json").read_text()) if i["c"] in ("v5", "v4") and i["r"] == 1]
    for n in range(0, len(items), 8): (J / f"g_audit{n // 8 + 1}.txt").write_text(p_audit(items[n:n + 8]))
    print(sorted(p.name for p in J.glob("g_*.txt")))
def load(pat):
    d = {}
    for f in J.glob(pat): d.update({re.sub(r"\D", "", k): v for k, v in json.loads(f.read_text()).items()})
    return d
def score():
    items = {str(i["id"]): i for i in json.loads((J / "items.json").read_text())}
    cases = {str(c["id"]): c for c in json.loads((J / "cases.json").read_text())}
    M = ["use_as_is", "fit", "originality", "specificity", "tone", "writing"]
    a = load("claude_abs*.json"); au = load("claude_audit*.json"); ov = load("claude_overlap.json"); gau = load("gpt_audit*.json")
    out = {"scores": {}, "by_task": {}, "h2h": {}}
    for c in C:
        ks = [k for k, i in items.items() if i["c"] == c]
        if c == "v5pre":
            out["scores"][c] = {"invented_claude": round(st.mean(len(au[k]["invented"]) for k in ks), 2)}; continue
        row = {m: round(st.mean(a[k][m] for k in ks), 2) for m in M}
        if c != "plain":
            row["invented_claude"] = round(st.mean(len(au[k]["invented"]) for k in ks), 2)
            row["shared"] = round(st.mean(ov[k]["shared"] for k in ks), 2)
            g = [k for k in ks if k in gau]
            if g: row["invented_gpt"] = round(st.mean(len(gau[k]["invented"]) for k in g), 2)
        out["scores"][c] = row
        for t in TASKS:
            out["by_task"].setdefault(t, {})[c] = {m: round(st.mean(a[k][m] for k in ks if items[k]["task"] == t), 2) for m in ["use_as_is", "fit", "originality"]}
    for judge, pat in (("claude", "claude_hh*.json"), ("gpt", "gpt_hh*.json")):
        v = load(pat)
        if not v: continue
        m = defaultdict(list)
        for cid, c in cases.items():
            if cid not in v: continue
            pos = 1 if c["first"][0] == "v5" else 2
            for q in ["prefer", "less_generic"]: m[(c["opp"], c["task"], c["who"], tuple(sorted([tuple(c["first"]), tuple(c["second"])])), q)].append(int(v[cid][q]) == pos)
        for opp in ("v4", "asks", "plain"):
            for q in ["prefer", "less_generic"]:
                pts = [sum(x) for k, x in m.items() if k[0] == opp and k[4] == q and len(x) == 2]
                if pts: out["h2h"].setdefault(judge, {}).setdefault(opp, {})[q] = {"won_share": round(sum(pts) / (2 * len(pts)), 2), "pairs": len(pts), "both": pts.count(2), "split": pts.count(1), "lost": pts.count(0)}
            pts = defaultdict(list)
            for k, x in m.items():
                if k[0] == opp and k[4] == "prefer" and len(x) == 2: pts[k[1]].append(sum(x))
            if pts: out["h2h"][judge][opp]["prefer_by_task"] = {t: round(sum(p) / (2 * len(p)), 2) for t, p in pts.items()}
    (J / "results.json").write_text(json.dumps(out, indent=1))
    for c, s in out["scores"].items(): print(c.ljust(6), s)
    print(json.dumps(out["h2h"], indent=1)); print(json.dumps(out["by_task"]))
if __name__ == "__main__":
    {"build": build, "claude": run_claude, "gpt_prompts": gpt_prompts, "score": score}[sys.argv[1]]()
