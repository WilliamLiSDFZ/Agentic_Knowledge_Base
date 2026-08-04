---
title: "Convergence and Complexity Guarantee for Inexact First-order Riemannian Optimization Algorithms"
source: "https://proceedings.mlr.press/v235/li24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24b/li24b.pdf"
categories: ['optimization-algorithms-convergence-theory', 'sampling-and-optimization-on-manifolds']
tags: ['Riemannian-optimization', 'inexact-gradient', 'nonconvex-optimization', 'retraction', 'convergence-complexity']
venue: "ICML 2024"
tldr: "Analyzes convergence and complexity of inexact Riemannian gradient descent with approximate gradients and retractions in nonconvex constrained settings."
---

# Convergence and Complexity Guarantee for Inexact First-order Riemannian Optimization Algorithms

**Source**: [https://proceedings.mlr.press/v235/li24b.html](https://proceedings.mlr.press/v235/li24b.html)

**TLDR**: Analyzes convergence and complexity of inexact Riemannian gradient descent with approximate gradients and retractions in nonconvex constrained settings.

## Abstract

We analyze inexact Riemannian gradient descent (RGD) where Riemannian gradients and retractions are inexactly (and cheaply) computed. Our focus is on understanding when inexact RGD converges and what is the complexity in the general nonconvex and constrained setting. We answer these questions in a general framework of tangential Block Majorization-Minimization (tBMM). We establish that tBMM converges to an $\epsilon$-stationary point within $O(\epsilon^{-2})$ iterations. Under a mild assumption, the results still hold when the subproblem is solved inexactly in each iteration provided the total optimality gap is bounded. Our general analysis applies to a wide range of classical algorithms with Riemannian constraints including inexact RGD and proximal gradient method on Stiefel manifolds. We numerically validate that tBMM shows improved performance over existing methods when applied to various problems, including nonnegative tensor decomposition with Riemannian constraints, regularized nonnegative matrix factorization, and low-rank matrix recovery problems.