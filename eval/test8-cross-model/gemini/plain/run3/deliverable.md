## The Opening Paragraph

"If you believe the tech headlines right now, my job today is to announce that we’re replacing the entire engineering department with a large language model and an unlimited cloud budget. Don't worry, we aren't. But we do need to talk about the reality of AI coding assistants. Right now, it feels like we’ve handed every engineer a superpower—the ability to generate hundreds of lines of code in seconds. But as anyone who has spent three hours debugging an AI’s hallucinated API endpoint knows, writing code fast is not the same as writing code *right*. For the next five minutes, I want to talk about how we can use these tools to eliminate our grunt work, without accidentally outsourcing our architecture, our security, or our common sense."

---

## 5-Minute Talk Outline

**1. The Reality Check (1 Minute)**

* **The Thesis:** AI is a tireless, eager junior developer. It is exceptionally fast, knows every language, but lacks the crucial context of our specific systems, business logic, and user needs.
* **The Mindset Shift:** We are moving from "authors" of every line of code to "reviewers and directors" of code.

**2. The Sweet Spots: Where You *Should* Use It (1.5 Minutes)**

* **Boilerplate & Setup:** Let the AI write the scaffolding, the repetitive CRUD operations, and the standard configuration files.
* **Test Generation:** Generating standard unit tests and edge cases (though engineers must verify the assertions).
* **Rubber Duck Debugging & Explanations:** Dropping an undocumented block of legacy code into the prompt and asking, "What is this doing?"
* **The Takeaway:** Use AI for the highly predictable, low-risk "brawn" of software development.

**3. The Danger Zones: Where You *Must* Take the Wheel (1.5 Minutes)**

* **Security & Data Privacy:** AI doesn't know our threat model. It will happily suggest insecure cryptographic hashes or expose sensitive data loops if not caught.
* **Architectural Decisions:** AI solves for the immediate prompt, not for the system's long-term scalability or maintainability.
* **The "Hallucination" Tax:** Creating phantom libraries or methods that look perfectly logical but don't actually exist.
* **The Takeaway:** Never blindly commit code you don't understand well enough to explain to a peer. You own the code, not the assistant.

**4. Our Philosophy Moving Forward (1 Minute)**

* **The Golden Rule:** The engineer whose name is on the pull request is 100% responsible for the code, regardless of who (or what) typed it.
* **Call to Action:** Encourage the team to experiment with these tools to boost their velocity, share the best prompts they discover in Slack, and aggressively call out AI-generated bad practices in code reviews.
* **Closing Thought:** AI won't replace engineers, but engineers who effectively use AI will replace those who don't. Let's make sure we are the former.