---
title: "Posterior Sampling-Based Bayesian Optimization with Tighter Bayesian Regret Bounds"
source: "https://proceedings.mlr.press/v235/takeno24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/takeno24a/takeno24a.pdf"
categories: ['bayesian-optimization-and-surrogate-methods']
tags: ['bayesian-optimization', 'Thompson-sampling', 'regret-bounds']
venue: "ICML 2024"
tldr: "A posterior sampling-based Bayesian optimization algorithm achieves tighter Bayesian regret bounds than GP-UCB and standard Thompson sampling."
---

# Posterior Sampling-Based Bayesian Optimization with Tighter Bayesian Regret Bounds

**Source**: [https://proceedings.mlr.press/v235/takeno24a.html](https://proceedings.mlr.press/v235/takeno24a.html)

**TLDR**: A posterior sampling-based Bayesian optimization algorithm achieves tighter Bayesian regret bounds than GP-UCB and standard Thompson sampling.

## Abstract

Among various acquisition functions (AFs) in Bayesian optimization (BO), Gaussian process upper confidence bound (GP-UCB) and Thompson sampling (TS) are well-known options with established theoretical properties regarding Bayesian cumulative regret (BCR). Recently, it has been shown that a randomized variant of GP-UCB achieves a tighter BCR bound compared with GP-UCB, which we call the tighter BCR bound for brevity. Inspired by this study, this paper first shows that TS achieves the tighter BCR bound. On the other hand, GP-UCB and TS often practically suffer from manual hyperparameter tuning and over-exploration issues, respectively. Therefore, we analyze yet another AF called a probability of improvement from the maximum of a sample path (PIMS). We show that PIMS achieves the tighter BCR bound and avoids the hyperparameter tuning, unlike GP-UCB. Furthermore, we demonstrate a wide range of experiments, focusing on the effectiveness of PIMS that mitigates the practical issues of GP-UCB and TS.