---
title: "Efficient Algorithms for Sum-Of-Minimum Optimization"
source: "https://proceedings.mlr.press/v235/ding24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ding24a/ding24a.pdf"
categories: ['submodular-optimization-and-combinatorial-algorithms', 'optimization-algorithms-convergence-theory']
tags: ['sum-of-minimum', 'optimization', 'clustering', 'combinatorial', 'efficient-algorithms']
venue: "ICML 2024"
tldr: "Introduces a novel sum-of-minimum optimization model and proposes efficient algorithms with applications to clustering and related combinatorial problems."
---

# Efficient Algorithms for Sum-Of-Minimum Optimization

**Source**: [https://proceedings.mlr.press/v235/ding24a.html](https://proceedings.mlr.press/v235/ding24a.html)

**TLDR**: Introduces a novel sum-of-minimum optimization model and proposes efficient algorithms with applications to clustering and related combinatorial problems.

## Abstract

In this work, we propose a novel optimization model termed “sum-of-minimum" optimization. This model seeks to minimize the sum or average of $N$ objective functions over $k$ parameters, where each objective takes the minimum value of a predefined sub-function with respect to the $k$ parameters. This universal framework encompasses numerous clustering applications in machine learning and related fields. We develop efficient algorithms for solving sum-of-minimum optimization problems, inspired by a randomized initialization algorithm for the classic $k$-means (Arthur & Vassilvitskii, 2007) and Lloyd’s algorithm (Lloyd, 1982). We establish a new tight bound for the generalized initialization algorithm and prove a gradient-descent-like convergence rate for generalized Lloyd’s algorithm. The efficiency of our algorithms is numerically examined on multiple tasks, including generalized principal component analysis, mixed linear regression, and small-scale neural network training. Our approach compares favorably to previous ones based on simpler-but-less-precise optimization reformulations.