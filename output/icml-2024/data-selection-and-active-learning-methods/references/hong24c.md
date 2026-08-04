---
title: "Diversified Batch Selection for Training Acceleration"
source: "https://proceedings.mlr.press/v235/hong24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hong24c/hong24c.pdf"
categories: ['data-selection-and-active-learning-methods', 'sampling-compression-and-dimensionality-reduction']
tags: ['batch-selection', 'training-acceleration', 'diversity', 'data-pruning']
venue: "ICML 2024"
tldr: "Proposes a diversified online batch selection strategy that accelerates training by selecting informative and diverse data subsets."
---

# Diversified Batch Selection for Training Acceleration

**Source**: [https://proceedings.mlr.press/v235/hong24c.html](https://proceedings.mlr.press/v235/hong24c.html)

**TLDR**: Proposes a diversified online batch selection strategy that accelerates training by selecting informative and diverse data subsets.

## Abstract

The remarkable success of modern machine learning models on large datasets often demands extensive training time and resource consumption. To save cost, a prevalent research line, known as online batch selection, explores selecting informative subsets during the training process. Although recent efforts achieve advancements by measuring the impact of each sample on generalization, their reliance on additional reference models inherently limits their practical applications, when there are no such ideal models available. On the other hand, the vanilla reference-model-free methods involve independently scoring and selecting data in a sample-wise manner, which sacrifices the diversity and induces the redundancy. To tackle this dilemma, we propose Diversified Batch Selection (DivBS), which is reference-model-free and can efficiently select diverse and representative samples. Specifically, we define a novel selection objective that measures the group-wise orthogonalized representativeness to combat the redundancy issue of previous sample-wise criteria, and provide a principled selection-efficient realization. Extensive experiments across various tasks demonstrate the significant superiority of DivBS in the performance-speedup trade-off. The code is publicly available.