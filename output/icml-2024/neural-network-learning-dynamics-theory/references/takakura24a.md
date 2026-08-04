---
title: "Mean-field Analysis on Two-layer Neural Networks from a Kernel Perspective"
source: "https://proceedings.mlr.press/v235/takakura24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/takakura24a/takakura24a.pdf"
categories: ['neural-network-learning-dynamics-theory']
tags: ['mean-field', 'neural-networks', 'kernel-methods']
venue: "ICML 2024"
tldr: "Feature learning in two-layer neural networks in the mean-field regime is analyzed through a two-timescale kernel perspective."
---

# Mean-field Analysis on Two-layer Neural Networks from a Kernel Perspective

**Source**: [https://proceedings.mlr.press/v235/takakura24a.html](https://proceedings.mlr.press/v235/takakura24a.html)

**TLDR**: Feature learning in two-layer neural networks in the mean-field regime is analyzed through a two-timescale kernel perspective.

## Abstract

In this paper, we study the feature learning ability of two-layer neural networks in the mean-field regime through the lens of kernel methods. To focus on the dynamics of the kernel induced by the first layer, we utilize a two-timescale limit, where the second layer moves much faster than the first layer. In this limit, the learning problem is reduced to the minimization problem over the intrinsic kernel. Then, we show the global convergence of the mean-field Langevin dynamics and derive time and particle discretization error. We also demonstrate that two-layer neural networks can learn a union of multiple reproducing kernel Hilbert spaces more efficiently than any kernel methods, and neural networks aquire data-dependent kernel which aligns with the target function. In addition, we develop a label noise procedure, which converges to the global optimum and show that the degrees of freedom appears as an implicit reguralization.