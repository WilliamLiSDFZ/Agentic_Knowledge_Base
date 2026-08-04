---
title: "SAM as the Guide: Mastering Pseudo-Label Refinement in Semi-Supervised Referring Expression Segmentation"
source: "https://proceedings.mlr.press/v235/yang24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24k/yang24k.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'test-time-adaptation-methods-and-evaluation']
tags: ['semi-supervised-learning', 'pseudo-labels', 'referring-expression-segmentation']
venue: "ICML 2024"
tldr: "SemiRES is a semi-supervised framework using SAM to refine noisy pseudo-labels for referring expression segmentation."
---

# SAM as the Guide: Mastering Pseudo-Label Refinement in Semi-Supervised Referring Expression Segmentation

**Source**: [https://proceedings.mlr.press/v235/yang24k.html](https://proceedings.mlr.press/v235/yang24k.html)

**TLDR**: SemiRES is a semi-supervised framework using SAM to refine noisy pseudo-labels for referring expression segmentation.

## Abstract

In this paper, we introduce SemiRES, a semi-supervised framework that effectively leverages a combination of labeled and unlabeled data to perform RES. A significant hurdle in applying semi-supervised techniques to RES is the prevalence of noisy pseudo-labels, particularly at the boundaries of objects. SemiRES incorporates the Segment Anything Model (SAM), renowned for its precise boundary demarcation, to improve the accuracy of these pseudo-labels. Within SemiRES, we offer two alternative matching strategies: IoU-based Optimal Matching (IOM) and Composite Parts Integration (CPI). These strategies are designed to extract the most accurate masks from SAM’s output, thus guiding the training of the student model with enhanced precision. In instances where a precise mask cannot be matched from the available candidates, we develop the Pixel-Wise Adjustment (PWA) strategy, guiding the student model’s training directly by the pseudo-labels. Extensive experiments on three RES benchmarks—RefCOCO, RefCOCO+, and G-Ref reveal its superior performance compared to fully supervised methods, especially in low-data scenarios. Remarkably, with only 1% labeled data, our SemiRES outperforms the supervised baseline by a large margin, e.g. +18.64% gains on RefCOCO val set.