---
title: "Hypergraph-enhanced Dual Semi-supervised Graph Classification"
source: "https://proceedings.mlr.press/v235/ju24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ju24a/ju24a.pdf"
categories: ['graph-neural-networks-and-topology', 'clustering-methods-and-multi-view-learning']
tags: ['hypergraph', 'semi-supervised', 'graph-classification', 'GNN']
venue: "ICML 2024"
tldr: "Proposes a hypergraph-enhanced dual semi-supervised framework for graph classification with limited labeled data."
---

# Hypergraph-enhanced Dual Semi-supervised Graph Classification

**Source**: [https://proceedings.mlr.press/v235/ju24a.html](https://proceedings.mlr.press/v235/ju24a.html)

**TLDR**: Proposes a hypergraph-enhanced dual semi-supervised framework for graph classification with limited labeled data.

## Abstract

In this paper, we study semi-supervised graph classification, which aims at accurately predicting the categories of graphs in scenarios with limited labeled graphs and abundant unlabeled graphs. Despite the promising capability of graph neural networks (GNNs), they typically require a large number of costly labeled graphs, while a wealth of unlabeled graphs fail to be effectively utilized. Moreover, GNNs are inherently limited to encoding local neighborhood information using message-passing mechanisms, thus lacking the ability to model higher-order dependencies among nodes. To tackle these challenges, we propose a Hypergraph-Enhanced DuAL framework named HEAL for semi-supervised graph classification, which captures graph semantics from the perspective of the hypergraph and the line graph, respectively. Specifically, to better explore the higher-order relationships among nodes, we design a hypergraph structure learning to adaptively learn complex node dependencies beyond pairwise relations. Meanwhile, based on the learned hypergraph, we introduce a line graph to capture the interaction between hyperedges, thereby better mining the underlying semantic structures. Finally, we develop a relational consistency learning to facilitate knowledge transfer between the two branches and provide better mutual guidance. Extensive experiments on real-world graph datasets verify the effectiveness of the proposed method against existing state-of-the-art methods.