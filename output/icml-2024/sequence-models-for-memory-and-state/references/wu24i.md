---
title: "Uniform Memory Retrieval with Larger Capacity for Modern Hopfield Models"
source: "https://proceedings.mlr.press/v235/wu24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24i/wu24i.pdf"
categories: ['neural-network-learning-dynamics-theory', 'sequence-models-for-memory-and-state']
tags: ['hopfield-networks', 'memory-retrieval', 'kernel-methods', 'energy-functions', 'feature-maps']
venue: "ICML 2024"
tldr: "Proposes U-Hop, a two-stage optimization formulation with learnable feature maps for modern Hopfield models that transforms energy functions into kernel space for improved memory retrieval capacity."
---

# Uniform Memory Retrieval with Larger Capacity for Modern Hopfield Models

**Source**: [https://proceedings.mlr.press/v235/wu24i.html](https://proceedings.mlr.press/v235/wu24i.html)

**TLDR**: Proposes U-Hop, a two-stage optimization formulation with learnable feature maps for modern Hopfield models that transforms energy functions into kernel space for improved memory retrieval capacity.

## Abstract

We propose a two-stage optimization formulation for the memory retrieval dynamics of modern Hopfield models, termed $\mathtt{U\text{-}Hop}$. Our key contribution is a learnable feature map $\Phi$ which transforms the Hopfield energy function into a kernel space. This transformation ensures convergence between the local minima of energy and the fixed points of retrieval dynamics within the kernel space. Consequently, the kernel norm induced by $\Phi$ serves as a novel similarity measure. It utilizes the stored memory patterns as learning data to enhance memory capacity across all modern Hopfield models. Specifically, we accomplish this by constructing a separation loss $\mathcal{L}_\Phi$ that separates the local minima of kernelized energy by separating stored memory patterns in kernel space. Methodologically, $\mathtt{U\text{-}Hop}$ memory retrieval process consists of: (Stage I:) minimizing separation loss for a more uniformed memory (local minimum) distribution, followed by (Stage II:) standard Hopfield energy minimization for memory retrieval. This results in significant reduction of possible meta-stable states in the Hopfield energy function, thus preventing memory confusion. Empirically, with real-world datasets, we demonstrate that $\mathtt{U\text{-}Hop}$ outperforms all existing modern Hopfield models and SOTA similarity measures, achieving a substantial margin in both associative memory retrieval and deep learning tasks. Code is available at GitHub; future updates are on arXiv.