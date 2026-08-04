---
title: "High-Probability Convergence for Composite and Distributed Stochastic Minimization and Variational Inequalities with Heavy-Tailed Noise"
source: "https://proceedings.mlr.press/v235/gorbunov24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gorbunov24a/gorbunov24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'privacy-preserving-federated-and-distributed-learning']
tags: ['high-probability-convergence', 'heavy-tailed-noise', 'gradient-clipping']
venue: "ICML 2024"
tldr: "This paper provides high-probability convergence guarantees for composite and distributed stochastic optimization under heavy-tailed noise using gradient clipping."
---

# High-Probability Convergence for Composite and Distributed Stochastic Minimization and Variational Inequalities with Heavy-Tailed Noise

**Source**: [https://proceedings.mlr.press/v235/gorbunov24a.html](https://proceedings.mlr.press/v235/gorbunov24a.html)

**TLDR**: This paper provides high-probability convergence guarantees for composite and distributed stochastic optimization under heavy-tailed noise using gradient clipping.

## Abstract

High-probability analysis of stochastic first-order optimization methods under mild assumptions on the noise has been gaining a lot of attention in recent years. Typically, gradient clipping is one of the key algorithmic ingredients to derive good high-probability guarantees when the noise is heavy-tailed. However, if implemented naively, clipping can spoil the convergence of the popular methods for composite and distributed optimization (Prox-SGD/Parallel SGD) even in the absence of any noise. Due to this reason, many works on high-probability analysis consider only unconstrained non-distributed problems, and the existing results for composite/distributed problems do not include some important special cases (like strongly convex problems) and are not optimal. To address this issue, we propose new stochastic methods for composite and distributed optimization based on the clipping of stochastic gradient differences and prove tight high-probability convergence results (including nearly optimal ones) for the new methods. In addition, we also develop new methods for composite and distributed variational inequalities and analyze the high-probability convergence of these methods.