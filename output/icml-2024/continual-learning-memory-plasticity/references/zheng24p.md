---
title: "Multi-layer Rehearsal Feature Augmentation for Class-Incremental Learning"
source: "https://proceedings.mlr.press/v235/zheng24p.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zheng24p/zheng24p.pdf"
categories: ['continual-learning-memory-plasticity']
tags: ['class-incremental-learning', 'rehearsal', 'feature-augmentation', 'catastrophic-forgetting']
venue: "ICML 2024"
tldr: "This paper proposes multi-layer rehearsal feature augmentation to improve replay-based class-incremental learning by enriching stored sample representations."
---

# Multi-layer Rehearsal Feature Augmentation for Class-Incremental Learning

**Source**: [https://proceedings.mlr.press/v235/zheng24p.html](https://proceedings.mlr.press/v235/zheng24p.html)

**TLDR**: This paper proposes multi-layer rehearsal feature augmentation to improve replay-based class-incremental learning by enriching stored sample representations.

## Abstract

Class-Incremental Learning (CIL) seeks to learn new concepts without forgetting previously learned knowledge. To achieve this, rehearsal-based methods keep a replay memory consisting of a small number of trained samples from previous tasks. However, recent studies show that rehearsal-based methods are prone to overfitting on rehearsal samples, resulting in poor generalization on previous tasks. Since the generalization error is bounded by the margin on the training dataset, in this paper, we study the generalization by all-layer margin on deep neural networks to alleviate catastrophic forgetting. Specifically, we show that the average margin of the rehearsal samples are smaller during incremental learning. To acquire larger margin thus better generalization on rehearsal samples, we propose Multi-layer Rehearsal Feature Augmentation (MRFA) in rehearsal training to optimize the all-layer margin on rehearsal samples. The proposed method augments the features of rehearsal samples at each layer by gradient ascent step of the current model with respect to the feature. With such augmentations on layer features, the margin on rehearsal samples are larger, rehearsal samples are able to provide more information for refining the decision boundary during incremental learning, thus alleviating catastrophic forgetting. Extensive experiments show the effectiveness of MRFA on various CIL scenarios.