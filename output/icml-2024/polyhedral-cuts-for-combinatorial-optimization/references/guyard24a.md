---
title: "A New Branch-and-Bound Pruning Framework for $\ell_0$-Regularized Problems"
source: "https://proceedings.mlr.press/v235/guyard24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/guyard24a/guyard24a.pdf"
categories: ['polyhedral-cuts-for-combinatorial-optimization', 'submodular-optimization-and-combinatorial-algorithms']
tags: ['branch-and-bound', 'L0-regularization', 'sparse-learning']
venue: "ICML 2024"
tldr: "A new pruning framework for branch-and-bound algorithms significantly accelerates solving L0-regularized learning problems by improving feasibility-based bounding tests."
---

# A New Branch-and-Bound Pruning Framework for $\ell_0$-Regularized Problems

**Source**: [https://proceedings.mlr.press/v235/guyard24a.html](https://proceedings.mlr.press/v235/guyard24a.html)

**TLDR**: A new pruning framework for branch-and-bound algorithms significantly accelerates solving L0-regularized learning problems by improving feasibility-based bounding tests.

## Abstract

We consider the resolution of learning problems involving $\ell_0$-regularization via Branch-and- Bound (BnB) algorithms. These methods explore regions of the feasible space of the problem and check whether they do not contain solutions through “pruning tests”. In standard implementations, evaluating a pruning test requires to solve a convex optimization problem, which may result in computational bottlenecks. In this paper, we present an alternative to implement pruning tests for some generic family of $\ell_0$-regularized problems. Our proposed procedure allows the simultaneous assessment of several regions and can be embedded in standard BnB implementations with a negligible computational overhead. We show through numerical simulations that our pruning strategy can improve the solving time of BnB procedures by several orders of magnitude for typical problems encountered in machine-learning applications.