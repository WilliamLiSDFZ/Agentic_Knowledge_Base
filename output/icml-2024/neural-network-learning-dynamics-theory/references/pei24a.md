---
title: "Multi-Track Message Passing: Tackling Oversmoothing and Oversquashing in Graph Learning via Preventing Heterophily Mixing"
source: "https://proceedings.mlr.press/v235/pei24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pei24a/pei24a.pdf"
categories: ['graph-neural-networks-and-topology', 'neural-network-learning-dynamics-theory']
tags: ['graph-neural-networks', 'oversmoothing', 'oversquashing', 'heterophily', 'message-passing']
venue: "ICML 2024"
tldr: "Proposes multi-track message passing to prevent heterophily mixing in aggregation, addressing oversmoothing and oversquashing in deep GNNs."
---

# Multi-Track Message Passing: Tackling Oversmoothing and Oversquashing in Graph Learning via Preventing Heterophily Mixing

**Source**: [https://proceedings.mlr.press/v235/pei24a.html](https://proceedings.mlr.press/v235/pei24a.html)

**TLDR**: Proposes multi-track message passing to prevent heterophily mixing in aggregation, addressing oversmoothing and oversquashing in deep GNNs.

## Abstract

The advancement toward deeper graph neural networks is currently obscured by two inherent issues in message passing, oversmoothing and oversquashing. We identify the root cause of these issues as information loss due to heterophily mixing in aggregation, where messages of diverse category semantics are mixed. We propose a novel multi-track graph convolutional network to address oversmoothing and oversquashing effectively. Our basic idea is intuitive: if messages are separated and independently propagated according to their category semantics, heterophilic mixing can be prevented. Consequently, we present a novel multi-track message passing scheme capable of preventing heterophilic mixing, enhancing long-distance information flow, and improving separation condition. Empirical validations show that our model achieved state-of-the-art performance on several graph datasets and effectively tackled oversmoothing and oversquashing, setting a new benchmark of $86.4$% accuracy on Cora.