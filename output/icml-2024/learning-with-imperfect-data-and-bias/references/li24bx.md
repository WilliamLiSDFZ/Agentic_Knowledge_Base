---
title: "Size-invariance Matters: Rethinking Metrics and Losses for Imbalanced Multi-object Salient Object Detection"
source: "https://proceedings.mlr.press/v235/li24bx.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bx/li24bx.pdf"
categories: ['neural-operators-for-pde-solving', 'learning-with-imperfect-data-and-bias']
tags: ['salient-object-detection', 'size-invariance', 'imbalanced-data']
venue: "ICML 2024"
tldr: "Identifies size-sensitivity issues in salient object detection metrics and proposes size-invariant metrics and losses for multi-object scenarios."
---

# Size-invariance Matters: Rethinking Metrics and Losses for Imbalanced Multi-object Salient Object Detection

**Source**: [https://proceedings.mlr.press/v235/li24bx.html](https://proceedings.mlr.press/v235/li24bx.html)

**TLDR**: Identifies size-sensitivity issues in salient object detection metrics and proposes size-invariant metrics and losses for multi-object scenarios.

## Abstract

This paper explores the size-invariance of evaluation metrics in Salient Object Detection (SOD), especially when multiple targets of diverse sizes co-exist in the same image. We observe that current metrics are size-sensitive, where larger objects are focused, and smaller ones tend to be ignored. We argue that the evaluation should be size-invariant because bias based on size is unjustified without additional semantic information. In pursuit of this, we propose a generic approach that evaluates each salient object separately and then combines the results, effectively alleviating the imbalance. We further develop an optimization framework tailored to this goal, achieving considerable improvements in detecting objects of different sizes. Theoretically, we provide evidence supporting the validity of our new metrics and present the generalization analysis of SOD. Extensive experiments demonstrate the effectiveness of our method.