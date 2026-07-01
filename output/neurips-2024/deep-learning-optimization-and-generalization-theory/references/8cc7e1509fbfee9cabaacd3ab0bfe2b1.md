---
title: "Robust Fine-tuning of Zero-shot Models via Variance Reduction"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/8cc7e1509fbfee9cabaacd3ab0bfe2b1-Abstract-Conference.html"
categories: ['machine-learning-theory-and-evaluation-methods', 'deep-learning-optimization-and-generalization-theory']
tags: ['zero-shot-models', 'fine-tuning-robustness', 'variance-reduction']
venue: "NeurIPS 2024"
tldr: "A variance reduction approach for fine-tuning zero-shot models like CLIP improves both in-distribution and out-of-distribution robustness."
---

# Robust Fine-tuning of Zero-shot Models via Variance Reduction

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/8cc7e1509fbfee9cabaacd3ab0bfe2b1-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/8cc7e1509fbfee9cabaacd3ab0bfe2b1-Abstract-Conference.html)

**TLDR**: A variance reduction approach for fine-tuning zero-shot models like CLIP improves both in-distribution and out-of-distribution robustness.

## Abstract

When fine-tuning zero-shot models like CLIP, our desideratum is for the fine-tuned model to excel in both in-distribution (ID) and out-of-distribution (OOD). Recently, ensemble-based models (ESM) have been shown to offer significant robustness improvement, while preserving high ID accuracy. However, our study finds that ESMs do not solve the ID-OOD trade-offs: they achieve peak performance for ID and OOD accuracy at different mixing coefficients. When optimized for OOD accuracy, the ensemble model exhibits a noticeable decline in ID accuracy, and vice versa. In contrast, we propose a sample-wise ensembling technique that can simultaneously attain the best ID and OOD accuracy without the trade-offs. Specifically, we construct a Zero-Shot Failure (ZSF) set containing training samples incorrectly predicted by the zero-shot model. For each test sample, we calculate its distance to the ZSF set and assign a higher weight to the fine-tuned model in the ensemble if the distance is small. We term our method Variance Reduction Fine-tuning (VRF), as it effectively reduces the variance in ensemble predictions, thereby decreasing residual error. On ImageNet and five derived distribution shifts, our VRF further improves the OOD accuracy by 1.5 - 2.0 pp over the ensemble baselines while maintaining or increasing ID accuracy. VRF achieves similar large robustness gains on (0.9 - 3.1 pp) on other distribution shifts19 benchmarks. Codes are available in https://github.com/BeierZhu/VRF.