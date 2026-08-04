---
title: "Generalizing Knowledge Graph Embedding with Universal Orthogonal Parameterization"
source: "https://proceedings.mlr.press/v235/li24ah.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24ah/li24ah.pdf"
categories: ['graph-neural-networks-and-topology', 'algebraic-structures-in-machine-learning']
tags: ['knowledge-graph-embedding', 'orthogonal-parameterization', 'relational-learning', 'hyperbolic']
venue: "ICML 2024"
tldr: "Universal orthogonal parameterization generalizes knowledge graph embeddings beyond rigid relational orthogonalization across Euclidean and hyperbolic spaces."
---

# Generalizing Knowledge Graph Embedding with Universal Orthogonal Parameterization

**Source**: [https://proceedings.mlr.press/v235/li24ah.html](https://proceedings.mlr.press/v235/li24ah.html)

**TLDR**: Universal orthogonal parameterization generalizes knowledge graph embeddings beyond rigid relational orthogonalization across Euclidean and hyperbolic spaces.

## Abstract

Recent advances in knowledge graph embedding (KGE) rely on Euclidean/hyperbolic orthogonal relation transformations to model intrinsic logical patterns and topological structures. However, existing approaches are confined to rigid relational orthogonalization with restricted dimension and homogeneous geometry, leading to deficient modeling capability. In this work, we move beyond these approaches in terms of both dimension and geometry by introducing a powerful framework named GoldE, which features a universal orthogonal parameterization based on a generalized form of Householder reflection. Such parameterization can naturally achieve dimensional extension and geometric unification with theoretical guarantees, enabling our framework to simultaneously capture crucial logical patterns and inherent topological heterogeneity of knowledge graphs. Empirically, GoldE achieves state-of-the-art performance on three standard benchmarks. Codes are available at https://github.com/xxrep/GoldE.