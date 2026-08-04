---
title: "Neural Tangent Kernels Motivate Cross-Covariance Graphs in Neural Networks"
source: "https://proceedings.mlr.press/v235/khalafi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/khalafi24a/khalafi24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'sufficient-dimension-reduction-correlation-methods']
tags: ['neural-tangent-kernels', 'cross-covariance-graphs', 'alignment']
venue: "ICML 2024"
tldr: "Shows that neural tangent kernel alignment motivates the use of cross-covariance graphs to understand learning and generalization in neural networks."
---

# Neural Tangent Kernels Motivate Cross-Covariance Graphs in Neural Networks

**Source**: [https://proceedings.mlr.press/v235/khalafi24a.html](https://proceedings.mlr.press/v235/khalafi24a.html)

**TLDR**: Shows that neural tangent kernel alignment motivates the use of cross-covariance graphs to understand learning and generalization in neural networks.

## Abstract

Neural tangent kernels (NTKs) provide a theoretical regime to analyze the learning and generalization behavior of over-parametrized neural networks. For a supervised learning task, the association between the eigenvectors of the NTK and given data (a concept referred to as alignment in this paper) can govern the rate of convergence of gradient descent, as well as generalization to unseen data. Building upon this concept and leveraging the structure of NTKs for graph neural networks (GNNs), we theoretically investigate NTKs and alignment, where our analysis reveals that optimizing the alignment translates to optimizing the graph representation or the graph shift operator (GSO) in a GNN. Our results further establish theoretical guarantees on the optimality of the alignment for a two-layer GNN and these guarantees are characterized by the graph shift operator being a function of the cross-covariance between the input and the output data. The theoretical insights drawn from the analysis of NTKs are validated by our experiments focused on a multi-variate time series prediction task for a publicly available dataset. Specifically, they demonstrate that GNN-based learning models that operate on the cross-covariance matrix indeed outperform those that operate on the covariance matrix estimated from only the input data.