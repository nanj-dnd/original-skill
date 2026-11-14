**Angle:** AI coding assistants are incredible at generating volume, but if we don't actively own the architecture and prune the output, we end up scaling our technical debt instead of our productivity.
**Built from:** 1c (scaffolding vs logic), 2 (test suite explosion), 3a (pragmatic/direct tone).
**Strongest objection:** AI models are improving so quickly that they will soon be able to identify and clean up their own redundant code, making this bloat just a temporary growing pain.
**Test:** Look at last week's PRs: are engineers currently spending more time debugging AI-generated tests than they are writing new core logic?
**Other direction:** Dedicate a sprint to using AI specifically to refactor and optimize the bloated test suite it helped create.

---

**Opening Paragraph**
Over the last year, our test suite jumped from 2,000 to 9,000 tests. On paper, that sounds like a massive win for code quality. But in reality, our nightly run went from 20 minutes to three hours. The truth is, most of those new tests were written by AI, and a huge chunk of them are just checking the exact same things in slightly different ways. AI coding assistants are incredible tools for generating volume, but volume isn't architecture. If we just treat these tools like an autopilot, we aren't actually shipping better product faster—we are just generating technical debt faster.

**Outline (5-Minute Talk)**

* **1. The Hook (0:00 - 1:00)**
* Deliver the opening paragraph above.
* Acknowledge that everyone loves the speed of tab-complete, but highlight the hidden cost: maintaining thousands of lines of redundant, AI-generated code.


* **2. Where AI Excels vs. Where It Fails (1:00 - 2:30)**
* *The Good:* Scaffolding, boilerplate, and getting from zero to a first draft. It removes the blank-page problem.
* *The Bad:* System-level context. The AI doesn't know that three other tests already cover the edge case it just wrote 50 lines for.


* **3. The New Rule of Thumb (2:30 - 4:00)**
* Humans own the logic; AI types it out.
* If you use AI to write a block of code or a batch of tests, you are fully responsible for understanding, pruning, and maintaining it.
* Review AI output with the exact same skepticism you would use when reviewing a PR from a junior engineer.


* **4. The Ask / Next Steps (4:00 - 5:00)**
* We are going to start aggressively pruning redundant tests to get our CI/CD pipeline times back down.
* Keep using the AI tools for scaffolding, but prioritize efficiency and architecture over raw lines of code.



---

**Before you use it:** Double-check with DevOps or QA that the nightly run is still strictly at the 3-hour mark (and hasn't recently been parallelized or optimized), just so nobody "well, actually"s you during the Q&A.
**Distance from the default:** We completely dropped the generic warnings about IP and security bugs. Because of your answer in step 2, the piece shifted from a theoretical HR warning into a highly specific, grounded critique about CI/CD bloat and redundancy.

*Let me know if you would like me to export this entire run (the task, default analysis, your answers, the angle block, and the piece) as a Markdown file or PDF for your records.*