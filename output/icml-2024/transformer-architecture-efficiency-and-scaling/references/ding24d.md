---
title: "Recurrent Distance Filtering for Graph Representation Learning"
source: "https://proceedings.mlr.press/v235/ding24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ding24d/ding24d.pdf"
categories: ['graph-neural-networks-and-topology', 'transformer-architecture-efficiency-and-scaling']
tags: ['graph-neural-networks', 'distance-filtering', 'message-passing', 'long-range-dependencies', 'graph-transformers']
venue: "ICML 2024"
tldr: "Proposes recurrent distance filtering for GNNs to effectively capture information from distant nodes without sacrificing graph inductive bias."
---

# Recurrent Distance Filtering for Graph Representation Learning

**Source**: [https://proceedings.mlr.press/v235/ding24d.html](https://proceedings.mlr.press/v235/ding24d.html)

**TLDR**: Proposes recurrent distance filtering for GNNs to effectively capture information from distant nodes without sacrificing graph inductive bias.

## Abstract

Graph neural networks based on iterative one-hop message passing have been shown to struggle in harnessing the information from distant nodes effectively. Conversely, graph transformers allow each node to attend to all other nodes directly, but lack graph inductive bias and have to rely on ad-hoc positional encoding. In this paper, we propose a new architecture to reconcile these challenges. Our approach stems from the recent breakthroughs in long-range modeling provided by deep state-space models: for a given target node, our model aggregates other nodes by their shortest distances to the target and uses a linear RNN to encode the sequence of hop representations. The linear RNN is parameterized in a particular diagonal form for stable long-range signal propagation and is theoretically expressive enough to encode the neighborhood hierarchy. With no need for positional encoding, we empirically show that the performance of our model is comparable to or better than that of state-of-the-art graph transformers on various benchmarks, with a significantly reduced computational cost. Our code is open-source at https://github.com/skeletondyh/GRED.