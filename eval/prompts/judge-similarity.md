You are judging how similar ideas are, blind. Read {DIR}/extract.json: 16 summaries (main claim + key choices) of responses to the same request. Ignore the quality fields; don't open any other files.

1. For every pair of ids (120 pairs), score how similar the IDEAS are:
   3 = same main claim and mostly the same choices; 2 = same main claim, different choices; 1 = different main claim but overlapping choices; 0 = different main claim and different choices.
   Judge the idea, not the wording. Two pieces that both say "use AI for boilerplate but review everything" are the same idea even if phrased differently.
2. Group the 16 into clusters where each cluster shares one main claim. Every id goes in exactly one cluster.

Write JSON to {DIR}/similarity.json as {"pairs": [{"a": id, "b": id, "score": n}, ...], "clusters": [[id, ...], ...]} with ids as strings. Reply with just "done".
