---
title: "Understanding MLP-Mixer as a wide and sparse MLP"
source: "https://proceedings.mlr.press/v235/hayase24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hayase24a/hayase24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'transformer-architecture-efficiency-and-scaling']
tags: ['mlp-mixer', 'sparse-networks', 'theoretical-analysis']
venue: "ICML 2024"
tldr: "MLP-Mixer is theoretically analyzed and shown to be equivalent to a wide and sparse MLP, explaining its empirical success over conventional MLPs."
---

# Understanding MLP-Mixer as a wide and sparse MLP

**Source**: [https://proceedings.mlr.press/v235/hayase24a.html](https://proceedings.mlr.press/v235/hayase24a.html)

**TLDR**: MLP-Mixer is theoretically analyzed and shown to be equivalent to a wide and sparse MLP, explaining its empirical success over conventional MLPs.

## Abstract

Multi-layer perceptron (MLP) is a fundamental component of deep learning, and recent MLP-based architectures, especially the MLP-Mixer, have achieved significant empirical success. Nevertheless, our understanding of why and how the MLP-Mixer outperforms conventional MLPs remains largely unexplored. In this work, we reveal that sparseness is a key mechanism underlying the MLP-Mixers. First, the Mixers have an effective expression as a wider MLP with Kronecker-product weights, clarifying that the Mixers efficiently embody several sparseness properties explored in deep learning. In the case of linear layers, the effective expression elucidates an implicit sparse regularization caused by the model architecture and a hidden relation to Monarch matrices, which is also known as another form of sparse parameterization. Next, for general cases, we empirically demonstrate quantitative similarities between the Mixer and the unstructured sparse-weight MLPs. Following a guiding principle proposed by Golubeva, Neyshabur and Gur-Ari (2021), which fixes the number of connections and increases the width and sparsity, the Mixers can demonstrate improved performance.