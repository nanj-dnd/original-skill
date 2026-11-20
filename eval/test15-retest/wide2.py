"""Wider test. python3 wide.py plain|turn1|ppl_prompts|ppl_load|turn2|check|strip"""
import json, sys, re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(Path(__file__).parent))
from bench import claude, EVAL
X = Path(__file__).parent; W = X / "wide2"; W.mkdir(exist_ok=True)
TASKS = {"email": "Write me a short cold email to the head of operations at a mid-size logistics company, pitching our route-optimisation software.",
         "linkedin": "Write me a LinkedIn post about what I learned in my first year as a manager.",
         "essay": "Give me a thesis and an outline for a 1,500-word essay on whether social media has been good or bad for democracy.",
         "hackathon": "Suggest a product idea for our weekend hackathon. The theme is climate. Give me the idea, what we'd build, and a demo plan."}
WHO = {"email": ["neha", "dev", "ollie"], "linkedin": ["kofi", "mei", "jordan"], "essay": ["arjun", "clara", "ben"], "hackathon": ["fatima", "luca", "wen"]}
PREFIX = {"email": "email", "linkedin": "linkedin", "essay": "essay", "hackathon": "hack"}
ARMS = {"v6": 2, "v5": 1, "asks": 1}
BODY = {"v6": "skill_body6.md", "v5": "skill_body5.md"}
ASKS = "Before you write anything, ask me whatever clarifying questions would help you do this well. Just ask the questions now; I'll answer, then you write.\n\n"
STATE = W / "state.json"
import os; CM = os.environ.get("CHECK_MODEL", "opus")
def st(): return json.loads(STATE.read_text()) if STATE.exists() else {}
def save(s): STATE.write_text(json.dumps(s, indent=1))
def runs(): return [(t, w, a, r) for t in TASKS for w in WHO[t] for a, n in ARMS.items() for r in range(1, n + 1)]
def key(t, w, a, r): return f"{t}/{w}/{a}{r}"
def d(k): p = W / k; p.mkdir(parents=True, exist_ok=True); return p
def card(t, w): return (EVAL / f"personas/{PREFIX[t]}-{w}.md").read_text().split("\n", 1)[1].strip()
def samples(t, ks=(1, 2, 3)): return "\n\n".join(f"--- PLAIN SAMPLE {k} ---\n" + (W / f"plain/{t}/run{k}.md").read_text().strip() for k in ks)
def plain():
    jobs = [(t, k) for t in TASKS for k in range(1, 7)]
    def one(j):
        t, k = j; p = d(f"plain/{t}") / f"run{k}.md"
        if not p.exists(): p.write_text(claude(TASKS[t], "opus")[0])
        return j
    with ThreadPoolExecutor(8) as ex: print(list(ex.map(one, jobs)))
def turn1():
    s = st()
    def one(j):
        t, w, a, r = j; k = key(*j)
        if k in s: return k
        first = ASKS + TASKS[t] if a == "asks" else "Follow these instructions for my task.\n\n--- INSTRUCTIONS ---\n" + (X / BODY[a]).read_text() + "\n--- END INSTRUCTIONS ---\n\nMy task: " + TASKS[t]
        q, sid, _ = claude(first, "opus"); (d(k) / "questions.md").write_text(q)
        return k, sid
    with ThreadPoolExecutor(8) as ex:
        for res in ex.map(one, runs()):
            if isinstance(res, tuple): s[res[0]] = {"sid": res[1]}; save(s); print(res[0], flush=True)
def ppl_prompts(per=12):
    tmpl = (EVAL / "prompts/persona.md").read_text().split("--- CHARACTER CARD ---")[0].strip()
    ks = [key(*j) for j in runs()]
    chunks = [ks[i:i + per] for i in range(0, len(ks), per)]
    for n, ch in enumerate(chunks, 1):
        cases = "\n\n".join(f"=== CASE {k} ===\nCHARACTER CARD:\n{card(*k.split('/')[:2])}\n\nTHE ASSISTANT'S MESSAGE TO THIS PERSON:\n{(W / k / 'questions.md').read_text().strip()}" for k in ch)
        head = ("Below are several separate role-play cases from a user test. In each case, play the person on the character card, replying to the assistant's message. Treat every case independently.\n\n"
                + tmpl.replace("Your character card is below. Stay in character.", "Stay in character.") +
                f"\n\nReply with ONE JSON code block and nothing else: an object mapping each case id to the person's reply as a string, covering these {len(ch)} cases: {', '.join(ch)}.\n\n")
        (W / f"ppl{n}.txt").write_text(head + cases)
    print(len(chunks), "prompts", [len((W / f'ppl{n}.txt').read_text()) for n in range(1, len(chunks) + 1)])
def ppl_load():
    s = st(); got = 0
    for f in sorted(W.glob("ppl*.json")):
        for k, v in json.loads(f.read_text()).items():
            if k in s: (W / k / "answers.md").write_text(v.strip()); got += 1
    print(got, "answers loaded of", len(s))
def turn2():
    s = st()
    def one(k):
        if (W / k / "deliverable.md").exists(): return None
        t = k.split("/")[0]; a = k.split("/")[2][:-1]
        msg = (W / k / "answers.md").read_text()
        if a in ("v5", "v6"): msg += "\n\n[The sampling step returned these three plain answers to the same task. The user has not seen them.]\n\n" + samples(t)
        out, _, _ = claude(msg, "opus", resume=s[k]["sid"]); (W / k / "deliverable.md").write_text(out); return k
    with ThreadPoolExecutor(8) as ex:
        for r in ex.map(one, list(s)): r and print(r, flush=True)
CHECK = ("You are checking a piece of writing for details about the user that their material does not support. Below are everything the user told the assistant, and the assistant's response containing the piece.\n\n"
         "List every statement the piece makes about the user (their life, work, past, habits, feelings, numbers, quotes, what they do or believe) that the material does not support, quoting each phrase exactly. General claims about people and advice don't count. "
         "Reply with the list only, one quoted phrase per line, or the single word NONE.\n\n--- WHAT THE USER TOLD THE ASSISTANT ---\nTheir task: {task}\n\nTheir answers to its questions:\n{ans}\n\n--- THE RESPONSE ---\n{piece}")
def check():
    s = st()
    def one(k):
        if not k.split("/")[2][:2] in ("v5", "v6") or (W / k / "final.md").exists(): return None
        t = k.split("/")[0]
        lst = claude(CHECK.format(task=TASKS[t], ans=(W / k / "answers.md").read_text(), piece=(W / k / "deliverable.md").read_text()), CM)[0].strip()
        (W / k / "checker.md").write_text(lst)
        if lst.upper().startswith("NONE"):
            (W / k / "final.md").write_text((W / k / "deliverable.md").read_text()); return k + " none"
        out, _, _ = claude("[The fresh reader's list of phrases about the user that your material does not support:]\n" + lst + "\n\nFix or cut each one, unless you can name the answer that supports it, and give the full response again.", CM, resume=s[k]["sid"])
        (W / k / "final.md").write_text(out); return k + f" fixed {len(lst.splitlines())}"
    with ThreadPoolExecutor(8) as ex:
        for r in ex.map(one, list(s)): r and print(r, flush=True)
if __name__ == "__main__":
    globals()[sys.argv[1]]()
