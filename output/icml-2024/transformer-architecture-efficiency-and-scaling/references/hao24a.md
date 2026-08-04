---
title: "Flora: Low-Rank Adapters Are Secretly Gradient Compressors"
source: "https://proceedings.mlr.press/v235/hao24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hao24a/hao24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'optimization-algorithms-convergence-theory']
tags: ['lora', 'gradient-compression', 'memory-efficiency']
venue: "ICML 2024"
tldr: "Flora reveals that low-rank adaptation implicitly performs gradient compression, enabling memory-efficient training of large neural networks."
---

# Flora: Low-Rank Adapters Are Secretly Gradient Compressors

**Source**: [https://proceedings.mlr.press/v235/hao24a.html](https://proceedings.mlr.press/v235/hao24a.html)

**TLDR**: Flora reveals that low-rank adaptation implicitly performs gradient compression, enabling memory-efficient training of large neural networks.

## Abstract

Despite large neural networks demonstrating remarkable abilities to complete different tasks, they require excessive memory usage to store the optimization states for training. To alleviate this, the low-rank adaptation (LoRA) is proposed to reduce the optimization states by training fewer parameters. However, LoRA restricts overall weight update matrices to be low-rank, limiting the model performance. In this work, we investigate the dynamics of LoRA and identify that it can be approximated by a random projection. Based on this observation, we propose Flora, which is able to achieve high-rank updates by resampling the projection matrices while enjoying the sublinear space complexity of optimization states. We conduct experiments across different tasks and model architectures to verify the effectiveness of our approach.