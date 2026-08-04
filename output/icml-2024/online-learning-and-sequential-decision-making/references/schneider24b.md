---
title: "Online Learning with Bounded Recall"
source: "https://proceedings.mlr.press/v235/schneider24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/schneider24b/schneider24b.pdf"
categories: ['online-learning-and-sequential-decision-making', 'dynamic-algorithms-and-complexity-theory']
tags: ['online-learning', 'bounded-recall', 'repeated-games', 'regret', 'memory-constraints']
venue: "ICML 2024"
tldr: "Online learning is studied under bounded-recall constraints where algorithms can only access a fixed window of recent rewards, characterizing achievable regret."
---

# Online Learning with Bounded Recall

**Source**: [https://proceedings.mlr.press/v235/schneider24b.html](https://proceedings.mlr.press/v235/schneider24b.html)

**TLDR**: Online learning is studied under bounded-recall constraints where algorithms can only access a fixed window of recent rewards, characterizing achievable regret.

## Abstract

We study the problem of full-information online learning in the “bounded recall” setting popular in the study of repeated games. An online learning algorithm $\mathcal{A}$ is $M$-bounded-recall if its output at time $t$ can be written as a function of the $M$ previous rewards (and not e.g. any other internal state of $\mathcal{A}$). We first demonstrate that a natural approach to constructing bounded-recall algorithms from mean-based no-regret learning algorithms (e.g., running Hedge over the last $M$ rounds) fails, and that any such algorithm incurs constant regret per round. We then construct a stationary bounded-recall algorithm that achieves a per-round regret of $\Theta(1/\sqrt{M})$, which we complement with a tight lower bound. Finally, we show that unlike the perfect recall setting, any low regret bound bounded-recall algorithm must be aware of the ordering of the past $M$ losses – any bounded-recall algorithm which plays a symmetric function of the past $M$ losses must incur constant regret per round.