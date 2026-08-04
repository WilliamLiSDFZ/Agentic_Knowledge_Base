---
title: "A Rate-Distortion View of Uncertainty Quantification"
source: "https://proceedings.mlr.press/v235/apostolopoulou24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/apostolopoulou24a/apostolopoulou24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'anomaly-and-out-of-distribution-detection']
tags: ['rate-distortion', 'uncertainty-quantification', 'out-of-distribution', 'evidential-learning']
venue: "ICML 2024"
tldr: "Proposes a rate-distortion framework for uncertainty quantification to determine input proximity to training data for reliable predictions."
---

# A Rate-Distortion View of Uncertainty Quantification

**Source**: [https://proceedings.mlr.press/v235/apostolopoulou24a.html](https://proceedings.mlr.press/v235/apostolopoulou24a.html)

**TLDR**: Proposes a rate-distortion framework for uncertainty quantification to determine input proximity to training data for reliable predictions.

## Abstract

In supervised learning, understanding an input’s proximity to the training data can help a model decide whether it has sufficient evidence for reaching a reliable prediction. While powerful probabilistic models such as Gaussian Processes naturally have this property, deep neural networks often lack it. In this paper, we introduce Distance Aware Bottleneck (DAB), i.e., a new method for enriching deep neural networks with this property. Building on prior information bottleneck approaches, our method learns a codebook that stores a compressed representation of all inputs seen during training. The distance of a new example from this codebook can serve as an uncertainty estimate for the example. The resulting model is simple to train and provides deterministic uncertainty estimates by a single forward pass. Finally, our method achieves better out-of-distribution (OOD) detection and misclassification prediction than prior methods, including expensive ensemble methods, deep kernel Gaussian Processes, and approaches based on the standard information bottleneck.