---
title: "DPOT: Auto-Regressive Denoising Operator Transformer for Large-Scale PDE Pre-Training"
source: "https://proceedings.mlr.press/v235/hao24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hao24d/hao24d.pdf"
categories: ['neural-operators-for-pde-solving', 'transformer-architecture-efficiency-and-scaling']
tags: ['neural-operators', 'pretraining', 'pde']
venue: "ICML 2024"
tldr: "DPOT is an auto-regressive denoising operator Transformer for large-scale pre-training on diverse PDE datasets to improve neural operator performance in data-scarce settings."
---

# DPOT: Auto-Regressive Denoising Operator Transformer for Large-Scale PDE Pre-Training

**Source**: [https://proceedings.mlr.press/v235/hao24d.html](https://proceedings.mlr.press/v235/hao24d.html)

**TLDR**: DPOT is an auto-regressive denoising operator Transformer for large-scale pre-training on diverse PDE datasets to improve neural operator performance in data-scarce settings.

## Abstract

Pre-training has been investigated to improve the efficiency and performance of training neural operators in data-scarce settings. However, it is largely in its infancy due to the inherent complexity and diversity, such as long trajectories, multiple scales and varying dimensions of partial differential equations (PDEs) data. In this paper, we present a new auto-regressive denoising pre-training strategy, which allows for more stable and efficient pre-training on PDE data and generalizes to various downstream tasks. Moreover, by designing a flexible and scalable model architecture based on Fourier attention, we can easily scale up the model for large-scale pre-training. We train our PDE foundation model with up to 0.5B parameters on 10+ PDE datasets with more than 100k trajectories. Extensive experiments show that we achieve SOTA on these benchmarks and validate the strong generalizability of our model to significantly enhance performance on diverse downstream PDE tasks like 3D data.