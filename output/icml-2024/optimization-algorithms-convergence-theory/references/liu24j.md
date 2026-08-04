---
title: "Zeroth-Order Methods for Constrained Nonconvex Nonsmooth Stochastic Optimization"
source: "https://proceedings.mlr.press/v235/liu24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24j/liu24j.pdf"
categories: ['optimization-algorithms-convergence-theory']
tags: ['zeroth-order', 'nonconvex', 'constrained-optimization']
venue: "ICML 2024"
tldr: "This paper proposes zeroth-order methods for constrained nonconvex nonsmooth stochastic optimization without reducing to unconstrained formulations."
---

# Zeroth-Order Methods for Constrained Nonconvex Nonsmooth Stochastic Optimization

**Source**: [https://proceedings.mlr.press/v235/liu24j.html](https://proceedings.mlr.press/v235/liu24j.html)

**TLDR**: This paper proposes zeroth-order methods for constrained nonconvex nonsmooth stochastic optimization without reducing to unconstrained formulations.

## Abstract

This paper studies the problem of solving nonconvex nonsmooth optimization over a closed convex set. Most previous works tackle such problems by transforming the constrained problem into an unconstrained problem that can be solved by the techniques developed in the unconstrained setting. However, they only provide asymptotic convergence analysis for their methods. In this work, we provide the non-asymptotic analysis for solving constrained nonconvex nonsmooth optimization. We first generalize classical gradient mapping and the Frank–Wolfe gap in the nonsmooth setting. Then we introduce novel notions of approximate stationarity concerning such generalized quantities. We also propose several stochastic zeroth-order algorithms for the problem, along with their non-asymptotic convergence guarantees of obtaining the proposed approximate stationarity. Finally, we conduct numerical experiments that demonstrate the effectiveness of our algorithms.