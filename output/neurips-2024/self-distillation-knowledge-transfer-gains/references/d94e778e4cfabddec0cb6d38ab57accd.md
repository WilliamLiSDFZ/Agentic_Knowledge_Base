---
title: "Learning from Offline Foundation Features with Tensor Augmentations"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/d94e778e4cfabddec0cb6d38ab57accd-Abstract-Conference.html"
categories: ['self-distillation-knowledge-transfer-gains', 'deep-learning-optimization-and-generalization-theory']
tags: ['foundation-models', 'offline-features', 'tensor-augmentation', 'efficient-training', 'limited-resources']
venue: "NeurIPS 2024"
tldr: "LOFF-TA trains compact classifiers on pre-extracted foundation model features with tensor augmentations to enable efficient learning in resource-constrained settings."
---

# Learning from Offline Foundation Features with Tensor Augmentations

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/d94e778e4cfabddec0cb6d38ab57accd-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/d94e778e4cfabddec0cb6d38ab57accd-Abstract-Conference.html)

**TLDR**: LOFF-TA trains compact classifiers on pre-extracted foundation model features with tensor augmentations to enable efficient learning in resource-constrained settings.

## Abstract

We introduce Learning from Offline Foundation Features with Tensor Augmentations (LOFF-TA), an efficient training scheme designed to harness the capabilities of foundation models in limited resource settings where their direct development is not feasible. LOFF-TA involves training a compact classifier on cached feature embeddings  from a frozen foundation model, resulting in up to  $37\times$ faster training and up to $26\times$ reduced GPU memory usage. Because the embeddings of augmented images would be too numerous to store, yet the augmentation process is essential for training, we propose to apply tensor augmentations to the cached embeddings of the original non-augmented images. LOFF-TA makes it possible to leverage the power of foundation models, regardless of their size, in settings with limited computational capacity. Moreover, LOFF-TA can be used to apply foundation models to high-resolution images without increasing compute.    In certain scenarios, we find that training with LOFF-TA yields better results than directly fine-tuning the foundation model.