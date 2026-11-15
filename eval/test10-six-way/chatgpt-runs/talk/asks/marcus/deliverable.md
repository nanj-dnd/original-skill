I think the strongest version of this talk is built around one distinction:

**We should automate the work, not outsource the understanding.**

That lets you make a case for AI adoption while challenging the assumption that more AI usage automatically makes an engineering organisation better.

Your aviation analogy is particularly strong because it reframes manual debugging as a form of operational resilience, not resistance to technological progress.

I'd also make one important distinction throughout: you're not arguing that engineers need to write every line of code themselves. You're arguing that they need to retain the ability to understand, diagnose and recover the systems they are responsible for.

## **Proposed five-minute talk**

**Working title: "The Skill We Can't Afford to Lose"**

Audience: 300-person company all-hands · Delivery: thoughtful, persuasive, slightly provocative · Central ask: six months of assistant-free debugging for junior engineers

# The Skill We Can't Afford to Lose

*Five-minute all-hands talk*

## 1. The opening: AI is genuinely making us better (0:00–0:45)

**Opening paragraph:**

I want to start by saying something that might sound contradictory given the title of this talk: I think AI coding assistants are one of the best things to happen to engineering in years. I use them myself. They help us move faster, explore ideas we might otherwise not have had time to explore, and take care of work that doesn't necessarily require our deepest attention. And in a business like ours, where the systems we build determine whether trucks move, whether deliveries happen and whether customers can trust us, that kind of leverage matters. But I think there's a question we're not asking enough: as we get better at making machines do the work, are we getting worse at understanding the work ourselves?

## 2. What we're getting right, and what we might be losing (0:45–1:30)

Acknowledge the genuine benefits:

- Faster development and prototyping.
- Less time spent on repetitive coding.
- More room to focus on architecture and higher-value problems.
- Better leverage for engineers across the organisation.

Then introduce the distinction:

There is a difference between being able to produce code and being able to understand a system.

AI can help us produce code. But when something breaks at 2am, we need engineers who understand what they're looking at.

Our responsibility isn't just to ship features. It's to keep the business running.

## 3. The signal we're seeing (1:30–2:30)

Bring in the data:

Over the last six months, our median time-to-resolve for P2 incidents has increased from 38 minutes to 61 minutes.

That's a roughly 61% increase.

Be careful not to claim AI caused this. There could be multiple contributing factors. But it is a signal worth investigating.

Then share what you're seeing in incident reviews:

- Engineers struggling to read stack traces.
- Difficulty tracing an error through code they helped write.
- Less confidence in reasoning through a problem without immediately asking an assistant.

The important point:

This isn't about engineers being less capable. It's about the habits we're building as an organisation.

## 4. The 2am incident (2:30–3:30)

Tell the story without identifying the engineer.

One night, we had an outage. The on-call engineer was trying to resolve it and did what many of us would instinctively do: pasted the error into an AI assistant.

Four times.

Four different answers. Four confident suggested fixes.

Meanwhile, the actual problem was sitting in the logs. It took roughly ten minutes of reading through them to identify what was happening.

The lesson isn't that the engineer shouldn't have used AI. The lesson is that when the tool couldn't reliably diagnose the issue, we needed someone who could reason independently.

**The dangerous situation isn't an AI giving us a wrong answer. It's an engineer not knowing how to recognise that the answer is wrong.**

## 5. The aviation analogy (3:30–4:15)

Think about commercial aviation.

Modern aircraft have extraordinarily sophisticated autopilot systems. Pilots don't spend every flight manually controlling every aspect of the aircraft.

But pilots still train to fly manually.

Why?

Because automation handles the routine. Human skill matters when the routine breaks down.

You don't learn to hand-fly a plane because you expect to do it every day. You learn because when automation hands you a mess at the worst possible moment, you need to know how to fly.

Engineering is no different.

AI should be our autopilot, not our replacement for understanding how to fly.

## 6. The concrete ask (4:15–4:45)

Here's what I'd like us to consider:

For the first six months of a junior engineer's career, let them use AI to write code, explore solutions and accelerate development.

But ask them to debug without an AI assistant.

Let them read the logs, trace the stack, understand the failure and explain the root cause themselves before turning to an assistant.

Managers should support this as a deliberate training practice, not treat it as a productivity penalty.

This isn't about making people slower. It's about building the foundational skills that make them effective when things go wrong.

## 7. Closing (4:45–5:00)

I don't want us to become an organisation that is slower because it refuses to use AI.

I want us to become an organisation that can move faster because it knows when to use AI, when to question it, and when it needs a human who genuinely understands the system.

**Let's make sure we're building engineers who can use the autopilot, but can still fly the plane.**

## **A few strategic recommendations before you deliver it**

There are three things I'd be particularly deliberate about.

**1. Don't let the incident become an anti-AI anecdote.**

The engineer did something entirely understandable. In fact, that's what makes the story useful. The failure wasn't using AI; it was having no reliable fallback when AI couldn't diagnose the problem.

**2. Be intellectually honest about the incident data.**

Your P2 resolution time going from 38 to 61 minutes is a compelling statistic. But don't suggest AI adoption caused that increase unless you have evidence. Say it's a worrying trend that raises questions about our debugging capabilities. That makes your argument much harder to dismiss.

**3. Make the six-month proposal a training standard, not a restriction.**

This is probably the most important political distinction.

You're not asking management to ban AI for juniors. You're asking them to deliberately preserve a core engineering competency during the period when foundational skills are being developed.

One possible refinement: have juniors attempt the initial diagnosis independently, document their reasoning and then use AI to challenge or validate their conclusions. This could be a natural progression after the initial training period.

## **One line I'd make sure people remember**

# **"The dangerous situation isn't an AI giving us a wrong answer. It's an engineer not knowing how to recognise that the answer is wrong."**

That's the thesis of your talk. I'd pause after saying it.

The audience might forget the statistics, the anecdote or even the proposal. But if they leave thinking about that distinction, you've achieved something meaningful.