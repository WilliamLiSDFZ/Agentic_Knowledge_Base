---
title: "Balanced Data, Imbalanced Spectra: Unveiling Class Disparities with Spectral Imbalance"
source: "https://proceedings.mlr.press/v235/kaushik24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kaushik24a/kaushik24a.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'learning-with-imperfect-data-and-bias']
tags: ['class-bias', 'spectral-imbalance', 'balanced-datasets']
venue: "ICML 2024"
tldr: "Reveals that class performance disparities in balanced datasets arise from spectral imbalance in feature representations."
---

# Balanced Data, Imbalanced Spectra: Unveiling Class Disparities with Spectral Imbalance

**Source**: [https://proceedings.mlr.press/v235/kaushik24a.html](https://proceedings.mlr.press/v235/kaushik24a.html)

**TLDR**: Reveals that class performance disparities in balanced datasets arise from spectral imbalance in feature representations.

## Abstract

Classification models are expected to perform equally well for different classes, yet in practice, there are often large gaps in their performance. This issue of class bias is widely studied in cases of datasets with sample imbalance, but is relatively overlooked in balanced datasets. In this work, we introduce the concept of spectral imbalance in features as a potential source for class disparities and study the connections between spectral imbalance and class bias in both theory and practice. To build the connection between spectral imbalance and class gap, we develop a theoretical framework for studying class disparities and derive exact expressions for the per-class error in a high-dimensional mixture model setting. We then study this phenomenon in 11 different state-of-the-art pre-trained encoders, and show how our proposed framework can be used to compare the quality of encoders, as well as evaluate and combine data augmentation strategies to mitigate the issue. Our work sheds light on the class-dependent effects of learning, and provides new insights into how state-of-the-art pre-trained features may have unknown biases that can be diagnosed through their spectra.