---
title: "KnowFormer: Revisiting Transformers for Knowledge Graph Reasoning"
source: "https://proceedings.mlr.press/v235/liu24au.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24au/liu24au.pdf"
categories: ['graph-neural-networks-and-topology', 'graph-clustering-and-matching-algorithms']
tags: ['knowledge-graph-reasoning', 'transformers', 'path-based-methods']
venue: "ICML 2024"
tldr: "A transformer-based model for knowledge graph reasoning that overcomes message-passing limitations such as missing paths and scalability issues."
---

# KnowFormer: Revisiting Transformers for Knowledge Graph Reasoning

**Source**: [https://proceedings.mlr.press/v235/liu24au.html](https://proceedings.mlr.press/v235/liu24au.html)

**TLDR**: A transformer-based model for knowledge graph reasoning that overcomes message-passing limitations such as missing paths and scalability issues.

## Abstract

Knowledge graph reasoning plays a vital role in various applications and has garnered considerable attention. Recently, path-based methods have achieved impressive performance. However, they may face limitations stemming from constraints in message-passing neural networks, such as missing paths and information over-squashing. In this paper, we revisit the application of transformers for knowledge graph reasoning to address the constraints faced by path-based methods and propose a novel method KnowFormer. KnowFormer utilizes a transformer architecture to perform reasoning on knowledge graphs from the message-passing perspective, rather than reasoning by textual information like previous pretrained language model based methods. Specifically, we define the attention computation based on the query prototype of knowledge graph reasoning, facilitating convenient construction and efficient optimization. To incorporate structural information into the self-attention mechanism, we introduce structure-aware modules to calculate query, key, and value respectively. Additionally, we present an efficient attention computation method for better scalability. Experimental results demonstrate the superior performance of KnowFormer compared to prominent baseline methods on both transductive and inductive benchmarks.