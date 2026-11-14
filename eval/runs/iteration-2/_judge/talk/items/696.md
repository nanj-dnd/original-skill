# "For everything?" Judgment and a rule

*Tech division all-hands, about 80 people (engineers plus risk and compliance). 5 minutes.*

## Opening paragraph

The question I was given is whether engineers should be using AI coding assistants for everything. My honest answer has two halves, and they're different kinds of answer. The first half is about which work you hand to these tools, and that's judgment. It's mostly yours, and I'm going to say less about it than you might expect. The second half is about what you put into them, and that isn't judgment. It's a rule. It isn't up to me or to you, and by the end of these five minutes I want everyone in this room to be able to say it back in one sentence.

## Outline

**0:00–0:40: Opening** (the paragraph above)
- Answer the title question by splitting it: "for everything" is a judgment call; "with everything" is not.

**0:40–1:50: Half one, judgment (which tasks)**
- Where I land: use it wherever you can check what it gives you. If you can't review it properly, you're not saving time, you're moving the cost into review and rework.
- You own what you ship, whoever typed it. "The assistant wrote it" is not an answer in a postmortem.
- That's most of the guidance on tasks. Keep it short on purpose: the point is that this half is yours.

**1:50–3:20: Half two, the rule (what goes in)**
- Say the rule plainly, on its own slide: **No customer data. No production logs. In any external tool. No exceptions.**
- The example: put one synthetic log line on screen, the kind you'd paste when debugging:
  `2026-11-12T02:14:07Z ERROR payment-svc charge failed user=jane.doe@example.com acct=88412093 ip=203.0.113.42 session=eyJhbGciOiJIUzI1NiJ9... card_last4=4242`
  - Point at each field: email, account ID, IP, session token, card digits. "This isn't a stack trace with some customer data in it. It *is* customer data, with a stack trace attached."
  - That's why the rule names logs and not just "customer data": logs are where it hides.
- Why it's a rule and not judgment: compliance forbids it. A vendor's "we don't train on your data" doesn't change that, and none of us gets to weigh those terms on our own.
- "Any external tool" means the chat window, IDE plugins, browser extensions, and personal accounts on a work laptop.

**3:20–4:20: What to do instead**
- Strip the identifying fields before you paste anything, or reproduce the bug with made-up data.
- [Confirm before Friday: is there an approved internal tool or redaction script? If so, name it here. If not, say who to ask, e.g. the incident channel or compliance.]
- Admit the cost: sometimes this will be slower, usually in the middle of an incident when slow hurts most. That's the price.
- We've had a few near misses: people about to paste and catching themselves. That's the rule working. Say it without names.

**4:20–5:00: Close**
- Repeat the two halves in one breath: which work you give it is your judgment; what you give it is a rule.
- End on the rule, word for word, so it's the last thing in the room: "No customer data, no production logs, in any external tool."

**Prep before Friday**
- Have compliance check the rule's exact wording, since some of them will be in the room.
- Build the synthetic log line from the fields a real service of yours actually logs, so engineers recognise it. Keep every value fake.
