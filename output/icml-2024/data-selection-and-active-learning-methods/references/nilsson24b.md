---
title: "Indirectly Parameterized Concrete Autoencoders"
source: "https://proceedings.mlr.press/v235/nilsson24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nilsson24b/nilsson24b.pdf"
categories: ['data-selection-and-active-learning-methods', 'sampling-compression-and-dimensionality-reduction']
tags: ['feature-selection', 'concrete-autoencoders', 'indirect-parameterization']
venue: "ICML 2024"
tldr: "Improves neural network-based feature selection via indirectly parameterized Concrete Autoencoders for more accurate and stable selection."
---

# Indirectly Parameterized Concrete Autoencoders

**Source**: [https://proceedings.mlr.press/v235/nilsson24b.html](https://proceedings.mlr.press/v235/nilsson24b.html)

**TLDR**: Improves neural network-based feature selection via indirectly parameterized Concrete Autoencoders for more accurate and stable selection.

## Abstract

Feature selection is a crucial task in settings where data is high-dimensional or acquiring the full set of features is costly. Recent developments in neural network-based embedded feature selection show promising results across a wide range of applications. Concrete Autoencoders (CAEs), considered state-of-the-art in embedded feature selection, may struggle to achieve stable joint optimization, hurting their training time and generalization. In this work, we identify that this instability is correlated with the CAE learning duplicate selections. To remedy this, we propose a simple and effective improvement: Indirectly Parameterized CAEs (IP-CAEs). IP-CAEs learn an embedding and a mapping from it to the Gumbel-Softmax distributions’ parameters. Despite being simple to implement, IP-CAE exhibits significant and consistent improvements over CAE in both generalization and training time across several datasets for reconstruction and classification. Unlike CAE, IP-CAE effectively leverages non-linear relationships and does not require retraining the jointly optimized decoder. Furthermore, our approach is, in principle, generalizable to Gumbel-Softmax distributions beyond feature selection.