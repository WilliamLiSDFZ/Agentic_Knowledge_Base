---
title: "Adam with model exponential moving average is effective for nonconvex optimization"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ac8ec9b4d94c03f0af8c4fe3d5fad4fd-Abstract-Conference.html"
categories: ['stochastic-optimization-convergence-and-variance-reduction']
tags: ['Adam-optimizer', 'exponential-moving-average', 'nonconvex-optimization', 'convergence-theory', 'adaptive-methods']
venue: "NeurIPS 2024"
tldr: "Theoretical analysis shows clipped Adam combined with model EMA provably converges for nonconvex optimization."
---

# Adam with model exponential moving average is effective for nonconvex optimization

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ac8ec9b4d94c03f0af8c4fe3d5fad4fd-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/ac8ec9b4d94c03f0af8c4fe3d5fad4fd-Abstract-Conference.html)

**TLDR**: Theoretical analysis shows clipped Adam combined with model EMA provably converges for nonconvex optimization.

## Abstract

In this work, we offer a theoretical analysis of two modern optimization techniques for training large and complex models: (i) adaptive optimization algorithms, such as Adam, and (ii) the model exponential moving average (EMA). Specifically, we demonstrate that a clipped version of Adam with model EMA achieves the optimal convergence rates in various nonconvex optimization settings, both smooth and nonsmooth. Moreover, when the scale varies significantly across different coordinates, we demonstrate that the coordinate-wise adaptivity of Adam is provably advantageous. Notably, unlike previous analyses of Adam, our analysis crucially relies on its core elements---momentum and discounting factors---as well as model EMA, motivating their wide applications in practice.