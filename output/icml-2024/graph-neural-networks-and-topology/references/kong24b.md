---
title: "Generalist Equivariant Transformer Towards 3D Molecular Interaction Learning"
source: "https://proceedings.mlr.press/v235/kong24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kong24b/kong24b.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'graph-neural-networks-and-topology']
tags: ['equivariant-transformer', '3D-molecular-interactions', 'protein-protein', 'drug-discovery', 'multi-granularity']
venue: "ICML 2024"
tldr: "A generalist equivariant transformer that jointly learns 3D molecular interactions across different types and granularities of molecules."
---

# Generalist Equivariant Transformer Towards 3D Molecular Interaction Learning

**Source**: [https://proceedings.mlr.press/v235/kong24b.html](https://proceedings.mlr.press/v235/kong24b.html)

**TLDR**: A generalist equivariant transformer that jointly learns 3D molecular interactions across different types and granularities of molecules.

## Abstract

Many processes in biology and drug discovery involve various 3D interactions between molecules, such as protein and protein, protein and small molecule, etc. Given that different molecules are usually represented in different granularity, existing methods usually encode each type of molecules independently with different models, leaving it defective to learn the various underlying interaction physics. In this paper, we first propose to universally represent an arbitrary 3D complex as a geometric graph of sets, shedding light on encoding all types of molecules with one model. We then propose a Generalist Equivariant Transformer (GET) to effectively capture both domain-specific hierarchies and domain-agnostic interaction physics. To be specific, GET consists of a bilevel attention module, a feed-forward module and a layer normalization module, where each module is E(3) equivariant and specialized for handling sets of variable sizes. Notably, in contrast to conventional pooling-based hierarchical models, our GET is able to retain fine-grained information of all levels. Extensive experiments on the interactions between proteins, small molecules and RNA/DNAs verify the effectiveness and generalization capability of our proposed method across different domains.