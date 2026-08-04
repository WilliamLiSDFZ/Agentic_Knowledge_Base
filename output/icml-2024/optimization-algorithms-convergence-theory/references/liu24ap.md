---
title: "Moreau Envelope for Nonconvex Bi-Level Optimization: A Single-Loop and Hessian-Free Solution Strategy"
source: "https://proceedings.mlr.press/v235/liu24ap.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24ap/liu24ap.pdf"
categories: ['optimization-algorithms-convergence-theory', 'fairness-aware-algorithmic-decision-making']
tags: ['bilevel-optimization', 'moreau-envelope', 'hessian-free']
venue: "ICML 2024"
tldr: "A single-loop, Hessian-free optimization strategy using the Moreau envelope to efficiently solve large-scale nonconvex bilevel optimization problems."
---

# Moreau Envelope for Nonconvex Bi-Level Optimization: A Single-Loop and Hessian-Free Solution Strategy

**Source**: [https://proceedings.mlr.press/v235/liu24ap.html](https://proceedings.mlr.press/v235/liu24ap.html)

**TLDR**: A single-loop, Hessian-free optimization strategy using the Moreau envelope to efficiently solve large-scale nonconvex bilevel optimization problems.

## Abstract

This work focuses on addressing two major challenges in the context of large-scale nonconvex Bi-Level Optimization (BLO) problems, which are increasingly applied in machine learning due to their ability to model nested structures. These challenges involve ensuring computational efficiency and providing theoretical guarantees. While recent advances in scalable BLO algorithms have primarily relied on lower-level convexity simplification, our work specifically tackles large-scale BLO problems involving nonconvexity in both the upper and lower levels. We simultaneously address computational and theoretical challenges by introducing an innovative single-loop gradient-based algorithm, utilizing the Moreau envelope-based reformulation, and providing non-asymptotic convergence analysis for general nonconvex BLO problems. Notably, our algorithm relies solely on first-order gradient information, enhancing its practicality and efficiency, especially for large-scale BLO learning tasks. We validate our approach’s effectiveness through experiments on various synthetic problems, two typical hyper-parameter learning tasks, and a real-world neural architecture search application, collectively demonstrating its superior performance.