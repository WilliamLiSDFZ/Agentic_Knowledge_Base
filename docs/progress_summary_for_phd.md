Hi Peijia,

I'm still working on the MLEvolve knowledge base and I'd like to share an update. I also
have some questions about what to do next.

All of this builds on Haoming's original pipeline. The paper fetching, the clustering into
categories, and the per-paper technique extraction were already there. What I mainly worked
on is the retrieval side, and testing whether the KB actually helps.

## What I did

**1. Fixed bugs in the KB pipeline.** A few papers were being dropped or given the wrong
category. I fixed those and started an update log so every change is written down.

**2. Found two problems in retrieval.** The old version asked the LLM to pick up to 5
category names, so I replaced that with semantic search over the papers. When I checked how
well it worked, I found two problems:

  (a) We were searching with the whole competition description. That text is mostly rules
      and prizes, so the search query was very vague.
  (b) All the paper vectors pointed in almost the same direction, because every paper in the
      corpus is an ML paper.

I fixed the first by adding a step that rewrites the description into a short task summary.
I fixed the second by subtracting the average vector. Together these took the number of
on-topic papers in the top 10 from 3 to 9.

**3. Made retrieval cheaper.** Before, we had to read every paper PDF up front. Now we search
the abstracts first and only read the full PDFs of the papers we actually retrieved, at most
20 per task, and they are cached so later tasks reuse them.

**4. Ran A/B tests** on OpenADMET, spooky-author-identification, and jigsaw toxic comments.

The results are not good. MLEvolve with the paper KB performs worse on both OpenADMET and
spooky-author-identification. For jigsaw I ran 3 seeds: two were slightly better with the KB
(+0.005 and +0.0002 AUC) but the third was worse by more than the best one gained (-0.007),
so on average there is no difference. So it seems like the knowledge base does not help, and
sometimes hurts.

## Two problems I found afterwards

**The KB text was going into the prompt in the wrong place.** It was being pasted into a
section called "Pretrained Model Strategy", right under a line telling the model to "copy the
code template exactly". So paper techniques were shown to the model as if they were
recommended pretrained models. All the experiments above ran with this bug. I have fixed it,
so those results probably need to be re-run.

**The KB only reaches the drafting step.** Out of about 15 solutions the agent produces in a
run, only the first 3 ever see the knowledge, so it cannot affect most of the search. I've
added an option to also show it during the improvement step, but it is off by default and I
haven't tested it yet.

## Comparing with AutoMind

I read the AutoMind paper. Their KB is very similar to ours and they report a positive result
(removing their KB costs 11.8% win rate). Two main differences:

  1. **Their knowledge base is mostly Kaggle solutions, not papers** — 3,237 forum posts from
     455 competitions. Ours is 100% papers. I checked our corpus and only about 0.2% of it is
     about the things that actually win competitions (feature engineering, cross-validation,
     ensembling, boosting). Most of it is theory and LLM research.
  2. **They insert papers in the drafting stage and Kaggle tricks in the improvement stage.**
     We only inject papers, and only in drafting.

Some things our system does that theirs does not:

  1. We pull out individual techniques from each paper and label whether the effect was
     positive or negative (this part was already in the pipeline before I took over), and my
     retrieval now works at the technique level instead of the paper level.
  2. They add tags to each paper and task and use those for retrieval. We use embeddings
     directly, plus the average-vector removal and the task summary described above.

## Three ideas, and I'm not sure where to start

  1. Turn on the improvement-step injection and re-run the test. The code is done but I
     haven't tested it yet.
  2. Add Kaggle solution write-ups to the KB, similar to AutoMind.
  3. Reproduce AutoMind's whole KB design on MLEvolve (their corpus, their label-based
     retrieval, papers→draft and tricks→improve).

One more idea I had: MLEvolve already gives the improvement step 2 successful and 2 failed
attempts from its own run, through the global memory. Those come from real results on the
actual dataset, while paper techniques are generic. Maybe the memory is simply more useful and
the papers are just extra noise. Both are config switches, so testing KB on/off together with
memory on/off would be cheap, and AutoMind cannot run this test because it has no memory of
its own runs.

## Questions

  1. Which of these should I start with?
  2. I'm also worried about how we measure the difference. Two runs with the same setting can
     differ by about 0.007 AUC, but the difference we are trying to measure is around 0.001.
     AutoMind avoids this by averaging over 15 tasks with 3 runs each and reporting one
     win-rate number. Should we switch to something like that, or use shorter runs so we can
     afford more repeats?
  3. Is it okay for me to keep making small changes inside MLEvolve (prompts, config
     switches), or should I keep everything on the knowledge base side?

Thanks,
Yuze
