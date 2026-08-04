---
title: "Smoothing Proximal Gradient Methods for Nonsmooth Sparsity Constrained Optimization: Optimality Conditions and Global Convergence"
source: "https://proceedings.mlr.press/v235/yuan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yuan24a/yuan24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['sparsity-constrained-optimization', 'proximal-gradient', 'nonsmooth', 'convergence']
venue: "ICML 2024"
tldr: "Smoothing proximal gradient methods with global convergence guarantees for nonsmooth sparsity-constrained optimization problems."
---

# Smoothing Proximal Gradient Methods for Nonsmooth Sparsity Constrained Optimization: Optimality Conditions and Global Convergence

**Source**: [https://proceedings.mlr.press/v235/yuan24a.html](https://proceedings.mlr.press/v235/yuan24a.html)

**TLDR**: Smoothing proximal gradient methods with global convergence guarantees for nonsmooth sparsity-constrained optimization problems.

## Abstract

Nonsmooth sparsity constrained optimization encompasses a broad spectrum of applications in machine learning. This problem is generally non-convex and NP-hard. Existing solutions to this problem exhibit several notable limitations, including their inability to address general nonsmooth problems, tendency to yield weaker optimality conditions, and lack of comprehensive convergence analysis. This paper considers Smoothing Proximal Gradient Methods (SPGM) as solutions to nonsmooth sparsity constrained optimization problems. Two specific variants of SPGM are explored: one based on Iterative Hard Thresholding (SPGM-IHT) and the other on Block Coordinate Decomposition (SPGM-BCD). It is shown that the SPGM-BCD algorithm finds stronger stationary points compared to previous methods. Additionally, novel theories for analyzing the convergence rates to approximate global optimal solutions of both the SPGM-IHT and SPGM-BCD algorithms are developed. Our theoretical bounds, capitalizing on the intrinsic sparsity of the optimization problem, are on par with the best-known error bounds available to date. Finally, numerical experiments reveal that SPGM-IHT performs comparably to current IHT-style methods, while SPGM-BCD consistently surpasses them.