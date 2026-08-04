---
title: "How Interpretable Are Interpretable Graph Neural Networks?"
source: "https://proceedings.mlr.press/v235/chen24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24b/chen24b.pdf"
categories: ['graph-neural-networks-and-topology', 'ai-explainability-uncertainty-human-decision-making']
tags: ['explainable-GNNs', 'attention-mechanism', 'subgraph-extraction', 'interpretability']
venue: "ICML 2024"
tldr: "An investigation of the interpretability limitations of attention-based explainable GNNs and how well they identify true explanatory subgraphs."
---

# How Interpretable Are Interpretable Graph Neural Networks?

**Source**: [https://proceedings.mlr.press/v235/chen24b.html](https://proceedings.mlr.press/v235/chen24b.html)

**TLDR**: An investigation of the interpretability limitations of attention-based explainable GNNs and how well they identify true explanatory subgraphs.

## Abstract

Interpretable graph neural networks (XGNNs ) are widely adopted in various scientific applications involving graph-structured data. Existing XGNNs predominantly adopt the attention-based mechanism to learn edge or node importance for extracting and making predictions with the interpretable subgraph. However, the representational properties and limitations of these methods remain inadequately explored. In this work, we present a theoretical framework that formulates interpretable subgraph learning with the multilinear extension of the subgraph distribution, coined as subgraph multilinear extension (SubMT). Extracting the desired interpretable subgraph requires an accurate approximation of SubMT, yet we find that the existing XGNNs can have a huge gap in fitting SubMT. Consequently, the SubMT approximation failure will lead to the degenerated interpretability of the extracted subgraphs. To mitigate the issue, we design a new XGNN architecture called Graph Multilinear neT (GMT), which is provably more powerful in approximating SubMT. We empirically validate our theoretical findings on a number of graph classification benchmarks. The results demonstrate that GMT outperforms the state-of-the-art up to 10% in terms of both interpretability and generalizability across 12 regular and geometric graph benchmarks.