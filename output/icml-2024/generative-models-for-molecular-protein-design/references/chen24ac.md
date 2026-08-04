---
title: "GeoMFormer: A General Architecture for Geometric Molecular Representation Learning"
source: "https://proceedings.mlr.press/v235/chen24ac.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24ac/chen24ac.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'generative-models-for-molecular-protein-design']
tags: ['molecular-modeling', 'equivariance', 'invariance', 'geometric-representation']
venue: "ICML 2024"
tldr: "Introduces GeoMFormer, a general transformer architecture respecting geometric symmetries for accurate molecular property prediction."
---

# GeoMFormer: A General Architecture for Geometric Molecular Representation Learning

**Source**: [https://proceedings.mlr.press/v235/chen24ac.html](https://proceedings.mlr.press/v235/chen24ac.html)

**TLDR**: Introduces GeoMFormer, a general transformer architecture respecting geometric symmetries for accurate molecular property prediction.

## Abstract

Molecular modeling, a central topic in quantum mechanics, aims to accurately calculate the properties and simulate the behaviors of molecular systems. The molecular model is governed by physical laws, which impose geometric constraints such as invariance and equivariance to coordinate rotation and translation. While numerous deep learning approaches have been developed to learn molecular representations under these constraints, most of them are built upon heuristic and costly modules. We argue that there is a strong need for a general and flexible framework for learning both invariant and equivariant features. In this work, we introduce a novel Transformer-based molecular model called GeoMFormer to achieve this goal. Using the standard Transformer modules, two separate streams are developed to maintain and learn invariant and equivariant representations. Carefully designed cross-attention modules bridge the two streams, allowing information fusion and enhancing geometric modeling in each stream. As a general and flexible architecture, we show that many previous architectures can be viewed as special instantiations of GeoMFormer. Extensive experiments are conducted to demonstrate the power of GeoMFormer. All empirical results show that GeoMFormer achieves strong performance on both invariant and equivariant tasks of different types and scales. Code and models will be made publicly available at https://github.com/c-tl/GeoMFormer.