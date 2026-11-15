import json, re, sys, html
src, dest, n = sys.argv[1], sys.argv[2], sys.argv[3]
BS = chr(92)
t = open(src).read()
t = html.unescape(t)
t = t.replace(BS + "\n", "\n")          # markdown line-break backslashes
t = t.replace(BS + "_", "_")            # escaped underscores
t = t.replace(BS + BS + '"', BS + '"')  # double-escaped quotes inside strings
d = json.loads(re.search(r"\{.*\}", t, re.S).group(0))
json.dump(d, open(dest, "w"), indent=1)
print(len(d), "of", n, "judgments")
