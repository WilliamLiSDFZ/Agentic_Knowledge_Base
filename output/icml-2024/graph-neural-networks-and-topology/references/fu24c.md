---
title: "Hyperbolic Geometric Latent Diffusion Model for Graph Generation"
source: "https://proceedings.mlr.press/v235/fu24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fu24c/fu24c.pdf"
categories: ['generative-models-and-variational-inference', 'graph-neural-networks-and-topology']
tags: ['hyperbolic-geometry', 'graph-generation', 'diffusion-models']
venue: "ICML 2024"
tldr: "A hyperbolic latent diffusion model for graph generation improves computational efficiency and training stability over discrete graph diffusion methods."
---

# Hyperbolic Geometric Latent Diffusion Model for Graph Generation

**Source**: [https://proceedings.mlr.press/v235/fu24c.html](https://proceedings.mlr.press/v235/fu24c.html)

**TLDR**: A hyperbolic latent diffusion model for graph generation improves computational efficiency and training stability over discrete graph diffusion methods.

## Abstract

Diffusion models have made significant contributions to computer vision, sparking a growing interest in the community recently regarding the application of it to graph generation. The existing discrete graph diffusion models exhibit heightened computational complexity and diminished training efficiency. A preferable and natural way is to directly diffuse the graph within the latent space. However, due to the non-Euclidean structure of graphs is not isotropic in the latent space, the existing latent diffusion models effectively make it difficult to capture and preserve the topological information of graphs. To address the above challenges, we propose a novel geometrically latent diffusion framework HypDiff. Specifically, we first establish a geometrically latent space with interpretability measures based on hyperbolic geometry, to define anisotropic latent diffusion processes for graphs. Then, we propose a geometrically latent diffusion process that is constrained by both radial and angular geometric properties, thereby ensuring the preservation of the original topological properties in the generative graphs. Extensive experimental results demonstrate the superior effectiveness of HypDiff for graph generation with various topologies.