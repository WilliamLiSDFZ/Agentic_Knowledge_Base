---
title: "VISPool: Enhancing Transformer Encoders with Vector Visibility Graph Neural Networks"
source: "https://aclanthology.org/2024.findings-acl.149/"
pdf_url: ""
categories: ['transformer-architecture-analysis-and-design']
tags: ['graph-neural-networks', 'transformer', 'text-representation']
venue: "ACL 2024"
tldr: "VISPool enhances transformer encoders by integrating vector visibility graph neural networks for improved text representations."
---

# VISPool: Enhancing Transformer Encoders with Vector Visibility Graph Neural Networks

**Source**: [https://aclanthology.org/2024.findings-acl.149/](https://aclanthology.org/2024.findings-acl.149/)

**TLDR**: VISPool enhances transformer encoders by integrating vector visibility graph neural networks for improved text representations.

## Abstract

AbstractThe emergence of transformers has revolutionized natural language processing (NLP), as evidenced in various NLP tasks. While graph neural networks (GNNs) show recent promise in NLP, they are not standalone replacements for transformers. Rather, recent research explores combining transformers and GNNs. Existing GNN-based approaches rely on static graph construction methods requiring excessive text processing, and most of them are not scalable with the increasing document and word counts. We address these limitations by proposing a novel dynamic graph construction method for text documents based on vector visibility graphs (VVGs) generated from transformer output. Then, we introduce visibility pooler (VISPool), a scalable model architecture that seamlessly integrates VVG convolutional networks into transformer pipelines. We evaluate the proposed model on the General Language Understanding Evaluation (GLUE) benchmark datasets. VISPool outperforms the baselines with less trainable parameters, demonstrating the viability of the visibility-based graph construction method for enhancing transformers with GNNs.