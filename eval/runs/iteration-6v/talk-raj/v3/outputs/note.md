## Angle

- **Angle:** Use assistants for a lot, as the standard advice says, but the half of that advice that decides whether it works is "review everything", and a QA lead is the person best placed to say what that half really costs and requires.
- **Built from:** 1a (your position matches the standard one, so the talk agrees with it rather than arguing against it), 4d (QA lead: the talk is told from the review and testing end, which is where you sit), 3a with some PMs (written for engineers, with one section aimed at PMs on planning), 5c (no policy ask; it ends on three questions for teams). 2d (keep it general) is why there are no stats or stories in it.
- **Strongest objection:** "Review everything" is just ordinary engineering. We review human-written code too, so a QA lead telling engineers to review their code is saying something they already know, and the talk could come across as QA asking for more process. An engineer might also say assistants make testing *easier*, since they write tests quickly.
- **Test:** Before Friday, check whether anything has actually changed on your side since assistants came into use: review turnaround, PR size, bugs found in QA versus in production, anything you can pull from your tracker. If something has moved, one sentence about it in section 2 answers the "nothing new" objection. If nothing has moved, keep the talk as it is, framed as "before this becomes a problem", and don't suggest it already is one. Section 3's point about the assistant writing both code and tests is your answer to "it makes testing easier"; make sure you're comfortable defending it in Q&A.
- **Other directions:**
  - A narrower talk entirely on tests: "If the AI writes the code and the tests, who decides what correct means?" Sharper and more specific to QA, but it covers less of the question you were given.
  - A practical version for engineers only: a short, concrete checklist for reviewing assistant-written code, dropping the PM section.

Because this is a talk, I would normally stop here and check the angle with you before writing it. You weren't available, so I went ahead. Redirect anything, or send me a line, an example or a different ending you'd like worked in.

## Before you use it

- **No figures or studies are cited**, so there's nothing to check. That's on purpose, since you asked to keep it general.
- **Confirm one small detail:** the opening says "I run QA" and "my team's day job." That assumes you lead a QA team. Adjust it if your role works differently, for example if QA is embedded in the engineering teams.
- **Real details you could add**, both optional:
  - In section 2, one real example from your own work, anonymised if needed: a change that looked clean and wasn't, or a set of generated tests that passed while missing the point. One sentence would do more than any industry stat.
  - In section 2 or the close, a single number if you have one (see the test above). One real figure from your own tracker would be the strongest line in the talk.

## Distance from the default

- **Speaker with a stake (4d):** the default speaks as a neutral observer. This one is told by the person whose job sits downstream of the code, and that's what the whole talk hangs on.
- **Focus (4d with 1a):** the default lists benefits and then risks such as security holes and made-up APIs. This one leaves the benefits list out and spends its time on the one part of the standard advice everyone agrees with but nobody spells out: what reviewing actually involves, including who owns the tests.
- **Audience (3a with some PMs):** it's still pitched at engineers, but it adds a section for PMs on planning ("count the checking, not just the writing"), which the default doesn't have.
- **Ending (5c):** instead of "use it wisely", it ends on three specific questions for teams to discuss, with no policy ask.
- **What did not move:** the position. Your answer to question 1 matches the standard advice, and with no case or number from question 2, the substance stays close to the default. What's new is the vantage point and the focus, not the claim. A real example or figure from your own work is what would move it further.
