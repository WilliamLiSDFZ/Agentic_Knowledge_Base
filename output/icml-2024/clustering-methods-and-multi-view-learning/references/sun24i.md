---
title: "Learning Graph Representation via Graph Entropy Maximization"
source: "https://proceedings.mlr.press/v235/sun24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sun24i/sun24i.pdf"
categories: ['graph-neural-networks-and-topology', 'clustering-methods-and-multi-view-learning']
tags: ['graph-representation-learning', 'entropy-maximization', 'graph-classification', 'diversity', 'information-theory']
venue: "ICML 2024"
tldr: "Graph entropy maximization is proposed as an objective for learning diverse and informative graph representations for downstream classification tasks."
---

# Learning Graph Representation via Graph Entropy Maximization

**Source**: [https://proceedings.mlr.press/v235/sun24i.html](https://proceedings.mlr.press/v235/sun24i.html)

**TLDR**: Graph entropy maximization is proposed as an objective for learning diverse and informative graph representations for downstream classification tasks.

## Abstract

Graph representation learning aims to represent graphs as vectors that can be utilized in downstream tasks such as graph classification. In this work, we focus on learning diverse representations that can capture the graph information as much as possible. We propose quantifying graph information using graph entropy, where we define a probability distribution of a graph based on its nodes’ representations and global-graph representation. However, the computation of graph entropy is NP-hard due to the complex vertex-packing polytope involved in its definition. To address this challenge, we provide an approximation method leveraging orthonormal representations for graph entropy maximization. The proposed method is implemented via graph neural networks, resulting in informative node-level and graph-level representations. Experimental results demonstrate the effectiveness of our method in comparison to many baselines in unsupervised learning and semi-supervised learning tasks. The code of our method is available at https://github.com/MathAdventurer/GeMax.