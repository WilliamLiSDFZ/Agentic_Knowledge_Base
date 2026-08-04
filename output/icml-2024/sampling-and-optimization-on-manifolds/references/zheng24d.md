---
title: "Constrained Exploration via Reflected Replica Exchange Stochastic Gradient Langevin Dynamics"
source: "https://proceedings.mlr.press/v235/zheng24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zheng24d/zheng24d.pdf"
categories: ['sampling-and-optimization-on-manifolds']
tags: ['stochastic-gradient-Langevin-dynamics', 'replica-exchange', 'sampling', 'constrained-exploration']
venue: "ICML 2024"
tldr: "This paper introduces reflected replica exchange SGLD to prevent stagnation in distribution tails during non-convex sampling for large-scale learning."
---

# Constrained Exploration via Reflected Replica Exchange Stochastic Gradient Langevin Dynamics

**Source**: [https://proceedings.mlr.press/v235/zheng24d.html](https://proceedings.mlr.press/v235/zheng24d.html)

**TLDR**: This paper introduces reflected replica exchange SGLD to prevent stagnation in distribution tails during non-convex sampling for large-scale learning.

## Abstract

Replica exchange stochastic gradient Langevin dynamics (reSGLD) is an effective sampler for non-convex learning in large-scale datasets. However, the simulation may encounter stagnation issues when the high-temperature chain delves too deeply into the distribution tails. To tackle this issue, we propose reflected reSGLD (r2SGLD): an algorithm tailored for constrained non-convex exploration by utilizing reflection steps within a bounded domain. Theoretically, we observe that reducing the diameter of the domain enhances mixing rates, exhibiting a quadratic behavior. Empirically, we test its performance through extensive experiments, including identifying dynamical systems with physical constraints, simulations of constrained multi-modal distributions, and image classification tasks. The theoretical and empirical findings highlight the crucial role of constrained exploration in improving the simulation efficiency.