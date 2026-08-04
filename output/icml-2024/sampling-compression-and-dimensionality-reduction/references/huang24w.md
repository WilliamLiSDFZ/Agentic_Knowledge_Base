---
title: "Quasi-Monte Carlo Features for Kernel Approximation"
source: "https://proceedings.mlr.press/v235/huang24w.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24w/huang24w.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'fast-sketching-methods-for-large-scale-optimization']
tags: ['quasi-monte-carlo', 'kernel-approximation', 'random-features', 'variance-reduction', 'gaussian-kernels']
venue: "ICML 2024"
tldr: "Shows that quasi-Monte Carlo methods improve over standard Monte Carlo random features for kernel approximation with better convergence guarantees."
---

# Quasi-Monte Carlo Features for Kernel Approximation

**Source**: [https://proceedings.mlr.press/v235/huang24w.html](https://proceedings.mlr.press/v235/huang24w.html)

**TLDR**: Shows that quasi-Monte Carlo methods improve over standard Monte Carlo random features for kernel approximation with better convergence guarantees.

## Abstract

Random features (Rahimi & Recht, 2007), based on Monte Carlo (MC) method, is one of the most popular approximation techniques to accelerate kernel methods. We show for a class of kernels, including Gaussian kernels, quasi-Monte Carlo (QMC) methods can be used in place of MC to improve the approximation error from $O_P(1/\sqrt{M})$ to $O(1/M)$ (up to logarithmic factors), for estimating both the kernel function itself and the associated integral operator, where $M$ is the number of features being used. Furthermore, we demonstrate the advantage of QMC features in the case of kernel ridge regression, where theoretically, fewer random features suffice to guarantee the same convergence rate of the excess risk. In practice, the QMC kernel approximation approach is easily implementable and shows superior performance, as supported by the empirical evidence provided in the paper.