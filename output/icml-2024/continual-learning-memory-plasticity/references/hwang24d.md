---
title: "EVEREST: Efficient Masked Video Autoencoder by Removing Redundant Spatiotemporal Tokens"
source: "https://proceedings.mlr.press/v235/hwang24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hwang24d/hwang24d.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'continual-learning-memory-plasticity']
tags: ['masked-video-autoencoder', 'token-pruning', 'redundancy-reduction', 'video-representation', 'efficiency']
venue: "ICML 2024"
tldr: "Proposes EVEREST, an efficient masked video autoencoder that removes redundant spatiotemporal tokens to reduce computation and memory costs."
---

# EVEREST: Efficient Masked Video Autoencoder by Removing Redundant Spatiotemporal Tokens

**Source**: [https://proceedings.mlr.press/v235/hwang24d.html](https://proceedings.mlr.press/v235/hwang24d.html)

**TLDR**: Proposes EVEREST, an efficient masked video autoencoder that removes redundant spatiotemporal tokens to reduce computation and memory costs.

## Abstract

Masked Video Autoencoder (MVA) approaches have demonstrated their potential by significantly outperforming previous video representation learning methods. However, they waste an excessive amount of computations and memory in predicting uninformative tokens/frames due to random masking strategies. (e.g., over 16 nodes with 128 NVIDIA A100 GPUs). To resolve this issue, we exploit the unequal information density among the patches in videos and propose EVEREST, a surprisingly efficient MVA approach for video representation learning that finds tokens containing rich motion features and discards uninformative ones during both pre-training and fine-tuning. We further present an information-intensive frame selection strategy that allows the model to focus on informative and causal frames with minimal redundancy. Our method significantly reduces the computation and memory requirements of MVA, enabling the pre-training and fine-tuning on a single machine with 8 GPUs while achieving comparable performance to computation- and memory-heavy baselines on multiple benchmarks and the uncurated Ego4D dataset. We hope that our work contributes to reducing the barrier to further research on video understanding.