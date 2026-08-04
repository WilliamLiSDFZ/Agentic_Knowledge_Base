---
title: "Straight-Through Meets Sparse Recovery: the Support Exploration Algorithm"
source: "https://proceedings.mlr.press/v235/mohamed24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mohamed24a/mohamed24a.pdf"
categories: ['neural-operators-for-pde-solving', 'sampling-compression-and-dimensionality-reduction']
tags: ['straight-through-estimator', 'sparse-recovery', 'quantization']
venue: "ICML 2024"
tldr: "Analyzes the straight-through estimator through the lens of sparse support recovery to better understand when and why it succeeds."
---

# Straight-Through Meets Sparse Recovery: the Support Exploration Algorithm

**Source**: [https://proceedings.mlr.press/v235/mohamed24a.html](https://proceedings.mlr.press/v235/mohamed24a.html)

**TLDR**: Analyzes the straight-through estimator through the lens of sparse support recovery to better understand when and why it succeeds.

## Abstract

The straight-through estimator (STE) is commonly used to optimize quantized neural networks, yet its contexts of effective performance are still unclear despite empirical successes. To make a step forward in this comprehension, we apply STE to a well-understood problem: sparse support recovery. We introduce the Support Exploration Algorithm (SEA), a novel algorithm promoting sparsity, and we analyze its performance in support recovery (a.k.a. model selection) problems. SEA explores more supports than the state-of-the-art, leading to superior performance in experiments, especially when the columns of $A$ are strongly coherent. The theoretical analysis considers recovery guarantees when the linear measurements matrix $A$ satisfies the Restricted Isometry Property (RIP). The sufficient conditions of recovery are comparable but more stringent than those of the state-of-the-art in sparse support recovery. Their significance lies mainly in their applicability to an instance of the STE.