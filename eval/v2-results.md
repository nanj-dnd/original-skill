# v2 check: does skipping the shortlist cost anything?

14 November 2026 · iteration 2 · same 8 personas with their same answers replayed through v2, plus 2 new vague personas

## Answer

**For users with specific answers, v2 gets the same result as v1 with one fewer turn.** The two versions reached the same main idea for 8 of 8 personas. Spread and fit were identical, and blog quality matched. Talk quality dipped slightly (4.8 to 4.2), partly because v1's pick step let users add tweaks, and partly because of a test-setup leak.

## Scores

| Task | Arm | Distinct ideas (of 4) | Same-idea score (lower = more spread) | Score vs plain | Fit | Quality | Embed within | Embed vs plain |
|---|---|---|---|---|---|---|---|---|
| talk | plain | 1 | 2.50 | — | 0.75 | 4.0 | 0.81 | — |
| talk | v1 | 4 | 0.00 | 0.69 | 1.00 | 4.8 | 0.56 | 0.60 |
| talk | v2 | 4 | 0.17 | 0.69 | 1.00 | 4.2 | 0.67 | 0.66 |
| blog | plain | 1 | 3.00 | — | 0.50 | 4.0 | 0.83 | — |
| blog | v1 | 4 | 0.17 | 0.75 | 1.00 | 4.8 | 0.51 | 0.63 |
| blog | v2 | 4 | 0.00 | 0.75 | 1.00 | 5.0 | 0.50 | 0.61 |

v1 vs v2 for the same persona: same idea and same choices for 6 of 8; same idea with different supporting choices for Priya and Sam.

## Why talk quality dipped

- **Marcus (5 → 4):** the v2 output mentions `route.md`, a file the test told it to write. This is a test-setup leak, not a skill problem.
- **Dana (4 → 4):** "thinner, leaves the key example to the user". v1 had the live vote and the "built day 1, done day 7" line, both of which Dana added when picking.
- **Sam (5 → 4):** "narrow focus". v1 had the stack-trace demo, which Sam added at pick time ("A with B's stack trace").

So the pick step does add something: it's a second, cheap moment for the user to contribute. v2 keeps a smaller version of it in the "Other directions" lines, which only help if the user replies.

## Routing (the new step 3)

| Persona | Answers | Expected | v2 | v2 with the tightened rule |
|---|---|---|---|---|
| 8 pilot personas | specific | direct | direct, 8/8 | — |
| Jo (talk) | letters, "not sure", no case | shortlist | shortlist ✓ | — |
| Max (blog) | letters, "not really", "friends I guess" | shortlist | **direct ✗** | shortlist ✓ |

v2 let picked options that differ from the default count as "a stated position". The fix: specifics must be in the user's own words and be something you couldn't have guessed, and a picked option counts as a direction, not a specific. That fix is in the shipped v2.

## Limits

Same as the pilot: 4 outputs per arm per task, one judge run, vivid model-written personas. Replaying the same answers isolates the skill change, but it means v2's questions weren't re-tested (they are unchanged from v1). Whether the shortlist actually improves outputs for vague users is still untested; this round only checked that they get routed to it.
