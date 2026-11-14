# "Careful" isn't a person: what our checkout form taught me about AI

*5 minutes, about 650 to 750 spoken words. Times are a rough guide.*

## Outline

**1. Open with the email (0:00 to 0:50)**
- The checkout form story, told plainly (opening paragraph below).
- End on the question the talk is really about: not "should engineers use AI for everything," but "who checks the parts nobody asked for?"

**2. Why a product designer is up here (0:50 to 1:20)**
- I'm not an engineer. I was asked because I apparently "have opinions about quality."
- Be honest about where you stand: "I think these tools are probably fine, as long as people are careful." Say that's what you believed going in, and that the rest of the talk is about what "careful" has to mean.

**3. What actually went wrong (1:20 to 2:30)**
- The form wasn't broken in the usual sense. It did what it was built to do and it shipped. What it didn't have was something nobody had written down as a requirement: labels a screen reader can read.
- Fair point to make out loud: people ship unlabeled forms too. This isn't "AI writes bad code." [Check before the talk: was this form reviewed, and did the review include any accessibility check? Ask engineering, so you can say it accurately.]
- What the tool changes is speed: more screens get built per week, and the parts nobody specifies are exactly the parts that fall out first.

**4. "As long as people are careful" (2:30 to 3:30)**
- Careful at what? Being careful only works when you know what to look for. Accessibility wasn't on anyone's checklist, so no amount of care from one engineer was going to catch it.
- The signal came back the long way: a customer had to email support, and you heard about it from support, not from engineering. Then it took two weeks to fix.
- So "careful" can't be a personal virtue we hope for. It has to be built in: who checks, against what list, and how fast a customer's complaint reaches the people who built the thing.

**5. Why this is everyone's question, not just engineering's (3:30 to 4:15)**
- Most of this room doesn't write code, and that's the point. Support heard about it first. Design decides what "done" looks like. Product decides what ships. [Add one or two other teams in your company that touch quality or customer feedback.]
- If AI makes building faster, the checks that sit outside engineering matter more, not less.
- Put the original question back on the table: "use AI for everything" is fine only if "everything" includes the parts a user can't see on the screen.

**6. Close (4:15 to 5:00)**
- [You haven't picked an ending yet. Suggested: one small ask per group, then back to the customer.]
  - Engineering: any AI-built screen gets a screen-reader check before it ships. [Confirm this is realistic with an engineering lead first.]
  - Support: a direct route to the team that shipped the feature when a customer reports something broken for them. [Name the channel or process if one exists.]
  - Everyone who writes a request or a spec: name the invisible parts (labels, error messages, keyboard use), because the tool will only build what you ask for.
- Last line, back to the opening: the next customer shouldn't have to email us to find out.

## Opening paragraph

Last quarter, a customer emailed our support team about our checkout form. They're blind, and they use a screen reader, and the form had no labels. Every field was there, but nothing told them what went in it. That form had been written with an AI coding assistant. It worked, it shipped, and it took two weeks to fix. I'm a product designer, so I want to be clear about how I found out: not from engineering, but from support. I've been asked to talk about whether engineers should use AI coding assistants for everything. I'll be honest: I don't have a big verdict. I think they're probably fine, as long as people are careful. But that email made me ask what "careful" actually means, and who it's supposed to be.
