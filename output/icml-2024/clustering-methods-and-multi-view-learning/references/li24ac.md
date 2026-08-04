---
title: "Integrating Global Context Contrast and Local Sensitivity for Blind Image Quality Assessment"
source: "https://proceedings.mlr.press/v235/li24ac.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24ac/li24ac.pdf"
categories: ['image-quality-assessment-and-super-resolution', 'clustering-methods-and-multi-view-learning']
tags: ['blind-IQA', 'global-context', 'local-sensitivity', 'image-quality', 'contrastive']
venue: "ICML 2024"
tldr: "A BIQA method integrates global context contrast and local sensitivity to better mirror human subjective quality judgments."
---

# Integrating Global Context Contrast and Local Sensitivity for Blind Image Quality Assessment

**Source**: [https://proceedings.mlr.press/v235/li24ac.html](https://proceedings.mlr.press/v235/li24ac.html)

**TLDR**: A BIQA method integrates global context contrast and local sensitivity to better mirror human subjective quality judgments.

## Abstract

Blind Image Quality Assessment (BIQA) mirrors subjective made by human observers. Generally, humans favor comparing relative qualities over predicting absolute qualities directly. However, current BIQA models focus on mining the "local" context, i.e., the relationship between information among individual images and the absolute quality of the image, ignoring the "global" context of the relative quality contrast among different images in the training data. In this paper, we present the Perceptual Context and Sensitivity BIQA (CSIQA), a novel contrastive learning paradigm that seamlessly integrates "global” and "local” perspectives into the BIQA. Specifically, the CSIQA comprises two primary components: 1) A Quality Context Contrastive Learning module, which is equipped with different contrastive learning strategies to effectively capture potential quality correlations in the global context of the dataset. 2) A Quality-aware Mask Attention Module, which employs the random mask to ensure the consistency with visual local sensitivity, thereby improving the model’s perception of local distortions. Extensive experiments on eight standard BIQA datasets demonstrate the superior performance to the state-of-the-art BIQA methods.