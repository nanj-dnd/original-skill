Got it — I'll pick something that's fun, visibly "AI," works for a mixed-skill team, and is hard to fail at demo time.

# The idea: **Rescue** — point your camera at your fridge, waste less food

**Pitch:** Food waste accounts for roughly 8–10% of global greenhouse gas emissions — more than aviation. Most of it happens at home, because people forget what's in the fridge. Rescue uses a vision model to look at your fridge, figure out what's about to go bad, and generate a meal that uses it *tonight*. Every meal you cook from "rescued" ingredients shows you the CO₂e you avoided.

Why this is a good hackathon pick:
- **Demo is live and physical.** You hold up a phone to a real fridge (or a box of groceries on the table) and it works in front of the judges. That's far more memorable than slides.
- **AI is the core**, not a bolt-on — vision + LLM reasoning + generation.
- **Scope is adjustable.** A minimal version is ~1 API call; there's a clear ladder of extras if you're fast.
- **Fresh angle.** Judges have seen a hundred carbon calculators; they haven't seen one that cooks dinner.

# What you'd build

**Core loop (must-have, aim to finish by Saturday afternoon):**
1. **Capture** — Mobile web app (no app store needed). User snaps 1–3 photos of fridge/pantry.
2. **Identify** — Send photos to a multimodal model (Claude, GPT-4o, Gemini). Prompt it to return structured JSON: `[{item, quantity_estimate, freshness: fresh/use_soon/urgent, confidence}]`. Ask it to rank perishability (herbs, berries, leafy greens, cooked leftovers = urgent).
3. **Rescue plan** — Second LLM call: given the inventory, propose 2–3 meals that maximize use of "urgent" items, using mostly what's on hand plus ≤2 pantry staples. Output recipe + "you're rescuing: spinach, half an avocado, leftover rice."
4. **Impact** — Multiply rescued items by a small lookup table of kg CO₂e per kg of food (beef ≈ 60, cheese ≈ 20, chicken ≈ 6, veg ≈ 0.5–2, etc. — source something like Poore & Nemecek 2018 / Our World in Data). Show "This meal avoided ~1.8 kg CO₂e ≈ 7 km of driving."
5. **Running tally** — Local storage: total meals rescued, total CO₂e avoided, a simple streak.

**Stretch (Sunday, pick in order):**
- "Expiry nudges": store the inventory and show a "use within 2 days" list on reopen.
- Voice mode: "What can I make in 15 minutes?" → spoken answer.
- Household leaderboard / share card for social.
- Swap suggestions: "You buy beef weekly; swapping one meal to lentils = X kg/year."

**Suggested stack (lowest-risk for an unknown team):**
- Frontend: Next.js or plain Vite + React, deployed on Vercel. Use `<input type="file" capture="environment">` for camera.
- Backend: Vercel/serverless function that calls the model API. One file.
- Model: whichever vision API someone already has a key for. Keep prompts in one file so anyone can tweak them.
- No database — localStorage is fine for 48h. Add Supabase only if you have a backend person who's bored.

**Team split (works for 3–5 people):**
- A: camera + UI flow
- B: prompts + JSON parsing + fallbacks (this is the whole product; put the most careful person here)
- C: impact math, results screen, share card
- D (optional): demo prep, pitch deck, test on 5 real fridges

# Demo plan (3 minutes)

**Setup:** Bring a cooler or a cardboard "fridge" with real items that photograph well and have an obvious story: wilting spinach, half a lemon, leftover rice in a container, eggs, cheese, a bruised banana. Test the exact photo angle and lighting the night before. Pre-record a backup video of the same flow.

1. **(0:00–0:30) Hook.** "Show of hands — who threw out food this week?" Then the stat: food waste ≈ 8–10% of global emissions; most of it is households, and the reason is simply forgetting.
2. **(0:30–1:30) Live demo.** Open the fridge/cooler, snap a photo on a phone (mirror to the screen). Show the inventory appear with freshness flags — point at the spinach: "it caught that it's wilting."
3. **(1:30–2:15) The rescue.** Tap "Rescue dinner." Read out the recipe — spinach-egg fried rice with lemon. Show the impact card: "1.4 kg CO₂e avoided, equivalent to ~6 km of driving."
4. **(2:15–2:45) The hook for scale.** Show the running tally / streak screen and say the one-liner: "Carbon apps ask you to feel guilty. Rescue asks you what's for dinner."
5. **(2:45–3:00) Close.** What you'd do next (grocery store partnerships, expiry nudges, household plans). Open for questions.

**Failure modes to cover:**
- Wi-Fi dies → hit "demo mode" with cached photo + cached response (build this; it's 20 lines).
- Model misidentifies something → laugh, say "it's 48 hours old," move on. Have the recipe step not depend on perfect inventory.
- Latency → show a progress state with a fun message ("sniffing the leftovers…"), and pre-warm the API before you walk up.

# If you want a backup idea
**"Is my home climate-ready?"** — type an address, pull public flood/wildfire/heat-risk data (FEMA, First Street, NOAA), and have an LLM write a plain-English risk report plus a prioritized adaptation checklist with cost estimates and rebates. Strong on impact, weaker on live-demo wow factor, and more dependent on flaky public APIs — so I'd only pick it if your team leans backend/data.

Want me to draft the two core prompts (inventory extraction + rescue plan) and the CO₂e lookup table so you can start building Friday night?