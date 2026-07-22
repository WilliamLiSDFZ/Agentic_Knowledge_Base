---
title: "AdaLomo: Low-memory Optimization with Adaptive Learning Rate"
source: "https://aclanthology.org/2024.findings-acl.742/"
categories: ['llm-training-alignment-and-evaluation', 'transformer-architecture-analysis-and-design']
tags: ['low-memory-optimization', 'adaptive-learning-rate', 'llm-training', 'parameter-efficiency', 'LOMO']
venue: "ACL 2024"
tldr: "Introduces AdaLomo, a low-memory optimizer with adaptive learning rates for efficient large language model training."
---

# AdaLomo: Low-memory Optimization with Adaptive Learning Rate

**Source**: [https://aclanthology.org/2024.findings-acl.742/](https://aclanthology.org/2024.findings-acl.742/)

**TLDR**: Introduces AdaLomo, a low-memory optimizer with adaptive learning rates for efficient large language model training.

## Abstract

AbstractLarge language models have achieved remarkable success, but their extensive parameter size necessitates substantial memory for training, thereby setting a high threshold. While the recently proposed low-memory optimization (LOMO) reduces memory footprint, its optimization technique, akin to stochastic gradient descent, is sensitive to hyper-parameters and exhibits suboptimal convergence, failing to match the performance of the prevailing optimizer for large language models, AdamW. Through analysis of the Adam optimizer, we found that, compared to momentum, the adaptive learning rate is more critical for bridging the gap. Building on this insight, we introduce the low-memory optimization with adaptive learning rate (AdaLomo), which offers an adaptive learning rate for each parameter and exhibits superior convergence performance compared to LOMO theoretically. To maintain memory efficiency, we employ non-negative matrix factorization for the second-order moment estimation. Additionally, we suggest the use of a grouped update normalization to stabilize convergence. Our experiments with instruction-tuning and further pre-training demonstrate that AdaLomo achieves results on par with AdamW, while significantly reducing memory requirements, thereby lowering the hardware barrier to training large language models. The code is accessible at https://github.com/OpenLMLab/LOMO.