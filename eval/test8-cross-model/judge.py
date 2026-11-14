import json, random, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from bench import claude, TASK, EVAL
X = Path(__file__).parent; J = X / "judging"
items = json.loads((J / "items.json").read_text())
NAMES = ["priya", "marcus", "jo", "raj"]

def p_extract():
    body = "\n\n".join(f"=== ITEM {i['qid']} ===\n{i['piece']}" for i in sorted(items, key=lambda i: int(i['qid'])))
    return ("You are judging writing samples blind. Below are 24 items, each a response to this request:\n\n\"" + TASK + "\"\n\n"
            "For each item record:\n- main_claim: the central claim or angle in one sentence, in plain words, stripped of style\n"
            "- choices: 3 to 5 short phrases for the key content choices (main examples, structure, recommendations, who it's written for)\n"
            "- quality: 1 to 5. Would a reasonable person who asked for this be glad to use it as is (coherent, fits the request, no factual errors)? 3 = usable, 5 = excellent. Judge quality only, not originality.\n"
            "- quality_reason: one short line\n\n"
            "Reply with ONLY a JSON object: {\"<item number>\": {\"main_claim\": ..., \"choices\": [...], \"quality\": n, \"quality_reason\": ...}, ...} covering all 24 items.\n\n" + body)

def p_similarity(extract):
    sets = []
    for m in ["claude", "gemini"]:
        grp = sorted([i for i in items if i["model"] == m], key=lambda i: int(i["sim_id"][1:]))
        lines = "\n".join(f"{i['sim_id']}: claim: {extract[i['qid']]['main_claim']} | choices: {'; '.join(extract[i['qid']]['choices'])}" for i in grp)
        sets.append(f"SET {m[0].upper()} (12 summaries):\n{lines}")
    return ("You are judging how similar ideas are, blind. Below are two separate sets of 12 summaries (main claim + key choices) of responses to the same request. Compare items only WITHIN a set.\n\n"
            "For every pair of ids within each set (66 pairs per set, 132 total), score how similar the IDEAS are:\n"
            "3 = same main claim and mostly the same choices; 2 = same main claim, different choices; 1 = different main claim but overlapping choices; 0 = different main claim and different choices.\n"
            "Judge the idea, not the wording. Two pieces that both say \"use AI for boilerplate but review everything\" are the same idea even if phrased differently.\n\n"
            "Reply with ONLY a JSON object: {\"pairs\": [{\"a\": id, \"b\": id, \"score\": n}, ...]} with all 132 pairs.\n\n" + "\n\n".join(sets))

def fit_cases():
    rnd = random.Random(7)
    cases = []
    for i in items:
        if i["arm"] == "plain":
            continue
        decoy = rnd.choice([n for n in NAMES if n != i["who"]])
        pair = [i["who"], decoy]; rnd.shuffle(pair)
        cases.append({"qid": i["qid"], "A": pair[0], "B": pair[1], "truth": "A" if pair[0] == i["who"] else "B"})
    return cases

def p_fit(cases):
    card = lambda n: (EVAL / f"personas/talk-{n}.md").read_text().split("\n", 1)[1].strip()
    blocks = []
    for k, c in enumerate(cases, 1):
        it = next(i for i in items if i["qid"] == c["qid"])
        blocks.append(f"=== CASE {k} ===\nOUTPUT:\n{it['piece']}\n\nPERSON A:\n{card(c['A'])}\n\nPERSON B:\n{card(c['B'])}")
    return ("Below are 16 cases. Each holds one written output and two people (A and B) who might have asked for it. For each case, decide which person the output was more likely written for, "
            "based on whether it reflects that person's views, cases, numbers, audience and constraints. If nothing in it points to either, still pick one (your best guess).\n\n"
            "Reply with ONLY a JSON object: {\"<case number>\": \"A\" or \"B\", ...} covering all 16 cases.\n\n" + "\n\n".join(blocks))

def parse(t):
    m = re.search(r"\{.*\}", t, re.S)
    return json.loads(m.group(0))

if __name__ == "__main__":
    judge = sys.argv[1]  # 'claude' runs Opus; 'gemini-prompts' writes prompts for pasting
    cases = fit_cases(); (J / "fit_cases.json").write_text(json.dumps(cases, indent=1))
    if judge == "claude":
        ex = parse(claude(p_extract(), "opus")[0]); (J / "claude_extract.json").write_text(json.dumps(ex, indent=1))
        sim = parse(claude(p_similarity(ex), "opus")[0]); (J / "claude_similarity.json").write_text(json.dumps(sim, indent=1))
        fit = parse(claude(p_fit(cases), "opus")[0]); (J / "claude_fit.json").write_text(json.dumps(fit, indent=1))
        print("claude judge done", len(ex), len(sim["pairs"]), len(fit))
    elif judge == "gemini-extract":
        (J / "gemini_p_extract.txt").write_text(p_extract()); print(len(p_extract()))
    elif judge == "gemini-sim":
        ex = json.loads((J / "gemini_extract.json").read_text()); t = p_similarity(ex); (J / "gemini_p_sim.txt").write_text(t); print(len(t))
    elif judge == "gemini-fit":
        t = p_fit(cases); (J / "gemini_p_fit.txt").write_text(t); print(len(t))
