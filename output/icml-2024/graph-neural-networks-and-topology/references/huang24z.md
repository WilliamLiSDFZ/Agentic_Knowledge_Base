---
title: "How Universal Polynomial Bases Enhance Spectral Graph Neural Networks: Heterophily, Over-smoothing, and Over-squashing"
source: "https://proceedings.mlr.press/v235/huang24z.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24z/huang24z.pdf"
categories: ['graph-neural-networks-and-topology', 'matrix-geometry-optimization-for-spectral-learning']
tags: ['spectral-gnn', 'polynomial-filters', 'heterophily', 'over-smoothing', 'over-squashing']
venue: "ICML 2024"
tldr: "Proposes universal polynomial bases for spectral GNNs that simultaneously address heterophily, over-smoothing, and over-squashing."
---

# How Universal Polynomial Bases Enhance Spectral Graph Neural Networks: Heterophily, Over-smoothing, and Over-squashing

**Source**: [https://proceedings.mlr.press/v235/huang24z.html](https://proceedings.mlr.press/v235/huang24z.html)

**TLDR**: Proposes universal polynomial bases for spectral GNNs that simultaneously address heterophily, over-smoothing, and over-squashing.

## Abstract

Spectral Graph Neural Networks (GNNs), alternatively known as graph filters, have gained increasing prevalence for heterophily graphs. Optimal graph filters rely on Laplacian eigendecomposition for Fourier transform. In an attempt to avert prohibitive computations, numerous polynomial filters have been proposed. However, polynomials in the majority of these filters are predefined and remain fixed across different graphs, failing to accommodate the varying degrees of heterophily. Addressing this gap, we demystify the intrinsic correlation between the spectral property of desired polynomial bases and the heterophily degrees via thorough theoretical analyses. Subsequently, we develop a novel adaptive heterophily basis wherein the basis vectors mutually form angles reflecting the heterophily degree of the graph. We integrate this heterophily basis with the homophily basis to construct a universal polynomial basis UniBasis, which devises a polynomial filter based graph neural network – UniFilter. It optimizes the convolution and propagation in GNN, thus effectively limiting over-smoothing and alleviating over-squashing. Our extensive experiments, conducted on datasets with a diverse range of heterophily, support the superiority of UniBasis in the universality but also its proficiency in graph explanation.