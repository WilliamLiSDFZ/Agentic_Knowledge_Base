---
title: "Wasserstein Wormhole: Scalable Optimal Transport Distance with Transformer"
source: "https://proceedings.mlr.press/v235/haviv24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/haviv24a/haviv24a.pdf"
categories: ['generative-models-and-variational-inference', 'transformer-architecture-efficiency-and-scaling']
tags: ['optimal-transport', 'wasserstein-distance', 'transformer-embedding']
venue: "ICML 2024"
tldr: "Wasserstein Wormhole uses a Transformer to learn an embedding space that approximates pairwise Wasserstein distances scalably."
---

# Wasserstein Wormhole: Scalable Optimal Transport Distance with Transformer

**Source**: [https://proceedings.mlr.press/v235/haviv24a.html](https://proceedings.mlr.press/v235/haviv24a.html)

**TLDR**: Wasserstein Wormhole uses a Transformer to learn an embedding space that approximates pairwise Wasserstein distances scalably.

## Abstract

Optimal transport (OT) and the related Wasserstein metric ($W$) are powerful and ubiquitous tools for comparing distributions. However, computing pairwise Wasserstein distances rapidly becomes intractable as cohort size grows. An attractive alternative would be to find an embedding space in which pairwise Euclidean distances map to OT distances, akin to standard multidimensional scaling (MDS). We present Wasserstein Wormhole, a transformer-based autoencoder that embeds empirical distributions into a latent space wherein Euclidean distances approximate OT distances. Extending MDS theory, we show that our objective function implies a bound on the error incurred when embedding non-Euclidean distances. Empirically, distances between Wormhole embeddings closely match Wasserstein distances, enabling linear time computation of OT distances. Along with an encoder that maps distributions to embeddings, Wasserstein Wormhole includes a decoder that maps embeddings back to distributions, allowing for operations in the embedding space to generalize to OT spaces, such as Wasserstein barycenter estimation and OT interpolation. By lending scalability and interpretability to OT approaches, Wasserstein Wormhole unlocks new avenues for data analysis in the fields of computational geometry and single-cell biology.