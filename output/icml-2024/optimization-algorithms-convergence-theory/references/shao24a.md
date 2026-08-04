---
title: "Improved Dimensionality Dependence for Zeroth-Order Optimisation over Cross-Polytopes"
source: "https://proceedings.mlr.press/v235/shao24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shao24a/shao24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'sampling-compression-and-dimensionality-reduction']
tags: ['zeroth-order-optimization', 'cross-polytopes', 'bandit-convex-optimization']
venue: "ICML 2024"
tldr: "An improved algorithm is proposed for gradient-free optimization over cross-polytopes with better dimensionality dependence for applications like adversarial attacks and sparse regression."
---

# Improved Dimensionality Dependence for Zeroth-Order Optimisation over Cross-Polytopes

**Source**: [https://proceedings.mlr.press/v235/shao24a.html](https://proceedings.mlr.press/v235/shao24a.html)

**TLDR**: An improved algorithm is proposed for gradient-free optimization over cross-polytopes with better dimensionality dependence for applications like adversarial attacks and sparse regression.

## Abstract

This work proposes an algorithm improving the dimensionality dependence for gradient-free optimisation over cross-polytopes, which has many applications such as adversarial attacks, explainable AI and sparse regression. For bandit convex optimisation with two-point feedback over cross-polytopes, the state-of-the-art algorithms have a dimensionality dependence of $\mathcal{O}(\sqrt{d\log d})$, while the known lower bound is of the form $\Omega(\sqrt{d(\log d)^{-1}})$. We propose a mirror descent algorithm equipped with a symmetric version of the negative $\frac{1}{2}$-Tsallis entropy. Combined with an $\ell_1$-ellipsoidal smoothing-based gradient estimator, the proposed algorithm guarantees a dimensionality dependence on $\mathcal{O}(\sqrt{d})$, which improves the state-of-the-art algorithms by a factor of $\sqrt{\log d}$. The idea can be further applied to optimising non-smooth and non-convex functions. We propose an algorithm with a convergence depending on $\mathcal{O}(d)$, which is the best-known dimensionality dependence.