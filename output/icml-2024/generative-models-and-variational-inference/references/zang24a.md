---
title: "DiffAug: Enhance Unsupervised Contrastive Learning with Domain-Knowledge-Free Diffusion-based Data Augmentation"
source: "https://proceedings.mlr.press/v235/zang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zang24a/zang24a.pdf"
categories: ['generative-models-and-variational-inference', 'clustering-methods-and-multi-view-learning']
tags: ['contrastive-learning', 'data-augmentation', 'diffusion-models']
venue: "ICML 2024"
tldr: "A diffusion-based data augmentation method for unsupervised contrastive learning that requires no domain knowledge to generate effective positive samples."
---

# DiffAug: Enhance Unsupervised Contrastive Learning with Domain-Knowledge-Free Diffusion-based Data Augmentation

**Source**: [https://proceedings.mlr.press/v235/zang24a.html](https://proceedings.mlr.press/v235/zang24a.html)

**TLDR**: A diffusion-based data augmentation method for unsupervised contrastive learning that requires no domain knowledge to generate effective positive samples.

## Abstract

Unsupervised Contrastive learning has gained prominence in fields such as vision, and biology, leveraging predefined positive/negative samples for representation learning. Data augmentation, categorized into hand-designed and model-based methods, has been identified as a crucial component for enhancing contrastive learning. However, hand-designed methods require human expertise in domain-specific data while sometimes distorting the meaning of the data. In contrast, generative model-based approaches usually require supervised or large-scale external data, which has become a bottleneck constraining model training in many domains. To address the problems presented above, this paper proposes DiffAug, a novel unsupervised contrastive learning technique with diffusion mode-based positive data generation. DiffAug consists of a semantic encoder and a conditional diffusion model; the conditional diffusion model generates new positive samples conditioned on the semantic encoding to serve the training of unsupervised contrast learning. With the help of iterative training of the semantic encoder and diffusion model, DiffAug improves the representation ability in an uninterrupted and unsupervised manner. Experimental evaluations show that DiffAug outperforms hand-designed and SOTA model-based augmentation methods on DNA sequence, visual, and bio-feature datasets. The code for review is released at DiffAug CODE.