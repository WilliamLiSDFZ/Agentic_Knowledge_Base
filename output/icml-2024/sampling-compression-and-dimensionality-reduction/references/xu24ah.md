---
title: "Exponential Spectral Pursuit: An Effective Initialization Method for Sparse Phase Retrieval"
source: "https://proceedings.mlr.press/v235/xu24ah.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24ah/xu24ah.pdf"
categories: ['sparse-phase-retrieval-with-priors', 'sampling-compression-and-dimensionality-reduction']
tags: ['sparse-phase-retrieval', 'spectral-methods', 'initialization']
venue: "ICML 2024"
tldr: "Proposes Exponential Spectral Pursuit as an efficient initialization method that reduces sampling complexity for sparse phase retrieval algorithms."
---

# Exponential Spectral Pursuit: An Effective Initialization Method for Sparse Phase Retrieval

**Source**: [https://proceedings.mlr.press/v235/xu24ah.html](https://proceedings.mlr.press/v235/xu24ah.html)

**TLDR**: Proposes Exponential Spectral Pursuit as an efficient initialization method that reduces sampling complexity for sparse phase retrieval algorithms.

## Abstract

Sparse phase retrieval aims to reconstruct an $n$-dimensional $k$-sparse signal from its phaseless measurements. For most of the existing reconstruction algorithms, their sampling complexity is known to be dominated by the initialization stage. In this paper, in order to improve the sampling complexity for initialization, we propose a novel method termed exponential spectral pursuit (ESP). Theoretically, our method offers a tighter bound of sampling complexity compared to the state-of-the-art ones, such as the truncated power method. Moreover, it empirically outperforms the existing initialization methods for sparse phase retrieval.