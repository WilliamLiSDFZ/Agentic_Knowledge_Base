---
title: "On Universally Optimal Algorithms for A/B Testing"
source: "https://proceedings.mlr.press/v235/wang24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24c/wang24c.pdf"
categories: ['online-learning-and-sequential-decision-making', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['best-arm-identification', 'A/B-testing', 'fixed-budget', 'Bernoulli-bandits', 'optimal-algorithms']
venue: "ICML 2024"
tldr: "This paper proves the existence of a universally optimal algorithm for fixed-budget A/B testing that matches the performance of uniform sampling."
---

# On Universally Optimal Algorithms for A/B Testing

**Source**: [https://proceedings.mlr.press/v235/wang24c.html](https://proceedings.mlr.press/v235/wang24c.html)

**TLDR**: This paper proves the existence of a universally optimal algorithm for fixed-budget A/B testing that matches the performance of uniform sampling.

## Abstract

We study the problem of best-arm identification with fixed budget in stochastic multi-armed bandits with Bernoulli rewards. For the problem with two arms, also known as the A/B testing problem, we prove that there is no algorithm that (i) performs as well as the algorithm sampling each arm equally (referred to as the uniform sampling algorithm) in all instances, and that (ii) strictly outperforms uniform sampling on at least one instance. In short, there is no algorithm better than the uniform sampling algorithm. To establish this result, we first introduce the natural class of consistent and stable algorithms, and show that any algorithm that performs as well as the uniform sampling algorithm in all instances belongs to this class. The proof then proceeds by deriving a lower bound on the error rate satisfied by any consistent and stable algorithm, and by showing that the uniform sampling algorithm matches this lower bound. Our results provide a solution to the two open problems presented in (Qin, 2022). For the general problem with more than two arms, we provide a first set of results. We characterize the asymptotic error rate of the celebrated Successive Rejects (SR) algorithm (Audibert et al., 2010) and show that, surprisingly, the uniform sampling algorithm outperforms the SR algorithm in some instances.