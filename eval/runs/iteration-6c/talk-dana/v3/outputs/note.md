## Angle

- **Angle:** The "for everything?" question is settled here; what AI changed is the job itself. Code is now the cheap part, and deciding what "correct" means (specs and tests) is the engineering, which is why "built in a day" still means "ships in a week," and why the people in sales and support are the best source of the cases we miss.
- **Built from:** 1 (question settled, the job changed, spec and tests are the engineering), 2b (7 of 12 are non-engineers; explain the day vs. week gap), 3 (CTO and cofounder, so you can say "this is how we work" without hedging), 4 (calendar sync: 140 tests, one day, six more days on recurring events across time zones), 5a (no policy debate needed). Plus your "fun and short" note for tone.
- **Strongest objection:** The calendar story can be read the other way. If an engineer had written that code by hand, the slow work of writing it might have forced them through the recurring-event and time-zone cases, and the gap would have shown up on day one instead of day two. In that reading, AI didn't just make code cheap; it removed the friction that used to catch spec gaps, and the extra six days are partly a cost of AI-first, not proof that the spec was always the real job.
- **Test:** Before Friday, ask whoever built calendar sync: would writing it by hand have surfaced the time-zone problem sooner? If yes, say so in section 3 in one line ("we used to trip over these while writing the code; now we have to go looking for them on purpose"). That makes the talk stronger and makes the ask in section 4 more urgent. If no, the story stands as written.
- **Other directions:**
  - Talk to your cofounder and the commercial side about estimates: a five-minute "how to read an engineering timeline now" talk, with calendar sync as the worked example.
  - Lead with the objection: "AI removed the friction that used to find our bugs, so here's what replaces it," with test 141 as the new process rather than a metaphor.

(This is a talk, so the skill would normally stop here and check the angle with you before writing. You weren't available, so I went ahead. Redirect freely.)

## Before you use it

- **Confirm the numbers as spoken:** the opening says calendar sync "also took seven" days (one day plus the six you mentioned) and "last month." Check both still hold on Friday.
- **"Test 141" is a framing device.** The real gap may have been several missing tests, not one. That's fine for the close, but if an engineer in the room would correct you, say "test 141 and friends" or "the tests we didn't write."
- **"We wrote 140 tests":** I used "we" throughout. If one engineer did it, naming them in section 2 is a free laugh and a credit.
- **Two real details that would make section 2 land with non-engineers:**
  - What actually went wrong, in customer terms. For example, what someone saw on their calendar when it broke. Say it in one plain sentence right after "meetings that repeat every week."
  - Who found it. If a customer or someone in support spotted it, say so. It turns section 4's ask ("bring us the weird cases") from advice into something that already happened.
- **Length:** the outline is timed for about 700 words. If you run long, cut the middle point of section 4 ("a spec argument is good news") first; the other two carry the ask.

## Distance from the default

- **Thesis:** the default hedges ("not for everything, use judgement"). This one starts from your answer that the question is settled and changes the subject to how the job changed (answer 1).
- **Audience:** the default talks to engineers. This one translates engineering for sales, support and your cofounder, and ends with something they can do (answer 2b).
- **Example:** the default uses generic boilerplate wins and hallucinated APIs plus an industry stat. This one runs on your calendar sync story and its 140 tests / 1 day / 6 days (answer 4), and uses no outside statistics.
- **Structure:** the default goes pros, cons, guidelines. This one is one story, one idea, three translations, and a callback close (answers 4 and 2b, plus your "fun and short").
- **Speaker:** the default speaker is neutral. This one speaks as the person who sets how the company works, so it states things instead of proposing them (answers 3 and 5a).
- **What didn't move:** the underlying point that humans still own judgement is close to the default's "keep humans in charge." It's reframed as "deciding what correct means is the job," but a skeptic would recognise it.
