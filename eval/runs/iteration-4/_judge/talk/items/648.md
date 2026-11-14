# Should Engineers Use AI for Everything? (5-minute all-hands talk)

**Main message:** Not for everything, and not for nothing. It's a useful tool, and it works best when the person using it still understands and owns the result.

---

## Opening paragraph (to say out loud)

Hi, I'm [name]. I'm a backend engineer, I've been here about two years, and I'm up here mostly because I got volunteered. The question I was given is: should engineers use AI coding assistants for everything? The short answer is no. The slightly longer answer is: also, not nothing. I use Copilot fairly often, and it's fine. Sometimes it saves me real time, and sometimes it gives me something that looks perfect and is quietly wrong. So I won't tell you it's the future or that it's a disaster. I'll spend the next few minutes on where it helps, where it bites, and the rule of thumb I use to tell which is which.

*(About 30 seconds.)*

---

## Outline (talking points)

### 1. What these tools are, in plain terms (about 45 sec)
- For non-engineers: it's autocomplete for code. You start typing, it suggests the next line or the whole function.
- It doesn't "know" our system. It's very good at guessing what code usually looks like.
- The engineer still decides what to keep. The tool suggests and the person signs off.
- A comparison everyone knows: autocorrect. Most of the time it's great, until it changes a word in an email to a client.

### 2. Where it helps (about 1 min)
- **Repetitive, boring code**: the same setup and patterns we write over and over.
- **First drafts of tests**: a starting point that you then check and fix.
- **Unfamiliar territory**: "how do I do X in a language I don't use much?"
- **Explaining old code**: "what is this function doing?" as a first pass.
- What these have in common: the work is easy to check, and getting it slightly wrong is cheap.

### 3. Where to be careful (about 1 min 15 sec)
- **It's confident even when it's wrong.** Nothing in the output tells you which parts are made up. Bad code can look exactly like good code.
- **Code you don't understand is code you can't fix.** If it breaks at 2 a.m., "the AI wrote it" won't help whoever is on call.
- **What you paste in matters.** Customer data, passwords, internal secrets: be careful what goes into any outside tool. *(Check before Friday whether we have a company policy on this. If we do, mention it here. If we don't, it's worth saying that we probably should.)*
- **Review still costs time.** Writing faster doesn't help much if reviewing takes longer.
- What these have in common: the work is hard to check, and mistakes are expensive or hard to see.

### 4. The rule of thumb (about 45 sec)
- **"If you couldn't explain it, don't ship it."**
- Treat it like a fast, eager new hire: helpful, but you review the work before it goes out.
- So, "for everything?" No. For a lot of the boring parts, sure, as long as a person is still the one responsible.

### 5. Close (about 30 sec)
- This isn't only about engineering. The same thinking works for AI-written emails, docs or summaries: fine as a draft, and you're still the one who has to stand behind it.
- One-line summary: "Use it where it's easy to check. Be careful where it isn't. Either way, you own the result."
- Thanks, and you're happy to talk more afterward.

*Total: about 4 min 45 sec, which leaves a little room if you run long.*

---

## Two optional things that would make it stronger

- **One real moment from your own Copilot use.** It doesn't need to be dramatic. "Last month it suggested ___ and it was wrong because ___" or "it saved me an afternoon on ___." Put it in section 2 or 3. A small true story will land better than anything general.
- **The company's AI tool policy, if there is one.** A quick message to your manager or IT will tell you. It fits naturally in section 3.

**On slides:** you don't need them. If you want one, use a single slide with the rule of thumb ("If you couldn't explain it, don't ship it") and leave it up the whole time.
