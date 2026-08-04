---
title: "Stability and Generalization for Stochastic Recursive Momentum-based Algorithms for (Strongly-)Convex One to $K$-Level Stochastic Optimizations"
source: "https://proceedings.mlr.press/v235/pan24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pan24e/pan24e.pdf"
categories: ['optimization-algorithms-convergence-theory']
tags: ['stochastic-optimization', 'recursive-momentum', 'generalization', 'stability', 'bilevel-optimization']
venue: "ICML 2024"
tldr: "Analyzes stability and generalization bounds for STORM-based algorithms applied to one-to-K-level stochastic optimization."
---

# Stability and Generalization for Stochastic Recursive Momentum-based Algorithms for (Strongly-)Convex One to $K$-Level Stochastic Optimizations

**Source**: [https://proceedings.mlr.press/v235/pan24e.html](https://proceedings.mlr.press/v235/pan24e.html)

**TLDR**: Analyzes stability and generalization bounds for STORM-based algorithms applied to one-to-K-level stochastic optimization.

## Abstract

STOchastic Recursive Momentum (STORM)-based algorithms have been widely developed to solve one to $K$-level ($K \geq 3$) stochastic optimization problems. Specifically, they use estimators to mitigate the biased gradient issue and achieve near-optimal convergence results. However, there is relatively little work on understanding their generalization performance, particularly evident during the transition from one to $K$-level optimization contexts. This paper provides a comprehensive generalization analysis of three representative STORM-based algorithms: STORM, COVER, and SVMR, for one, two, and $K$-level stochastic optimizations under both convex and strongly convex settings based on algorithmic stability. Firstly, we define stability for $K$-level optimizations and link it to generalization. Then, we detail the stability results for three prominent STORM-based algorithms. Finally, we derive their excess risk bounds by balancing stability results with optimization errors. Our theoretical results provide strong evidence to complete STORM-based algorithms: (1) Each estimator may decrease their stability due to variance with its estimation target. (2) Every additional level might escalate the generalization error, influenced by the stability and the variance between its cumulative stochastic gradient and the true gradient. (3) Increasing the batch size for the initial computation of estimators presents a favorable trade-off, enhancing the generalization performance.