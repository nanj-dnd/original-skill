# AI originality and idea diversity

*13 November 2026. Research was cut short twice by a usage limit, so coverage is uneven; see "Coverage limits" at the end.*

## Bottom line

1. **The "two people paste the same task" problem is real and measured.** Same-model answers to the same open-ended prompt are near-duplicates at the level of ideas, and different vendors' models are almost as similar to each other.
2. **Most popular fixes do nothing.** Personas, "be bold", tipping, threats, higher temperature and example ideas barely move idea diversity, and some make it worse.
3. **One mechanism does work: make the model look at what already exists and differ from it.** That covers its own earlier answers, the default answer, and prior work.
4. **A huge interview is not supported by the evidence.** Returns flatten after roughly 20 to 30 minutes of questions, and richer personal context pulls a model's answers toward the average, not away from it. Short, well-chosen questions beat volume.
5. **Selection is the hard part.** Every system that produced a verified new result had an evaluator independent of the generator's own taste. LLM judges are weakest on exactly the thing wanted here, which is novelty.
6. **The core of the proposed tool is untested.** No study was found that measures whether personal context makes a model's ideas more original, as opposed to better fitted to the person.

## 1. How similar are answers to the same prompt?

- In a benchmark of 26,070 real open-ended queries across 70+ models, 79% of same-model response sets had average pairwise similarity above 0.8. Different models' answers to the same query were 71 to 82% similar. Asked for a metaphor about time, 25 models mostly produced "time is a river" ([Jiang et al. 2025](https://arxiv.org/abs/2510.22954)).
- A population of 22 models from 7 vendors was far less varied than 102 humans on standard creativity tests: 0.459 against 0.738 on one measure ([Wenger & Kenett 2025](https://arxiv.org/abs/2501.19361)).
- Asked for 4,000 research ideas on a topic, Claude 3.5 Sonnet produced about 200 distinct ones, or 5% ([Si et al. 2024](https://arxiv.org/abs/2409.04109)).
- People who write with AI help produce work that is individually rated better but more alike. Stories gained 5 to 8% in novelty while becoming more similar to each other ([Doshi & Hauser 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532/)). A preprint meta-analysis of 28 studies puts the loss of idea diversity at g = -0.86 ([Holzner et al. 2025](https://arxiv.org/abs/2505.17241)).

**Novel on paper is not the same as good.** Experts rated AI research ideas more novel than human ones (5.64 against 4.84 out of 10). When 43 researchers then spent about 103 hours each executing the ideas, the AI ideas' scores fell much further: overall 5.38 to 3.41, against 4.60 to 3.97 for human ideas ([Si et al. 2025](https://arxiv.org/abs/2506.20803)).

**Cause.** The best-supported explanation is preference tuning. Human raters prefer typical-sounding text, so training on their preferences sharpens the model toward the typical. Untuned base models are measurably more diverse ([Zhang et al. 2025](https://arxiv.org/abs/2510.01171)).

## 2. What moves a model off the default

Figures are similarity within a pool of ideas, where lower means more diverse. The base prompt scored 0.377 and a pool of human ideas 0.243 ([Meincke et al. 2024](https://arxiv.org/abs/2402.01727), GPT-4, not peer-reviewed).

| Method | Result |
|---|---|
| Personas, "be bold and novel", tipping, threats, pleading | 0.348 to 0.406: within about 0.03 of the base prompt |
| Giving example "good ideas" | 0.403 to 0.432: worse than base |
| Simulated team that picks its best ideas | 0.393: worse than base |
| List the ideas, then revise them to be bolder and more different | 0.255: close to the human pool |
| Picking the most different ideas from a large pool afterwards | 0.144: better than any prompt |

Other findings:

- **Temperature** gives weak novelty gains at a cost in coherence and does not remove the convergence ([Peeperkorn et al. 2024](https://arxiv.org/abs/2405.00492)).
- **Keeping earlier answers in view and asking for a different one** was the only prompting strategy that reached human-level diversity in one benchmark ([NoveltyBench](https://arxiv.org/abs/2504.05228)).
- **Asking for several answers with probabilities** ("Verbalized Sampling") raised diversity 1.6 to 2.1 times ([Zhang et al. 2025](https://arxiv.org/abs/2510.01171)).
- **Banning an earlier answer** works once. One ban nearly tripled divergence (4.5 to 11.9), but by the third ban correctness had collapsed ([Lu et al. 2025](https://arxiv.org/abs/2407.09007)).
- **Comparing each idea with existing work and regenerating** raised rated novelty for about 56% of ideas per round ([SciMON](https://arxiv.org/abs/2305.14259)). Gains stop after two or three rounds in every system studied.
- **Different prompt strategies produce pools that barely overlap**, so mixing strategies adds coverage.

Two corrections to an earlier version of this design:

- **Distant analogies.** In 2,341 design concepts, citing more distant sources of inspiration lowered the odds of being shortlisted by experts ([Chan, Dow & Schunn 2015](https://joelchan.github.io/files/2014-desstudies-nearfar-manuscript.pdf)). Forcing a collision with an unrelated field is not supported as a route to better ideas.
- **"Name the obvious answers and ban them."** No study isolating this exact pattern was found. The nearby evidence supports the mechanism, with the limit of one ban per round.

## 3. Interviews and personal context

- **A two-hour AI interview captures attitudes, with fast-diminishing returns.** Interview-based agents predicted a person's survey answers at 0.83 of that person's own two-week consistency. Four demographic facts alone scored 0.74. Deleting 80% of the interview only dropped the score to 0.79, and a bullet-point summary kept 0.81 ([Park et al., 2026 revision](https://arxiv.org/abs/2411.10109), preprint).
- **An independent test was less favourable.** Across 19 studies, agents built from 500+ answers per person were no more accurate than agents given demographics only, and their answers were less varied than real people's in 94% of outcomes ([Peng et al. 2025](https://arxiv.org/html/2509.19088v2), preprint).
- **Being asked beats writing your own brief.** Model-led questioning matched or beat user-written prompts in most settings at equal or lower effort. People rated their own prompt's coverage at 5.3 out of 7 before seeing test cases and 3.9 after ([GATE, Li et al. 2023](https://ar5iv.labs.arxiv.org/html/2310.11589)).
- **Question choice matters more than question count.** Picking each question by expected information roughly doubled success, from 45% to 93% in one test ([BED-LLM](https://arxiv.org/html/2508.21184v3)). Left to itself, a model interviewer repeats questions and asks things it could guess ([Handa et al. 2024](https://arxiv.org/html/2403.05534)).
- **Length costs answers.** Survey completion fell from 68% to 47% when the announced length went from 10 to 30 minutes, and later answers were shorter and more uniform ([Galesic & Bosnjak 2009](https://academic.oup.com/poq/article/73/2/349/1823115)).

All of these studies measure whether the model predicts or fits the person. None measures whether it produces more original ideas for them.

## 4. Where verified machine originality has come from

- **AlphaGo's move 37** was a move its human-imitating network rated at about 1 in 10,000. Search and a win-probability estimate promoted it anyway. The originality came from an evaluator that did not depend on human opinion. *(Figure from DeepMind's page, not re-checked against a paper.)*
- **FunSearch and AlphaEvolve** pair a model that mutates programs with an automatic scorer and an archive that keeps varied candidates. AlphaEvolve's authors name the need for an automatic evaluator as its main limit ([AlphaEvolve paper](https://arxiv.org/html/2506.13131)).
- **Independent 2026 analyses** find that how the problem is framed matters more than the search algorithm, and that simple baselines match elaborate pipelines ([Gideoni et al. 2026](https://arxiv.org/abs/2602.16805)).
- **Hit rates are low.** DeepMind's prover solved 9 of 353 attempted Erdős problems ([AlphaProof Nexus](https://arxiv.org/html/2605.22763v1)). About 18 AI solutions had no known precedent, while about 15 turned out to be already in the literature ([Tao's wiki](https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems)). A proof checker confirms correctness, not novelty.
- **Without an automatic checker, judging is weak.** LLM judges agreed with experts on non-obviousness 22 to 40% of the time and preferred machine-written questions ([arXiv 2606.12071](https://arxiv.org/html/2606.12071), two experts only). The best judge in a 6,000-comparison study matched human preference 72.6% of the time against a 50% baseline, and most multi-step ideation pipelines scored below the bare model ([Ideation Arena 2026](https://arxiv.org/html/2608.29696v1)).

## 5. What this changes in the design

| Part of the earlier design | Verdict | Change |
|---|---|---|
| Write the default answer first, measure distance from it | Supported | Keep. Differing from visible prior output is the mechanism with the largest measured effect. |
| Ask a very large number of questions | Not supported | Ask 5 to 10 adaptive questions per task, each aimed at a choice the default answer made. Stop when answers stop changing the draft. |
| Growing personal profile | Partly supported | Store a short summary of facts and positions. Summaries performed as well as full transcripts. |
| Generate many candidates | Supported, with method | One session: list, revise to differ, ask for low-probability options, one ban per round, two or three rounds. Mix prompt styles. Give no example ideas. |
| Critic that kills weak ideas | Weak as specified | Use a critic for depth of revision. Do not let a model score novelty. Remove near-duplicates by similarity, check against existing work by search, and have the person pick from a shortlist. |
| Notebook of open questions | Supported indirectly | Also record rejected ideas. Loops without that memory re-proposed old material about 30% of the time. |
| Distant-field analogies | Evidence against | Drop as a default. |

Two additions:

- **Give each surviving idea a test.** A written rebuttal it has to survive, a fact it depends on, or a prediction that can be checked later.
- **Build the simplest version first.** Elaborate pipelines often underperformed a plain model.

## 6. Existing tools (partial)

- **Spiral v3** (Every, October 2025, $25 a month) interviews the user about what they are trying to say, then offers three drafts. It is the closest product found.
- ChatGPT deep research asks a few clarifying questions before a run. ChatGPT, Claude and Gemini all now keep cross-chat memory.
- No tool was found that shows how far an output is from the default answer. This part of the search was not finished, so that is not evidence of a gap.

## Coverage limits

- **Not completed:** whether personal context raises originality, sycophancy and privacy risks, user reaction to being interviewed, most of the product landscape, and most of creativity theory.
- **Unverified numbers:** the figures for AlphaGo, AlphaZero, FunSearch internals and novelty search were taken from memory or search summaries, not re-read in the primary papers.
- **Preprints:** many of the 2025 and 2026 sources are not peer-reviewed. Several studies used older models (GPT-3.5, GPT-4, Claude 3.5), so effect sizes may differ on current ones.
- **Transfer:** no controlled study applies a generate, select and test loop to essays, arguments or product ideas with human-verified outcomes. The design lessons are carried over from code, mathematics and biology.

Full notes with every source are in `research_notes/AI originality and idea diversity/`.
