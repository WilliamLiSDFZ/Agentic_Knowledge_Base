---
title: "Double Momentum Method for Lower-Level Constrained Bilevel Optimization"
source: "https://proceedings.mlr.press/v235/shi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shi24a/shi24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'neural-operators-for-pde-solving']
tags: ['bilevel-optimization', 'momentum-methods', 'hypergradient']
venue: "ICML 2024"
tldr: "A double momentum method is proposed for lower-level constrained bilevel optimization problems arising in machine learning with improved convergence properties."
---

# Double Momentum Method for Lower-Level Constrained Bilevel Optimization

**Source**: [https://proceedings.mlr.press/v235/shi24a.html](https://proceedings.mlr.press/v235/shi24a.html)

**TLDR**: A double momentum method is proposed for lower-level constrained bilevel optimization problems arising in machine learning with improved convergence properties.

## Abstract

Bilevel optimization (BO) has recently gained prominence in many machine learning applications due to its ability to capture the nested structure inherent in these problems. Recently, many hypergradient methods have been proposed as effective solutions for solving large-scale problems. However, current hypergradient methods for the lower-level constrained bilevel optimization (LCBO) problems need very restrictive assumptions, namely, where optimality conditions satisfy the differentiability and invertibility conditions, and lack a solid analysis of the convergence rate. What’s worse, existing methods require either double-loop updates, which are sometimes less efficient. To solve this problem, in this paper, we propose a new hypergradient of LCBO leveraging the theory of nonsmooth implicit function theorem instead of using the restrive assumptions. In addition, we propose a single-loop single-timescale algorithm based on the double-momentum method and adaptive step size method and prove it can return a $(\delta, \epsilon)$-stationary point with $\tilde{\mathcal{O}}(d_2^2\epsilon^{-4})$ iterations. Experiments on two applications demonstrate the effectiveness of our proposed method.