---
title: "Monotone, Bi-Lipschitz, and Polyak-Łojasiewicz Networks"
source: "https://proceedings.mlr.press/v235/wang24p.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24p/wang24p.pdf"
categories: ['adversarial-robustness-and-model-security', 'optimization-algorithms-convergence-theory']
tags: ['bi-Lipschitz', 'invertible-networks', 'Polyak-Łojasiewicz', 'monotone-networks', 'Lipschitz-constraints']
venue: "ICML 2024"
tldr: "BiLipNet introduces invertible neural networks with controllable Lipschitz and inverse Lipschitz constants, enabling robust and monotone architectures."
---

# Monotone, Bi-Lipschitz, and Polyak-Łojasiewicz Networks

**Source**: [https://proceedings.mlr.press/v235/wang24p.html](https://proceedings.mlr.press/v235/wang24p.html)

**TLDR**: BiLipNet introduces invertible neural networks with controllable Lipschitz and inverse Lipschitz constants, enabling robust and monotone architectures.

## Abstract

This paper presents a new bi-Lipschitz invertible neural network, the BiLipNet, which has the ability to smoothly control both its Lipschitzness (output sensitivity to input perturbations) and inverse Lipschitzness (input distinguishability from different outputs). The second main contribution is a new scalar-output network, the PLNet, which is a composition of a BiLipNet and a quadratic potential. We show that PLNet satisfies the Polyak-Łojasiewicz condition and can be applied to learn non-convex surrogate losses with a unique and efficiently-computable global minimum. The central technical element in these networks is a novel invertible residual layer with certified strong monotonicity and Lipschitzness, which we compose with orthogonal layers to build the BiLipNet. The certification of these properties is based on incremental quadratic constraints, resulting in much tighter bounds than can be achieved with spectral normalization. Moreover, we formulate the calculation of the inverse of a BiLipNet – and hence the minimum of a PLNet – as a series of three-operator splitting problems, for which fast algorithms can be applied.