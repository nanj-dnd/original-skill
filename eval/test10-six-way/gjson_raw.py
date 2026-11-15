import json, re, sys, html
src, dest, n = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(src).read()
t = html.unescape(t).replace("\\\n", "\n").replace("\\_", "_")
d = json.loads(re.search(r"\{.*\}", t, re.S).group(0))
json.dump(d, open(dest, "w"), indent=1); print(len(d), "of", n, "judgments")
