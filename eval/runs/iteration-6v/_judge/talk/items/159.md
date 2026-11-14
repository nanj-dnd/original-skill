# Outline: "Review everything" is the hard half

Five minutes, about 700 words spoken. Timings are rough.

**1. Opening: the question, my answer, and why I'm taking the second half (0:00–0:45)**
- The question: should engineers use AI coding assistants for everything?
- My answer is the one you've heard: use them for a lot, and review everything.
- I run QA, so I'm spending my five minutes on the half of that sentence that usually gets said in a rush.

**2. Why the review half is where the real question is (0:45–1:45)**
- These tools make writing code cheaper. They don't make checking it cheaper at the same rate. The work doesn't disappear; it moves downstream.
- Assistant output looks finished: tidy, confident, consistently formatted. That's exactly the kind of code that's easy to skim and approve.
- When review is thin, the miss doesn't vanish. It lands on the next person in line: the code reviewer, then QA, then a customer.

**3. What "review everything" has to mean in practice (1:45–3:00)**
- For the author: you read every line you submit as if you'd typed it. If you can't explain why it works, it isn't ready to open as a PR.
- For the reviewer: "it looks clean" is not the same as "I checked it." Clean is what these tools produce by default.
- For tests, the one closest to my job: if the assistant wrote the code and the tests, the tests confirm what it built, not what you meant. Someone who knows the intent has to own what "correct" means: the acceptance criteria, the edge cases, the "what should happen when this fails."

**4. A word for the PMs in the room (3:00–3:45)**
- "The AI wrote it in an hour" tells you when the code appeared, not when it's done.
- If we plan around how fast code shows up, review and testing are the part that gets squeezed, and that squeeze is invisible until something ships broken.
- When you size work, count the checking, not just the writing.

**5. Close: no policy today, three questions to take back to your team (3:45–5:00)**
- I'm not asking anyone to vote on anything. I'd like each team to talk about three questions:
  1. When did you last reject or rewrite something an assistant gave you, and what tipped you off?
  2. On your team, who checks the tests the assistant wrote?
  3. If review were getting squeezed, would we notice before our users did?
- Closing line: Use the tools. Use them a lot. Just make sure "review everything" is something we actually do, not something we say on the way out of the meeting.

---

## Opening paragraph

I was asked to talk about whether engineers should be using AI coding assistants for everything. My short answer is the one you've probably heard a dozen times: use them for a lot, and review everything they write. I agree with that. But I run QA, so I want to spend my five minutes on the second half of the sentence, the half people usually say on their way to the door. "Review everything" is where the work ends up. Checking code is my team's day job, and when code gets faster to write, checking it doesn't get faster on its own. So I'm not really here to tell you whether to use these tools. I'm here to ask what "review everything" actually means once we do.
