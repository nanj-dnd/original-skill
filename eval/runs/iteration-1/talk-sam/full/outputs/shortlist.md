**Updated fixed parts:** 5 minutes, about 80 people in the tech division (mostly engineers, plus some risk and compliance staff), next Friday, about 1 minute of the 5 on the rule. The rule as you gave it: compliance forbids putting customer data or production logs into any external tool.

**Where you agree with the default:** you picked the middle position (1a) and speed against quality (3a), so on those two you agree with it. I'm not inventing a contrarian position. The ideas below come from what you added: the room, the near misses, and your hard line on data.

**The one thing banned:** the default's main claim, "AI is a powerful tool but not for everything: use it for the boring stuff, keep humans on the hard stuff."

## Candidates

1. **Judgment and rule.** Which tasks you use AI for is your judgment, and I'll mostly leave it to you. What you put into it is a rule, and it isn't up to any of us.
2. **The line is about data, not tasks.** "For everything?" asks which tasks to use AI on, but the line that matters is drawn around what goes into it.
3. **The most dangerous paste is a stack trace.** Engineers don't think of logs as customer data, but a typical prod log line carries emails, IDs, IPs and tokens.
4. **Draw the line for 2am.** A rule that only holds when you're calm doesn't hold. Write it for an incident at 2am, when pasting the log into a chatbot is the fastest fix.
5. **The near misses are the warning.** It has "almost" happened several times. This talk comes before the first real incident, and the people who caught themselves are the system working, not people to shame.
6. **"But the vendor doesn't train on our data."** Answer the room's best objection head on: the line doesn't depend on a vendor's terms, because compliance forbids it whatever those terms say.
7. **Rule first, permission after.** Open with the line in minute one, then spend the next four on how widely everything else is open.
8. **Admit the cost.** The line will sometimes slow you down. Say so plainly, and say what to do instead (redact, build a synthetic repro, ask).
9. **One line for two audiences.** Engineers and compliance staff hear the same sentence in the same room, so afterwards nobody can say "I didn't know that's what they meant."
10. **One repeatable sentence.** Boil the line down to something people can recite: "No customer data, no prod logs, no external tool, no exceptions."
11. **Unlikely: live spot-the-data.** Put a synthetic prod log on screen and give the room 10 seconds to find the customer data in it.
12. **Unlikely: hand the minute to compliance.** A risk or compliance person delivers the rule minute themselves.
13. **Unlikely: say outright that it's a safety briefing.** Answer "for everything?" in 30 seconds ("mostly up to you") and call the rest of the talk what it is.
14. **The temptation is the speed.** Pasting the log is tempting because it's the fastest way to debug, so the speed-against-quality tradeoff you care about is exactly where the line gets crossed.
15. **What "external" covers.** It's not only the chat window: IDE plugins, browser extensions, personal accounts on a work laptop. These are the pastes you don't notice.

## Cuts

- **2:** near-duplicate of 1; 1 says the same thing and also covers the task question.
- **10:** a technique rather than an angle. It goes into the deliverable whichever idea you pick.
- **12:** cut because you said you want to deliver the minute yourself.
- **13:** near-duplicate of 7 (both shrink the debate and put the rule up front).
- **14:** near-duplicate of 4 (both are about the temptation under time pressure).
- **6, 8, 9, 15:** strong, but each sits close to a shortlisted idea and can go inside it as a supporting beat (6 and 9 inside 1, 15 inside 3, 8 inside 4).
- **7:** survives, but it's a structure, so whichever idea you pick can use it.
- No prior-work search: this is a talk, so its value doesn't depend on being new to the world.

## Shortlist

**A. Judgment and rule.** Split AI use into two parts. Which tasks to use it for is judgment, and you trust the room with it. What goes into it is a rule: no customer data, no prod logs, any external tool, no exceptions. The title question then has a clean answer: "for everything" is your call; "with everything" is not.
- **Only yours because:** it puts your middle position on tasks (1a) next to your hard line on data (5b).
- **Strongest objection:** "judgment for everything else" may sound like a dodge to someone who wanted guidance on code quality.
- **Test:** after the talk, ask three people what the rule is. If they say the sentence back without "it depends", it worked.

**B. The most dangerous paste is a stack trace.** Build the talk around one surprise: engineers already know not to paste a customer table, but a prod log line often has emails, account IDs, IPs or session tokens in it. Show one (made-up) line and point at each piece.
- **Only yours because:** it uses your case (people nearly pasting prod logs, 4) and that your rule names logs specifically (5b).
- **Strongest objection:** if your logging is already well scrubbed, the example overstates the risk and engineers will notice.
- **Test:** before Friday, pull one real log line from a service you own and check what customer-identifying fields it actually has. Build the synthetic example to match.

**C. Draw the line for 2am.** The rule isn't for a calm afternoon. It's for the incident when you're tired, the log is right there, and the chatbot would solve it in 30 seconds. Name that moment, and give people the alternative before they're in it.
- **Only yours because:** it uses your speed-against-quality concern (3a) and the near misses (4), which most likely happened while people were debugging.
- **Strongest objection:** if there's no fast approved alternative, "don't do the fast thing" under pressure is a rule people will break.
- **Test:** does a quick way to redact or reproduce safely exist today? If not, name what people should do instead, even if it's "ask in the incident channel".

**D. Unlikely: live spot-the-data.** Spend about 60 seconds on an exercise. A synthetic prod log goes on screen, and the room gets 10 seconds to shout out the customer data. Then say the line. A rule people have just seen at work sticks better than one they've heard.
- **Only yours because:** it uses that your rule names logs (5b) and that compliance staff are in the room (2), who can confirm what counts.
- **Strongest objection:** live audience moments can fall flat in a 5-minute slot and eat the time.
- **Test:** try it on two colleagues this week. If they find most of the fields in 10 seconds, it works; if they stare blankly, keep it as a static slide.

**E. The near misses are the warning.** Open with "nothing has happened yet, and that's why I'm talking now." Say there have been several near misses, credit the people who caught themselves, and turn that catch into the rule for everyone.
- **Only yours because:** it uses your case (4), people *almost* pasting customer data or logs, and nothing big having happened.
- **Strongest objection:** mentioning near misses at all can make the people involved feel singled out, even without names.
- **Test:** check with compliance that you can mention the near misses in front of 80 people without identifying anyone.

**I recommend A.** It's the only one that answers the question in your title as well as delivering the rule. B or C fit inside it as the example for the rule minute.

**Which one do you want developed?** Reply with a letter. You can also combine them, like "A with B's stack trace".
