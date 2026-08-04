---
title: "ELTA: An Enhancer against Long-Tail for Aesthetics-oriented Models"
source: "https://proceedings.mlr.press/v235/liu24w.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24w/liu24w.pdf"
categories: ['fairness-aware-algorithmic-decision-making']
tags: ['long-tail', 'image-aesthetics', 'fairness']
venue: "ICML 2024"
tldr: "ELTA is proposed to mitigate long-tail distribution effects in image aesthetics assessment models to improve fairness and generalization."
---

# ELTA: An Enhancer against Long-Tail for Aesthetics-oriented Models

**Source**: [https://proceedings.mlr.press/v235/liu24w.html](https://proceedings.mlr.press/v235/liu24w.html)

**TLDR**: ELTA is proposed to mitigate long-tail distribution effects in image aesthetics assessment models to improve fairness and generalization.

## Abstract

Real-world datasets often exhibit long-tailed distributions, compromising the generalization and fairness of learning-based models. This issue is particularly pronounced in Image Aesthetics Assessment (IAA) tasks, where such imbalance is difficult to mitigate due to a severe distribution mismatch between features and labels, as well as the great sensitivity of aesthetics to image variations. To address these issues, we propose an Enhancer against Long-Tail for Aesthetics-oriented models (ELTA). ELTA first utilizes a dedicated mixup technique to enhance minority feature representation in high-level space while preserving their intrinsic aesthetic qualities. Next, it aligns features and labels through a similarity consistency approach, effectively alleviating the distribution mismatch. Finally, ELTA adopts a specific strategy to refine the output distribution, thereby enhancing the quality of pseudo-labels. Experiments on four representative datasets (AVA, AADB, TAD66K, and PARA) show that our proposed ELTA achieves state-of-the-art performance by effectively mitigating the long-tailed issue in IAA datasets. Moreover, ELTA is designed with plug-and-play capabilities for seamless integration with existing methods. To our knowledge, this is the first contribution in the IAA community addressing long-tail. All resources are available in here.