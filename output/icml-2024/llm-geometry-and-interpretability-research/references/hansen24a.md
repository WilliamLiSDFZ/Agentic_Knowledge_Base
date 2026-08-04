---
title: "Interpreting Equivariant Representations"
source: "https://proceedings.mlr.press/v235/hansen24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hansen24a/hansen24a.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'llm-geometry-and-interpretability-research']
tags: ['equivariant-networks', 'latent-representations', 'interpretability']
venue: "ICML 2024"
tldr: "This paper demonstrates that inductive biases from equivariant models must be considered when interpreting latent representations to avoid misleading conclusions."
---

# Interpreting Equivariant Representations

**Source**: [https://proceedings.mlr.press/v235/hansen24a.html](https://proceedings.mlr.press/v235/hansen24a.html)

**TLDR**: This paper demonstrates that inductive biases from equivariant models must be considered when interpreting latent representations to avoid misleading conclusions.

## Abstract

Latent representations are extensively used for tasks like visualization, interpolation, or feature extraction in deep learning models. This paper demonstrates the importance of considering the inductive bias imposed by an equivariant model when using latent representations as neglecting these biases can lead to decreased performance in downstream tasks. We propose principles for choosing invariant projections of latent representations and show their effectiveness in two examples: A permutation equivariant variational auto-encoder for molecular graph generation, where an invariant projection can be designed to maintain information without loss, and for a rotation-equivariant representation in image classification, where random invariant projections proves to retain a high degree of information. In both cases, the analysis of invariant latent representations proves superior to their equivariant counterparts. Finally, we illustrate that the phenomena documented here for equivariant neural networks have counterparts in standard neural networks where invariance is encouraged via augmentation.