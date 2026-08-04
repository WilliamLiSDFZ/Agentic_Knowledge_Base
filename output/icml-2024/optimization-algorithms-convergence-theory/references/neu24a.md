---
title: "Dealing With Unbounded Gradients in Stochastic Saddle-point Optimization"
source: "https://proceedings.mlr.press/v235/neu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/neu24a/neu24a.pdf"
categories: ['optimization-algorithms-convergence-theory']
tags: ['saddle-point-optimization', 'unbounded-gradients', 'stochastic-methods']
venue: "ICML 2024"
tldr: "New stochastic first-order methods are proposed for convex-concave saddle-point problems robust to unbounded gradient growth."
---

# Dealing With Unbounded Gradients in Stochastic Saddle-point Optimization

**Source**: [https://proceedings.mlr.press/v235/neu24a.html](https://proceedings.mlr.press/v235/neu24a.html)

**TLDR**: New stochastic first-order methods are proposed for convex-concave saddle-point problems robust to unbounded gradient growth.

## Abstract

We study the performance of stochastic first-order methods for finding saddle points of convex-concave functions. A notorious challenge faced by such methods is that the gradients can grow arbitrarily large during optimization, which may result in instability and divergence. In this paper, we propose a simple and effective regularization technique that stabilizes the iterates and yields meaningful performance guarantees even if the domain and the gradient noise scales linearly with the size of the iterates (and is thus potentially unbounded). Besides providing a set of general results, we also apply our algorithm to a specific problem in reinforcement learning, where it leads to performance guarantees for finding near-optimal policies in an average-reward MDP without prior knowledge of the bias span.