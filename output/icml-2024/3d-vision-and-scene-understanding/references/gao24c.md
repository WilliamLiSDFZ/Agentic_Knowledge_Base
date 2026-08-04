---
title: "An Intrinsic Vector Heat Network"
source: "https://proceedings.mlr.press/v235/gao24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gao24c/gao24c.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', '3d-vision-and-scene-understanding']
tags: ['vector-fields', 'manifold-learning', 'tangent-vectors', 'geometric-deep-learning']
venue: "ICML 2024"
tldr: "An intrinsic vector heat network learns tangent vector fields on manifold surfaces embedded in 3D using a novel geometric neural architecture."
---

# An Intrinsic Vector Heat Network

**Source**: [https://proceedings.mlr.press/v235/gao24c.html](https://proceedings.mlr.press/v235/gao24c.html)

**TLDR**: An intrinsic vector heat network learns tangent vector fields on manifold surfaces embedded in 3D using a novel geometric neural architecture.

## Abstract

Vector fields are widely used to represent and model flows for many science and engineering applications. This paper introduces a novel neural network architecture for learning tangent vector fields that are intrinsically defined on manifold surfaces embedded in 3D. Previous approaches to learning vector fields on surfaces treat vectors as multi-dimensional scalar fields, using traditional scalar-valued architectures to process channels individually, thus fail to preserve fundamental intrinsic properties of the vector field. The core idea of this work is to introduce a trainable vector heat diffusion module to spatially propagate vector-valued feature data across the surface, which we incorporate into our proposed architecture that consists of vector-valued neurons. Our architecture is invariant to rigid motion of the input, isometric deformation, and choice of local tangent bases, and is robust to discretizations of the surface. We evaluate our Vector Heat Network on triangle meshes, and empirically validate its invariant properties. We also demonstrate the effectiveness of our method on the useful industrial application of quadrilateral mesh generation.