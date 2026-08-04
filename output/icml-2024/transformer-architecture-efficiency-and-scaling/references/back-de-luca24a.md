---
title: "Simulation of Graph Algorithms with Looped Transformers"
source: "https://proceedings.mlr.press/v235/back-de-luca24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/back-de-luca24a/back-de-luca24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'graph-neural-networks-and-topology']
tags: ['looped-transformers', 'graph-algorithms', 'neural-reasoning']
venue: "ICML 2024"
tldr: "This work studies how looped transformers can simulate graph algorithm reasoning steps on relational data."
---

# Simulation of Graph Algorithms with Looped Transformers

**Source**: [https://proceedings.mlr.press/v235/back-de-luca24a.html](https://proceedings.mlr.press/v235/back-de-luca24a.html)

**TLDR**: This work studies how looped transformers can simulate graph algorithm reasoning steps on relational data.

## Abstract

The execution of graph algorithms using neural networks has recently attracted significant interest due to promising empirical progress. This motivates further understanding of how neural networks can replicate reasoning steps with relational data. In this work, we study the ability of transformer networks to simulate algorithms on graphs from a theoretical perspective. The architecture we use is a looped transformer with extra attention heads that interact with the graph. We prove by construction that this architecture can simulate individual algorithms such as Dijkstra’s shortest path, Breadth- and Depth-First Search, and Kosaraju’s strongly connected components, as well as multiple algorithms simultaneously. The number of parameters in the networks does not increase with the input graph size, which implies that the networks can simulate the above algorithms for any graph. Despite this property, we show a limit to simulation in our solution due to finite precision. Finally, we show a Turing Completeness result with constant width when the extra attention heads are utilized.