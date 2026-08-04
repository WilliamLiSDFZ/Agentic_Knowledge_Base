---
title: "Bridging Mini-Batch and Asymptotic Analysis in Contrastive Learning: From InfoNCE to Kernel-Based Losses"
source: "https://proceedings.mlr.press/v235/koromilas24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/koromilas24a/koromilas24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'anomaly-and-out-of-distribution-detection']
tags: ['contrastive-learning', 'InfoNCE', 'kernel-methods', 'representation-learning', 'loss-analysis']
venue: "ICML 2024"
tldr: "Theoretical analysis bridging mini-batch and asymptotic contrastive learning losses, showing InfoNCE converges to kernel-based objectives."
---

# Bridging Mini-Batch and Asymptotic Analysis in Contrastive Learning: From InfoNCE to Kernel-Based Losses

**Source**: [https://proceedings.mlr.press/v235/koromilas24a.html](https://proceedings.mlr.press/v235/koromilas24a.html)

**TLDR**: Theoretical analysis bridging mini-batch and asymptotic contrastive learning losses, showing InfoNCE converges to kernel-based objectives.

## Abstract

What do different contrastive learning (CL) losses actually optimize for? Although multiple CL methods have demonstrated remarkable representation learning capabilities, the differences in their inner workings remain largely opaque. In this work, we analyse several CL families and prove that, under certain conditions, they admit the same minimisers when optimizing either their batch-level objectives or their expectations asymptotically. In both cases, an intimate connection with the hyperspherical energy minimisation (HEM) problem resurfaces. Drawing inspiration from this, we introduce a novel CL objective, coined Decoupled Hyperspherical Energy Loss (DHEL). DHEL simplifies the problem by decoupling the target hyperspherical energy from the alignment of positive examples while preserving the same theoretical guarantees. Going one step further, we show the same results hold for another relevant CL family, namely kernel contrastive learning (KCL), with the additional advantage of the expected loss being independent of batch size, thus identifying the minimisers in the non-asymptotic regime. Empirical results demonstrate improved downstream performance and robustness across combinations of different batch sizes and hyperparameters and reduced dimensionality collapse, on several computer vision datasets.