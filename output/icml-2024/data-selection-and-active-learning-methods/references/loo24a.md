---
title: "Large Scale Dataset Distillation with Domain Shift"
source: "https://proceedings.mlr.press/v235/loo24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/loo24a/loo24a.pdf"
categories: ['data-selection-and-active-learning-methods', 'learning-with-imperfect-data-and-bias']
tags: ['dataset-distillation', 'domain-shift', 'large-scale', 'data-compression']
venue: "ICML 2024"
tldr: "Extends dataset distillation to large-scale high-resolution datasets by addressing domain shift challenges."
---

# Large Scale Dataset Distillation with Domain Shift

**Source**: [https://proceedings.mlr.press/v235/loo24a.html](https://proceedings.mlr.press/v235/loo24a.html)

**TLDR**: Extends dataset distillation to large-scale high-resolution datasets by addressing domain shift challenges.

## Abstract

Dataset Distillation seeks to summarize a large dataset by generating a reduced set of synthetic samples. While there has been much success at distilling small datasets such as CIFAR-10 on smaller neural architectures, Dataset Distillation methods fail to scale to larger high-resolution datasets and architectures. In this work, we introduce Dataset Distillation with Domain Shift (D3S), a scalable distillation algorithm, made by reframing the dataset distillation problem as a domain shift one. In doing so, we derive a universal bound on the distillation loss, and provide a method for efficiently approximately optimizing it. We achieve state-of-the-art results on Tiny-ImageNet, ImageNet-1k, and ImageNet-21K over a variety of recently proposed baselines, including high cross-architecture generalization. Additionally, our ablation studies provide lessons on the importance of validation-time hyperparameters on distillation performance, motivating the need for standardization.