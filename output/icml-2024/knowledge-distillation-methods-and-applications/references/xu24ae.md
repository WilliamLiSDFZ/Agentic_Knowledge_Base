---
title: "Out-of-Distribution Detection via Deep Multi-Comprehension Ensemble"
source: "https://proceedings.mlr.press/v235/xu24ae.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24ae/xu24ae.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'knowledge-distillation-methods-and-applications']
tags: ['out-of-distribution-detection', 'ensemble-methods', 'feature-representation']
venue: "ICML 2024"
tldr: "Proposes a deep multi-comprehension ensemble method to expand OOD feature representation fields for improved detection performance."
---

# Out-of-Distribution Detection via Deep Multi-Comprehension Ensemble

**Source**: [https://proceedings.mlr.press/v235/xu24ae.html](https://proceedings.mlr.press/v235/xu24ae.html)

**TLDR**: Proposes a deep multi-comprehension ensemble method to expand OOD feature representation fields for improved detection performance.

## Abstract

Recent research works demonstrate that one of the significant factors for the model Out-of-Distirbution detection performance is the scale of the OOD feature representation field. Consequently, model ensemble emerges as a trending method to expand this feature representation field leveraging expected model diversity. However, by proposing novel qualitative and quantitative model ensemble evaluation methods (i.e., Loss Basin/Barrier Visualization and Self-Coupling Index), we reveal that the previous ensemble methods incorporate affine-transformable weights with limited variability and fail to provide desired feature representation diversity. Therefore, we escalate the traditional model ensemble dimensions (different weight initialization, data holdout, etc.) into distinct supervision tasks, which we name as Multi-Comprehension (MC) Ensemble. MC Ensemble leverages various training tasks to form different comprehensions of the data and labels, resulting in the extension of the feature representation field. In experiments, we demonstrate the superior performance of the MC Ensemble strategy in the OOD detection task compared to both the naive Deep Ensemble method and the standalone model of comparable size.