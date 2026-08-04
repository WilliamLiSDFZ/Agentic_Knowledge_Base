---
title: "Convex Relaxations of ReLU Neural Networks Approximate Global Optima in Polynomial Time"
source: "https://proceedings.mlr.press/v235/kim24ac.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24ac/kim24ac.pdf"
categories: ['neural-network-learning-dynamics-theory', 'optimization-algorithms-convergence-theory']
tags: ['ReLU-networks', 'convex-relaxation', 'optimality-gap']
venue: "ICML 2024"
tldr: "Shows that convex relaxations of two-layer ReLU networks achieve near-global optima with polynomial-time guarantees on random data."
---

# Convex Relaxations of ReLU Neural Networks Approximate Global Optima in Polynomial Time

**Source**: [https://proceedings.mlr.press/v235/kim24ac.html](https://proceedings.mlr.press/v235/kim24ac.html)

**TLDR**: Shows that convex relaxations of two-layer ReLU networks achieve near-global optima with polynomial-time guarantees on random data.

## Abstract

In this paper, we study the optimality gap between two-layer ReLU networks regularized with weight decay and their convex relaxations. We show that when the training data is random, the relative optimality gap between the original problem and its relaxation can be bounded by a factor of O(√log n), where n is the number of training samples. A simple application leads to a tractable polynomial-time algorithm that is guaranteed to solve the original non-convex problem up to a logarithmic factor. Moreover, under mild assumptions, we show that local gradient methods converge to a point with low training loss with high probability. Our result is an exponential improvement compared to existing results and sheds new light on understanding why local gradient methods work well.