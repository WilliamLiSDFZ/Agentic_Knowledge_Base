---
title: "Stacking Deep Set Networks and Pooling by Quantiles"
source: "https://proceedings.mlr.press/v235/chen24bo.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24bo/chen24bo.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'clustering-methods-and-multi-view-learning']
tags: ['deep-sets', 'quantile-pooling', 'set-learning']
venue: "ICML 2024"
tldr: "Stacked Deep Sets with Quantile Pooling introduces a novel permutation-invariant pooling operation for improved learning on set-structured data."
---

# Stacking Deep Set Networks and Pooling by Quantiles

**Source**: [https://proceedings.mlr.press/v235/chen24bo.html](https://proceedings.mlr.press/v235/chen24bo.html)

**TLDR**: Stacked Deep Sets with Quantile Pooling introduces a novel permutation-invariant pooling operation for improved learning on set-structured data.

## Abstract

We propose Stacked Deep Sets and Quantile Pooling for learning tasks on set data. We introduce Quantile Pooling, a novel permutation-invariant pooling operation that synergizes max and average pooling. Just like max pooling, quantile pooling emphasizes the most salient features of the data. Like average pooling, it captures the overall distribution and subtle features of the data. Like both, it is lightweight and fast. We demonstrate the effectiveness of our approach in a variety of tasks, showing that quantile pooling can outperform both max and average pooling in each of their respective strengths. We also introduce a variant of deep set networks that is more expressive and universal. While Quantile Pooling balances robustness and sensitivity, Stacked Deep Sets enhances learning with depth.