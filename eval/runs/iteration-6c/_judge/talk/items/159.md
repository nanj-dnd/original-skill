# Who owns the line? (5-minute all-hands talk)

## Outline

About 700 words spoken in total. Timings are rough.

**1. The August migration (0:00 to 0:45)**
- Open with the story, not a statistic (opening paragraph below).
- Explain the constraint in plain words so sales, ops and compliance follow it: a rule that said a field could never be left empty.
- Land the turn: the person who merged it couldn't explain it.

**2. "For everything?" is the wrong question (0:45 to 1:30)**
- Say it straight: we are not banning these tools. They're fine, and they're staying.
- The question that matters is who is accountable for what ships.
- The rule: the author owns every line they merge, however it was written. "The AI wrote it" is never an answer in a postmortem.

**3. Where the cost actually went (1:30 to 2:45)**
- Writing code got cheap. Understanding it didn't.
- The numbers: PR volume is up about 60% since spring. Review time for each of our two senior engineers has gone from about 4 hours a week to about 11. That's roughly 14 extra hours a week between two people, close to two working days.
- The tension to say out loud: we say the author owns every line, but when the author doesn't understand the change, the reviewer becomes the only person who does. Ownership has been quietly moving from the person who merges to the two people who review.
- Line to keep: "The code got cheaper to write. It did not get cheaper to understand, and someone still has to."

**4. Why this is everyone's problem, not just engineering's (2:45 to 3:45)**
- Turn to the half of the room that isn't engineering: you live with the fallout when something breaks.
- August didn't show up as a bug. It showed up as a reconciliation mismatch, and it was three weeks before anyone could say why.
- So when engineering looks faster, part of that speed is a bill: paid in review hours now, or in weeks of tracing later.

**5. The ask (3:45 to 4:40)**
- To engineers: use AI for as much of the work as you like. If you merge it, you can explain it, line by line, to a reviewer or in a postmortem, exactly as if you'd typed it.
- To everyone else: when something breaks, don't ask whether AI wrote it. Ask who can explain it. There should always be a name, and it should be the person who merged it.
- From me, as the lead: my job is to stop the review bill landing on the same two people.

**6. Close (4:40 to 5:00)**
- Back to August: the next time something goes quietly wrong, the answer to "who can explain this?" should come in minutes, not three weeks, and it should come from the person whose name is on the change.

## Opening paragraph

In August, a change to one of our databases quietly removed a single rule: the one that said a particular field could never be left empty. Nobody noticed at the time. It surfaced later as a reconciliation mismatch, and it took us three weeks to trace it back to that change. When we got there, the engineer who had merged it couldn't explain what it did, because they hadn't really written it. An AI assistant had. So when people ask whether our engineers should be using AI for everything, my honest answer is that it's the wrong question. The tools are fine. The question is who owns the code once it's in, and right now that isn't always the person whose name is on it.
