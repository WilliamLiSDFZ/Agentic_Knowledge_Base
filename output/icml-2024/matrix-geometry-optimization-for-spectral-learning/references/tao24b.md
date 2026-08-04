---
title: "Learning in Feature Spaces via Coupled Covariances: Asymmetric Kernel SVD and Nyström method"
source: "https://proceedings.mlr.press/v235/tao24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tao24b/tao24b.pdf"
categories: ['matrix-geometry-optimization-for-spectral-learning', 'sufficient-dimension-reduction-correlation-methods']
tags: ['asymmetric-kernels', 'singular-value-decomposition', 'Nyström-method']
venue: "ICML 2024"
tldr: "Coupled covariance operators in feature spaces are used to develop asymmetric kernel SVD and a corresponding Nyström approximation method for efficient learning."
---

# Learning in Feature Spaces via Coupled Covariances: Asymmetric Kernel SVD and Nyström method

**Source**: [https://proceedings.mlr.press/v235/tao24b.html](https://proceedings.mlr.press/v235/tao24b.html)

**TLDR**: Coupled covariance operators in feature spaces are used to develop asymmetric kernel SVD and a corresponding Nyström approximation method for efficient learning.

## Abstract

In contrast with Mercer kernel-based approaches as used e.g. in Kernel Principal Component Analysis (KPCA), it was previously shown that Singular Value Decomposition (SVD) inherently relates to asymmetric kernels and Asymmetric Kernel Singular Value Decomposition (KSVD) has been proposed. However, the existing formulation to KSVD cannot work with infinite-dimensional feature mappings, the variational objective can be unbounded, and needs further numerical evaluation and exploration towards machine learning. In this work, i) we introduce a new asymmetric learning paradigm based on coupled covariance eigenproblem (CCE) through covariance operators, allowing infinite-dimensional feature maps. The solution to CCE is ultimately obtained from the SVD of the induced asymmetric kernel matrix, providing links to KSVD. ii) Starting from the integral equations corresponding to a pair of coupled adjoint eigenfunctions, we formalize the asymmetric Nyström method through a finite sample approximation to speed up training. iii) We provide the first empirical evaluations verifying the practical utility and benefits of KSVD and compare with methods resorting to symmetrization or linear SVD across multiple tasks.