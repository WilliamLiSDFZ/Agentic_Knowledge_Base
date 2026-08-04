---
title: "SelMatch: Effectively Scaling Up Dataset Distillation via Selection-Based Initialization and Partial Updates by Trajectory Matching"
source: "https://proceedings.mlr.press/v235/lee24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24g/lee24g.pdf"
categories: ['data-selection-and-active-learning-methods', 'learning-with-imperfect-data-and-bias']
tags: ['dataset-distillation', 'trajectory-matching', 'initialization', 'scaling']
venue: "ICML 2024"
tldr: "Introduces SelMatch, combining selection-based initialization and partial trajectory matching updates to scale dataset distillation to higher image-per-class regimes."
---

# SelMatch: Effectively Scaling Up Dataset Distillation via Selection-Based Initialization and Partial Updates by Trajectory Matching

**Source**: [https://proceedings.mlr.press/v235/lee24g.html](https://proceedings.mlr.press/v235/lee24g.html)

**TLDR**: Introduces SelMatch, combining selection-based initialization and partial trajectory matching updates to scale dataset distillation to higher image-per-class regimes.

## Abstract

Dataset distillation aims to synthesize a small number of images per class (IPC) from a large dataset to approximate full dataset training with minimal performance loss. While effective in very small IPC ranges, many distillation methods become less effective, even underperforming random sample selection, as IPC increases. Our examination of state-of-the-art trajectory-matching based distillation methods across various IPC scales reveals that these methods struggle to incorporate the complex, rare features of harder samples into the synthetic dataset even with the increased IPC, resulting in a persistent coverage gap between easy and hard test samples. Motivated by such observations, we introduce SelMatch, a novel distillation method that effectively scales with IPC. SelMatch uses selection-based initialization and partial updates through trajectory matching to manage the synthetic dataset’s desired difficulty level tailored to IPC scales. When tested on CIFAR-10/100 and TinyImageNet, SelMatch consistently outperforms leading selection-only and distillation-only methods across subset ratios from 5% to 30%.