import json, sys
d = {k: {"invented": ["x"] * v} for k, v in json.loads(sys.argv[2]).items()}
json.dump(d, open(f"{sys.argv[3]}/gpt_audit{sys.argv[1]}.json", "w")); print(sys.argv[1], len(d))
