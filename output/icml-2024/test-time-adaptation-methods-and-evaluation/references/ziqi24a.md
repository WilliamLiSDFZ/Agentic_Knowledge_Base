---
title: "Batch Singular Value Polarization and Weighted Semantic Augmentation for Universal Domain Adaptation"
source: "https://proceedings.mlr.press/v235/ziqi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ziqi24a/ziqi24a.pdf"
categories: ['test-time-adaptation-methods-and-evaluation']
tags: ['universal-domain-adaptation', 'singular-value-polarization', 'semantic-augmentation']
venue: "ICML 2024"
tldr: "A novel method combining batch singular value polarization and weighted semantic augmentation is proposed for universal domain adaptation with category shift."
---

# Batch Singular Value Polarization and Weighted Semantic Augmentation for Universal Domain Adaptation

**Source**: [https://proceedings.mlr.press/v235/ziqi24a.html](https://proceedings.mlr.press/v235/ziqi24a.html)

**TLDR**: A novel method combining batch singular value polarization and weighted semantic augmentation is proposed for universal domain adaptation with category shift.

## Abstract

As a more challenging domain adaptation setting, universal domain adaptation (UniDA) introduces category shift on top of domain shift, which needs to identify unknown category in the target domain and avoid misclassifying target samples into source private categories. To this end, we propose a novel UniDA approach named Batch Singular value Polarization and Weighted Semantic Augmentation (BSP-WSA). Specifically, we adopt an adversarial classifier to identify the target unknown category and align feature distributions between the two domains. Then, we propose to perform SVD on the classifier’s outputs to maximize larger singular values while minimizing those smaller ones, which could prevent target samples from being wrongly assigned to source private classes. To better bridge the domain gap, we propose a weighted semantic augmentation approach for UniDA to generate data on common categories between the two domains. Extensive experiments on three benchmarks demonstrate that BSP-WSA could outperform existing state-of-the-art UniDA approaches.