---
title: "Hyperbolic Active Learning for Semantic Segmentation under Domain Shift"
source: "https://proceedings.mlr.press/v235/franco24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/franco24a/franco24a.pdf"
categories: ['data-selection-and-active-learning-methods', 'test-time-adaptation-methods-and-evaluation']
tags: ['active-learning', 'semantic-segmentation', 'hyperbolic-geometry']
venue: "ICML 2024"
tldr: "Hyperbolic neural networks are used for pixel-level active learning in semantic segmentation, using hyperbolic radius to identify scarce data regions."
---

# Hyperbolic Active Learning for Semantic Segmentation under Domain Shift

**Source**: [https://proceedings.mlr.press/v235/franco24a.html](https://proceedings.mlr.press/v235/franco24a.html)

**TLDR**: Hyperbolic neural networks are used for pixel-level active learning in semantic segmentation, using hyperbolic radius to identify scarce data regions.

## Abstract

We introduce a hyperbolic neural network approach to pixel-level active learning for semantic segmentation. Analysis of the data statistics leads to a novel interpretation of the hyperbolic radius as an indicator of data scarcity. In HALO (Hyperbolic Active Learning Optimization), for the first time, we propose the use of epistemic uncertainty as a data acquisition strategy, following the intuition of selecting data points that are the least known. The hyperbolic radius, complemented by the widely-adopted prediction entropy, effectively approximates epistemic uncertainty. We perform extensive experimental analysis based on two established synthetic-to-real benchmarks, i.e. GTAV $\rightarrow$ Cityscapes and SYNTHIA $\rightarrow$ Cityscapes. Additionally, we test HALO on Cityscape $\rightarrow$ ACDC for domain adaptation under adverse weather conditions, and we benchmark both convolutional and attention-based backbones. HALO sets a new state-of-the-art in active learning for semantic segmentation under domain shift and it is the first active learning approach that surpasses the performance of supervised domain adaptation while using only a small portion of labels (i.e., 1%).