---
title: "No Free Prune: Information-Theoretic Barriers to Pruning at Initialization"
source: "https://proceedings.mlr.press/v235/kumar24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kumar24a/kumar24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['lottery-tickets', 'pruning-at-initialization', 'information-theoretic-limits']
venue: "ICML 2024"
tldr: "Information-theoretic barriers are established showing fundamental limits to identifying sparse subnetworks at initialization without training the dense model."
---

# No Free Prune: Information-Theoretic Barriers to Pruning at Initialization

**Source**: [https://proceedings.mlr.press/v235/kumar24a.html](https://proceedings.mlr.press/v235/kumar24a.html)

**TLDR**: Information-theoretic barriers are established showing fundamental limits to identifying sparse subnetworks at initialization without training the dense model.

## Abstract

The existence of “lottery tickets” (Frankle & Carbin, 2018) at or near initialization raises the tantalizing question of whether large models are necessary in deep learning, or whether sparse networks can be quickly identified and trained without ever training the dense models that contain them. However, efforts to find these sparse subnetworks without training the dense model (“pruning at initialization”) have been broadly unsuccessful (Frankle et al., 2020b). We put forward a theoretical explanation for this, based on the model’s effective parameter count, $p_\text{eff}$, given by the sum of the number of non-zero weights in the final network and the mutual information between the sparsity mask and the data. We show the Law of Robustness of (Bubeck & Sellke, 2023) extends to sparse networks with the usual parameter count replaced by $p_\text{eff}$, meaning a sparse neural network which robustly interpolates noisy data requires a heavily data-dependent mask. We posit that pruning during and after training outputs masks with higher mutual information than those produced by pruning at initialization. Thus two networks may have the same sparsities, but differ in effective parameter count based on how they were trained. This suggests that pruning near initialization may be infeasible and explains why lottery tickets exist, but cannot be found fast (i.e. without training the full network). Experiments on neural networks confirm that information gained during training may indeed affect model capacity.