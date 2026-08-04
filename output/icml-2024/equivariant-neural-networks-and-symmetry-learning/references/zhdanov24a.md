---
title: "Clifford-Steerable Convolutional Neural Networks"
source: "https://proceedings.mlr.press/v235/zhdanov24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhdanov24a/zhdanov24a.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning']
tags: ['equivariant-CNNs', 'Clifford-algebra', 'pseudo-Euclidean-spaces', 'geometric-deep-learning']
venue: "ICML 2024"
tldr: "CS-CNNs are a novel class of E(p,q)-equivariant convolutional neural networks that process multivector fields on pseudo-Euclidean spaces using Clifford algebra."
---

# Clifford-Steerable Convolutional Neural Networks

**Source**: [https://proceedings.mlr.press/v235/zhdanov24a.html](https://proceedings.mlr.press/v235/zhdanov24a.html)

**TLDR**: CS-CNNs are a novel class of E(p,q)-equivariant convolutional neural networks that process multivector fields on pseudo-Euclidean spaces using Clifford algebra.

## Abstract

We present Clifford-Steerable Convolutional Neural Networks (CS-CNNs), a novel class of ${\operatorname{E}}(p, q)$-equivariant CNNs. CS-CNNs process multivector fields on pseudo-Euclidean spaces $\mathbb{R}^{p,q}$. They specialize, for instance, to ${\operatorname{E}}(3)$-equivariance on $\mathbb{R}^3$ and Poincaré-equivariance on Minkowski spacetime $\mathbb{R}^{1,3}$. Our approach is based on an implicit parametrization of ${\operatorname{O}}(p,q)$-steerable kernels via Clifford group equivariant neural networks. We significantly and consistently outperform baseline methods on fluid dynamics as well as relativistic electrodynamics forecasting tasks.