---
title: "A Doubly Recursive Stochastic Compositional Gradient Descent Method for Federated Multi-Level Compositional Optimization"
source: "https://proceedings.mlr.press/v235/gao24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gao24a/gao24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'optimization-algorithms-convergence-theory']
tags: ['federated-learning', 'compositional-optimization', 'stochastic-gradient', 'multi-level']
venue: "ICML 2024"
tldr: "A doubly recursive stochastic compositional gradient method is proposed for multi-level compositional optimization in federated settings with improved convergence rates."
---

# A Doubly Recursive Stochastic Compositional Gradient Descent Method for Federated Multi-Level Compositional Optimization

**Source**: [https://proceedings.mlr.press/v235/gao24a.html](https://proceedings.mlr.press/v235/gao24a.html)

**TLDR**: A doubly recursive stochastic compositional gradient method is proposed for multi-level compositional optimization in federated settings with improved convergence rates.

## Abstract

Federated compositional optimization has been actively studied in the past few years. However, existing methods mainly focus on the two-level compositional optimization problem, which cannot be directly applied to the multi-level counterparts. Moreover, the convergence rate of existing federated two-level compositional optimization learning algorithms fails to achieve linear speedup with respect to the number of workers under heterogeneous settings. After identifying the reason for this failure, we developed a novel federated stochastic multi-level compositional optimization algorithm by introducing a novel Jacobian-vector product estimator. This innovation mitigates both the heterogeneity issue and the communication efficiency issue simultaneously. We then theoretically proved that our algorithm can achieve the level-independent and linear speedup convergence rate for nonconvex problems. To our knowledge, this is the first time that a federated learning algorithm can achieve such a favorable convergence rate for multi-level compositional problems. Moreover, experimental results confirm the efficacy of our algorithm.