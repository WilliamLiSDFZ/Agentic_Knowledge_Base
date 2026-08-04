---
title: "Synergistic Integration of Coordinate Network and Tensorial Feature for Improving Neural Radiance Fields from Sparse Inputs"
source: "https://proceedings.mlr.press/v235/kim24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24j/kim24j.pdf"
categories: ['3d-vision-and-scene-understanding', 'generative-models-and-variational-inference']
tags: ['neural-radiance-fields', 'multi-plane-representation', 'sparse-inputs']
venue: "ICML 2024"
tldr: "Combines coordinate networks with tensorial features to improve NeRF performance under sparse input conditions."
---

# Synergistic Integration of Coordinate Network and Tensorial Feature for Improving Neural Radiance Fields from Sparse Inputs

**Source**: [https://proceedings.mlr.press/v235/kim24j.html](https://proceedings.mlr.press/v235/kim24j.html)

**TLDR**: Combines coordinate networks with tensorial features to improve NeRF performance under sparse input conditions.

## Abstract

The multi-plane representation has been highlighted for its fast training and inference across static and dynamic neural radiance fields. This approach constructs relevant features via projection onto learnable grids and interpolating adjacent vertices. However, it has limitations in capturing low-frequency details and tends to overuse parameters for low-frequency features due to its bias toward fine details, despite its multi-resolution concept. This phenomenon leads to instability and inefficiency when training poses are sparse. In this work, we propose a method that synergistically integrates multi-plane representation with a coordinate-based MLP network known for strong bias toward low-frequency signals. The coordinate-based network is responsible for capturing low-frequency details, while the multi-plane representation focuses on capturing fine-grained details. We demonstrate that using residual connections between them seamlessly preserves their own inherent properties. Additionally, the proposed progressive training scheme accelerates the disentanglement of these two features. We demonstrate empirically that our proposed method not only outperforms baseline models for both static and dynamic NeRFs with sparse inputs, but also achieves comparable results with fewer parameters.