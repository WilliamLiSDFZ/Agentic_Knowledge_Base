---
title: "Sparsest Models Elude Pruning: An Exposé of Pruning’s Current Capabilities"
source: "https://proceedings.mlr.press/v235/zhang24av.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24av/zhang24av.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'neural-network-learning-dynamics-theory']
tags: ['model-pruning', 'sparsity', 'neural-network-compression', 'benchmarking', 'synthetic-data']
venue: "ICML 2024"
tldr: "Extensive experiments reveal that current pruning algorithms fail to recover the sparsest models even on synthetic datasets."
---

# Sparsest Models Elude Pruning: An Exposé of Pruning’s Current Capabilities

**Source**: [https://proceedings.mlr.press/v235/zhang24av.html](https://proceedings.mlr.press/v235/zhang24av.html)

**TLDR**: Extensive experiments reveal that current pruning algorithms fail to recover the sparsest models even on synthetic datasets.

## Abstract

Pruning has emerged as a promising approach for compressing large-scale models, yet its effectiveness in recovering the sparsest of models has not yet been explored. We conducted an extensive series of 485,838 experiments, applying a range of state-of-the-art pruning algorithms to a synthetic dataset we created, named the Cubist Spiral. Our findings reveal a significant gap in performance compared to ideal sparse networks, which we identified through a novel combinatorial search algorithm. We attribute this performance gap to current pruning algorithms’ poor behaviour under overparameterization, their tendency to induce disconnected paths throughout the network, and their propensity to get stuck at suboptimal solutions, even when given the optimal width and initialization. This gap is concerning, given the simplicity of the network architectures and datasets used in our study. We hope that our research encourages further investigation into new pruning techniques that strive for true network sparsity.