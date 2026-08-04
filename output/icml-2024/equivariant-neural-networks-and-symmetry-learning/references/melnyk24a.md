---
title: "O$n$ Learning Deep O($n$)-Equivariant Hyperspheres"
source: "https://proceedings.mlr.press/v235/melnyk24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/melnyk24a/melnyk24a.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning']
tags: ['O(n)-equivariance', 'hyperspheres', 'deep-features']
venue: "ICML 2024"
tldr: "Proposes O(n)-equivariant neurons using hyperspheres and regular simplexes for learning rotation- and reflection-equivariant deep features."
---

# O$n$ Learning Deep O($n$)-Equivariant Hyperspheres

**Source**: [https://proceedings.mlr.press/v235/melnyk24a.html](https://proceedings.mlr.press/v235/melnyk24a.html)

**TLDR**: Proposes O(n)-equivariant neurons using hyperspheres and regular simplexes for learning rotation- and reflection-equivariant deep features.

## Abstract

In this paper, we utilize hyperspheres and regular $n$-simplexes and propose an approach to learning deep features equivariant under the transformations of $n$D reflections and rotations, encompassed by the powerful group of O$(n)$. Namely, we propose O$(n)$-equivariant neurons with spherical decision surfaces that generalize to any dimension $n$, which we call Deep Equivariant Hyperspheres. We demonstrate how to combine them in a network that directly operates on the basis of the input points and propose an invariant operator based on the relation between two points and a sphere, which as we show, turns out to be a Gram matrix. Using synthetic and real-world data in $n$D, we experimentally verify our theoretical contributions and find that our approach is superior to the competing methods for O$(n)$-equivariant benchmark datasets (classification and regression), demonstrating a favorable speed/performance trade-off. The code is available on GitHub.