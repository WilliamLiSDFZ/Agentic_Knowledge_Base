---
title: "Simplicity Bias of Two-Layer Networks beyond Linearly Separable Data"
source: "https://proceedings.mlr.press/v235/tsoy24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tsoy24a/tsoy24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'learning-with-imperfect-data-and-bias']
tags: ['simplicity-bias', 'two-layer-networks', 'out-of-distribution-generalization']
venue: "ICML 2024"
tldr: "Theoretically characterizes simplicity bias in two-layer networks beyond linearly separable data settings."
---

# Simplicity Bias of Two-Layer Networks beyond Linearly Separable Data

**Source**: [https://proceedings.mlr.press/v235/tsoy24a.html](https://proceedings.mlr.press/v235/tsoy24a.html)

**TLDR**: Theoretically characterizes simplicity bias in two-layer networks beyond linearly separable data settings.

## Abstract

Simplicity bias, the propensity of deep models to over-rely on simple features, has been identified as a potential reason for limited out-of-distribution generalization of neural networks (Shah et al., 2020). Despite the important implications, this phenomenon has been theoretically confirmed and characterized only under strong dataset assumptions, such as linear separability (Lyu et al., 2021). In this work, we characterize simplicity bias for general datasets in the context of two-layer neural networks initialized with small weights and trained with gradient flow. Specifically, we prove that in the early training phases, network features cluster around a few directions that do not depend on the size of the hidden layer. Furthermore, for datasets with an XOR-like pattern, we precisely identify the learned features and demonstrate that simplicity bias intensifies during later training stages. These results indicate that features learned in the middle stages of training may be more useful for OOD transfer. We support this hypothesis with experiments on image data.