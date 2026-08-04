---
title: "Universality of Linear Recurrences Followed by Non-linear Projections: Finite-Width Guarantees and Benefits of Complex Eigenvalues"
source: "https://proceedings.mlr.press/v235/orvieto24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/orvieto24a/orvieto24a.pdf"
categories: ['sequence-models-for-memory-and-state']
tags: ['linear-RNNs', 'state-space-models', 'sequence-modeling', 'universality', 'complex-eigenvalues']
venue: "ICML 2024"
tldr: "Provides finite-width universality guarantees for linear recurrence plus nonlinear projection architectures and analyzes benefits of complex eigenvalues."
---

# Universality of Linear Recurrences Followed by Non-linear Projections: Finite-Width Guarantees and Benefits of Complex Eigenvalues

**Source**: [https://proceedings.mlr.press/v235/orvieto24a.html](https://proceedings.mlr.press/v235/orvieto24a.html)

**TLDR**: Provides finite-width universality guarantees for linear recurrence plus nonlinear projection architectures and analyzes benefits of complex eigenvalues.

## Abstract

Deep neural networks based on linear RNNs interleaved with position-wise MLPs are gaining traction as competitive approaches for sequence modeling. Examples of such architectures include state-space models (SSMs) like S4, LRU, and Mamba: recently proposed models that achieve promising performance on text, genetics, and other data that require long-range reasoning. Despite experimental evidence highlighting these architectures’ effectiveness and computational efficiency, their expressive power remains relatively unexplored, especially in connection to specific choices crucial in practice - e.g., carefully designed initialization distribution and potential use of complex numbers. In this paper, we show that combining MLPs with both real or complex linear diagonal recurrences leads to arbitrarily precise approximation of regular causal sequence-to-sequence maps. At the heart of our proof, we rely on a separation of concerns: the linear RNN provides a lossless encoding of the input sequence, and the MLP performs non-linear processing on this encoding. While we show that real diagonal linear recurrences are enough to achieve universality in this architecture, we prove that employing complex eigenvalues near unit disk - i.e., empirically the most successful strategy in S4 - greatly helps the RNN in storing information. We connect this finding with the vanishing gradient issue and provide experiments supporting our claims.