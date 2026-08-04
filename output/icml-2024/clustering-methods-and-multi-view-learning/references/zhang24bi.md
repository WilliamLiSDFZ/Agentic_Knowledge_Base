---
title: "Matrix Information Theory for Self-Supervised Learning"
source: "https://proceedings.mlr.press/v235/zhang24bi.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24bi/zhang24bi.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'generative-models-and-variational-inference']
tags: ['self-supervised-learning', 'matrix-information-theory', 'contrastive-learning', 'maximum-entropy', 'representation-learning']
venue: "ICML 2024"
tldr: "Introduces Matrix-SSL, leveraging matrix information theory to unify and improve non-contrastive self-supervised learning methods."
---

# Matrix Information Theory for Self-Supervised Learning

**Source**: [https://proceedings.mlr.press/v235/zhang24bi.html](https://proceedings.mlr.press/v235/zhang24bi.html)

**TLDR**: Introduces Matrix-SSL, leveraging matrix information theory to unify and improve non-contrastive self-supervised learning methods.

## Abstract

The maximum entropy encoding framework provides a unified perspective for many non-contrastive learning methods like SimSiam, Barlow Twins, and MEC. Inspired by this framework, we introduce Matrix-SSL, a novel approach that leverages matrix information theory to interpret the maximum entropy encoding loss as matrix uniformity loss. Furthermore, Matrix-SSL enhances the maximum entropy encoding method by seamlessly incorporating matrix alignment loss, directly aligning covariance matrices in different branches. Experimental results reveal that Matrix-SSL outperforms state-of-the-art methods on the ImageNet dataset under linear evaluation settings and on MS-COCO for transfer learning tasks. Specifically, when performing transfer learning tasks on MS-COCO, our method outperforms previous SOTA methods such as MoCo v2 and BYOL up to 3.3% with only 400 epochs compared to 800 epochs pre-training. We also try to introduce representation learning into the language modeling regime by fine-tuning a 7B model using matrix cross-entropy loss, with a margin of 3.1% on the GSM8K dataset over the standard cross-entropy loss.