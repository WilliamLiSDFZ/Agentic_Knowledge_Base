---
title: "Dynamic Anisotropic Smoothing for Noisy Derivative-Free Optimization"
source: "https://proceedings.mlr.press/v235/reifenstein24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/reifenstein24a/reifenstein24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'bayesian-optimization-and-surrogate-methods']
tags: ['derivative-free-optimization', 'anisotropic-smoothing', 'noisy-optimization', 'Hessian-approximation', 'adaptive-kernel']
venue: "ICML 2024"
tldr: "A novel derivative-free optimization algorithm is proposed that dynamically adapts a smoothing kernel shape to account for heterogeneous curvature of the objective."
---

# Dynamic Anisotropic Smoothing for Noisy Derivative-Free Optimization

**Source**: [https://proceedings.mlr.press/v235/reifenstein24a.html](https://proceedings.mlr.press/v235/reifenstein24a.html)

**TLDR**: A novel derivative-free optimization algorithm is proposed that dynamically adapts a smoothing kernel shape to account for heterogeneous curvature of the objective.

## Abstract

We propose a novel algorithm that extends the methods of ball smoothing and Gaussian smoothing for noisy derivative-free optimization by accounting for the heterogeneous curvature of the objective function. The algorithm dynamically adapts the shape of the smoothing kernel to approximate the Hessian of the objective function around a local optimum. This approach significantly reduces the error in estimating the gradient from noisy evaluations through sampling. We demonstrate the efficacy of our method through numerical experiments on artificial problems. Additionally, we show improved performance when tuning NP-hard combinatorial optimization solvers compared to existing state-ofthe-art heuristic derivative-free and Bayesian optimization methods.