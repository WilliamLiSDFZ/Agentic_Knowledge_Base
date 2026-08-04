---
title: "Positional Knowledge is All You Need: Position-induced Transformer (PiT) for Operator Learning"
source: "https://proceedings.mlr.press/v235/chen24au.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24au/chen24au.pdf"
categories: ['neural-operators-for-pde-solving', 'transformer-architecture-efficiency-and-scaling']
tags: ['operator-learning', 'transformers', 'PDEs', 'positional-encoding']
venue: "ICML 2024"
tldr: "Introduces Position-induced Transformer (PiT), showing that positional knowledge alone suffices for effective neural operator learning on PDEs."
---

# Positional Knowledge is All You Need: Position-induced Transformer (PiT) for Operator Learning

**Source**: [https://proceedings.mlr.press/v235/chen24au.html](https://proceedings.mlr.press/v235/chen24au.html)

**TLDR**: Introduces Position-induced Transformer (PiT), showing that positional knowledge alone suffices for effective neural operator learning on PDEs.

## Abstract

Operator learning for Partial Differential Equations (PDEs) is rapidly emerging as a promising approach for surrogate modeling of intricate systems. Transformers with the self-attention mechanism—a powerful tool originally designed for natural language processing—have recently been adapted for operator learning. However, they confront challenges, including high computational demands and limited interpretability. This raises a critical question: Is there a more efficient attention mechanism for Transformer-based operator learning? This paper proposes the Position-induced Transformer (PiT), built on an innovative position-attention mechanism, which demonstrates significant advantages over the classical self-attention in operator learning. Position-attention draws inspiration from numerical methods for PDEs. Different from self-attention, position-attention is induced by only the spatial interrelations of sampling positions for input functions of the operators, and does not rely on the input function values themselves, thereby greatly boosting efficiency. PiT exhibits superior performance over current state-of-the-art neural operators in a variety of complex operator learning tasks across diverse PDE benchmarks. Additionally, PiT possesses an enhanced discretization convergence feature, compared to the widely-used Fourier neural operator.