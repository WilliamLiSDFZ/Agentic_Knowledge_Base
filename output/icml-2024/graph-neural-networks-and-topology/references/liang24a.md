---
title: "Graph External Attention Enhanced Transformer"
source: "https://proceedings.mlr.press/v235/liang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liang24a/liang24a.pdf"
categories: ['graph-neural-networks-and-topology']
tags: ['graph-transformer', 'attention-mechanism', 'graph-representation']
venue: "ICML 2024"
tldr: "Graph External Attention Enhanced Transformer incorporates external attention to improve graph representation learning."
---

# Graph External Attention Enhanced Transformer

**Source**: [https://proceedings.mlr.press/v235/liang24a.html](https://proceedings.mlr.press/v235/liang24a.html)

**TLDR**: Graph External Attention Enhanced Transformer incorporates external attention to improve graph representation learning.

## Abstract

The Transformer architecture has recently gained considerable attention in the field of graph representation learning, as it naturally overcomes several limitations of Graph Neural Networks (GNNs) with customized attention mechanisms or positional and structural encodings. Despite making some progress, existing works tend to overlook external information of graphs, specifically the correlation between graphs. Intuitively, graphs with similar structures should have similar representations. Therefore, we propose Graph External Attention (GEA) — a novel attention mechanism that leverages multiple external node/edge key-value units to capture inter-graph correlations implicitly. On this basis, we design an effective architecture called Graph External Attention Enhanced Transformer (GEAET), which integrates local structure and global interaction information for more comprehensive graph representations. Extensive experiments on benchmark datasets demonstrate that GEAET achieves state-of-the-art empirical performance. The source code is available for reproducibility at: https://github.com/icm1018/GEAET.