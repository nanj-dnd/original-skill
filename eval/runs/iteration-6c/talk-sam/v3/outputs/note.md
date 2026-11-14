**Angle:** How much to lean on AI assistants is a judgment call about speed against quality, and it should stay one; what goes *into* them isn't: no customer data and no production logs in any external tool.

**Built from:** 1a (the middle is right, so the talk doesn't fake a contrarian stance on usage), 2 (tech division of about 80, mostly engineers, with risk and compliance people in the room), 3a (speed against quality is the frame for the judgment part), 4 (the repeated near-misses with customer data and prod logs), 5b (a minute that states the line plainly).

**Where the answers pull against each other:** 3a says the question is speed against quality, but the case in 4 is about data leaving the building, which speed against quality doesn't touch. The talk uses that gap as its turn: the speed pressure from 3a is exactly what produces the near-misses in 4, so the judgment part sets up why the bright line has to be a rule and not a judgment.

**Strongest objection:** A blanket "any external tool" rule gets broken in the middle of an incident, when it matters most, unless there's a sanctioned way to get help with real logs; and if the company has an approved or contracted assistant, "any external tool" may not match what the policy actually says, which the compliance people in the room will notice.

**Test:** Before Friday, check the exact wording of the compliance rule with the risk and compliance folks: does it say "external", does any approved AI tool exist, and do scrubbed or anonymized logs count? The line you say on stage should match the policy word for word.

**Other directions:**
- Drop section 2 almost entirely and spend four minutes on the near-misses: the moment it happens, why it's tempting, the line.
- Pair the ban with a safe path (an approved tool, or a shared habit of building synthetic examples), so the talk adopts a norm and also removes the reason people reach for real data.

*(For a talk, this block would normally go to you first for a go-ahead or anything you want worked in. That step was skipped for this run, so the outline and opening were written straight from it.)*

## Before you use it

- No figures or studies are cited, so there's nothing to check there. The default's "X% faster" stat was left out on purpose.
- The opening says "we've come close to getting it wrong more than once." That rests on your "people keep almost pasting"; confirm it's fair to say out loud to this group.
- Section 4 says "if you're not sure, ask first" without naming who. Add the person or channel to ask (possibly one of the compliance folks who'll be in the room), so the ask has somewhere to go.
- Section 3 is stronger with one real near-miss, described without names: what was almost pasted and in what situation. The outline holds without it.
- Section 2 is stronger with one example from your own team of AI saving time or costing it.
- Whether scrubbed or anonymized logs are allowed is a policy question. The talk as written says "no production logs" with no exceptions, which matches what you asked for.

## Distance from the default

- **Audience:** written for a tech division of about 80, mostly engineers with risk and compliance present, not a whole company (answer 2). That's why section 2 can stay short: this room already has the speed and quality evidence.
- **The case:** the center of the talk is what people put into these tools (customer data, prod logs), which the default left out entirely. Its risks were about the code coming out (answer 4).
- **The ending:** a single line said twice, word for word, instead of "use it wisely" (answer 5b).
- **The link:** speed against quality isn't a separate section listing pros and cons. It's the reason the near-misses happen (answers 3a and 4 together).
- **What didn't move:** the position on usage is still the default's middle ("some yes, some no, use judgment"), because that's what you chose (1a), and section 2 is close to the default's benefits and risks list, kept to about a minute. The difference is in what the talk is for, not in its stance on AI.
