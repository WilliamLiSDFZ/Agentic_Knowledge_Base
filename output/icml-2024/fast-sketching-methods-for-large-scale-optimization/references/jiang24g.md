---
title: "Projection-Free Variance Reduction Methods for Stochastic Constrained Multi-Level Compositional Optimization"
source: "https://proceedings.mlr.press/v235/jiang24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jiang24g/jiang24g.pdf"
categories: ['optimization-algorithms-convergence-theory', 'fast-sketching-methods-for-large-scale-optimization']
tags: ['projection-free', 'variance-reduction', 'multi-level-compositional-optimization', 'stochastic']
venue: "ICML 2024"
tldr: "Projection-free variance reduction algorithms are developed for stochastic constrained multi-level compositional optimization with improved complexity guarantees."
---

# Projection-Free Variance Reduction Methods for Stochastic Constrained Multi-Level Compositional Optimization

**Source**: [https://proceedings.mlr.press/v235/jiang24g.html](https://proceedings.mlr.press/v235/jiang24g.html)

**TLDR**: Projection-free variance reduction algorithms are developed for stochastic constrained multi-level compositional optimization with improved complexity guarantees.

## Abstract

This paper investigates projection-free algorithms for stochastic constrained multi-level optimization. In this context, the objective function is a nested composition of several smooth functions, and the decision set is closed and convex. Existing projection-free algorithms for solving this problem suffer from two limitations: 1) they solely focus on the gradient mapping criterion and fail to match the optimal sample complexities in unconstrained settings; 2) their analysis is exclusively applicable to non-convex functions, without considering convex and strongly convex objectives. To address these issues, we introduce novel projection-free variance reduction algorithms and analyze their complexities under different criteria. For gradient mapping, our complexities improve existing results and match the optimal rates for unconstrained problems. For the widely-used Frank-Wolfe gap criterion, we provide theoretical guarantees that align with those for single-level problems. Additionally, by using a stage-wise adaptation, we further obtain complexities for convex and strongly convex functions. Finally, numerical experiments on different tasks demonstrate the effectiveness of our methods.