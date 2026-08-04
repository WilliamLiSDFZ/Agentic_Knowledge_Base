---
title: "PAC-Bayesian Generalization Bounds for Knowledge Graph Representation Learning"
source: "https://proceedings.mlr.press/v235/lee24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24i/lee24i.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'graph-neural-networks-and-topology']
tags: ['PAC-Bayes', 'knowledge-graph', 'representation-learning', 'generalization-bounds']
venue: "ICML 2024"
tldr: "Derives the first PAC-Bayesian generalization bounds for knowledge graph representation learning methods."
---

# PAC-Bayesian Generalization Bounds for Knowledge Graph Representation Learning

**Source**: [https://proceedings.mlr.press/v235/lee24i.html](https://proceedings.mlr.press/v235/lee24i.html)

**TLDR**: Derives the first PAC-Bayesian generalization bounds for knowledge graph representation learning methods.

## Abstract

While a number of knowledge graph representation learning (KGRL) methods have been proposed over the past decade, very few theoretical analyses have been conducted on them. In this paper, we present the first PAC-Bayesian generalization bounds for KGRL methods. To analyze a broad class of KGRL models, we propose a generic framework named ReED (Relation-aware Encoder-Decoder), which consists of a relation-aware message passing encoder and a triplet classification decoder. Our ReED framework can express at least 15 different existing KGRL models, including not only graph neural network-based models such as R-GCN and CompGCN but also shallow-architecture models such as RotatE and ANALOGY. Our generalization bounds for the ReED framework provide theoretical grounds for the commonly used tricks in KGRL, e.g., parameter-sharing and weight normalization schemes, and guide desirable design choices for practical KGRL methods. We empirically show that the critical factors in our generalization bounds can explain actual generalization errors on three real-world knowledge graphs.