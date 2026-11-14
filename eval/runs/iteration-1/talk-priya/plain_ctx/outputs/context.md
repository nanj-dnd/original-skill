QUESTIONS YOU WERE ASKED:
Reply like `1b 2a 3c 4b 5: <own words>`. Any answer can be in your own words.

**1. Your position.** The default lands in the middle: "not for everything, keep a human in the loop." Where are you?
- a) That middle position is basically right
- b) Yes, for everything: using it should be the default, and not using it is what needs a reason
- c) "Everything or not" is the wrong question. The real issue is something else (who's accountable, what we measure, what we're slowly losing)
- d) Your own words

**2. Who you're talking to.** The default talks to engineers. But at an all-hands, most of the room probably isn't engineering. Who is this talk really for?
- a) Engineers: it's about how they work
- b) Everyone else (sales, support, ops and so on): what it means for the product and work they depend on
- c) Leadership: there's a decision or budget question behind it
- d) Your own words

**3. What's at stake.** The default's main worry is code quality and risk. What do you think matters most here?
- a) Quality, bugs and security
- b) Engineers' skills and judgement, and how juniors learn
- c) Speed and cost: what we ship and how fast
- d) Your own words

**4. Where you stand.** The default speaker is a neutral explainer. What's your role, and what's your own experience with these tools?
- a) An engineer who uses them daily
- b) An engineering lead or manager watching a team use them
- c) Not an engineer: I see the results from outside
- d) Your own words (including how much you actually use them)

**5. A real case.** Is there something real behind this talk, at your company or from your own work?
- a) Something AI-written that broke, slipped through review, or cost us time
- b) Something it made much faster or possible, that we couldn't have done otherwise
- c) A live debate or decision here (a mandate, licences, a policy, a hiring question)
- d) Nothing specific, or your own words: the case in a sentence or two

MY ANSWERS:
1c: Not banning them, they're fine. The real issue is who's accountable: the author owns every line, and "the AI wrote it" is never an excuse in a postmortem. 2: Everyone. About half the room is sales, ops and compliance, and they live with the fallout when something breaks. 3: The cost moved from writing code to reviewing it, and it landed on my two seniors. PR volume is up ~60% since spring, and review time per senior went from ~4 to ~11 hours a week. 4b: I lead 7 engineers. 5a: In August an AI-generated DB migration quietly dropped a NOT NULL constraint. That caused a reconciliation mismatch that took three weeks to trace, and the engineer who merged it couldn't explain what the migration did.