---
title: "Optimal Hessian/Jacobian-Free Nonconvex-PL Bilevel Optimization"
source: "https://proceedings.mlr.press/v235/huang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24a/huang24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'neural-network-learning-dynamics-theory']
tags: ['bilevel-optimization', 'nonconvex-optimization', 'hessian-free']
venue: "ICML 2024"
tldr: "Develops optimal Hessian/Jacobian-free algorithms for nonconvex-PL bilevel optimization problems common in meta-learning and hyperparameter tuning."
---

# Optimal Hessian/Jacobian-Free Nonconvex-PL Bilevel Optimization

**Source**: [https://proceedings.mlr.press/v235/huang24a.html](https://proceedings.mlr.press/v235/huang24a.html)

**TLDR**: Develops optimal Hessian/Jacobian-free algorithms for nonconvex-PL bilevel optimization problems common in meta-learning and hyperparameter tuning.

## Abstract

Bilevel optimization is widely applied in many machine learning tasks such as hyper-parameter learning, meta learning and reinforcement learning. Although many algorithms recently have been developed to solve the bilevel optimization problems, they generally rely on the (strongly) convex lower-level problems. More recently, some methods have been proposed to solve the nonconvex-PL bilevel optimization problems, where their upper-level problems are possibly nonconvex, and their lower-level problems are also possibly nonconvex while satisfying Polyak-Łojasiewicz (PL) condition. However, these methods still have a high convergence complexity or a high computation complexity such as requiring compute expensive Hessian/Jacobian matrices and its inverses. In the paper, thus, we propose an efficient Hessian/Jacobian-free method (i.e., HJFBiO) with the optimal convergence complexity to solve the nonconvex-PL bilevel problems. Theoretically, under some mild conditions, we prove that our HJFBiO method obtains an optimal convergence rate of $O(\frac{1}{T})$, where $T$ denotes the number of iterations, and has an optimal gradient complexity of $O(\epsilon^{-1})$ in finding an $\epsilon$-stationary solution. We conduct some numerical experiments on the bilevel PL game and hyper-representation learning task to demonstrate efficiency of our proposed method.