import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from score2 import card
from h2h import TASKS
R = Path(__file__).parent / "rerun"
items = json.loads((R / "items.json").read_text())
def prompt(chunk):
    blocks = [f"=== PIECE {i['id']} ===\nTHE PERSON (everything known about them):\n{card(i['task'], i['who'])}\n\nTHE PIECE:\n{i['piece']}" for i in chunk]
    ids = ", ".join(str(i["id"]) for i in chunk)
    return ("You are auditing written pieces for invented personal details, blind. Each piece was written for the person described. The description is EVERYTHING that is known about them.\n\n"
            "For each piece, list every statement it makes about the person, their life, family, work, company, colleagues, past attempts, habits, feelings or experiences that is NOT supported by the description. "
            "Quote the exact phrase from the piece. Count a detail as supported if it is stated in the description or follows directly from it (for example, 700 days is about two years). "
            "Do not count: general advice, claims about people in general, rhetorical examples clearly framed as hypothetical, or the piece's structure and wording.\n\n"
            f"Reply with ONLY a JSON object covering pieces {ids}: {{\"<piece>\": {{\"invented\": [\"quoted phrase\", ...], \"count\": n}}, ...}}\n\n" + "\n\n".join(blocks))
for n, ch in enumerate([items[:12], items[12:]], 1):
    (R / f"audit{n}.txt").write_text(prompt(ch)); print(n, len((R / f"audit{n}.txt").read_text()))
