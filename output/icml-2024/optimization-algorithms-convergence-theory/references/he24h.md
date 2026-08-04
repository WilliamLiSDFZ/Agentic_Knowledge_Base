---
title: "Riemannian Accelerated Zeroth-order Algorithm: Improved Robustness and Lower Query Complexity"
source: "https://proceedings.mlr.press/v235/he24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/he24h/he24h.pdf"
categories: ['sampling-and-optimization-on-manifolds', 'optimization-algorithms-convergence-theory']
tags: ['zeroth-order-optimization', 'riemannian-manifolds', 'robustness']
venue: "ICML 2024"
tldr: "A Riemannian accelerated zeroth-order algorithm is proposed with improved robustness and lower query complexity for optimization on manifolds without gradient access."
---

# Riemannian Accelerated Zeroth-order Algorithm: Improved Robustness and Lower Query Complexity

**Source**: [https://proceedings.mlr.press/v235/he24h.html](https://proceedings.mlr.press/v235/he24h.html)

**TLDR**: A Riemannian accelerated zeroth-order algorithm is proposed with improved robustness and lower query complexity for optimization on manifolds without gradient access.

## Abstract

Optimization problems with access to only zeroth-order information of the objective function on Riemannian manifolds arise in various applications, spanning from statistical learning to robot learning. While various zeroth-order algorithms have been proposed in Euclidean space, they are not inherently designed to handle the challenging constraints imposed by Riemannian manifolds. The proper adaptation of zeroth-order techniques to Riemannian manifolds remained unknown until the pioneering work of (Li et al., 2023a). However, zeroth-order algorithms are widely observed to converge slowly and be unstable in practice. To alleviate these issues, we propose a Riemannian accelerated zeroth-order algorithm with improved robustness. Regarding efficiency, our accelerated algorithm has the function query complexity of $\mathcal{O}(\epsilon^{-7/4}d)$ for finding an $\epsilon$-approximate first-order stationary point. By introducing a small perturbation, it exhibits a function query complexity of $\tilde{\mathcal{O}}(\epsilon^{-7/4}d)$ for seeking a second-order stationary point with a high probability, matching state-of-the-art result in Euclidean space. Moreover, we further establish the almost sure convergence in the asymptotic sense through the Stable Manifold Theorem. Regarding robustness, our algorithm requires larger smoothing parameters in the order of $\tilde{\mathcal{O}}(\epsilon^{7/8}d^{-1/2})$, improving the existing result by a factor of $\tilde{\mathcal{O}}(\epsilon^{3/4})$.