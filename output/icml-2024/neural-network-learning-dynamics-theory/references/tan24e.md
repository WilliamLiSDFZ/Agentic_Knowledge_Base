---
title: "Information Flow in Self-Supervised Learning"
source: "https://proceedings.mlr.press/v235/tan24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tan24e/tan24e.pdf"
categories: ['neural-network-learning-dynamics-theory']
tags: ['self-supervised-learning', 'matrix-mutual-information', 'Siamese-networks']
venue: "ICML 2024"
tldr: "Barlow Twins and spectral contrastive learning are analyzed through matrix mutual information, revealing implicit optimization of information-theoretic objectives."
---

# Information Flow in Self-Supervised Learning

**Source**: [https://proceedings.mlr.press/v235/tan24e.html](https://proceedings.mlr.press/v235/tan24e.html)

**TLDR**: Barlow Twins and spectral contrastive learning are analyzed through matrix mutual information, revealing implicit optimization of information-theoretic objectives.

## Abstract

In this paper, we conduct a comprehensive analysis of two dual-branch (Siamese architecture) self-supervised learning approaches, namely Barlow Twins and spectral contrastive learning, through the lens of matrix mutual information. We prove that the loss functions of these methods implicitly optimize both matrix mutual information and matrix joint entropy. This insight prompts us to further explore the category of single-branch algorithms, specifically MAE and U-MAE, for which mutual information and joint entropy become the entropy. Building on this intuition, we introduce the Matrix Variational Masked Auto-Encoder (M-MAE), a novel method that leverages the matrix-based estimation of entropy as a regularizer and subsumes U-MAE as a special case. The empirical evaluations underscore the effectiveness of M-MAE compared with the state-of-the-art methods, including a 3.9% improvement in linear probing ViT-Base, and a 1% improvement in fine-tuning ViT-Large, both on ImageNet.