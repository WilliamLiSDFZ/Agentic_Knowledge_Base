---
title: "Inferring Dynamic Networks from Marginals with Iterative Proportional Fitting"
source: "https://proceedings.mlr.press/v235/chang24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chang24b/chang24b.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'graph-clustering-and-matching-algorithms']
tags: ['dynamic-networks', 'iterative-proportional-fitting', 'network-inference', 'marginal-constraints']
venue: "ICML 2024"
tldr: "Adapts iterative proportional fitting to infer dynamic networks from time-aggregated adjacency matrices and time-varying marginals."
---

# Inferring Dynamic Networks from Marginals with Iterative Proportional Fitting

**Source**: [https://proceedings.mlr.press/v235/chang24b.html](https://proceedings.mlr.press/v235/chang24b.html)

**TLDR**: Adapts iterative proportional fitting to infer dynamic networks from time-aggregated adjacency matrices and time-varying marginals.

## Abstract

A common network inference problem, arising from real-world data constraints, is how to infer a dynamic network from its time-aggregated adjacency matrix and time-varying marginals (i.e., row and column sums). Prior approaches to this problem have repurposed the classic iterative proportional fitting (IPF) procedure, also known as Sinkhorn’s algorithm, with promising empirical results. However, the statistical foundation for using IPF has not been well understood: under what settings does IPF provide principled estimation of a dynamic network from its marginals, and how well does it estimate the network? In this work, we establish such a setting, by identifying a generative network model whose maximum likelihood estimates are recovered by IPF. Our model both reveals implicit assumptions on the use of IPF in such settings and enables new analyses, such as structure-dependent error bounds on IPF’s parameter estimates. When IPF fails to converge on sparse network data, we introduce a principled algorithm that guarantees IPF converges under minimal changes to the network structure. Finally, we conduct experiments with synthetic and real-world data, which demonstrate the practical value of our theoretical and algorithmic contributions.