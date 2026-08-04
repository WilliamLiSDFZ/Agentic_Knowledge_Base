---
title: "Sparse and Structured Hopfield Networks"
source: "https://proceedings.mlr.press/v235/santos24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/santos24a/santos24a.pdf"
categories: ['neural-operators-for-pde-solving', 'transformer-architecture-efficiency-and-scaling']
tags: ['Hopfield-networks', 'sparse-attention', 'Fenchel-Young-losses', 'transformers', 'energy-based-models']
venue: "ICML 2024"
tldr: "A unified framework for sparse Hopfield networks is established via Fenchel-Young losses, yielding a new family of Hopfield energies with sparse and structured updates."
---

# Sparse and Structured Hopfield Networks

**Source**: [https://proceedings.mlr.press/v235/santos24a.html](https://proceedings.mlr.press/v235/santos24a.html)

**TLDR**: A unified framework for sparse Hopfield networks is established via Fenchel-Young losses, yielding a new family of Hopfield energies with sparse and structured updates.

## Abstract

Modern Hopfield networks have enjoyed recent interest due to their connection to attention in transformers. Our paper provides a unified framework for sparse Hopfield networks by establishing a link with Fenchel-Young losses. The result is a new family of Hopfield-Fenchel-Young energies whose update rules are end-to-end differentiable sparse transformations. We reveal a connection between loss margins, sparsity, and exact memory retrieval. We further extend this framework to structured Hopfield networks via the SparseMAP transformation, which can retrieve pattern associations instead of a single pattern. Experiments on multiple instance learning and text rationalization demonstrate the usefulness of our approach.