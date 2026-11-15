"""Benchmark v2: six contestants x 2 tasks x 4 users. Usage: score2.py build | claude | score"""
import json, random, re, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).parent))
from bench import claude, EVAL
from h2h import TASKS, STRIP
X = Path(__file__).parent; S = X / "score2"; S.mkdir(exist_ok=True)
CONTESTANTS = ["original", "claude_plain", "gemini_plain", "gemini_asks", "chatgpt_plain", "chatgpt_asks"]
LABEL = {"original": "/original (Claude + skill)", "claude_plain": "Claude, plain", "gemini_plain": "Gemini, plain", "gemini_asks": "Gemini, asks first", "chatgpt_plain": "ChatGPT, plain", "chatgpt_asks": "ChatGPT, asks first"}
MARKERS = {"priya": ["60%", "11 hours", "11 hrs", "~11", "NOT NULL", "three weeks", "400 "], "marcus": ["38", "61 ", "61.", "pilot", "six months", "hand-fly", "autopilot"], "raj": ["9,000", "2,000", "3 hours", "three hours"], "jo": [],
           "leah": ["6am", "6 a.m", "14 months", "shift", "nurse"], "tomas": ["fourth", "4th", "wedding", "six years", "smok"], "max": [], "grace": ["Welsh", "700", "daughter"]}
CLICHES = ["game-changer", "game changer", "double-edged sword", "co-pilot, not", "copilot, not", "autopilot", "not a replacement", "here's the thing", "at the end of the day", "in today's", "fast-paced", "SMART goal", "Atomic Habits", "new year, new you", "new year, new me", "it's not about", "rather than", "unlock", "journey", "gyms are packed", "packed gyms", "by february", "second week of february", "80%", "88%", "92%", "willpower", "start small", "be kind to yourself", "power tool", "the real question"]

def card(task, who):
    return (EVAL / f"personas/{TASKS[task][3]}-{who}.md").read_text().split("\n", 1)[1].strip()

def build():
    h = json.loads((X / "h2h/cases.json").read_text())
    pieces = {}
    for c in h:
        pieces[(c["task"], c["first"], c["who"])] = c["p1"]; pieces[(c["task"], c["second"], c["who"])] = c["p2"]
    todo = []
    for t, (task, base, people, _) in TASKS.items():
        for k, who in enumerate(people, 1):
            todo.append(((t, "chatgpt_plain", who), X / "chatgpt" / t / "plain" / f"run{k}" / "deliverable.md"))
            todo.append(((t, "chatgpt_asks", who), X / "chatgpt" / t / "asks" / who / "deliverable.md"))
    def strip(kp):
        key, p = kp
        return key, claude(STRIP.replace("{task}", TASKS[key[0]][0]) + p.read_text(), "opus")[0].strip()
    with ThreadPoolExecutor(8) as ex:
        for key, piece in ex.map(strip, todo): pieces[key] = piece
    items = []
    for t, (task, base, people, _) in TASKS.items():
        for who in people:
            for c in CONTESTANTS:
                items.append({"task": t, "who": who, "c": c, "piece": pieces[(t, c, who)]})
    rnd = random.Random(2026)
    rnd.shuffle(items)
    for n, it in enumerate(items, 1): it["id"] = n
    (S / "items.json").write_text(json.dumps(items, indent=1))
    # extra head-to-head cases vs ChatGPT
    cases = []
    for t, (task, base, people, _) in TASKS.items():
        for who in people:
            for opp in ["chatgpt_plain", "chatgpt_asks"]:
                for order in (0, 1):
                    a, b = ("original", opp) if order == 0 else (opp, "original")
                    cases.append({"task": t, "who": who, "opp": opp, "first": a, "second": b, "p1": pieces[(t, a, who)], "p2": pieces[(t, b, who)]})
    rnd.shuffle(cases)
    for n, c in enumerate(cases, 101): c["id"] = n
    (S / "h2h_cases.json").write_text(json.dumps(cases, indent=1))
    return items, cases

