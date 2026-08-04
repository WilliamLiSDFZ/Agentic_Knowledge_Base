---
title: "A Tensor Decomposition Perspective on Second-order RNNs"
source: "https://proceedings.mlr.press/v235/lizaire24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lizaire24a/lizaire24a.pdf"
categories: ['sequence-models-for-memory-and-state', 'algebraic-structures-in-machine-learning']
tags: ['second-order-RNN', 'tensor-decomposition', 'sequence-modeling', 'formal-language-theory']
venue: "ICML 2024"
tldr: "Analyzes second-order RNNs through tensor decomposition to address their parameter inefficiency while preserving expressive power."
---

# A Tensor Decomposition Perspective on Second-order RNNs

**Source**: [https://proceedings.mlr.press/v235/lizaire24a.html](https://proceedings.mlr.press/v235/lizaire24a.html)

**TLDR**: Analyzes second-order RNNs through tensor decomposition to address their parameter inefficiency while preserving expressive power.

## Abstract

Second-order Recurrent Neural Networks (2RNNs) extend RNNs by leveraging second-order interactions for sequence modelling. These models are provably more expressive than their first-order counterparts and have connections to well-studied models from formal language theory. However, their large parameter tensor makes computations intractable. To circumvent this issue, one approach known as MIRNN consists in limiting the type of interactions used by the model. Another is to leverage tensor decomposition to diminish the parameter count. In this work, we study the model resulting from parameterizing 2RNNs using the CP decomposition, which we call CPRNN. Intuitively, the rank of the decomposition should reduce expressivity. We analyze how rank and hidden size affect model capacity and show the relationships between RNNs, 2RNNs, MIRNNs, and CPRNNs based on these parameters. We support these results empirically with experiments on the Penn Treebank dataset which demonstrate that, with a fixed parameter budget, CPRNNs outperforms RNNs, 2RNNs, and MIRNNs with the right choice of rank and hidden size.