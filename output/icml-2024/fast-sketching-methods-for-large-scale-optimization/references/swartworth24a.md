---
title: "Fast Sampling-Based Sketches for Tensors"
source: "https://proceedings.mlr.press/v235/swartworth24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/swartworth24a/swartworth24a.pdf"
categories: ['fast-sketching-methods-for-large-scale-optimization']
tags: ['tensor-sketching', 'l0-sampling', 'l1-embedding']
venue: "ICML 2024"
tldr: "A new sampling-based sketching approach for two- and three-mode tensors achieves efficient ℓ0 sampling and ℓ1 embeddings with improved complexity."
---

# Fast Sampling-Based Sketches for Tensors

**Source**: [https://proceedings.mlr.press/v235/swartworth24a.html](https://proceedings.mlr.press/v235/swartworth24a.html)

**TLDR**: A new sampling-based sketching approach for two- and three-mode tensors achieves efficient ℓ0 sampling and ℓ1 embeddings with improved complexity.

## Abstract

We introduce a new approach for applying sampling-based sketches to two and three mode tensors. We illustrate our technique to construct sketches for the classical problems of $\ell_0$ sampling and producing $\ell_1$ embeddings. In both settings we achieve sketches that can be applied to a rank one tensor in $(\mathbb{R}^d)^{\otimes q}$ (for $q=2,3$) in time scaling with $d$ rather than $d^2$ or $d^3$. Our main idea is a particular sampling construction based on fast convolution which allows us to quickly compute sums over sufficiently random subsets of tensor entries.