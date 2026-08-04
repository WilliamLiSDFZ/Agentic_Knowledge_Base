---
title: "Sarah Frank-Wolfe: Methods for Constrained Optimization with Best Rates and Practical Features"
source: "https://proceedings.mlr.press/v235/beznosikov24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/beznosikov24a/beznosikov24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'fast-sketching-methods-for-large-scale-optimization']
tags: ['Frank-Wolfe', 'constrained-optimization', 'stochastic-optimization', 'convergence', 'machine-learning']
venue: "ICML 2024"
tldr: "Proposes Sarah Frank-Wolfe, a stochastic variant of the Frank-Wolfe method achieving best known convergence rates with practical features for constrained optimization."
---

# Sarah Frank-Wolfe: Methods for Constrained Optimization with Best Rates and Practical Features

**Source**: [https://proceedings.mlr.press/v235/beznosikov24a.html](https://proceedings.mlr.press/v235/beznosikov24a.html)

**TLDR**: Proposes Sarah Frank-Wolfe, a stochastic variant of the Frank-Wolfe method achieving best known convergence rates with practical features for constrained optimization.

## Abstract

The Frank-Wolfe (FW) method is a popular approach for solving optimization problems with structured constraints that arise in machine learning applications. In recent years, stochastic versions of FW have gained popularity, motivated by large datasets for which the computation of the full gradient is prohibitively expensive. In this paper, we present two new variants of the FW algorithms for stochastic finite-sum minimization. Our algorithms have the best convergence guarantees of existing stochastic FW approaches for both convex and non-convex objective functions. Our methods do not have the issue of permanently collecting large batches, which is common to many stochastic projection-free approaches. Moreover, our second approach does not require either large batches or full deterministic gradients, which is a typical weakness of many techniques for finite-sum problems. The faster theoretical rates of our approaches are confirmed experimentally.