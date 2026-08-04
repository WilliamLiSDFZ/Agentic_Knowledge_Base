---
title: "Implicit Bias of AdamW: $\ell_∞$-Norm Constrained Optimization"
source: "https://proceedings.mlr.press/v235/xie24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xie24e/xie24e.pdf"
categories: ['optimization-algorithms-convergence-theory', 'neural-network-learning-dynamics-theory']
tags: ['AdamW', 'implicit-bias', 'weight-decay']
venue: "ICML 2024"
tldr: "Theoretically characterizes the implicit bias of AdamW as favoring ℓ∞-norm constrained solutions, explaining its generalization advantage over Adam with ℓ2 regularization."
---

# Implicit Bias of AdamW: $\ell_∞$-Norm Constrained Optimization

**Source**: [https://proceedings.mlr.press/v235/xie24e.html](https://proceedings.mlr.press/v235/xie24e.html)

**TLDR**: Theoretically characterizes the implicit bias of AdamW as favoring ℓ∞-norm constrained solutions, explaining its generalization advantage over Adam with ℓ2 regularization.

## Abstract

Adam with decoupled weight decay, also known as AdamW, is widely acclaimed for its superior performance in language modeling tasks, surpassing Adam with $\ell_2$ regularization in terms of generalization and optimization. However, this advantage is not theoretically well-understood. One challenge here is that though intuitively Adam with $\ell_2$ regularization optimizes the $\ell_2$ regularized loss, it is not clear if AdamW optimizes a specific objective. In this work, we make progress toward understanding the benefit of AdamW by showing that it implicitly performs constrained optimization. More concretely, we show in the full-batch setting, if AdamW converges with any non-increasing learning rate schedule whose partial sum diverges, it must converge to a KKT point of the original loss under the constraint that the $\ell_\infty$ norm of the parameter is bounded by the inverse of the weight decay factor. This result is built on the observation that Adam can be viewed as a smoothed version of SignGD, which is the normalized steepest descent with respect to $\ell_\infty$ norm, and a surprising connection between normalized steepest descent with weight decay and Frank-Wolfe.