---
title: "On Convergence of Incremental Gradient for Non-convex Smooth Functions"
source: "https://proceedings.mlr.press/v235/koloskova24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/koloskova24a/koloskova24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'neural-network-learning-dynamics-theory']
tags: ['incremental-gradient', 'SGD', 'non-convex', 'convergence', 'random-reshuffle']
venue: "ICML 2024"
tldr: "Convergence analysis of incremental gradient and shuffling-based SGD methods for non-convex smooth optimization."
---

# On Convergence of Incremental Gradient for Non-convex Smooth Functions

**Source**: [https://proceedings.mlr.press/v235/koloskova24a.html](https://proceedings.mlr.press/v235/koloskova24a.html)

**TLDR**: Convergence analysis of incremental gradient and shuffling-based SGD methods for non-convex smooth optimization.

## Abstract

In machine learning and neural network optimization, algorithms like incremental gradient, single shuffle SGD, and random reshuffle SGD are popular due to their cache-mismatch efficiency and good practical convergence behavior. However, their optimization properties in theory, especially for non-convex smooth functions, remain incompletely explored. This paper delves into the convergence properties of SGD algorithms with arbitrary data ordering, within a broad framework for non-convex smooth functions. Our findings show enhanced convergence guarantees for incremental gradient and single shuffle SGD. Particularly if $n$ is the training set size, we improve $n$ times the optimization term of convergence guarantee to reach accuracy $\epsilon$ from $O \left( \frac{n}{\epsilon} \right)$ to $O \left( \frac{1}{\epsilon}\right)$.