---
title: "Cooperative Graph Neural Networks"
source: "https://proceedings.mlr.press/v235/finkelshtein24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/finkelshtein24a/finkelshtein24a.pdf"
categories: ['graph-neural-networks-and-topology', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['graph-neural-networks', 'message-passing', 'cooperative-nodes']
venue: "ICML 2024"
tldr: "Cooperative GNNs allow nodes to choose whether to share, receive, or ignore messages, improving expressivity over standard message-passing."
---

# Cooperative Graph Neural Networks

**Source**: [https://proceedings.mlr.press/v235/finkelshtein24a.html](https://proceedings.mlr.press/v235/finkelshtein24a.html)

**TLDR**: Cooperative GNNs allow nodes to choose whether to share, receive, or ignore messages, improving expressivity over standard message-passing.

## Abstract

Graph neural networks are popular architectures for graph machine learning, based on iterative computation of node representations of an input graph through a series of invariant transformations. A large class of graph neural networks follow a standard message-passing paradigm: at every layer, each node state is updated based on an aggregate of messages from its neighborhood. In this work, we propose a novel framework for training graph neural networks, where every node is viewed as a player that can choose to either listen, broadcast, listen and broadcast, or to isolate. The standard message propagation scheme can then be viewed as a special case of this framework where every node listens and broadcasts to all neighbors. Our approach offers a more flexible and dynamic message-passing paradigm, where each node can determine its own strategy based on their state, effectively exploring the graph topology while learning. We provide a theoretical analysis of the new message-passing scheme which is further supported by an extensive empirical analysis on a synthetic and real-world datasets.