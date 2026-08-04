---
title: "Mitigating Oversmoothing Through Reverse Process of GNNs for Heterophilic Graphs"
source: "https://proceedings.mlr.press/v235/park24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/park24d/park24d.pdf"
categories: ['graph-neural-networks-and-topology', 'neural-network-learning-dynamics-theory']
tags: ['GNN', 'oversmoothing', 'heterophilic-graphs', 'reverse-diffusion']
venue: "ICML 2024"
tldr: "Proposes using the reverse process of GNN message passing to counteract oversmoothing and produce distinguishable node representations for heterophilic graphs."
---

# Mitigating Oversmoothing Through Reverse Process of GNNs for Heterophilic Graphs

**Source**: [https://proceedings.mlr.press/v235/park24d.html](https://proceedings.mlr.press/v235/park24d.html)

**TLDR**: Proposes using the reverse process of GNN message passing to counteract oversmoothing and produce distinguishable node representations for heterophilic graphs.

## Abstract

Graph Neural Network (GNN) resembles the diffusion process, leading to the over-smoothing of learned representations when stacking many layers. Hence, the reverse process of message passing can produce the distinguishable node representations by inverting the forward message propagation. The distinguishable representations can help us to better classify neighboring nodes with different labels, such as in heterophilic graphs. In this work, we apply the design principle of the reverse process to the three variants of the GNNs. Through the experiments on heterophilic graph data, where adjacent nodes need to have different representations for successful classification, we show that the reverse process significantly improves the prediction performance in many cases. Additional analysis reveals that the reverse mechanism can mitigate the over-smoothing over hundreds of layers. Our code is available at https://github.com/ml-postech/reverse-gnn.