# Route

**Path: step 4 (specific answers, build directly).** The answers carry concrete things the default didn't have: a named audience (tech division, about 80 people, mostly engineers plus some risk/compliance), a real recurring case (people almost pasting customer data or production logs into these tools, which compliance forbids), and a hard norm they want stated (no customer data, no production logs, in any external tool). Their position (1a) matches the default's middle, so I'm building from the specifics, not from a contrarian stance they don't hold.

Correction to the fixed parts: this is a tech-division meeting of about 80 people, not a company all-hands. Still 5 minutes, next Friday, outline plus opening paragraph.

## Lines shown before the deliverable

**Angle:** Which tasks you hand to an AI assistant is a judgment call, and mostly yours; what you hand it is not. The talk spends little time on the "for everything?" debate and spends its weight on the one line that isn't up for debate: no customer data, no production logs, in any external tool.

**Built from:** 1 (the middle is right, so the task question stays a judgment call), 2 (tech division with compliance people in the room, so the line can be stated with them present), 3 (speed vs quality frames the judgment part), 4 (the repeated near-misses are why the line needs saying out loud), 5 (about a minute that says "here is the line").

**Tension used:** your stated stake (3a: speed against quality) and your real case (4: data leaving the building) are different problems. The talk uses that gap as its turn: the speed/quality trade-off is negotiable and people will get it a bit wrong and recover; data exposure is not negotiable and can't be recovered.

**Strongest objection:** "Compliance already forbids this and everyone knows it, so why spend all-hands time on it?" The near-misses are the answer: people know the rule but not what counts. The minute has to name the forms it actually takes (a stack trace with a payload in it, a log excerpt, a screenshot, a test fixture copied from prod), or it will just repeat a rule people already think they follow.

**Test (do before Friday):** check the line word for word with your compliance folks, especially "any external tool." If the company has an approved, contracted assistant, ask whether it counts as external under the policy; your line must not contradict the tool people are told to use. Also check whether your assistant can read files or terminal output in the workspace on its own (agent-style tools often can): if so, data can leave without anyone pasting it, and the line should cover "letting it read" as well as "pasting."

**Other directions:**
- Make the near-misses the hook and the whole talk: a 5-minute data-hygiene talk that only touches the "for everything?" question in the last 30 seconds.
- Keep the talk on speed vs quality (3a) with a concrete review norm, and make the data line a short closing coda.
