---
title: "Universal Gradient Methods for Stochastic Convex Optimization"
source: "https://proceedings.mlr.press/v235/rodomanov24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/rodomanov24a/rodomanov24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['universal-gradient-methods', 'stochastic-convex-optimization', 'Holder-smoothness', 'adaptive-algorithms', 'oracle-noise']
venue: "ICML 2024"
tldr: "Universal gradient methods are developed for stochastic convex optimization that automatically adapt to both oracle noise and Hölder smoothness without prior knowledge."
---

# Universal Gradient Methods for Stochastic Convex Optimization

**Source**: [https://proceedings.mlr.press/v235/rodomanov24a.html](https://proceedings.mlr.press/v235/rodomanov24a.html)

**TLDR**: Universal gradient methods are developed for stochastic convex optimization that automatically adapt to both oracle noise and Hölder smoothness without prior knowledge.

## Abstract

We develop universal gradient methods for Stochastic Convex Optimization (SCO). Our algorithms automatically adapt not only to the oracle’s noise but also to the Hölder smoothness of the objective function without a priori knowledge of the particular setting. The key ingredient is a novel strategy for adjusting step-size coefficients in the Stochastic Gradient Method (SGD). Unlike AdaGrad, which accumulates gradient norms, our Universal Gradient Method accumulates appropriate combinations of gradientand iterate differences. The resulting algorithm has state-of-the-art worst-case convergence rate guarantees for the entire Hölder class including, in particular, both nonsmooth functions and those with Lipschitz continuous gradient. We also present the Universal Fast Gradient Method for SCO enjoying optimal efficiency estimates.