---
title: "A Study of First-Order Methods with a Deterministic Relative-Error Gradient Oracle"
source: "https://proceedings.mlr.press/v235/hallak24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hallak24a/hallak24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'fast-sketching-methods-for-large-scale-optimization']
tags: ['gradient-oracle', 'relative-error', 'projected-gradient', 'conditional-gradient', 'convergence']
venue: "ICML 2024"
tldr: "Analyzes convergence guarantees of projected and conditional gradient methods under deterministic biased relative-error gradient oracles."
---

# A Study of First-Order Methods with a Deterministic Relative-Error Gradient Oracle

**Source**: [https://proceedings.mlr.press/v235/hallak24a.html](https://proceedings.mlr.press/v235/hallak24a.html)

**TLDR**: Analyzes convergence guarantees of projected and conditional gradient methods under deterministic biased relative-error gradient oracles.

## Abstract

This paper studies the theoretical guarantees of the classical projected gradient and conditional gradient methods applied to constrained optimization problems with biased relative-error gradient oracles. These oracles are used in various settings, such as distributed optimization systems or derivative-free optimization, and are particularly common when gradients are compressed, quantized, or estimated via finite differences computations. Several settings are investigated: Optimization over the box with a coordinate-wise erroneous gradient oracle, optimization over a general compact convex set, and three more specific scenarios. Convergence guarantees are established with respect to the relative-error magnitude, and in particular, we show that the conditional gradient is invariant to relative-error when applied over the box with a coordinate-wise erroneous gradient oracle, and the projected gradient maintains its convergence guarantees when optimizing a nonconvex objective function.