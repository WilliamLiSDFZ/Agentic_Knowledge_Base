---
title: "Adaptive Hierarchical Certification for Segmentation using Randomized Smoothing"
source: "https://proceedings.mlr.press/v235/anani24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/anani24a/anani24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['randomized-smoothing', 'certification', 'segmentation', 'hierarchical-classification']
venue: "ICML 2024"
tldr: "Proposes adaptive hierarchical certification for segmentation that reduces abstain rates by leveraging class hierarchies with randomized smoothing."
---

# Adaptive Hierarchical Certification for Segmentation using Randomized Smoothing

**Source**: [https://proceedings.mlr.press/v235/anani24a.html](https://proceedings.mlr.press/v235/anani24a.html)

**TLDR**: Proposes adaptive hierarchical certification for segmentation that reduces abstain rates by leveraging class hierarchies with randomized smoothing.

## Abstract

Certification for machine learning is proving that no adversarial sample can evade a model within a range under certain conditions, a necessity for safety-critical domains. Common certification methods for segmentation use a flat set of fine-grained classes, leading to high abstain rates due to model uncertainty across many classes. We propose a novel, more practical setting, which certifies pixels within a multi-level hierarchy, and adaptively relaxes the certification to a coarser level for unstable components classic methods would abstain from, effectively lowering the abstain rate whilst providing more certified semantically meaningful information. We mathematically formulate the problem setup, introduce an adaptive hierarchical certification algorithm and prove the correctness of its guarantees. Since certified accuracy does not take the loss of information into account for coarser classes, we introduce the Certified Information Gain ($\mathrm{CIG}$) metric, which is proportional to the class granularity level. Our extensive experiments on the datasets Cityscapes, PASCAL-Context, ACDC and COCO-Stuff demonstrate that our adaptive algorithm achieves a higher $\mathrm{CIG}$ and lower abstain rate compared to the current state-of-the-art certification method. Our code can be found here: https://github.com/AlaaAnani/adaptive-certify.