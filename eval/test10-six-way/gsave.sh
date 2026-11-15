#!/bin/bash
# gsave.sh <dest> [prev-file]: save the clipboard as UTF-8, refuse if it equals prev-file
dest="$1"; prev="$2"; mkdir -p "$(dirname "$dest")"
LANG=en_US.UTF-8 pbpaste > "$dest"
if [ -n "$prev" ] && cmp -s "$dest" "$prev"; then echo "STALE (clipboard unchanged)"; exit 1; fi
echo "saved $(wc -c < "$dest") chars: $(head -c 90 "$dest" | tr '\n' ' ')"
