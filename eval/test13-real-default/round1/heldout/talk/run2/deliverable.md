Here's a 5-minute outline and opening. (Looks like a Python snippet got pasted in with your message — I've ignored it, but let me know if you wanted something done with it.)

---

## Talk: "Should engineers use AI coding assistants for everything?"

**Thesis:** Use them aggressively, but not indiscriminately. The question isn't "AI or no AI" — it's "which decisions are we still willing to own?"

### Outline (~5 min)

**1. Hook (30s)**
- Open with a concrete, slightly uncomfortable example: a PR that shipped last month that nobody on the team could fully explain. (Use a real one if you have it — anonymized.)
- Frame the actual question: not whether to use these tools, but where the boundary is.

**2. What "everything" gets right (60s)**
- Boilerplate, tests, migrations, glue code, unfamiliar APIs — this is where assistants are a clear net win and resisting them is just slower.
- The "blank page" problem is gone. First drafts are cheap now.
- Honest admission: the people who refuse entirely are falling behind.

**3. What "everything" gets wrong (90s)**
- **Understanding debt.** Code you didn't write and didn't read is code you can't debug at 2am. Review fatigue is real — people rubber-stamp generated code faster than human code.
- **Design decisions by default.** Assistants are great at "how," weak at "whether." They'll happily build the wrong thing beautifully.
- **Skill atrophy.** Juniors who never struggle through a problem don't build the intuition they'll need to judge the assistant's output later. This is the one I actually worry about.

**4. A working rule of thumb (60s)**
- Proposed line: *Use AI for anything you could verify. Be cautious with anything you'd have to trust.*
- Practically: generate freely, but the author owns the PR as if they typed every line. "The AI wrote it" is never an answer in code review.
- Keep some deliberate manual practice — especially in the parts of the system where we have the most tribal knowledge.

**5. Ask / close (30s)**
- Not asking for a policy today. Asking each team to answer one question this quarter: *what's the one area where we should slow down and do it ourselves?*
- Close by returning to the hook.

---

### Opening paragraph

> Last month we merged a pull request that nobody in the room could fully explain. It passed tests. It passed review. It did the job. And when something adjacent broke two weeks later, it took three people most of a day to figure out why — because none of them had actually *read* it the first time. I'm not telling that story to scare anyone off AI coding tools. I use them every day, and I think anyone who's refusing to is making a mistake. I'm telling it because the question we keep asking — "should engineers use AI assistants?" — is the wrong question. We already do. The real question is where the line is: which parts of our work we're still willing to own, understand, and be accountable for, and which parts we're comfortable handing off. I've got five minutes, so let me try to draw that line.

---

Want me to tune the tone (more playful, more direct), swap the hook for a different kind of example, or draft speaker notes for any section?