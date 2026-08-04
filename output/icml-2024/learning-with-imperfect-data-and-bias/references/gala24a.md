---
title: "Leverage Class-Specific Accuracy to Guide Data Generation for Improving Image Classification"
source: "https://proceedings.mlr.press/v235/gala24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gala24a/gala24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'data-selection-and-active-learning-methods']
tags: ['data-augmentation', 'generative-models', 'class-specific-accuracy', 'image-classification']
venue: "ICML 2024"
tldr: "A class-accuracy-guided data generation method leverages deep generative models to selectively augment training data for improving image classification."
---

# Leverage Class-Specific Accuracy to Guide Data Generation for Improving Image Classification

**Source**: [https://proceedings.mlr.press/v235/gala24a.html](https://proceedings.mlr.press/v235/gala24a.html)

**TLDR**: A class-accuracy-guided data generation method leverages deep generative models to selectively augment training data for improving image classification.

## Abstract

In many image classification applications, the number of labeled training images is limited, which leads to model overfitting. To mitigate the lack of training data, deep generative models have been leveraged to generate synthetic training data. However, existing methods generate data for individual classes based on how much training data they have without considering their actual data needs. To address this limitation, we propose needs-aware image generation, which automatically identifies the different data needs of individual classes based on their classification performance and divides a limited data generation budget into these classes according to their needs. We propose a multi-level optimization based framework which performs four learning stages in an end-to-end manner. Experiments on both imbalanced and balanced classification datasets demonstrate the effectiveness of our proposed method.