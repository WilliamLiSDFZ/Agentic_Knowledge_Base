---
title: "From Inverse Optimization to Feasibility to ERM"
source: "https://proceedings.mlr.press/v235/mishra24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mishra24a/mishra24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'neural-symbolic-combinatorial-optimization-learning']
tags: ['inverse-optimization', 'contextual-learning', 'empirical-risk-minimization']
venue: "ICML 2024"
tldr: "Reformulates contextual inverse optimization as a feasibility and empirical risk minimization problem, enabling efficient learning of unknown optimization parameters."
---

# From Inverse Optimization to Feasibility to ERM

**Source**: [https://proceedings.mlr.press/v235/mishra24a.html](https://proceedings.mlr.press/v235/mishra24a.html)

**TLDR**: Reformulates contextual inverse optimization as a feasibility and empirical risk minimization problem, enabling efficient learning of unknown optimization parameters.

## Abstract

Inverse optimization involves inferring unknown parameters of an optimization problem from known solutions and is widely used in fields such as transportation, power systems, and healthcare. We study the contextual inverse optimization setting that utilizes additional contextual information to better predict the unknown problem parameters. We focus on contextual inverse linear programming (CILP) addressing the challenges posed by the non-differentiable nature of LPs. For a linear prediction model, we reduce CILP to a convex feasibility problem allowing the use of standard algorithms such as alternating projections. The resulting algorithm for CILP is equipped with theoretical convergence guarantees without additional assumptions such as degeneracy or interpolation. Next, we reduce CILP to empirical risk minimization (ERM) on a smooth, convex loss that satisfies the Polyak-Lojasiewicz condition. This reduction enables the use of scalable first-order optimization methods to solve large non-convex problems while maintaining theoretical guarantees in the convex setting. Subsequently, we use the reduction to ERM to quantify the generalization performance of the proposed algorithm on previously unseen instances. Finally, we experimentally validate our approach on synthetic and real-world problems and demonstrate improved performance compared to existing methods.