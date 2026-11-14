# Route

**Path: step 4 (build directly).** The answers are specific: a real incident (the 2am outage, four confident wrong fixes, cause found in about 10 minutes from the log), a number (median P2 time-to-resolve went from 38 to 61 minutes over six months), a named seat (staff engineer, on call, runs the incident reviews), a named audience (engineers and the managers who decide how juniors are trained) and one concrete ask (juniors debug without an assistant for their first six months). There's nothing to gain from a shortlist.

## Lines shown before the deliverable

**Angle:** "AI for everything?" is the wrong question. The line that matters is between writing code and debugging it. Keep the assistant for writing, but protect the skill of reading a failure yourself, the way pilots keep logging manual hours, because our incident data says that skill is going. Concretely, juniors debug without an assistant for their first six months.

**Built from:** 1 (the real question is skills, not quality, and "don't make me sound anti-AI"), 3 (the 2am outage), 4 (staff engineer who runs incident reviews, so it's said from the seat that sees the failures), 2 (spoken to engineers and the managers who set junior training, with a one-line gist for everyone else), 5 (one change, not a list of guidelines). The autopilot analogy is yours, from the note on 1.

**Strongest objection:** The jump from 38 to 61 minutes has other likely causes: more services, a harder mix of incidents, newer people on the rotation, or a change in what counts as a P2. The engineers in the room will think of these straight away. If the number doesn't hold up, the talk rests on one 2am story.

**Test:** Before Friday, check whether the P2 count and severity mix changed over those six months, and split the P2s by on-call tenure (or by whether an assistant was used during the incident, if that's recorded). If you can't separate it out, say so in the talk ("I can't prove the cause from this number alone; here's what I see in the reviews") rather than implying it.

**A tension worth using, not smoothing over:** what you see in reviews is *engineers* who can't follow a stack trace through code they wrote, not only juniors, but the rule covers only juniors. Someone will ask "what about the rest of us?" The outline has a line ready for that question. It answers it without adding a second ask.

**Other directions:**
- Make it about the on-call rotation rather than juniors: anyone who takes the pager does a regular debugging drill with no assistant, the way pilots practise hand-flying.
- Make it about the incident reviews: start recording in every P2 review whether an assistant was used and whether it helped, so in six months the argument rests on data instead of one 2am story.
