---
title: "Bayesian Regret Minimization in Offline Bandits"
source: "https://proceedings.mlr.press/v235/petrik24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/petrik24a/petrik24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'bayesian-optimization-and-surrogate-methods']
tags: ['offline-bandits', 'Bayesian-regret', 'LCB', 'decision-making', 'exploration']
venue: "ICML 2024"
tldr: "Challenges the use of LCB in offline bandits and proposes a new algorithm that minimizes Bayesian regret more effectively."
---

# Bayesian Regret Minimization in Offline Bandits

**Source**: [https://proceedings.mlr.press/v235/petrik24a.html](https://proceedings.mlr.press/v235/petrik24a.html)

**TLDR**: Challenges the use of LCB in offline bandits and proposes a new algorithm that minimizes Bayesian regret more effectively.

## Abstract

We study how to make decisions that minimize Bayesian regret in offline linear bandits. Prior work suggests that one must take actions with maximum lower confidence bound (LCB) on their reward. We argue that reliance on LCB is inherently flawed in this setting and propose a new algorithm that directly minimizes upper-bounds on the Bayesian regret using efficient conic optimization solvers. Our bounds build heavily on new connections to monetary risk measures. Proving a matching lower-bound, we show that our upper-bounds are tight, and by minimizing them we are guaranteed to outperform the LCB approach. Our numerical results on synthetic domains confirm that our approach is superior to maximizing LCB.