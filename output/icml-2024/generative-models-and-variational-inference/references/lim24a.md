---
title: "Graph Geometry-Preserving Autoencoders"
source: "https://proceedings.mlr.press/v235/lim24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lim24a/lim24a.pdf"
categories: ['graph-neural-networks-and-topology', 'generative-models-and-variational-inference']
tags: ['graph-autoencoder', 'manifold-learning', 'geometry-preservation']
venue: "ICML 2024"
tldr: "An autoencoder framework that preserves the geometry of data manifolds by accounting for non-Euclidean structure in high-dimensional graph data."
---

# Graph Geometry-Preserving Autoencoders

**Source**: [https://proceedings.mlr.press/v235/lim24a.html](https://proceedings.mlr.press/v235/lim24a.html)

**TLDR**: An autoencoder framework that preserves the geometry of data manifolds by accounting for non-Euclidean structure in high-dimensional graph data.

## Abstract

When using an autoencoder to learn the low-dimensional manifold of high-dimensional data, it is crucial to find the latent representations that preserve the geometry of the data manifold. However, most existing studies assume a Euclidean nature for the high-dimensional data space, which is arbitrary and often does not precisely reflect the underlying semantic or domain-specific attributes of the data. In this paper, we propose a novel autoencoder regularization framework based on the premise that the geometry of the data manifold can often be better captured with a well-designed similarity graph associated with data points. Given such a graph, we utilize a Riemannian geometric distortion measure as a regularizer to preserve the geometry derived from the graph Laplacian and make it suitable for larger-scale autoencoder training. Through extensive experiments, we show that our method outperforms existing state-of-the-art geometry-preserving and graph-based autoencoders with respect to learning accurate latent structures that preserve the graph geometry, and is particularly effective in learning dynamics in the latent space. Code is available at https://github.com/JungbinLim/GGAE-public.