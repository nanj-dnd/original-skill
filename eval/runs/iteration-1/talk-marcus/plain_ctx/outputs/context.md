QUESTIONS YOU WERE ASKED:
Reply like `1b 2a 3c 4b 5: <own words>`. Any answer can be your own words instead of a letter.

1. **Position.** The default says the balanced middle: "for some things, not everything." Where do you actually land?
   a) The balanced middle is right.
   b) Yes, for basically everything. AI-first should be the default, and humans should have to justify the exceptions.
   c) "Everything vs. not" is the wrong question. What matters is something else, like who's accountable for the code, what we measure or what we stop learning.
   d) Your own words.

2. **Who it's for.** The default talks to engineers. Who in that room do you most need to reach?
   a) The engineers.
   b) Everyone else (sales, support, ops, leadership) and what this means for them.
   c) The people who set policy or budget.
   d) Your own words.

3. **A real case.** Is there something concrete behind your view?
   a) An incident: AI-written code that caused a bug, an outage or a messy review.
   b) A win: something that shipped much faster or got built only because of an assistant.
   c) A number: adoption rate, PR volume, review time, cost or a survey.
   d) Nothing specific yet. Tell me in your own words if there is.

4. **Your seat.** The default speaker has no stake. Who are you in this?
   a) An engineer who uses these tools daily (or refuses to).
   b) An engineering lead or manager who has to answer for quality and output.
   c) Someone outside engineering, like an exec, product, design or ops.
   d) Your own words.

5. **What you want afterwards.** The default ends on a list of do's and don'ts. What should happen after Friday?
   a) A shared set of guidelines.
   b) One concrete change starting Monday, like a policy, an experiment or a rule.
   c) An argument the company keeps having: leave them with an open question.
   d) Your own words.

MY ANSWERS:
1c 2: Mostly the engineers and their managers. Sure, it's the whole company in the room, and sales and support should get the gist, but the people who actually have to change something are the engineers and the managers deciding how juniors get trained. 3a 4: Staff engineer. I'm on the on-call rotation and I run our incident reviews, so I'm the one who watches these incidents get picked apart afterwards. 5b

On 1, so it's clear: my worry isn't code quality. It's that we're losing skills. Over the last six months our median time-to-resolve for P2 incidents went from 38 to 61 minutes. In reviews I keep seeing engineers who can't follow a stack trace through code they supposedly wrote. I'm fine with assistants for writing new code, and I use them myself, so please don't make me sound like I'm against AI. Think of it like the autopilot in a plane. It's great, but you still have to be able to hand-fly when it drops out, and pilots still train on manual flying for that reason.

On 3: we had a 2am outage where the on-call engineer pasted the error into the assistant four times and got four different fixes, each one stated with total confidence. I found the cause in about 10 minutes just by reading the log.

On 5: the change I want is that juniors do their first six months of debugging without an assistant. They can still use it to write code, just not to debug. Same idea as pilots logging manual hours before they lean on the automation.