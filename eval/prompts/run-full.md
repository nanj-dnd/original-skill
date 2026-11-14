You are running one test of a skill. Read the skill at /home/user/original/SKILL.md (and its references/research.md if the skill tells you to) and follow it to handle the user's task below.

You are talking to a user, but only through messages:
- Do NOT use AskUserQuestion. Whenever the skill tells you to ask the user something (the questions in step 2, the pick in step 5), write it as plain text in your final message, formatted so the user can reply like `1b 2a 3: <own words>`, and then stop. The user's reply will arrive as a new message and you continue from there.
- When the skill offers an export (step 7), assume the user says no.
- Don't use the web unless the skill's step 4 truly calls for a prior-work search.

Files: save to {OUT}
- questions.md: the "What everyone gets" section and your questions, exactly as shown to the user (write this before you stop the first time)
- shortlist.md: candidates, cuts and the shortlist as shown to the user
- deliverable.md: the final deliverable only (the outline/post itself), with nothing before it
- distance.md: the "Distance from the default" section

User's task:
{TASK}
