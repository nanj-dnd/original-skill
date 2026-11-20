import json, sys
n, raw = sys.argv[1], sys.argv[2]
d = {k: {"prefer": v[0], "less_generic": v[1]} for k, v in json.loads(raw).items()}
json.dump(d, open(f"{sys.argv[3]}/gpt_hh{n}.json", "w")); print(n, len(d))
