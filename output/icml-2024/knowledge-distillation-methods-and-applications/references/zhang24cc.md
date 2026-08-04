---
title: "Lightweight Image Super-Resolution via Flexible Meta Pruning"
source: "https://proceedings.mlr.press/v235/zhang24cc.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24cc/zhang24cc.pdf"
categories: ['image-quality-assessment-and-super-resolution', 'knowledge-distillation-methods-and-applications']
tags: ['image-super-resolution', 'model-pruning', 'lightweight-networks']
venue: "ICML 2024"
tldr: "Proposes flexible meta-pruning to further reduce redundancy in lightweight image super-resolution networks."
---

# Lightweight Image Super-Resolution via Flexible Meta Pruning

**Source**: [https://proceedings.mlr.press/v235/zhang24cc.html](https://proceedings.mlr.press/v235/zhang24cc.html)

**TLDR**: Proposes flexible meta-pruning to further reduce redundancy in lightweight image super-resolution networks.

## Abstract

Lightweight image super-resolution (SR) methods have obtained promising results with moderate model complexity. These approaches primarily focus on a lightweight architecture design, but neglect to further reduce network redundancy. While some model compression techniques try to achieve more lightweight SR models with neural architecture search, knowledge distillation, or channel pruning, they typically require considerable extra computational resources or neglect to prune weights. To address these issues, we propose a flexible meta pruning (FMP) for lightweight image SR, where the network channels and weights are pruned simultaneously. Specifically, we control the network sparsity via channel vectors and weight indicators. We feed them into a hypernetwork, whose parameters act as meta-data for the parameters of the SR backbone. Consequently, for each network layer, we conduct structured pruning with channel vectors, which control the output and input channels. Besides, we conduct unstructured pruning with weight indicators to influence the sparsity of kernel weights, resulting in flexible pruning. During pruning, the sparsity of both channel vectors and weight indicators are regularized. We optimize the channel vectors and weight indicators with proximal gradient and SGD. We conduct extensive experiments to investigate critical factors in the flexible channel and weight pruning for image SR, demonstrating the superiority of our FMP when applied to baseline image SR architectures.