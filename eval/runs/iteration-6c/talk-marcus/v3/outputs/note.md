**Angle:** The real risk isn't AI writing bad code. It's that we're losing the ability to debug without it. So keep the assistants for writing code, and have juniors do their first six months of debugging by hand, the way pilots log manual hours.

**Built from:** 1 (your own words: losing skills, not code quality; not anti-AI; the autopilot), 2 (engineers and the managers who train juniors, with others getting the gist), 3 (the 2am outage), 4 (staff engineer, on call, runs incident reviews), 5b plus your own words (the six-month no-assistant debugging rule).

**Strongest objection:** The jump from 38 to 61 minutes may not have much to do with assistants. Six months can also bring new services, new hires, a harder mix of incidents or fewer senior responders, and a median over a few dozen P2s can swing on a handful of bad nights. Someone in the room will probably say this. A related pushback from managers: six months of juniors debugging by hand costs time now, for a payoff you can't show yet.

**Test before Friday:** Split the P2s from both periods by who responded (their tenure, and if you can tell, whether they used an assistant) and by incident type, and count how many P2s are in each period. If the rise holds across incident types, or clusters among newer responders, say the number with confidence. If it doesn't, keep the number but make the incident-review pattern your main evidence, and present the number as what made you start looking. Section 3 is already written so it works either way.

**Other directions:**
- Make the change something you own outright: add one question to every incident review, "could the responder explain the fix without the assistant?", and report back next quarter.
- Lean into the tension in your answers: if engineers can't trace code they "supposedly wrote", the problem may start at writing, not debugging. That leads to a different rule: you have to be able to explain any AI-written code you submit for review.

*(For a talk, the skill would normally show you this block and wait for a go-ahead before writing. I wrote straight through, so if you want a different angle, a particular line or another ending, that's easy to change.)*

---

**Before you use it**

- **Ask the on-call engineer first.** Even told anonymously, people in an all-hands may know who was on call that night. The opening already says it isn't about blame, but get their okay.
- **Check the number's footing.** Confirm 38 and 61 are both medians, for P2s defined the same way, over the same six-month window. The "more than half" and "23 minutes" in section 3 come from your figures (61 − 38 = 23; 23/38 is about 60%).
- **Proposal or decision?** The outline says "the change, starting Monday." If engineering leadership hasn't agreed to it yet, say "what I'm asking for, starting Monday" so it doesn't land as a policy you can't enforce. Also decide who counts as junior, and whether current juniors' six months start Monday or from their hire date. Managers will ask.
- **Details that would make it stronger:**
  - What the cause actually was, in one plain sentence, right after "I read the log" in the opening or in section 1. People outside engineering will remember a concrete cause better than "I read the log."
  - In section 5, how juniors get help without the assistant, e.g. pairing with a senior on call. I left this out because you didn't say, but managers will want to know.
- **The aviation fact.** I kept the analogy to what you said (pilots train on manual flying). If you want an outside fact behind it, such as aviation regulators encouraging airlines to give pilots manual-flying practice, check it before you use it. I couldn't verify it, so it isn't in the text.

---

**Distance from the default**

- **Thesis:** the default's balanced "some things, not everything" became "that's the wrong question; the risk is losing the skill to debug." (Answer 1)
- **Evidence:** generic "X% faster" statistics were replaced by your P2 median (38 to 61 minutes) and the four-fixes outage. (Answers 1 and 3)
- **Speaker:** a neutral voice became a staff engineer who runs incident reviews and uses the tools himself, which is what keeps it from sounding anti-AI. (Answers 4 and 1)
- **Ending:** a list of do's and don'ts became one rule for juniors, aimed at the managers who'd adopt it. (Answers 5 and 2)
- **What didn't move:** it's still "use AI, with a limit." The writing-versus-debugging line is a cousin of the default's "good for boilerplate, bad for architecture" split, drawn somewhere else and backed by your own data. The audience also moved only a little, from engineers to engineers plus their managers. And the autopilot comparison is common in talks about AI, so some people will have heard it. Your incident-review details are what make it yours.
