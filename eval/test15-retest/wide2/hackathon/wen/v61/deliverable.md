## Angle

- **Angle:** A personal-footprint app works best for a first hackathon if it does one thing well. Show people which of two everyday choices is heavier at the moment they choose, and let judges play with it on their own phones.
- **Built from:** 1d (individuals, done well), 2d (no material yet, so it uses public data), 3d (a slick software demo), and 4 (first hackathon, simple and cool, skills and hours unknown).
- **Strongest objection:** Carbon calculators already exist, and judges may see this as one more, with average figures that hide real variation. **Test:** Before Saturday lunch, hand the prototype to two people outside the team for one minute. If neither says "wait, really?" at some comparison, swap in more surprising pairs before you polish anything.
- **Other direction:** A receipt-scanning footprint tracker. It's more impressive if the scanning works, but riskier for a first build.

---

# Tip the Scale

**The idea.** A big animated balance scale on one web page. You pick two things you might choose between, such as a beef burger or a bean burrito, driving to the station or taking the bus, or a weekend flight or the train. You drop one on each pan and the scale tips, showing the kg of CO₂e on each side. Then you can stack a whole day on one side and see how far one swap moves it.

The app doesn't track anything, needs no account and asks for nothing to be logged. The point is that you'll remember which way the scale tipped next time you order lunch.

It suits your team because it's genuinely simple to build and genuinely fun to use, and the "cool" comes from the animation and the surprise, not from hard engineering.

## What you'd build

The whole thing is a static website with no server, no database and no login. That means nothing can break on demo day except the Wi-Fi, and even that can be handled (see below).

**Three pieces:**

1. **The data file.** This is a spreadsheet of 30 to 40 everyday items, exported to JSON. Each row has a name, an emoji, a category (food, travel, home, stuff) and kg CO₂e per serving, trip or use.
   - Food figures come from the Our World in Data food emissions charts, which are based on Poore & Nemecek (2018). Convert per-kg figures to a typical serving.
   - Travel figures come from the UK government's greenhouse gas conversion factors (per passenger-km). Pick a typical trip length for each item.
   - This piece needs no coding at all. Someone careful with a spreadsheet owns it.
2. **The scale.** This is one SVG or a few divs, with the beam rotated by CSS according to the ratio between the two pans. Cap the angle so huge gaps still look good, and add a little bounce when it settles. Show each pan's total in big type underneath.
3. **The picker.** This is a row of emoji cards by category that you tap or drag onto a pan. Add a "clear" button and a "load a day" button that fills one pan with a typical day's choices. That gives you a "swap one thing" moment: replace one card and watch the beam move.

**Scope by time** (you don't know the hours yet, so pick a level once you do):

| If you get… | Build |
|---|---|
| One evening | Two fixed dropdowns, the scale, and the numbers. Already demoable. |
| A full day | Emoji cards, the animation, 30+ items, and a mobile layout. |
| The whole weekend | "Load a day" mode, a share-image button ("I tipped the scale by 4 kg today"), and a sources page. |

**Tools:** Plain HTML/CSS/JavaScript, or React if someone already knows it. Host free on GitHub Pages, Netlify or Vercel. Anyone can learn the CSS rotation part in an hour.

**Splitting the work without knowing skills:** Divide it by job rather than by role. The jobs are the data spreadsheet, the scale and animation, the card picker, and the look plus the pitch. Whoever has never coded takes the data or the pitch, and both are essential.

## Demo plan

The demo works by letting the judges play rather than by walking through features.

1. **Before you speak,** put a big QR code on the screen that links to the live site. Judges open it on their phones.
2. **Start with a bet.** Pick a pair where the answer surprises people (your data person will know which ones). Ask the judges to guess which way it tips, then drop the cards on your screen and let the scale swing. Read out the real number it shows.
3. **Let them try one,** so for 30 seconds the judges drop their own pairs on their phones. That's the moment they remember: using it themselves, not watching you.
4. **Show a day.** Hit "load a day," swap one card, and show the beam move. Say the point in one line: you don't have to change everything, just know which choice is the heavy one.
5. **Point at the sources page** so the numbers have credibility. Close with what you'd add next, such as more items, local data for your country, or a browser extension that shows the scale on food delivery sites.

**Safety net:** Keep a local copy that runs offline on your laptop, and a 30-second screen recording of the scale tipping in case the projector or Wi-Fi fails.

---

**Before you use it**
- I couldn't check the figures in this session. Pull every number straight from the Our World in Data food charts and the UK conversion factors, and write down your serving and trip-length assumptions on the sources page.
- Check the hackathon rules on whether you can prepare data or code before the start.
- Once you know the hours and judging criteria, pick a row from the scope table. If there's a "best design" or "beginner" track, this idea fits it well.

**Distance from the default:** This stays close to the default. It's still personal footprint, for individuals, as polished software, because you chose 1d and 3d. What changed is the shape: a decision-moment comparison instead of tracking, a demo the judges play themselves, and scope tiers for unknown hours, all because of your answer to 4. It still shares the Poore & Nemecek food data and the "swap one thing" idea with the plain answers.