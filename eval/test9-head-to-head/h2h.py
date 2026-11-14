import json, random, re, sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).parent))
from bench import claude, EVAL
X = Path(__file__).parent; H = X / "h2h"; H.mkdir(exist_ok=True)
TASKS = {"talk": ("I've got 5 minutes at our company all-hands next Friday to talk about whether engineers should be using AI coding assistants for everything. Can you write me an outline and the opening paragraph?", X, ["priya", "marcus", "jo", "raj"], "talk"),
         "blog": ("Write me a ~400-word blog post on why most New Year's resolutions fail. It's for my personal blog.", X / "blog", ["leah", "tomas", "max", "grace"], "resolutions")}
STRIP = ("Below is a response to this request: \"{task}\"\n\nReturn ONLY the deliverable itself, copied verbatim. Remove everything else: any 'What everyone gets' section, any Angle / Built from / "
         "Strongest objection / Test / Other direction block, any 'Before you use it' or 'Distance from the default' notes, and any questions, offers or commentary before or after the deliverable. "
         "Do not rewrite, summarise or fix anything. Reply with the deliverable only.\n\n--- RESPONSE ---\n")
OPP = {"gemini_plain": "Gemini, plain", "gemini_asks": "Gemini, asks first", "claude_plain": "Claude, plain"}

def path(task, contestant, who, k):
    base = TASKS[task][1]
    return {"original": base / "claude/skill" / who, "claude_plain": base / "claude/plain" / f"run{k}",
            "gemini_plain": base / "gemini/plain" / f"run{k}", "gemini_asks": base / "gemini/asks" / who}[contestant] / "deliverable.md"

def build():
    talk_items = {Path(i["src"]): i["piece"] for i in json.loads((X / "judging/items.json").read_text())}
    need = {}
    for t, (task, base, people, _) in TASKS.items():
        for k, who in enumerate(people, 1):
            for c in ["original", "claude_plain", "gemini_plain", "gemini_asks"]:
                need[(t, c, who)] = path(t, c, who, k)
    pieces = {}
    todo = [(key, p) for key, p in need.items() if p not in talk_items]
    for key, p in need.items():
        if p in talk_items: pieces[key] = talk_items[p]
    def strip(kp):
        key, p = kp
        return key, claude(STRIP.replace("{task}", TASKS[key[0]][0]) + p.read_text(), "opus")[0].strip()
    with ThreadPoolExecutor(max_workers=8) as ex:
        for key, piece in ex.map(strip, todo): pieces[key] = piece
    rnd = random.Random(15)
    cases = []
    for t, (task, base, people, prefix) in TASKS.items():
        for who in people:
            for opp in OPP:
                for order in (0, 1):
                    first, second = ("original", opp) if order == 0 else (opp, "original")
                    cases.append({"task": t, "who": who, "opp": opp, "first": first, "second": second,
                                  "p1": pieces[(t, first, who)], "p2": pieces[(t, second, who)]})
    rnd.shuffle(cases)
    for n, c in enumerate(cases, 1): c["id"] = n
    (H / "cases.json").write_text(json.dumps(cases, indent=1))
    return cases

def prompt(chunk):
    def card(c):
        prefix = TASKS[c["task"]][3]
        return (EVAL / f"personas/{prefix}-{c['who']}.md").read_text().split("\n", 1)[1].strip()
    blocks = [f"=== CASE {c['id']} ===\nTHE PERSON:\n{card(c)}\n\nWHAT THEY ASKED FOR: \"{TASKS[c['task']][0]}\"\n\nPIECE 1:\n{c['p1']}\n\nPIECE 2:\n{c['p2']}" for c in chunk]
    ids = ", ".join(str(c["id"]) for c in chunk)
    return ("You are judging pairs of written pieces, blind. In each case below, one person asked for a piece of writing, and two different assistants produced PIECE 1 and PIECE 2. "
            "You see the person's real situation, views and audience.\n\nFor each case answer two questions:\n"
            "- prefer: which piece would this person rather use as is? Weigh how well it fits their views, situation, material and audience, and how good and ready to use it is.\n"
            "- less_generic: which piece is further from the answer anyone would get by pasting the same request into an AI?\n"
            "Answer 1 or 2 for each; no ties. Add a one-line reason for prefer.\n\n"
            f"Reply with ONLY a JSON object covering cases {ids}: {{\"<case>\": {{\"prefer\": 1 or 2, \"less_generic\": 1 or 2, \"reason\": \"...\"}}, ...}}\n\n" + "\n\n".join(blocks))

if __name__ == "__main__":
    cases = build() if not (H / "cases.json").exists() else json.loads((H / "cases.json").read_text())
    chunks = [cases[i:i + 12] for i in range(0, len(cases), 12)]
    for n, ch in enumerate(chunks, 1):
        (H / f"prompt{n}.txt").write_text(prompt(ch))
    print(len(cases), "cases in", len(chunks), "chunks;", [len((H / f'prompt{n}.txt').read_text()) for n in range(1, len(chunks) + 1)])
