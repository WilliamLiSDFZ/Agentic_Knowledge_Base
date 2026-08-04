---
title: "SpikeZIP-TF: Conversion is All You Need for Transformer-based SNN"
source: "https://proceedings.mlr.press/v235/you24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/you24b/you24b.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['spiking-neural-networks', 'ANN-to-SNN', 'transformer', 'conversion']
venue: "ICML 2024"
tldr: "SpikeZIP-TF converts transformer-based ANNs to SNNs achieving comparable accuracy with ultra-low latency via a lossless conversion method."
---

# SpikeZIP-TF: Conversion is All You Need for Transformer-based SNN

**Source**: [https://proceedings.mlr.press/v235/you24b.html](https://proceedings.mlr.press/v235/you24b.html)

**TLDR**: SpikeZIP-TF converts transformer-based ANNs to SNNs achieving comparable accuracy with ultra-low latency via a lossless conversion method.

## Abstract

Spiking neural network (SNN) has attracted great attention due to its characteristic of high efficiency and accuracy. Currently, the ANN-to-SNN conversion methods can obtain ANN on-par accuracy SNN with ultra-low latency (8 time-steps) in CNN structure on computer vision (CV) tasks. However, as Transformer-based networks have achieved prevailing precision on both CV and natural language processing (NLP), the Transformer-based SNNs are still encounting the lower accuracy w.r.t the ANN counterparts. In this work, we introduce a novel ANN-to-SNN conversion method called SpikeZIP-TF, where ANN and SNN are exactly equivalent, thus incurring no accuracy degradation. SpikeZIP-TF achieves 83.82% accuracy on CV dataset (ImageNet) and 93.79% accuracy on NLP dataset (SST-2), which are higher than SOTA Transformer-based SNNs. The code is available in GitHub: https://github.com/Intelligent-Computing-Research-Group/SpikeZIP_transformer