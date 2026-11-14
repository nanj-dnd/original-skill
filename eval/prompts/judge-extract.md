You are judging writing samples blind. In {DIR}/items/ there are 16 files, each a response to this request:

"{TASK}"

For each file, read it and record:
- main_claim: the central claim or angle in one sentence, in plain words, stripped of style
- choices: 3 to 5 short phrases for the key content choices (main examples, structure, recommendations, who it's written for)
- quality: 1 to 5. Would a reasonable person who asked for this be glad to use it (coherent, fits the request, no factual errors)? 3 = usable, 5 = excellent. Judge quality only, not originality.
- quality_reason: one short line

Write JSON to {DIR}/extract.json as {"<file id>": {"main_claim": ..., "choices": [...], "quality": n, "quality_reason": ...}, ...} using the number in the file name as id. Reply with just "done".
