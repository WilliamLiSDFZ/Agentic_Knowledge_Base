---
title: "Operator SVD with Neural Networks via Nested Low-Rank Approximation"
source: "https://proceedings.mlr.press/v235/ryu24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ryu24b/ryu24b.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'matrix-geometry-optimization-for-spectral-learning']
tags: ['eigenvalue-decomposition', 'neural-networks', 'low-rank-approximation', 'eigenfunctions', 'operator-SVD']
venue: "ICML 2024"
tldr: "A nested low-rank approximation approach using neural networks is proposed to efficiently compute leading eigenvalues and eigenfunctions of high-dimensional linear operators."
---

# Operator SVD with Neural Networks via Nested Low-Rank Approximation

**Source**: [https://proceedings.mlr.press/v235/ryu24b.html](https://proceedings.mlr.press/v235/ryu24b.html)

**TLDR**: A nested low-rank approximation approach using neural networks is proposed to efficiently compute leading eigenvalues and eigenfunctions of high-dimensional linear operators.

## Abstract

Computing eigenvalue decomposition (EVD) of a given linear operator, or finding its leading eigenvalues and eigenfunctions, is a fundamental task in many machine learning and scientific simulation problems. For high-dimensional eigenvalue problems, training neural networks to parameterize the eigenfunctions is considered as a promising alternative to the classical numerical linear algebra techniques. This paper proposes a new optimization framework based on the low-rank approximation characterization of a truncated singular value decomposition, accompanied by new techniques called nesting for learning the top-$L$ singular values and singular functions in the correct order. The proposed method promotes the desired orthogonality in the learned functions implicitly and efficiently via an unconstrained optimization formulation, which is easy to solve with off-the-shelf gradient-based optimization algorithms. We demonstrate the effectiveness of the proposed optimization framework for use cases in computational physics and machine learning.