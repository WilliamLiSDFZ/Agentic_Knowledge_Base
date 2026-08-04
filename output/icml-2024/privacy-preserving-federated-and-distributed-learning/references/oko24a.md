---
title: "SILVER: Single-loop variance reduction and application to federated learning"
source: "https://proceedings.mlr.press/v235/oko24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/oko24a/oko24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning']
tags: ['variance-reduction', 'federated-learning', 'single-loop', 'distributed-optimization']
venue: "ICML 2024"
tldr: "Presents SILVER, a single-loop variance-reduced gradient estimator applicable to federated and distributed optimization."
---

# SILVER: Single-loop variance reduction and application to federated learning

**Source**: [https://proceedings.mlr.press/v235/oko24a.html](https://proceedings.mlr.press/v235/oko24a.html)

**TLDR**: Presents SILVER, a single-loop variance-reduced gradient estimator applicable to federated and distributed optimization.

## Abstract

Most variance reduction methods require multiple times of full gradient computation, which is time-consuming and hence a bottleneck in application to distributed optimization. We present a single-loop variance-reduced gradient estimator named SILVER (SIngle-Loop VariancE-Reduction) for the finite-sum non-convex optimization, which does not require multiple full gradients but nevertheless achieves the optimal gradient complexity. Notably, unlike existing methods, SILVER provably reaches second-order optimality, with exponential convergence in the Polyak-Łojasiewicz (PL) region, and achieves further speedup depending on the data heterogeneity. Owing to these advantages, SILVER serves as a new base method to design communication-efficient federated learning algorithms: we combine SILVER with local updates which gives the best communication rounds and number of communicated gradients across all range of Hessian heterogeneity, and, at the same time, guarantees second-order optimality and exponential convergence in the PL region.