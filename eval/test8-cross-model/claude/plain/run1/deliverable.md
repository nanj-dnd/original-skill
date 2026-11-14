Here's a 5-minute version (~700 words spoken) built around a clear thesis: **use AI for most of the work, but never for the judgment.** Adjust the stance if yours differs.

---

## Outline

**1. Hook & thesis (0:00–0:45)**
- Open with a concrete, slightly uncomfortable example (see paragraph below)
- Thesis: "Everything" is the wrong frame. The question isn't *whether* we use AI assistants, it's *which parts of the job we hand them and which parts we don't.*

**2. Where they clearly win (0:45–1:45)**
- Boilerplate, glue code, migrations, test scaffolding, config
- Reading unfamiliar codebases and explaining them
- First drafts of docs, PR descriptions, commit messages
- Rubber-ducking: "why might this fail?"
- Point: this is 50–70% of raw keystrokes for most of us. Refusing it is like refusing autocomplete in 2010.

**3. Where "everything" breaks down (1:45–3:00)**
- **Judgment calls**: architecture, tradeoffs, what *not* to build — the model doesn't know our customers, our on-call history, or our six-month roadmap
- **Verification debt**: code that *looks* right ships faster than code that *is* right. Review load shifts from writing to reading, and reading is harder.
- **Skill atrophy**: if juniors never struggle through a problem, they don't become seniors. (Cite: the "learning requires productive difficulty" point.)
- **Security & data**: what goes into the prompt, what comes out with a license attached
- One memorable line: *"AI makes the easy parts free and the hard parts more expensive."*

**4. A working rule of thumb (3:00–4:00)**
- Three questions before you delegate a task:
  1. Can I verify the output faster than I could write it?
  2. Do I understand it well enough to own it in a 3am incident?
  3. Would I learn something important by doing it myself?
- If yes/yes/no → delegate freely. If any flip → slow down.
- Team-level: AI-generated ≠ lower review bar. Author owns every line.

**5. Close & ask (4:00–5:00)**
- Reframe: the goal isn't "more code," it's "better decisions, faster"
- Specific ask: [pick one — e.g., "try the three-question check for two weeks and share what you learned in #eng," or "we're drafting usage guidelines; comments open until X"]
- End on the thesis in one sentence

---

## Opening paragraph

> Last month I watched a PR get approved in four minutes. Three hundred lines, two reviewers, both thumbs-up. It was clean, well-commented, and had tests. It also silently broke retries for one of our payment paths, and nobody — not the author, not the reviewers, not the model that wrote most of it — noticed until a customer did. I'm not telling that story to scare anyone off AI tools. I use them every day and I think everyone in this room should too. I'm telling it because the question we keep asking — "should engineers use AI assistants for *everything*?" — is the wrong question. It treats this as a yes-or-no decision when it's actually a *which-parts* decision. So for the next five minutes I want to split the job of engineering into the pieces we should hand over without hesitation and the pieces we absolutely can't, and give you one simple test to tell the difference.

---

A couple of notes:
- If the PR story isn't true for your company, swap in a real one — specificity is what makes the opening land. A generic hypothetical will feel like a LinkedIn post.
- Section 3 is the part people will remember; don't let section 2 eat its time.
- If you want, tell me your actual stance and company context (size, AI policy, any recent incident) and I'll tighten the language and the closing ask.