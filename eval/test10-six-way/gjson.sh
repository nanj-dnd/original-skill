#!/bin/bash
# gjson.sh <dest.json> <expected-count>: parse JSON from the clipboard
X=$(dirname "$0"); LANG=en_US.UTF-8 pbpaste > "$1.raw"
python3 - "$1" "$2" <<'PY'
import json, re, sys
t = open(sys.argv[1] + ".raw").read()
d = json.loads(re.search(r"\{.*\}", t, re.S).group(0))
json.dump(d, open(sys.argv[1], "w"), indent=1)
print(len(d), "of", sys.argv[2], "judgments")
PY
