---
title: "Lie Neurons: Adjoint-Equivariant Neural Networks for Semisimple Lie Algebras"
source: "https://proceedings.mlr.press/v235/lin24aa.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24aa/lin24aa.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'algebraic-structures-in-machine-learning']
tags: ['Lie-algebra', 'equivariant-networks', 'adjoint-representation']
venue: "ICML 2024"
tldr: "Lie Neurons is an adjoint-equivariant neural network framework for data lying in semisimple Lie algebras."
---

# Lie Neurons: Adjoint-Equivariant Neural Networks for Semisimple Lie Algebras

**Source**: [https://proceedings.mlr.press/v235/lin24aa.html](https://proceedings.mlr.press/v235/lin24aa.html)

**TLDR**: Lie Neurons is an adjoint-equivariant neural network framework for data lying in semisimple Lie algebras.

## Abstract

This paper proposes an equivariant neural network that takes data in any finite-dimensional semi-simple Lie algebra as input. The corresponding group acts on the Lie algebra as adjoint operations, making our proposed network adjoint-equivariant. Our framework generalizes the Vector Neurons, a simple $\mathrm{SO}(3)$-equivariant network, from 3-D Euclidean space to Lie algebra spaces, building upon the invariance property of the Killing form. Furthermore, we propose novel Lie bracket layers and geometric channel mixing layers that extend the modeling capacity. Experiments are conducted for the $\mathfrak{so}(3)$, $\mathfrak{sl}(3)$, and $\mathfrak{sp}(4)$ Lie algebras on various tasks, including fitting equivariant and invariant functions, learning system dynamics, point cloud registration, and homography-based shape classification. Our proposed equivariant network shows wide applicability and competitive performance in various domains.