---
title: "Achieving Lossless Gradient Sparsification via Mapping to Alternative Space in Federated Learning"
source: "https://proceedings.mlr.press/v235/kim24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24e/kim24e.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'sampling-compression-and-dimensionality-reduction']
tags: ['federated-learning', 'gradient-sparsification', 'communication-compression']
venue: "ICML 2024"
tldr: "Achieves lossless gradient sparsification in federated learning by mapping gradients to an alternative space before compression."
---

# Achieving Lossless Gradient Sparsification via Mapping to Alternative Space in Federated Learning

**Source**: [https://proceedings.mlr.press/v235/kim24e.html](https://proceedings.mlr.press/v235/kim24e.html)

**TLDR**: Achieves lossless gradient sparsification in federated learning by mapping gradients to an alternative space before compression.

## Abstract

Handling the substantial communication burden in federated learning (FL) still remains a significant challenge. Although recent studies have attempted to compress the local gradients to address this issue, they typically perform compression only within the original parameter space, which may potentially limit the fundamental compression rate of the gradient. In this paper, instead of restricting our scope to a fixed traditional space, we consider an alternative space that provides an improved compressibility of the gradient. To this end, we utilize the structures of input activation and output gradient in designing our mapping function to a new space, which enables lossless gradient sparsification, i.e., mapping the gradient to our new space induces a greater number of near-zero elements without any loss of information. In light of this attribute, employing sparsification-based compressors in our new space allows for more aggressive compression with minimal information loss than the baselines. More surprisingly, our model even reaches higher accuracies than the full gradient uploading strategy in some cases, an extra benefit for utilizing the new space. We also theoretically confirm that our approach does not alter the existing, best known convergence rate of FL thanks to the orthogonal transformation properties of our mapping.