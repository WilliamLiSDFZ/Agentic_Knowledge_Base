---
title: "Reweighted Solutions for Weighted Low Rank Approximation"
source: "https://proceedings.mlr.press/v235/woodruff24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/woodruff24b/woodruff24b.pdf"
categories: ['fast-sketching-methods-for-large-scale-optimization', 'matrix-geometry-optimization-for-spectral-learning']
tags: ['weighted-low-rank-approximation', 'reweighting', 'bicriteria', 'matrix-factorization']
venue: "ICML 2024"
tldr: "Proposes reweighted solution algorithms for weighted low rank approximation that improve computational tractability while maintaining approximation quality."
---

# Reweighted Solutions for Weighted Low Rank Approximation

**Source**: [https://proceedings.mlr.press/v235/woodruff24b.html](https://proceedings.mlr.press/v235/woodruff24b.html)

**TLDR**: Proposes reweighted solution algorithms for weighted low rank approximation that improve computational tractability while maintaining approximation quality.

## Abstract

Weighted low rank approximation (WLRA) is an important yet computationally challenging primitive with applications ranging from statistical analysis, model compression, and signal processing. To cope with the NP-hardness of this problem, prior work considers heuristics, bicriteria, or parameterized tractable algorithms to solve this problem. In this work, we introduce a new relaxed solution to WLRA which outputs a matrix that is not necessarily low rank, but can be stored using very few parameters and gives provable approximation guarantees when the weight matrix has low rank. Our central idea is to use the weight matrix itself to reweight a low rank solution, which gives an extremely simple algorithm with remarkable empirical performance in applications to model compression and on synthetic datasets. Our algorithm also gives nearly optimal communication complexity bounds for a natural distributed problem associated with this problem, for which we show matching communication lower bounds. Together, our communication complexity bounds show that the rank of the weight matrix provably parameterizes the communication complexity of WLRA. We also obtain the first relative error guarantees for feature selection with a weighted objective.