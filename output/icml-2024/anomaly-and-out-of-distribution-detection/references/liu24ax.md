---
title: "Fast Decision Boundary based Out-of-Distribution Detector"
source: "https://proceedings.mlr.press/v235/liu24ax.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24ax/liu24ax.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'adversarial-robustness-and-model-security']
tags: ['out-of-distribution-detection', 'decision-boundary', 'efficiency']
venue: "ICML 2024"
tldr: "A fast OOD detector based on decision boundaries that achieves effective detection with significantly reduced computational overhead compared to feature-space methods."
---

# Fast Decision Boundary based Out-of-Distribution Detector

**Source**: [https://proceedings.mlr.press/v235/liu24ax.html](https://proceedings.mlr.press/v235/liu24ax.html)

**TLDR**: A fast OOD detector based on decision boundaries that achieves effective detection with significantly reduced computational overhead compared to feature-space methods.

## Abstract

Efficient and effective Out-of-Distribution (OOD) detection is essential for the safe deployment of AI systems. Existing feature space methods, while effective, often incur significant computational overhead due to their reliance on auxiliary models built from training features. In this paper, we propose a computationally-efficient OOD detector without using auxiliary models while still leveraging the rich information embedded in the feature space. Specifically, we detect OOD samples based on their feature distances to decision boundaries. To minimize computational cost, we introduce an efficient closed-form estimation, analytically proven to tightly lower bound the distance. Based on our estimation, we discover that In-Distribution (ID) features tend to be further from decision boundaries than OOD features. Additionally, ID and OOD samples are better separated when compared at equal deviation levels from the mean of training features. By regularizing the distances to decision boundaries based on feature deviation from the mean, we develop a hyperparameter-free, auxiliary model-free OOD detector. Our method matches or surpasses the effectiveness of state-of-the-art methods in extensive experiments while incurring negligible overhead in inference latency. Overall, our approach significantly improves the efficiency-effectiveness trade-off in OOD detection. Code is available at: https://github.com/litianliu/fDBD-OOD.