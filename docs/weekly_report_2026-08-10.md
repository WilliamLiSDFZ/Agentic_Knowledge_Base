# Weekly report — Aug 4 to Aug 10

**Short version:** I finished the A/B experiments on the knowledge base. The result is
negative — the KB does not improve MLEvolve, and on one task it clearly hurts. While looking
for the reason I found a real bug in how the KB text was inserted into the prompt, so these
results will need to be re-run once it is fixed.

## Experiments

I ran paired tests (same setup, knowledge base on vs off) with official mle-bench scoring.

| task | metric | baseline | with KB | result |
|---|---|---|---|---|
| OpenADMET | lower better | 0.678 | 0.741 / 0.726 | KB worse |
| spooky-author-identification | log loss, lower better | **0.2366** (silver) | 0.2883 (bronze) | KB worse at every ensemble size |
| jigsaw toxic comments | ROC AUC, higher better | — | — | no difference |

For jigsaw I ran 3 repeats, since one run is not enough to trust. The difference between the
two arms was +0.005, +0.0002, and −0.007, so the average is slightly negative and clearly not
significant (t = −0.34).

## Two problems I found

**1. The KB text was inserted in the wrong place.** It was being pasted into a prompt section
called "Pretrained Model Strategy", right under a line telling the model to "copy the code
template exactly". So paper techniques were being shown as if they were recommended pretrained
models. Every experiment above ran with this bug. I have fixed it.

**2. The KB only reached the drafting step.** The agent produces about 15 solutions per run,
but only the first 3 ever saw the knowledge. I added an option to also show it during the
improvement step. It is off by default so it does not affect any running experiment.

## Comparison with AutoMind

I read the AutoMind paper (Zhejiang University / Ant Group). They build a very similar
knowledge base and report that it helps: removing it costs 11.8% win rate. Two differences
stand out.

- **Their knowledge base is mostly Kaggle solutions**, not papers — 3,237 forum posts from 455
  competitions. Ours is 100% papers. I audited our corpus: of about 23,000 papers, only 49
  (0.2%) are about the things that actually decide competitions — feature engineering,
  cross-validation, ensembling, boosting. 21% is theory and 19% is LLM research.
- **They send the two types to different places**: papers when drafting a new solution,
  Kaggle tricks when improving an existing one.

So the two biggest differences between us and a system that works are the *kind* of knowledge
and *where* it is inserted — which matches the two problems above.

## A measurement problem I would like your view on

Two runs of the *same* setting differ by about 0.007 AUC, while the effect we are trying to
measure is around 0.001. To detect something that small we would need roughly 70 paired runs,
which is far more compute than we have. AutoMind avoids this by averaging over 15 tasks with 3
runs each and reporting a single win-rate number.

Should we switch to that kind of aggregate metric, or use shorter runs so we can afford more
repeats? I do not think it is worth starting more experiments until this is settled, because
otherwise the results will keep coming out inconclusive.

## Next week

1. Test the knowledge base together with MLEvolve's own memory. The improvement step already
   receives 2 successful and 2 failed attempts from the current run, measured on the real
   dataset, while paper techniques are generic. It is possible the internal memory is simply
   better and the papers add noise. Both are config switches, so this is cheap.
2. Start collecting Kaggle solution write-ups, since this is the clearest gap.
3. Re-run the A/B with the prompt bug fixed and the improvement-step injection on.
