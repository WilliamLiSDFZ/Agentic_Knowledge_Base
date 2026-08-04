---
title: "On the Expressive Power of Spectral Invariant Graph Neural Networks"
source: "https://proceedings.mlr.press/v235/zhang24ck.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ck/zhang24ck.pdf"
categories: ['graph-neural-networks-and-topology', 'algebraic-structures-in-machine-learning']
tags: ['spectral-GNNs', 'eigenvector-ambiguity', 'expressive-power']
venue: "ICML 2024"
tldr: "Analyzes the expressive power of spectral invariant graph neural network architectures that handle eigenvector ambiguity."
---

# On the Expressive Power of Spectral Invariant Graph Neural Networks

**Source**: [https://proceedings.mlr.press/v235/zhang24ck.html](https://proceedings.mlr.press/v235/zhang24ck.html)

**TLDR**: Analyzes the expressive power of spectral invariant graph neural network architectures that handle eigenvector ambiguity.

## Abstract

Incorporating spectral information to enhance Graph Neural Networks (GNNs) has shown promising results but raises a fundamental challenge due to the inherent ambiguity of eigenvectors. Various architectures have been proposed to address this ambiguity, referred to as spectral invariant architectures. Notable examples include GNNs and Graph Transformers that use spectral distances, spectral projection matrices, or other invariant spectral features. However, the potential expressive power of these spectral invariant architectures remains largely unclear. The goal of this work is to gain a deep theoretical understanding of the expressive power obtainable when using spectral features. We first introduce a novel message-passing framework for designing spectral invariant GNNs, called Eigenspace Projection GNN (EPNN). Our comprehensive analysis shows that EPNN essentially unifies all prior spectral invariant architectures, in that they are either strictly less expressive or equivalent to EPNN. A fine-grained expressiveness hierarchy among different architectures is also established. On the other hand, we present a surprising result that EPNN itself is bounded by a recently proposed class of Subgraph GNNs, implying that all these spectral invariant architectures are strictly less expressive than 3-WL. Finally, we demonstrate that these spectral features offer no additional advantage when combined with more expressive GNNs.