def p_abs(chunk):
    blocks = [f"=== PIECE {i['id']} ===\nTHE PERSON:\n{card(i['task'], i['who'])}\n\nWHAT THEY ASKED FOR: \"{TASKS[i['task']][0]}\"\n\nTHE PIECE:\n{i['piece']}" for i in chunk]
    ids = ", ".join(str(i["id"]) for i in chunk)
    return ("You are scoring written pieces, blind. Each was produced by an AI assistant for the person described. You see the person's real situation, views, material and audience; the assistant may or may not have known them.\n\n"
            "Score each piece:\n- use_as_is (1-5): would this person be glad to use it as is?\n- fit (1-5): does it reflect THIS person's views, cases, numbers, audience and constraints?\n"
            "- originality (1-5): how far is it from the answer anyone would get by pasting the same request into an AI? 1 = the stock answer.\n- specificity (1-5): concrete details, examples and numbers vs vague general claims.\n"
            "- tone (1-5): does the voice suit this person and their readers as described?\n- writing (1-5): clear, well structured, engaging, right length for the request.\n"
            "- invented (integer): how many personal details, anecdotes or facts about the person or their company it states as true that are NOT in the person's description.\n"
            "- unsupported_stats (integer): how many statistics or studies it cites as fact without a source.\n\n"
            f"Reply with ONLY a JSON object covering pieces {ids}: {{\"<piece>\": {{\"use_as_is\": n, \"fit\": n, \"originality\": n, \"specificity\": n, \"tone\": n, \"writing\": n, \"invented\": n, \"unsupported_stats\": n}}, ...}}\n\n" + "\n\n".join(blocks))

def p_h2h(chunk):
    blocks = [f"=== CASE {c['id']} ===\nTHE PERSON:\n{card(c['task'], c['who'])}\n\nWHAT THEY ASKED FOR: \"{TASKS[c['task']][0]}\"\n\nPIECE 1:\n{c['p1']}\n\nPIECE 2:\n{c['p2']}" for c in chunk]
    ids = ", ".join(str(c["id"]) for c in chunk)
    return ("You are judging pairs of written pieces, blind. In each case below, one person asked for a piece of writing, and two different assistants produced PIECE 1 and PIECE 2. You see the person's real situation, views and audience.\n\n"
            "For each case answer two questions:\n- prefer: which piece would this person rather use as is? Weigh fit to their views, situation, material and audience, and how good and ready to use it is.\n"
            "- less_generic: which piece is further from the answer anyone would get by pasting the same request into an AI?\nAnswer 1 or 2 for each; no ties. Add a one-line reason for prefer.\n\n"
            f"Reply with ONLY a JSON object covering cases {ids}: {{\"<case>\": {{\"prefer\": 1 or 2, \"less_generic\": 1 or 2, \"reason\": \"...\"}}, ...}}\n\n" + "\n\n".join(blocks))

def prompts():
    items = json.loads((S / "items.json").read_text()); cases = json.loads((S / "h2h_cases.json").read_text())
    out = []
    for n in range(4):
        (S / f"abs{n + 1}.txt").write_text(p_abs(items[n * 12:(n + 1) * 12])); out.append(f"abs{n + 1}")
    for n in range(3):
        ch = cases[n * 11:(n + 1) * 11]
        (S / f"hh{n + 1}.txt").write_text(p_h2h(ch)); out.append(f"hh{n + 1}")
    return out

def run_claude():
    def one(name):
        t = claude((S / f"{name}.txt").read_text(), "opus")[0]
        d = json.loads(re.search(r"\{.*\}", t, re.S).group(0)); (S / f"claude_{name}.json").write_text(json.dumps(d, indent=1)); return name, len(d)
    names = [p.stem for p in sorted(S.glob("abs*.txt")) + sorted(S.glob("hh*.txt"))]
    with ThreadPoolExecutor(7) as ex:
        for r in ex.map(one, names): print(r, flush=True)

if __name__ == "__main__":
    if sys.argv[1] == "build":
        items, cases = build(); print(len(items), "pieces,", len(cases), "h2h cases;", prompts(), [len((S / f'{p}.txt').read_text()) for p in prompts()])
    elif sys.argv[1] == "claude":
        run_claude()
