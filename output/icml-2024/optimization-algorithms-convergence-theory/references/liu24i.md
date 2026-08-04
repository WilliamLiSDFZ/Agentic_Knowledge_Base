---
title: "Decentralized Convex Finite-Sum Optimization with Better Dependence on Condition Numbers"
source: "https://proceedings.mlr.press/v235/liu24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24i/liu24i.pdf"
categories: ['optimization-algorithms-convergence-theory']
tags: ['decentralized-optimization', 'variance-reduction', 'condition-numbers']
venue: "ICML 2024"
tldr: "A stochastic variance-reduced method for decentralized finite-sum optimization is proposed with improved dependence on condition numbers."
---

# Decentralized Convex Finite-Sum Optimization with Better Dependence on Condition Numbers

**Source**: [https://proceedings.mlr.press/v235/liu24i.html](https://proceedings.mlr.press/v235/liu24i.html)

**TLDR**: A stochastic variance-reduced method for decentralized finite-sum optimization is proposed with improved dependence on condition numbers.

## Abstract

This paper studies decentralized optimization problem, where the local objective on each node is an average of a finite set of convex functions and the global function is strongly convex. We propose an efficient stochastic variance reduced first-order method that allows the different nodes to establish their stochastic local gradient estimator with different mini-batch sizes per iteration. We prove the upper bound on the computation time of the proposed method contains the dependence on the global condition number, which is sharper than the previous results that only depend on the local condition numbers. Compared with the state-of-the-art methods, we also show that our method requires less local incremental first-order oracle calls and comparable communication cost. We further perform numerical experiments to validate the advantage of our method.