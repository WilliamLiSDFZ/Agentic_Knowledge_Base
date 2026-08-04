---
title: "Compact Optimality Verification for Optimization Proxies"
source: "https://proceedings.mlr.press/v235/chen24bj.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24bj/chen24bj.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'optimization-algorithms-convergence-theory']
tags: ['optimization-proxies', 'optimality-verification', 'machine-learning-for-optimization']
venue: "ICML 2024"
tldr: "A compact verification framework checks the near-optimality of solutions produced by machine learning optimization proxies."
---

# Compact Optimality Verification for Optimization Proxies

**Source**: [https://proceedings.mlr.press/v235/chen24bj.html](https://proceedings.mlr.press/v235/chen24bj.html)

**TLDR**: A compact verification framework checks the near-optimality of solutions produced by machine learning optimization proxies.

## Abstract

Recent years have witnessed increasing interest in optimization proxies, i.e., machine learning models that approximate the input-output mapping of parametric optimization problems and return near-optimal feasible solutions. Following recent work by (Nellikkath & Chatzivasileiadis, 2021), this paper reconsiders the optimality verification problem for optimization proxies, i.e., the determination of the worst-case optimality gap over the instance distribution. The paper proposes a compact formulation for optimality verification and a gradient-based primal heuristic that brings significant computational benefits to the original formulation. The compact formulation is also more general and applies to non-convex optimization problems. The benefits of the compact formulation are demonstrated on large-scale DC Optimal Power Flow and knapsack problems.