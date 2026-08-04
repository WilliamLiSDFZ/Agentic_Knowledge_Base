---
title: "Rejuvenating image-GPT as Strong Visual Representation Learners"
source: "https://proceedings.mlr.press/v235/ren24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ren24d/ren24d.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'generative-models-and-variational-inference']
tags: ['autoregressive-pretraining', 'image-GPT', 'visual-representation', 'semantic-tokens', 'next-token-prediction']
venue: "ICML 2024"
tldr: "Image-GPT is enhanced by shifting prediction targets from raw pixels to semantic tokens and introducing other improvements for stronger visual representation learning."
---

# Rejuvenating image-GPT as Strong Visual Representation Learners

**Source**: [https://proceedings.mlr.press/v235/ren24d.html](https://proceedings.mlr.press/v235/ren24d.html)

**TLDR**: Image-GPT is enhanced by shifting prediction targets from raw pixels to semantic tokens and introducing other improvements for stronger visual representation learning.

## Abstract

This paper enhances image-GPT (iGPT), one of the pioneering works that introduce autoregressive pretraining to predict the next pixels for visual representation learning. Two simple yet essential changes are made. First, we shift the prediction target from raw pixels to semantic tokens, enabling a higher-level understanding of visual content. Second, we supplement the autoregressive modeling by instructing the model to predict not only the next tokens but also the visible tokens. This pipeline is particularly effective when semantic tokens are encoded by discriminatively trained models, such as CLIP. We introduce this novel approach as D-iGPT. Extensive experiments showcase that D-iGPT excels as a strong learner of visual representations: A notable achievement is its compelling performance on the ImageNet-1K dataset — by training on publicly available datasets, D-iGPT unprecedentedly achieves 90.0% top-1 accuracy with a vanilla ViT-H. Additionally, D-iGPT shows strong generalization on the downstream task. Code is available at https://github.com/OliverRensu/D-iGPT.