---
title: "Uncertainty for Active Learning on Graphs"
source: "https://proceedings.mlr.press/v235/fuchsgruber24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fuchsgruber24a/fuchsgruber24a.pdf"
categories: ['data-selection-and-active-learning-methods', 'graph-neural-networks-and-topology']
tags: ['active-learning', 'graph-neural-networks', 'uncertainty-sampling']
venue: "ICML 2024"
tldr: "This paper investigates uncertainty sampling strategies for active learning specifically on graph-structured data to improve label efficiency."
---

# Uncertainty for Active Learning on Graphs

**Source**: [https://proceedings.mlr.press/v235/fuchsgruber24a.html](https://proceedings.mlr.press/v235/fuchsgruber24a.html)

**TLDR**: This paper investigates uncertainty sampling strategies for active learning specifically on graph-structured data to improve label efficiency.

## Abstract

Uncertainty Sampling is an Active Learning strategy that aims to improve the data efficiency of machine learning models by iteratively acquiring labels of data points with the highest uncertainty. While it has proven effective for independent data its applicability to graphs remains under-explored. We propose the first extensive study of Uncertainty Sampling for node classification: (1) We benchmark Uncertainty Sampling beyond predictive uncertainty and highlight a significant performance gap to other Active Learning strategies. (2) We develop ground-truth Bayesian uncertainty estimates in terms of the data generating process and prove their effectiveness in guiding Uncertainty Sampling toward optimal queries. We confirm our results on synthetic data and design an approximate approach that consistently outperforms other uncertainty estimators on real datasets. (3) Based on this analysis, we relate pitfalls in modeling uncertainty to existing methods. Our analysis enables and informs the development of principled uncertainty estimation on graphs.