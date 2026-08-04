---
title: "MMPareto: Boosting Multimodal Learning with Innocent Unimodal Assistance"
source: "https://proceedings.mlr.press/v235/wei24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wei24d/wei24d.pdf"
categories: ['clustering-methods-and-multi-view-learning']
tags: ['multimodal-learning', 'gradient-conflict', 'pareto-optimization']
venue: "ICML 2024"
tldr: "MMPareto addresses gradient conflicts between multimodal and unimodal objectives to improve balanced multimodal representation learning."
---

# MMPareto: Boosting Multimodal Learning with Innocent Unimodal Assistance

**Source**: [https://proceedings.mlr.press/v235/wei24d.html](https://proceedings.mlr.press/v235/wei24d.html)

**TLDR**: MMPareto addresses gradient conflicts between multimodal and unimodal objectives to improve balanced multimodal representation learning.

## Abstract

Multimodal learning methods with targeted unimodal learning objectives have exhibited their superior efficacy in alleviating the imbalanced multimodal learning problem. However, in this paper, we identify the previously ignored gradient conflict between multimodal and unimodal learning objectives, potentially misleading the unimodal encoder optimization. To well diminish these conflicts, we observe the discrepancy between multimodal loss and unimodal loss, where both gradient magnitude and covariance of the easier-to-learn multimodal loss are smaller than the unimodal one. With this property, we analyze Pareto integration under our multimodal scenario and propose MMPareto algorithm, which could ensure a final gradient with direction that is common to all learning objectives and enhanced magnitude to improve generalization, providing innocent unimodal assistance. Finally, experiments across multiple types of modalities and frameworks with dense cross-modal interaction indicate our superior and extendable method performance. Our method is also expected to facilitate multi-task cases with a clear discrepancy in task difficulty, demonstrating its ideal scalability. The source code and dataset are available at https://github.com/GeWu-Lab/MMPareto_ICML2024.