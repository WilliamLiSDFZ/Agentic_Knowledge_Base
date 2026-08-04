---
title: "OT-CLIP: Understanding and Generalizing CLIP via Optimal Transport"
source: "https://proceedings.mlr.press/v235/shi24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shi24b/shi24b.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'time-series-modeling-and-forecasting-methods']
tags: ['CLIP', 'optimal-transport', 'contrastive-learning']
venue: "ICML 2024"
tldr: "This paper reinterprets CLIP training through the lens of optimal transport, showing the two InfoNCE losses correspond to bilevel optimization of modified OT objectives."
---

# OT-CLIP: Understanding and Generalizing CLIP via Optimal Transport

**Source**: [https://proceedings.mlr.press/v235/shi24b.html](https://proceedings.mlr.press/v235/shi24b.html)

**TLDR**: This paper reinterprets CLIP training through the lens of optimal transport, showing the two InfoNCE losses correspond to bilevel optimization of modified OT objectives.

## Abstract

We propose to understand Contrastive Language-Image Pretraining model (CLIP) from the Optimal Transport (OT) perspective. Specifically, we show that training of CLIP is an embodiment of inverse OT and the adopted two InfoNCE losses in CLIP correspond to a special case of bilevel optimization of modified entropic OT. We then generalize the original CLIP loss to an OT-based loss family using variants of Regularized OT (e.g. Fused Gromov OT, unbalanced OT, etc.), and demonstrate their superior performance on public datasets for both image and text downstream tasks. We also rethink the inference stage of CLIP by using the tool of OT, and propose to adopt the fused Gromov OT for (zero-shot) classification, in which the prediction is based on the graph representation whereby images and texts are nodes for graph matching. By our new technique, we show how to generalize zero-shot classification to other more flexible zero-shot tasks with competitive performance: long-tailed classification and selective classification. The former assumes the known prior distribution of labels, while in the latter case, only a subset of samples are asked to predict, yet with high prediction confidence.