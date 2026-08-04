---
title: "Improved Generalization of Weight Space Networks via Augmentations"
source: "https://proceedings.mlr.press/v235/shamsian24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shamsian24a/shamsian24a.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'large-language-model-alignment-and-capabilities']
tags: ['weight-space-networks', 'data-augmentation', 'neural-fields']
venue: "ICML 2024"
tldr: "This paper improves generalization of deep weight space networks by introducing augmentation strategies for neural network weight processing tasks."
---

# Improved Generalization of Weight Space Networks via Augmentations

**Source**: [https://proceedings.mlr.press/v235/shamsian24a.html](https://proceedings.mlr.press/v235/shamsian24a.html)

**TLDR**: This paper improves generalization of deep weight space networks by introducing augmentation strategies for neural network weight processing tasks.

## Abstract

Learning in deep weight spaces (DWS), where neural networks process the weights of other neural networks, is an emerging research direction, with applications to 2D and 3D neural fields (INRs, NeRFs), as well as making inferences about other types of neural networks. Unfortunately, weight space models tend to suffer from substantial overfitting. We empirically analyze the reasons for this overfitting and find that a key reason is the lack of diversity in DWS datasets. While a given object can be represented by many different weight configurations, typical INR training sets fail to capture variability across INRs that represent the same object. To address this, we explore strategies for data augmentation in weight spaces and propose a MixUp method adapted for weight spaces. We demonstrate the effectiveness of these methods in two setups. In classification, they improve performance similarly to having up to 10 times more data. In self-supervised contrastive learning, they yield substantial 5-10% gains in downstream classification.