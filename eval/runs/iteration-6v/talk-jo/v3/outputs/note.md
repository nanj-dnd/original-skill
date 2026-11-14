## Angle

- **Angle**: "For everything?" is the wrong question. An ordinary user's honest answer is "it's fine", and the useful rule is to use it where checking the output is cheaper than writing it, which each engineer can test on their own work in a week.
- **Built from**: 1 (the balanced middle, kept, not turned contrarian), 3 (speaking to engineers about their daily work), 4 (people try something next week: the two-swap experiment), 5 (backend engineer, two years, got volunteered, uses Copilot sometimes, "it's fine": this sets the speaker's stance and the opening). 2 gave no case, so the talk uses no incident and no industry stat.
- **Strongest objection**: a week of self-reported impressions is weak evidence. People are bad at judging their own speed, and "did I trust it" isn't "was it right". An engineer could finish the week more confident and no more accurate. A manager might also say a personal experiment dodges the question the company actually asked, which was whether there should be a norm.
- **Test**: before Friday, check what the company already allows: which assistants are approved and what code may go into them. If there's a policy, the experiment has to sit inside it (section 4 assumes so). If there isn't one, expect the first audience question to be "are we even allowed to?", and have an answer ready.
- **Other directions**: (1) Make it about juniors and skill growth: what "for everything" does to people who are still learning the codebase. (2) Propose one team norm instead of an experiment, such as noting in the PR when a change was mostly written by an assistant, so reviewers know where to look harder.

Normally I'd stop here for a go-ahead before writing a talk. I went ahead so you have something to react to. Tell me if you want a line, an example or a different ending worked in.

## Before you use it

- No figures or studies are cited, so nothing needs checking there. If you want one number to back up the "write it down" step, there's a 2025 study I recall in which experienced developers believed AI tools made them faster when they had actually been slower. I couldn't check it, so look it up before you use it.
- Small things I added that you should confirm: the cheap-to-check and expensive-to-check examples in section 2 (serializers and fixtures against retry loops, migrations, auth, money). Swap them for the kinds of task your team actually works on. The line "I suspect it's where a lot of us are" is a guess about the room. Keep it only if it feels true to you.
- Real details that would strengthen it: in section 3, one ordinary moment from your own Copilot use, when it was fine and when it was mildly annoying. Nothing dramatic is needed. That's the point of the section. In section 5, if you're willing to collect people's three-line notes and share what came back, saying so gives the talk a follow-up and a reason to do the experiment.

## Distance from the default

- **The speaker's stance**: the default could be given by anyone. This one is given by a moderate user who got volunteered and calls the tool "fine", and that becomes the hook and the frame (answer 5).
- **The ending**: the default closes on "use it wisely". This closes on a specific one-week, two-swap experiment with a three-line note (answer 4).
- **Examples**: no industry stat and no generic hallucination story. The talk says plainly that there's no dramatic story, and makes that part of the argument (answer 2).
- **Structure**: the pros, cons and guidelines are replaced by a single working rule (cheaper to check than to write) that the audience then tests. This comes from pairing answer 1's middle position with answer 3's engineers-at-work audience.
- **What did not move**: the position is still the default's balanced "a lot, not everything", and the audience is still engineers. Your answers were thin on specifics, so the claim stays close to the default. What changed is who is saying it, the rule it rests on, and what it asks people to do.
