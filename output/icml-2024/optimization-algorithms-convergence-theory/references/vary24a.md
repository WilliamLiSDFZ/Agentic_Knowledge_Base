---
title: "Optimization without Retraction on the Random Generalized Stiefel Manifold"
source: "https://proceedings.mlr.press/v235/vary24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/vary24a/vary24a.pdf"
categories: ['sampling-and-optimization-on-manifolds', 'optimization-algorithms-convergence-theory']
tags: ['generalized-stiefel-manifold', 'optimization', 'CCA', 'ICA', 'retraction-free']
venue: "ICML 2024"
tldr: "Proposes a retraction-free optimization method for the generalized Stiefel manifold applicable to CCA, ICA, and related problems involving sampled covariance matrices."
---

# Optimization without Retraction on the Random Generalized Stiefel Manifold

**Source**: [https://proceedings.mlr.press/v235/vary24a.html](https://proceedings.mlr.press/v235/vary24a.html)

**TLDR**: Proposes a retraction-free optimization method for the generalized Stiefel manifold applicable to CCA, ICA, and related problems involving sampled covariance matrices.

## Abstract

Optimization over the set of matrices $X$ that satisfy $X^\top B X = I_p$, referred to as the generalized Stiefel manifold, appears in many applications involving sampled covariance matrices such as the canonical correlation analysis (CCA), independent component analysis (ICA), and the generalized eigenvalue problem (GEVP). Solving these problems is typically done by iterative methods that require a fully formed $B$. We propose a cheap stochastic iterative method that solves the optimization problem while having access only to a random estimates of $B$. Our method does not enforce the constraint in every iteration; instead, it produces iterations that converge to critical points on the generalized Stiefel manifold defined in expectation. The method has lower per-iteration cost, requires only matrix multiplications, and has the same convergence rates as its Riemannian optimization counterparts that require the full matrix $B$. Experiments demonstrate its effectiveness in various machine learning applications involving generalized orthogonality constraints, including CCA, ICA, and the GEVP.