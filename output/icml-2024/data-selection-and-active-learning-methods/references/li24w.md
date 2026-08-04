---
title: "Adaptive Feature Selection for No-Reference Image Quality Assessment by Mitigating Semantic Noise Sensitivity"
source: "https://proceedings.mlr.press/v235/li24w.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24w/li24w.pdf"
categories: ['image-quality-assessment-and-super-resolution', 'data-selection-and-active-learning-methods']
tags: ['no-reference-IQA', 'feature-selection', 'semantic-noise', 'image-quality']
venue: "ICML 2024"
tldr: "An adaptive feature selection method mitigates semantic noise sensitivity in no-reference image quality assessment."
---

# Adaptive Feature Selection for No-Reference Image Quality Assessment by Mitigating Semantic Noise Sensitivity

**Source**: [https://proceedings.mlr.press/v235/li24w.html](https://proceedings.mlr.press/v235/li24w.html)

**TLDR**: An adaptive feature selection method mitigates semantic noise sensitivity in no-reference image quality assessment.

## Abstract

The current state-of-the-art No-Reference Image Quality Assessment (NR-IQA) methods typically rely on feature extraction from upstream semantic backbone networks, assuming that all extracted features are relevant. However, we make a key observation that not all features are beneficial, and some may even be harmful, necessitating careful selection. Empirically, we find that many image pairs with small feature spatial distances can have vastly different quality scores, indicating that the extracted features may contain quality-irrelevant noise. To address this issue, we propose a Quality-Aware Feature Matching IQA Metric (QFM-IQM) that employs an adversarial perspective to remove harmful semantic noise features from the upstream task. Specifically, QFM-IQM enhances the semantic noise distinguish capabilities by matching image pairs with similar quality scores but varying semantic features as adversarial semantic noise and adaptively adjusting the upstream task’s features by reducing sensitivity to adversarial noise perturbation. Furthermore, we utilize a distillation framework to expand the dataset and improve the model’s generalization ability. Extensive experiments conducted on eight standard IQA datasets have demonstrated the effectiveness of our proposed QFM-IQM.