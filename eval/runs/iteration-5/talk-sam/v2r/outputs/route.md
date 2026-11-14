# Route

**Path: specific answers → step 4 (build directly).** Your answers include things I couldn't have guessed: the room is the tech division (about 80 people, mostly engineers, plus risk/compliance), there's a real recurring near-miss (people almost pasting customer data or prod logs into these tools), and a hard line you want stated for about a minute. Because this is a talk, here's the plan first. I'll write it once you reply.

---

**Angle:** For most work the answer to "AI for everything?" is "use judgment, and check it like any other code." But the one thing that isn't up to judgment is what goes *into* the tool. The line isn't about tasks, it's about data: no customer data and no production logs in any external tool, ever.

**Built from:** 1 (you hold the middle position, so the talk doesn't fight it, it narrows it), 2 (tech division of about 80 with risk/compliance in the room, so it's engineer-to-engineer and compliance hears its rule stated plainly), 4 (the near-misses keep happening), 5 (one clear minute: "here is the line"), 3 (speed against quality, which is used in the tension below).

**The tension I'm using:** you framed the stakes as speed against quality (3a), but your real case isn't a quality problem, it's a speed problem. Pasting a prod log is the *fastest* way to debug, and that's exactly why people nearly do it. So the talk admits the line costs some speed, and says that cost is the one we don't trade. That lets the "use judgment" part and the "no exceptions" part sit side by side without contradicting each other.

**Planned shape (5 min):**
1. Opening (about 30s): the near-miss, told as a moment everyone recognises (stuck on a bug, the log is right there, Cmd-V), with no names.
2. The honest middle (about 1 min): yes for lots of work, no blanket rule on tasks, own and review what you ship, judge it on speed against quality.
3. Where judgment stops (about 1 min, the core): the line, said slowly and once. No customer data. No production logs. In any external tool. Why it's absolute when everything else is judgment: once it's pasted, you can't take it back.
4. What to do instead (about 1 min): [your redaction / synthetic data / approved internal tool, if one exists]. Who to ask: [named compliance contact, possibly someone in the room].
5. Close (about 30s): repeat the line word for word. That's the one sentence they leave with.

**Strongest objection:** "Everyone already knows this is forbidden. A minute repeating policy at an all-hands is a lecture, and you'll lose the room." **Test:** the line only works if it comes with a quicker safe path than pasting (section 4). If you can't name one, the talk is just a reminder and the near-misses will continue. Before Friday, also check the exact wording with compliance: does the rule really cover *any* external tool, and is there an approved tool (for example an enterprise contract with no data retention) that changes "any"? If there is, the line needs to name it, or engineers will spot the gap in front of the compliance folks.

**Other directions:**
- Drop the "for everything" debate entirely and spend all 5 minutes on the line and the safe path. Sharper, but it doesn't answer the question you were given.
- Keep speed against quality as the main thread (review load, rework) and save the data line for a 1-minute closer. Closer to the default, with the line as the takeaway.

**Reply with:** a go-ahead, a redirect, or anything you want worked in: the safe alternative people should use, whether to name the compliance contact, a line you want in, or how you want it to end.

---

# After the go-ahead

The user approved the plan. Section 4 is now: "use redacted or made-up sample data, and if you're not sure, ask the compliance team first." No person is named, the approved-tool question is left as a pre-Friday check, the ending repeats the line word for word, and the "all-hands" wording is gone. The deliverable is in deliverable.md.

**Flagged details to check:** the bug-that-only-shows-up-in-production scene in the opening is an illustration I made up, framed as "you know the moment", not a claim about a specific incident. "More than once" comes from what you said ("people keep almost pasting"). Adjust it if that's too strong. "Once it's pasted, you can't take it back" is the general reason. Your compliance team may want to word the exact risk themselves.

**Distance from the default**
- The talk's core is a rule about what goes *into* the tool (data), not a list of which tasks AI is good or bad at. That came from answers 4 and 5.
- It opens on a real, recurring near-miss in your own division instead of a hook question or a productivity stat. That came from answer 4.
- It ends on one sentence repeated word for word instead of "use it wisely". That came from answer 5 and your go-ahead.
- It talks to engineers with compliance in the room, and names the compliance team as the place to ask. That came from answer 2 and your go-ahead.
- It admits the line costs speed, which turns your speed-against-quality framing into the reason the rule needs saying. That came from the tension between answers 3 and 4.
- What did not move: the overall position is still the balanced middle ("use judgment for most work"). You chose that (1a), and section 2 is close to the default.
