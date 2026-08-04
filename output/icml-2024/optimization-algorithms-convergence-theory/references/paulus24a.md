---
title: "LPGD: A General Framework for Backpropagation through Embedded Optimization Layers"
source: "https://proceedings.mlr.press/v235/paulus24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/paulus24a/paulus24a.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'optimization-algorithms-convergence-theory']
tags: ['optimization-layers', 'backpropagation', 'differentiable-optimization', 'neural-combinatorial']
venue: "ICML 2024"
tldr: "Introduces LPGD, a general framework for backpropagating through embedded optimization layers by addressing degenerate derivatives in parameterized optimization problems."
---

# LPGD: A General Framework for Backpropagation through Embedded Optimization Layers

**Source**: [https://proceedings.mlr.press/v235/paulus24a.html](https://proceedings.mlr.press/v235/paulus24a.html)

**TLDR**: Introduces LPGD, a general framework for backpropagating through embedded optimization layers by addressing degenerate derivatives in parameterized optimization problems.

## Abstract

Embedding parameterized optimization problems as layers into machine learning architectures serves as a powerful inductive bias. Training such architectures with stochastic gradient descent requires care, as degenerate derivatives of the embedded optimization problem often render the gradients uninformative. We propose Lagrangian Proximal Gradient Descent (LPGD), a flexible framework for training architectures with embedded optimization layers that seamlessly integrates into automatic differentiation libraries. LPGD efficiently computes meaningful replacements of the degenerate optimization layer derivatives by re-running the forward solver oracle on a perturbed input. LPGD captures various previously proposed methods as special cases, while fostering deep links to traditional optimization methods. We theoretically analyze our method and demonstrate on historical and synthetic data that LPGD converges faster than gradient descent even in a differentiable setup.