import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from score2 import card
X = Path(__file__).parent; R = X / "rerun"
items = json.loads((R / "items.json").read_text())
def answers(i):
    t, c, w = i["task"], i["c"], i["who"]
    p = {("talk", "original"): X / "claude/skill" / w, ("blog", "original"): X / "blog/claude/skill" / w,
         ("talk", "original_v2"): R / "talk/skill" / w, ("blog", "original_v2"): R / "blog/skill" / w,
         ("talk", "chatgpt_asks"): X / "chatgpt/talk/asks" / w, ("blog", "chatgpt_asks"): X / "chatgpt/blog/asks" / w}[(t, c)]
    return (p / "answers.md").read_text().strip()
def prompt(chunk):
    blocks = [f"=== PIECE {i['id']} ===\nTHE PERSON (their description):\n{card(i['task'], i['who'])}\n\nWHAT THEY TOLD THE ASSISTANT (their answers to its questions):\n{answers(i)}\n\nTHE PIECE:\n{i['piece']}" for i in chunk]
    ids = ", ".join(str(i["id"]) for i in chunk)
    return ("You are auditing written pieces for invented personal details, blind. Each piece was written for the person described, after they answered the assistant's questions. "
            "Their description plus their answers are EVERYTHING that is known about them.\n\n"
            "For each piece, list every statement it makes about the person, their life, family, work, company, colleagues, past attempts, habits, feelings or experiences that is supported by NEITHER the description NOR their answers. "
            "Quote the exact phrase from the piece. Count a detail as supported if it is stated in the description or the answers, or follows directly from them (for example, 700 days is about two years). "
            "Do not count: general advice, claims about people in general, rhetorical examples clearly framed as hypothetical, or the piece's structure and wording.\n\n"
            f"Reply with ONLY a JSON object covering pieces {ids}: {{\"<piece>\": {{\"invented\": [\"quoted phrase\", ...], \"count\": n}}, ...}}\n\n" + "\n\n".join(blocks))
for n, ch in enumerate([items[:12], items[12:]], 1):
    (R / f"audit2_{n}.txt").write_text(prompt(ch)); print(n, len((R / f"audit2_{n}.txt").read_text()))
