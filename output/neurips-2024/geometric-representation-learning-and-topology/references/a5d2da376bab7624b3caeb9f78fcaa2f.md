---
title: "Learning Structured Representations with Hyperbolic Embeddings"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a5d2da376bab7624b3caeb9f78fcaa2f-Abstract-Conference.html"
categories: ['graph-neural-networks-and-representation-learning', 'geometric-representation-learning-and-topology']
tags: ['hyperbolic-embeddings', 'hierarchical-representation', 'label-structure']
venue: "NeurIPS 2024"
tldr: "Proposes structured representation learning using hyperbolic embeddings to incorporate natural label hierarchies present in real-world datasets."
---

# Learning Structured Representations with Hyperbolic Embeddings

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a5d2da376bab7624b3caeb9f78fcaa2f-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/a5d2da376bab7624b3caeb9f78fcaa2f-Abstract-Conference.html)

**TLDR**: Proposes structured representation learning using hyperbolic embeddings to incorporate natural label hierarchies present in real-world datasets.

## Abstract

Most real-world datasets consist of a natural hierarchy between classes or an inherent label structure that is either already available or can be constructed cheaply. However, most existing representation learning methods ignore this hierarchy, treating labels as permutation invariant. Recent work [Zeng et al., 2022] proposes using this structured information explicitly, but the use of Euclidean distance may distort the underlying semantic context [Chen et al., 2013]. In this work, motivated by the advantage of hyperbolic spaces in modeling hierarchical relationships, we propose a novel approach HypStructure: a Hyperbolic Structured regularization approach to accurately embed the label hierarchy into the learned representations. HypStructure is a simple-yet-effective regularizer that consists of a hyperbolic tree-based representation loss along with a centering loss, and can be combined with any standard task loss to learn hierarchy-informed features. Extensive experiments on several large-scale vision benchmarks demonstrate the efficacy of HypStructure in reducing distortion and boosting generalization performance especially under low dimensional scenarios. For a better understanding of structured representation, we perform eigenvalue analysis that links the representation geometry to improved Out-of-Distribution (OOD) detection performance seen empirically.