---
title: "Distribution Alignment Optimization through Neural Collapse for Long-tailed Classification"
source: "https://proceedings.mlr.press/v235/gao24s.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gao24s/gao24s.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'fairness-aware-algorithmic-decision-making']
tags: ['neural-collapse', 'long-tailed-classification', 'distribution-alignment', 'imbalanced-learning']
venue: "ICML 2024"
tldr: "Distribution alignment optimization via neural collapse geometry improves classification performance on long-tailed datasets by encouraging balanced feature structures."
---

# Distribution Alignment Optimization through Neural Collapse for Long-tailed Classification

**Source**: [https://proceedings.mlr.press/v235/gao24s.html](https://proceedings.mlr.press/v235/gao24s.html)

**TLDR**: Distribution alignment optimization via neural collapse geometry improves classification performance on long-tailed datasets by encouraging balanced feature structures.

## Abstract

A well-trained deep neural network on balanced datasets usually exhibits the Neural Collapse (NC) phenomenon, which is an informative indicator of the model achieving good performance. However, NC is usually hard to be achieved for a model trained on long-tailed datasets, leading to the deteriorated performance of test data. This work aims to induce the NC phenomenon in imbalanced learning from the perspective of distribution matching. By enforcing the distribution of last-layer representations to align the ideal distribution of the ETF structure, we develop a Distribution Alignment Optimization (DisA) loss, acting as a plug-and-play method can be combined with most of the existing long-tailed methods, we further instantiate it to the cases of fixing classifier and learning classifier. The extensive experiments show the effectiveness of DisA, providing a promising solution to the imbalanced issue. Our code is available at DisA.