---
title: "Graph Neural Networks Use Graphs When They Shouldn’t"
source: "https://proceedings.mlr.press/v235/bechler-speicher24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bechler-speicher24a/bechler-speicher24a.pdf"
categories: ['graph-neural-networks-and-topology', 'learning-with-imperfect-data-and-bias']
tags: ['graph-neural-networks', 'spurious-correlations', 'topology', 'inductive-bias', 'tabular-data']
venue: "ICML 2024"
tldr: "Demonstrates that GNNs can fail by relying on graph structure when ignoring it would yield better predictions."
---

# Graph Neural Networks Use Graphs When They Shouldn’t

**Source**: [https://proceedings.mlr.press/v235/bechler-speicher24a.html](https://proceedings.mlr.press/v235/bechler-speicher24a.html)

**TLDR**: Demonstrates that GNNs can fail by relying on graph structure when ignoring it would yield better predictions.

## Abstract

Predictions over graphs play a crucial role in various domains, including social networks and medicine. Graph Neural Networks (GNNs) have emerged as the dominant approach for learning on graph data. Although a graph-structure is provided as input to the GNN, in some cases the best solution can be obtained by ignoring it. While GNNs have the ability to ignore the graph-structure in such cases, it is not clear that they will. In this work, we show that GNNs actually tend to overfit the given graph-structure in the sense that they use it even when a better solution can be obtained by ignoring it. We analyze the implicit bias of gradient-descent learning of GNNs and prove that when the ground truth function does not use the graphs, GNNs are not guaranteed to learn a solution that ignores the graph, even with infinite data. We examine this phenomenon with respect to different graph distributions and find that regular graphs are more robust to this overfitting. We also prove that within the family of regular graphs, GNNs are guaranteed to extrapolate when learning with gradient descent. Finally, based on our empirical and theoretical findings, we demonstrate on real-data how regular graphs can be leveraged to reduce graph overfitting and enhance performance.