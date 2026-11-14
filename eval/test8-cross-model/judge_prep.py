import json, random, sys, re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).parent))
from bench import claude, TASK, EVAL

X = Path(__file__).parent
J = X / "judging"; J.mkdir(exist_ok=True)
items = []
for model in ["claude", "gemini"]:
    for f in sorted((X / model).glob("*/*/deliverable.md")):
        arm, who = f.parts[-3], f.parts[-2]
        items.append({"model": model, "arm": arm, "who": who, "src": str(f)})

STRIP = ("Below is a response to this request: \"" + TASK + "\"\n\nReturn ONLY the deliverable itself (the talk outline and the opening paragraph), "
         "copied verbatim. Remove everything else: any 'What everyone gets' section, any Angle / Built from / Strongest objection / Test / Other direction block, "
         "any 'Before you use it' or 'Distance from the default' notes, and any questions, offers or commentary before or after the deliverable. "
         "Do not rewrite, summarise or fix anything. Reply with the deliverable only.\n\n--- RESPONSE ---\n")

def strip(it):
    text = Path(it["src"]).read_text()
    piece = claude(STRIP + text, "opus")[0]
    it["piece"] = piece.strip()
    return it

with ThreadPoolExecutor(max_workers=8) as ex:
    items = list(ex.map(strip, items))

random.seed(20261114)
for model in ["claude", "gemini"]:
    group = [i for i in items if i["model"] == model]
    random.shuffle(group)
    for n, it in enumerate(group, 1):
        it["sim_id"] = f"{model[0].upper()}{n}"
allq = items[:]
random.shuffle(allq)
for n, it in enumerate(allq, 1):
    it["qid"] = str(n)
(J / "items.json").write_text(json.dumps(items, indent=1))
print(len(items), "items stripped and keyed")
