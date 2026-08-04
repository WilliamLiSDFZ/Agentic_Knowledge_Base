---
title: "Few-shot Adaptation to Distribution Shifts By Mixing Source and Target Embeddings"
source: "https://proceedings.mlr.press/v235/xue24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xue24a/xue24a.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['few-shot-adaptation', 'distribution-shift', 'embedding-interpolation']
venue: "ICML 2024"
tldr: "Addresses few-shot domain adaptation by mixing source and target embeddings to handle distribution shifts with minimal labeled target data."
---

# Few-shot Adaptation to Distribution Shifts By Mixing Source and Target Embeddings

**Source**: [https://proceedings.mlr.press/v235/xue24a.html](https://proceedings.mlr.press/v235/xue24a.html)

**TLDR**: Addresses few-shot domain adaptation by mixing source and target embeddings to handle distribution shifts with minimal labeled target data.

## Abstract

Pretrained machine learning models need to be adapted to distribution shifts when deployed in new target environments. When obtaining labeled data from the target distribution is expensive, few-shot adaptation with only a few examples from the target distribution becomes essential. In this work, we propose MixPro, a lightweight and highly data-efficient approach for few-shot adaptation. MixPro first generates a relatively large dataset by mixing (linearly combining) pre-trained embeddings of large source data with those of the few target examples. This process preserves important features of both source and target distributions, while mitigating the specific noise in the small target data. Then, it trains a linear classifier on the mixed embeddings to effectively adapts the model to the target distribution without overfitting the small target data. Theoretically, we demonstrate the advantages of MixPro over previous methods. Our experiments, conducted across various model architectures on 8 datasets featuring different types of distribution shifts, reveal that MixPro can outperform baselines by as much as 7%, with only 2-4 target examples.