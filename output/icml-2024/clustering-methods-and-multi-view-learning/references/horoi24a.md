---
title: "Harmony in Diversity: Merging Neural Networks with Canonical Correlation Analysis"
source: "https://proceedings.mlr.press/v235/horoi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/horoi24a/horoi24a.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'sufficient-dimension-reduction-correlation-methods']
tags: ['model-merging', 'model-fusion', 'canonical-correlation-analysis', 'ensembling', 'neural-networks']
venue: "ICML 2024"
tldr: "Uses canonical correlation analysis to merge multiple neural networks into a single model, reducing computational costs while preserving ensemble diversity."
---

# Harmony in Diversity: Merging Neural Networks with Canonical Correlation Analysis

**Source**: [https://proceedings.mlr.press/v235/horoi24a.html](https://proceedings.mlr.press/v235/horoi24a.html)

**TLDR**: Uses canonical correlation analysis to merge multiple neural networks into a single model, reducing computational costs while preserving ensemble diversity.

## Abstract

Combining the predictions of multiple trained models through ensembling is generally a good way to improve accuracy by leveraging the different learned features of the models, however it comes with high computational and storage costs. Model fusion, the act of merging multiple models into one by combining their parameters reduces these costs but doesn’t work as well in practice. Indeed, neural network loss landscapes are high-dimensional and non-convex and the minima found through learning are typically separated by high loss barriers. Numerous recent works have been focused on finding permutations matching one network features to the features of a second one, lowering the loss barrier on the linear path between them in parameter space. However, permutations are restrictive since they assume a one-to-one mapping between the different models’ neurons exists. We propose a new model merging algorithm, CCA Merge, which is based on Canonical Correlation Analysis and aims to maximize the correlations between linear combinations of the model features. We show that our alignment method leads to better performances than past methods when averaging models trained on the same, or differing data splits. We also extend this analysis into the harder setting where more than 2 models are merged, and we find that CCA Merge works significantly better than past methods. Our code is publicly available at https://github.com/shoroi/align-n-merge