---
title: "Confidence-aware Contrastive Learning for Selective Classification"
source: "https://proceedings.mlr.press/v235/wu24s.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24s/wu24s.pdf"
categories: ['uncertainty-calibration-and-distribution-shift-adaptation', 'anomaly-and-out-of-distribution-detection']
tags: ['selective-classification', 'confidence-calibration', 'contrastive-learning', 'uncertainty', 'safety']
venue: "ICML 2024"
tldr: "Proposes confidence-aware contrastive learning for selective classification, enabling models to abstain from predictions when insufficiently confident to enhance safety."
---

# Confidence-aware Contrastive Learning for Selective Classification

**Source**: [https://proceedings.mlr.press/v235/wu24s.html](https://proceedings.mlr.press/v235/wu24s.html)

**TLDR**: Proposes confidence-aware contrastive learning for selective classification, enabling models to abstain from predictions when insufficiently confident to enhance safety.

## Abstract

Selective classification enables models to make predictions only when they are sufficiently confident, aiming to enhance safety and reliability, which is important in high-stakes scenarios. Previous methods mainly use deep neural networks and focus on modifying the architecture of classification layers to enable the model to estimate the confidence of its prediction. This work provides a generalization bound for selective classification, disclosing that optimizing feature layers helps improve the performance of selective classification. Inspired by this theory, we propose to explicitly improve the selective classification model at the feature level for the first time, leading to a novel Confidence-aware Contrastive Learning method for Selective Classification, CCL-SC, which similarizes the features of homogeneous instances and differentiates the features of heterogeneous instances, with the strength controlled by the model’s confidence. The experimental results on typical datasets, i.e., CIFAR-10, CIFAR-100, CelebA, and ImageNet, show that CCL-SC achieves significantly lower selective risk than state-of-the-art methods, across almost all coverage degrees. Moreover, it can be combined with existing methods to bring further improvement.