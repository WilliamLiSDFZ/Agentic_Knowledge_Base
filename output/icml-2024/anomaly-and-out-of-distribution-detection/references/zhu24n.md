---
title: "CRoFT: Robust Fine-Tuning with Concurrent Optimization for OOD Generalization and Open-Set OOD Detection"
source: "https://proceedings.mlr.press/v235/zhu24n.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhu24n/zhu24n.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['fine-tuning', 'OOD-generalization', 'open-set-detection', 'vision-language-models', 'robust-fine-tuning']
venue: "ICML 2024"
tldr: "CRoFT concurrently optimizes for OOD generalization and open-set OOD detection during fine-tuning of vision-language pre-trained models."
---

# CRoFT: Robust Fine-Tuning with Concurrent Optimization for OOD Generalization and Open-Set OOD Detection

**Source**: [https://proceedings.mlr.press/v235/zhu24n.html](https://proceedings.mlr.press/v235/zhu24n.html)

**TLDR**: CRoFT concurrently optimizes for OOD generalization and open-set OOD detection during fine-tuning of vision-language pre-trained models.

## Abstract

Recent vision-language pre-trained models (VL-PTMs) have shown remarkable success in open-vocabulary tasks. However, downstream use cases often involve further fine-tuning of VL-PTMs, which may distort their general knowledge and impair their ability to handle distribution shifts. In real-world scenarios, machine learning systems inevitably encounter both covariate shifts (e.g., changes in image styles) and semantic shifts (e.g., test-time unseen classes). This highlights the importance of enhancing out-of-distribution (OOD) generalization on covariate shifts and simultaneously detecting semantic-shifted unseen classes. Thus a critical but underexplored question arises: How to improve VL-PTMs’ generalization ability to closed-set OOD data, while effectively detecting open-set unseen classes during fine-tuning? In this paper, we propose a novel objective function of OOD detection that also serves to improve OOD generalization. We show that minimizing the gradient magnitude of energy scores on training data leads to domain-consistent Hessians of classification loss, a strong indicator for OOD generalization revealed by theoretical analysis. Based on this finding, we have developed a unified fine-tuning framework that allows for concurrent optimization of both tasks. Extensive experiments have demonstrated the superiority of our method. The code is available at https://github.com/LinLLLL/CRoFT.