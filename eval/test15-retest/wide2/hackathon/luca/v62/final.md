Both phrases trace to your answers, so I've kept them, with the wording now closer to the option text:
- **"for technical judges"** comes from **4a**, which read "A live demo to technical judges, where working code matters most."
- **"you left the case to me"** comes from **3d**, which read "Nothing specific. Pick a case that fits our team." It's now worded as "no specific case; pick one that fits."

---

**Angle:** Footprint apps fail because they treat every action as equally worth logging. Gut Check skips the logging: you guess which of your choices matter most, then see the real proportions for your own life.
**Built from:** 1a (individuals, but sharper than a tracker), 2a plus your note (solo, frontend only, about 24 hours), 3d (no specific case; pick one that fits), 4a (3-minute live demo for technical judges, finished and polished).
**Strongest objection:** It's a one-time quiz with no reason to come back, and judges may call it a calculator with nice animations. **Test:** Before you start building, give the eight action cards to three people and ask them to rank them. If their guesses roughly match the real order, the reveal has no surprise and you should pick another idea.
**Other direction:** A frontend-only "run it when the grid is cleanest" planner using a free grid carbon-intensity API.

---

# Gut Check: guess what matters, then see the real proportions

## The idea
Most people's sense of which climate actions matter is out of proportion. Small, visible habits feel big, and one or two large choices hide in the background. Gut Check asks four quick questions about your life, then gives you eight action cards to drag into the order you *think* matters most. Then it reveals the real order for you. The cards resize to true scale and reorder themselves, and the small habits shrink to slivers. At the end you get one move that matters for your life, plus a "gut vs. reality" gap score.

It has no logging, streaks or badges. It does its job in about 90 seconds.

## What you'd build
Everything runs in the browser. It needs no backend, no external API calls and no login, so nothing can break on stage.

**Screens**
1. **About you:** four inputs. These are weekly car km, return flights per year (short and long haul), diet (meat most days, some, none) and home heating type. A "load demo profile" button fills them instantly.
2. **Rank it:** eight cards to drag into your guessed order. Use a mix of high and low impact actions: recycle everything, switch to LED bulbs, wash clothes cold, skip one long-haul return flight, go car-free or switch to an EV, cut beef, move to a plant-based diet, switch to a heat pump or a green tariff.
3. **The reveal:** cards animate into the true order, and each bar's width is set by the kg CO₂e per year it saves *given your inputs*. Your guessed rank stays shown as a ghost position next to each card.
4. **Your one move:** your biggest lever in one sentence and your gap score. If an input zeroes an action out (you don't fly, so skipping a flight saves nothing), the card says so instead of showing a fake number.

**Data**
- A single `factors.json` file built from published sources. Use the UK government's greenhouse gas conversion factors (or the EPA's, if your judges are US-based) for car km, flights and heating. Use Our World in Data's food emissions figures for diet.
- Each action is one small formula in a `calculate.ts` file. Show the sources in a footer on the reveal screen.

**Stack:** React or Svelte, with dnd-kit or SortableJS for dragging and Framer Motion layout animations for the reveal. Deploy to Vercel or Netlify, and keep a local build ready for the demo.

## 24-hour plan
| Hours | Work |
|---|---|
| 0–2 | Pull the factors, write the formulas and sanity-check the outputs in a spreadsheet. Run the three-person test. |
| 2–5 | Input screen and demo-profile button |
| 5–9 | Drag-to-rank screen |
| 9–13 | Reveal animation, the part judges will remember, so give it the most time |
| 13–15 | One-move screen and gap score |
| 15–18 | Visual polish, projector-sized type, mobile layout |
| 18–20 | Sources footer and zero-value edge cases |
| 20–22 | Deploy, then test on a projector and on a phone |
| 22–24 | Rehearse three times, with the rest as buffer |

**Cut first if behind:** gap score, then mobile layout. Never cut the reveal.

## 3-minute demo
1. **0:00–0:20, ask the room.** "Which saves more in a year: recycling everything you use, or skipping one long-haul return flight?" Get a show of hands, and don't answer yet.
2. **0:20–0:45, about you.** Load the demo profile and change one input live, so judges can see it's real input.
3. **0:45–1:25, rank it.** Drag the cards into your honest gut order and say your reasoning out loud. The judges will be ranking along in their heads.
4. **1:25–2:10, the reveal.** Hit reveal and let the animation run in silence for two seconds. Then point at the slivers and at where your gut placed them. Answer the opening question.
5. **2:10–2:40, it's personal.** Set flights to zero and reveal again. The ranking reshuffles, which shows it isn't a fixed listicle. Read out the one-move sentence.
6. **2:40–3:00, close.** "Trackers make you log every coffee cup. This shows you the one or two choices that are bigger than all of them. It runs entirely in the browser on public conversion factors, and the sources are on screen."

**Demo safety:** run the local build so venue Wi-Fi can't hurt you. Because the whole demo is live clicks on a fast app, you don't need a backup video.

---

**Before you use it**
- Write your opening question only after computing both numbers from your own `factors.json`. If recycling doesn't come out clearly smaller for your demo profile, swap in a pair that does.
- If you want to say people misjudge which actions matter, check published research before quoting it. The live guess-then-reveal shows it anyway, so you don't need a citation.

**Distance from the default:** The tracker's logging, streaks and LLM tips are gone (1a). The samples' backend, smart plug and team-of-four scope are replaced with a frontend-only build sized for one person in 24 hours (2a). Their stat-and-chart opening and their roadmap close are replaced by a live question to the room and a re-run that shows the result is personal (4a). It still shares two things with the samples: a personal footprint estimate built on public emission factors, and a "biggest item" reveal as the memorable moment, much like the receipt scanner's beef reveal.