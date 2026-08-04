---
title: "Graph Distillation with Eigenbasis Matching"
source: "https://proceedings.mlr.press/v235/liu24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24d/liu24d.pdf"
categories: ['graph-neural-networks-and-topology']
tags: ['graph-distillation', 'eigenbasis', 'GNN']
venue: "ICML 2024"
tldr: "Graph distillation via eigenbasis matching is proposed to efficiently train GNNs on small synthetic graphs that preserve spectral properties of large real graphs."
---

# Graph Distillation with Eigenbasis Matching

**Source**: [https://proceedings.mlr.press/v235/liu24d.html](https://proceedings.mlr.press/v235/liu24d.html)

**TLDR**: Graph distillation via eigenbasis matching is proposed to efficiently train GNNs on small synthetic graphs that preserve spectral properties of large real graphs.

## Abstract

The increasing amount of graph data places requirements on the efficient training of graph neural networks (GNNs). The emerging graph distillation (GD) tackles this challenge by distilling a small synthetic graph to replace the real large graph, ensuring GNNs trained on real and synthetic graphs exhibit comparable performance. However, existing methods rely on GNN-related information as supervision, including gradients, representations, and trajectories, which have two limitations. First, GNNs can affect the spectrum (i.e., eigenvalues) of the real graph, causing spectrum bias in the synthetic graph. Second, the variety of GNN architectures leads to the creation of different synthetic graphs, requiring traversal to obtain optimal performance. To tackle these issues, we propose Graph Distillation with Eigenbasis Matching (GDEM), which aligns the eigenbasis and node features of real and synthetic graphs. Meanwhile, it directly replicates the spectrum of the real graph and thus prevents the influence of GNNs. Moreover, we design a discrimination constraint to balance the effectiveness and generalization of GDEM. Theoretically, the synthetic graphs distilled by GDEM are restricted spectral approximations of the real graphs. Extensive experiments demonstrate that GDEM outperforms state-of-the-art GD methods with powerful cross-architecture generalization ability and significant distillation efficiency. Our code is available at https://github.com/liuyang-tian/GDEM.