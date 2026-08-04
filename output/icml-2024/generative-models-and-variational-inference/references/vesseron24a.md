---
title: "On a Neural Implementation of Brenier’s Polar Factorization"
source: "https://proceedings.mlr.press/v235/vesseron24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/vesseron24a/vesseron24a.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-and-optimization-on-manifolds']
tags: ['polar-factorization', 'optimal-transport', 'neural-networks', 'Brenier', 'vector-fields']
venue: "ICML 2024"
tldr: "Proposes a neural network implementation of Brenier's polar factorization theorem for vector fields using optimal transport principles."
---

# On a Neural Implementation of Brenier’s Polar Factorization

**Source**: [https://proceedings.mlr.press/v235/vesseron24a.html](https://proceedings.mlr.press/v235/vesseron24a.html)

**TLDR**: Proposes a neural network implementation of Brenier's polar factorization theorem for vector fields using optimal transport principles.

## Abstract

In 1991, Brenier proved a theorem that generalizes the polar decomposition for square matrices – factored as PSD $\times$ unitary – to any vector field $F:\mathbb{R}^d\rightarrow \mathbb{R}^d$. The theorem, known as the polar factorization theorem, states that any field $F$ can be recovered as the composition of the gradient of a convex function $u$ with a measure-preserving map $M$, namely $F=\nabla u \circ M$. We propose a practical implementation of this far-reaching theoretical result, and explore possible uses within machine learning. The theorem is closely related to optimal transport (OT) theory, and we borrow from recent advances in the field of neural optimal transport to parameterize the potential $u$ as an input convex neural network. The map $M$ can be either evaluated pointwise using $u^*$, the convex conjugate of $u$, through the identity $M=\nabla u^* \circ F$, or learned as an auxiliary network. Because $M$ is, in general, not injective, we consider the additional task of estimating the ill-posed inverse map that can approximate the pre-image measure $M^{-1}$ using a stochastic generator. We illustrate possible applications of Brenier’s polar factorization to non-convex optimization problems, as well as sampling of densities that are not log-concave.