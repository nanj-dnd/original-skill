# Who's Flying the Plane? Talk outline (5 minutes)

**Core message:** AI assistants are great for writing code. Debugging is a skill you only keep by practicing it, so new engineers should build that skill before they hand it off.

**The ask:** Engineering managers change how juniors are onboarded and how debugging and on-call work, starting now. No new rule required.

Spoken pace is roughly 140 words a minute, so the whole talk is about 700 words.

---

## Opening paragraph (0:00–0:50)

> Not long ago I got pulled into an outage at two in the morning. By the time I joined, our on-call engineer had pasted the error into an AI assistant four times and gotten four different fixes, every one of them completely confident. Four answers to one problem. I opened the log, read it, and found the cause in about ten minutes. That's not a hero story. I didn't do anything clever. I just read what the system was telling us. That's a skill, and I think we're slowly losing it. So let me be clear up front: I use these tools every day, and for writing new code I think they're a clear win. This talk isn't about *whether* we use them. It's about what we stop practicing when we use them for everything.

---

## 1. Where I stand (0:50–1:20, about 70 words)

- Say who you are in one line: staff engineer, on the on-call rotation, and you run incident review. That's why you see this pattern.
- Head off the "luddite" reading right away: "I'm not here to take anyone's tools away."
- Name the concern: **skill atrophy, not code quality.** The code the assistants write is mostly fine. The problem is what happens to us when it breaks.

## 2. What I'm seeing (1:20–2:20, about 140 words)

- Incident reviews keep showing the same thing: engineers who can't follow a stack trace through code they supposedly wrote.
  - One line for the non-engineers: "A stack trace is the system's own account of what broke and where. It's the black box recorder."
- **Slide: P2 median time-to-resolve, 38 min → 61 min over six months.**
  - Say the caveat yourself, before anyone else can: "I'm not claiming the assistants are the only cause. But the timing lines up with what I see in the reviews."
  - Put it in terms the whole room feels: 23 more minutes per incident is 23 more minutes of shipments, customers and ops teams waiting on us.

## 3. Why debugging is different (2:20–3:20, about 140 words)

- Writing code: you ask, you get a draft, and you judge it. Your skill is in the loop the whole time.
- Debugging: the assistant can only guess, and it guesses confidently. If you can't read the log yourself, you have no way to tell which of the four fixes is right. So you paste it in a fifth time.
- **The aviation line (use it here):** "Pilots have very good autopilots, and they still train on manual flying and hand-fly approaches. That's because the autopilot is great right up until it disconnects at the worst possible moment. Then you need someone in the seat who can actually fly the plane."
- 2am incidents are exactly when the autopilot disconnects.

## 4. The line I'd draw (3:20–4:20, about 140 words)

- **Junior engineers do their first six months of debugging without an assistant.** They can still write code with one. This applies to debugging only.
- What it isn't: a ban, or a rule for senior engineers, or a judgment on anyone who's used the tools so far.
- What it looks like in practice, for managers (suggestions to adapt):
  - **Onboarding:** pair juniors with a senior engineer on real bugs, with the log open and no assistant.
  - **On-call shadowing:** read the logs and form a guess before reaching for any tool.
  - **Incident review:** I'll start asking one new question in every review: "What was the system telling us, and when did we first read it?"

## 5. Close (4:20–5:00, about 90 words)

- Speak directly to the managers: "I'd much rather you leave here agreeing with this than have a policy land on your team. If it becomes a rule later, fine, but I want to start with you."
- Come back to the opening: the 2am fix took ten minutes, not because of anything special, but because someone had practiced reading the log.
- Last line: "Use the autopilot. Just make sure everyone on your team can still fly the plane."
