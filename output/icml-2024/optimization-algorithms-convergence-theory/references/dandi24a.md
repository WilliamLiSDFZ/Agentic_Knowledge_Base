---
title: "The Benefits of Reusing Batches for Gradient Descent in Two-Layer Networks: Breaking the Curse of Information and Leap Exponents"
source: "https://proceedings.mlr.press/v235/dandi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dandi24a/dandi24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'optimization-algorithms-convergence-theory']
tags: ['two-layer-networks', 'gradient-descent', 'multi-index-functions', 'training-dynamics', 'multi-pass']
venue: "ICML 2024"
tldr: "Shows that multi-pass gradient descent on two-layer networks can learn a broader class of multi-index functions than single-pass, breaking information and leap exponent barriers."
---

# The Benefits of Reusing Batches for Gradient Descent in Two-Layer Networks: Breaking the Curse of Information and Leap Exponents

**Source**: [https://proceedings.mlr.press/v235/dandi24a.html](https://proceedings.mlr.press/v235/dandi24a.html)

**TLDR**: Shows that multi-pass gradient descent on two-layer networks can learn a broader class of multi-index functions than single-pass, breaking information and leap exponent barriers.

## Abstract

We investigate the training dynamics of two-layer neural networks when learning multi-index target functions. We focus on multi-pass gradient descent (GD) that reuses the batches multiple times and show that it significantly changes the conclusion about which functions are learnable compared to single-pass gradient descent. In particular, multi-pass GD with finite stepsize is found to overcome the limitations of gradient flow and single-pass GD given by the information exponent (Ben Arous et al., 2021) and leap exponent (Abbe et al., 2023) of the target function. We show that upon re-using batches, the network achieves in just two time steps an overlap with the target subspace even for functions not satisfying the staircase property (Abbe et al., 2021). We characterize the (broad) class of functions efficiently learned in finite time. The proof of our results is based on the analysis of the Dynamical Mean-Field Theory (DMFT). We further provide a closed-form description of the dynamical process of the low-dimensional projections of the weights, and numerical experiments illustrating the theory.