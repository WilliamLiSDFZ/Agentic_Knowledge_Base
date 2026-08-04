---
title: "Mind the Boundary: Coreset Selection via Reconstructing the Decision Boundary"
source: "https://proceedings.mlr.press/v235/yang24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24b/yang24b.pdf"
categories: ['data-selection-and-active-learning-methods', 'sampling-compression-and-dimensionality-reduction']
tags: ['coreset-selection', 'decision-boundary', 'data-pruning']
venue: "ICML 2024"
tldr: "Proposes a geometry-based coreset selection method that identifies informative training samples by reconstructing the classifier's decision boundary."
---

# Mind the Boundary: Coreset Selection via Reconstructing the Decision Boundary

**Source**: [https://proceedings.mlr.press/v235/yang24b.html](https://proceedings.mlr.press/v235/yang24b.html)

**TLDR**: Proposes a geometry-based coreset selection method that identifies informative training samples by reconstructing the classifier's decision boundary.

## Abstract

Existing paradigms of pushing the state of the art require exponentially more training data in many fields. Coreset selection seeks to mitigate this growing demand by identifying the most efficient subset of training data. In this paper, we delve into geometry-based coreset methods and preliminarily link the geometry of data distribution with models’ generalization capability in theoretics. Leveraging these theoretical insights, we propose a novel coreset construction method by selecting training samples to reconstruct the decision boundary of a deep neural network learned on the full dataset. Extensive experiments across various popular benchmarks demonstrate the superiority of our method over multiple competitors. For the first time, our method achieves a 50% data pruning rate on the ImageNet-1K dataset while sacrificing less than 1% in accuracy. Additionally, we showcase and analyze the remarkable cross-architecture transferability of the coresets derived from our approach.