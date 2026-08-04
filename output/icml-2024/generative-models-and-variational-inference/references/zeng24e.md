---
title: "Graph Mixup on Approximate Gromov–Wasserstein Geodesics"
source: "https://proceedings.mlr.press/v235/zeng24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zeng24e/zeng24e.pdf"
categories: ['graph-neural-networks-and-topology', 'generative-models-and-variational-inference']
tags: ['graph-mixup', 'Gromov-Wasserstein', 'data-augmentation']
venue: "ICML 2024"
tldr: "A graph mixup method that interpolates along approximate Gromov-Wasserstein geodesics to generate meaningful synthetic graph training samples."
---

# Graph Mixup on Approximate Gromov–Wasserstein Geodesics

**Source**: [https://proceedings.mlr.press/v235/zeng24e.html](https://proceedings.mlr.press/v235/zeng24e.html)

**TLDR**: A graph mixup method that interpolates along approximate Gromov-Wasserstein geodesics to generate meaningful synthetic graph training samples.

## Abstract

Mixup, which generates synthetic training samples on the data manifold, has been shown to be highly effective in augmenting Euclidean data. However, finding a proper data manifold for graph data is non-trivial, as graphs are non-Euclidean data in disparate spaces. Though efforts have been made, most of the existing graph mixup methods neglect the intrinsic geodesic guarantee, thereby generating inconsistent sample-label pairs. To address this issue, we propose GeoMix to mixup graphs on the Gromov-Wasserstein (GW) geodesics. A joint space over input graphs is first defined based on the GW distance, and graphs are then transformed into the GW space through equivalence-preserving transformations. We further show that the linear interpolation of the transformed graph pairs defines a geodesic connecting the original pairs on the GW manifold, hence ensuring the consistency between generated samples and labels. An accelerated mixup algorithm on the approximate low-dimensional GW manifold is further proposed. Extensive experiments show that the proposed GeoMix promotes the generalization and robustness of GNN models.