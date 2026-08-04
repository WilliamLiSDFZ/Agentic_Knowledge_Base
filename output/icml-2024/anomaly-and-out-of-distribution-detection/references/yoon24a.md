---
title: "Uncertainty Estimation by Density Aware Evidential Deep Learning"
source: "https://proceedings.mlr.press/v235/yoon24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yoon24a/yoon24a.pdf"
categories: ['anomaly-and-out-of-distribution-detection']
tags: ['evidential-deep-learning', 'uncertainty-estimation', 'OOD-detection', 'density-awareness']
venue: "ICML 2024"
tldr: "Density-aware evidential deep learning is proposed to improve OOD detection and uncertainty estimation beyond standard EDL."
---

# Uncertainty Estimation by Density Aware Evidential Deep Learning

**Source**: [https://proceedings.mlr.press/v235/yoon24a.html](https://proceedings.mlr.press/v235/yoon24a.html)

**TLDR**: Density-aware evidential deep learning is proposed to improve OOD detection and uncertainty estimation beyond standard EDL.

## Abstract

Evidential deep learning (EDL) has shown remarkable success in uncertainty estimation. However, there is still room for improvement, particularly in out-of-distribution (OOD) detection and classification tasks. The limited OOD detection performance of EDL arises from its inability to reflect the distance between the testing example and training data when quantifying uncertainty, while its limited classification performance stems from its parameterization of the concentration parameters. To address these limitations, we propose a novel method called Density Aware Evidential Deep Learning (DAEDL). DAEDL integrates the feature space density of the testing example with the output of EDL during the prediction stage, while using a novel parameterization that resolves the issues in the conventional parameterization. We prove that DAEDL enjoys a number of favorable theoretical properties. DAEDL demonstrates state-of-the-art performance across diverse downstream tasks related to uncertainty estimation and classification.