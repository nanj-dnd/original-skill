# Can We Still Hand-Fly? (5-minute all-hands talk)

About 650 spoken words in total, at around 130 words a minute.

## Outline

**1. The 2am outage (0:00–0:50)**
- Opening paragraph below. Four pastes, four fixes, all confident; about ten minutes with the log.
- Don't name the on-call engineer and don't make them the joke. The point is that most of us would have done the same thing.

**2. Where I'm standing (0:50–1:20)**
- Staff engineer, on the on-call rotation, and I run our incident reviews, so I see these afterwards, in detail.
- I use these tools myself, for writing code. This isn't an anti-AI talk.
- So "should we use it for everything?" is the wrong question. The useful line is between *writing* code and *debugging* it.

**3. What the reviews show (1:20–2:10)**
- Over the last six months, median time-to-resolve for P2 incidents went from 38 minutes to 61. That's 23 minutes, about 60% longer.
- For everyone outside engineering: that's the time a customer-facing problem stays open. Sales and support feel it before we do.
- In the reviews I keep seeing engineers who can't follow a stack trace through code they wrote themselves.
- Say plainly what the number does and doesn't prove (see the test in route.md). That earns you the room.

**4. Autopilot (2:10–3:00)**
- Autopilot is great, and pilots use it most of the time.
- They still train on manual flying and log the hours, because when the automation drops out, they have to be able to hand-fly.
- In our work, the automation drops out during an incident at 2am, when the assistant gives four confident answers and only one of them, or none, is right.

**5. The ask: one change, starting Monday (3:00–4:15)**
- For their first six months, juniors debug without an assistant. They keep using it to write code, just not to debug.
- It's the same idea as pilots logging manual hours before they rely on the automation.
- To the managers: you decide how juniors get trained, so this is yours to adopt. (Before Friday, decide who owns it, when it starts, and who juniors go to when they're stuck.)
- Ready for "what about the rest of us?": the reviews say it isn't only juniors. This is where we start because it's where the habit forms. It doesn't mean everyone else is fine.

**6. Close (4:15–5:00)**
- Back to the 2am log: the fix was in the log, and reading it took ten minutes.
- Last line, something like: "Use it to write. Make sure you can still fly without it."

## Opening paragraph

We had an outage at two in the morning. The engineer on call did what a lot of us would do: copied the error into the assistant. Then did it again. Four times, and four different fixes, each one stated with complete confidence. I opened the log and found the cause in about ten minutes. I'm not telling you this because I'm smarter than the assistant, and I'm not here to tell you to stop using it. I use it myself. I'm telling you because reading that log is a skill, and I think we're quietly losing it. I'm on the on-call rotation and I run our incident reviews, and over the last six months our median time to resolve a P2 has gone from 38 minutes to 61. So I don't want to argue about whether we should use AI for everything. I want to ask for one thing we shouldn't use it for yet.

---

*Details to check:* "did what a lot of us would do" and "copied" are my framing of the incident; you said "pasted the error into the assistant four times." I added "quietly losing it" and the closing line. The section timings and word count are estimates. I didn't add any aviation facts beyond what you said, and I'd keep it that way unless you can source them.
