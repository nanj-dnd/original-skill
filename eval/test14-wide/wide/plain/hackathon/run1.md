# Hackathon Idea: **ReceiptPrint** — Carbon footprint from your grocery receipt

## The idea
Most carbon-footprint apps ask users to log meals manually, which nobody does. But everyone already has a grocery receipt. Snap a photo of it, and ReceiptPrint estimates the carbon footprint of your shopping trip, line by line, and suggests a few cheap swaps that cut the most emissions without changing your habits much.

It's climate-relevant, instantly demoable, and the "aha" moment (seeing that one pack of beef outweighs the rest of the cart combined) lands in about five seconds.

## What you'd build (weekend scope)

**Core pipeline (must-have):**
1. **Receipt capture** — mobile web page with camera upload (no app store needed).
2. **OCR + parsing** — run the image through an OCR service (Google Vision, AWS Textract, or Tesseract locally), then pass the raw text to an LLM to normalize cryptic receipt lines like `GRND BF 80/20 1LB` → `{item: "ground beef", qty: 1, unit: "lb"}`.
3. **Emissions lookup** — map normalized items to a food emissions dataset. Poore & Nemecek (2018) gives kgCO2e per kg for ~40 food categories and is public; pre-load it as a JSON table with fuzzy matching.
4. **Results view** — a stacked bar showing the cart's total, sorted by impact, with the top 2–3 offenders highlighted and a "swap suggestion" for each (e.g., beef → chicken saves X kg; dairy milk → oat milk saves Y kg).

**Nice-to-haves if time allows:**
- Running history across receipts ("you're down 18% from last week")
- Shareable summary card
- Store-level comparison if you get receipts from different stores

**Stack suggestion:** Next.js or plain React frontend, a small Python/Node backend for OCR + LLM calls, SQLite or no DB at all for the demo. Keep the emissions table in-repo so there's no external dependency at demo time.

## Demo plan (aim for ~3 minutes)

1. **Hook (20s):** "Climate apps fail because they ask you to track things. We ask you to do one thing you already do: keep your receipt."
2. **Live scan (45s):** Hold up a real receipt from someone on the team's actual weekend shopping. Snap it on a phone. Show the parsed items appearing. *Prepare a fallback pre-captured image in case lighting is bad.*
3. **The reveal (45s):** Show the breakdown. Call out the single biggest item and what percentage of the cart it is. This is the moment judges remember.
4. **The swap (30s):** Click the suggestion. Show the recalculated total. Emphasize it's a *small* change, not "go vegan."
5. **Second receipt (30s):** Scan a second, lower-impact receipt to show the history/trend view, proving it's not a one-off.
6. **Close (20s):** Scale story — grocery loyalty programs already have this data digitally; the receipt scan is the wedge, the integration is the business.

## Risks to pre-empt
- **OCR flakiness:** Test on 5–6 real receipts from different stores Friday night. Have 2 known-good images ready.
- **Item matching gaps:** When an item can't be mapped, show it as "unknown, excluded" rather than guessing wildly — judges respect honesty over fake precision.
- **Numbers being questioned:** Cite the dataset on-screen in a footer. One line of attribution makes it credible.

Want me to sketch the emissions lookup table or a starter repo structure for this?