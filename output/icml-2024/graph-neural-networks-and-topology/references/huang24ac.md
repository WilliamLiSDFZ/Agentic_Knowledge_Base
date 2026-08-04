---
title: "Enhancing Size Generalization in Graph Neural Networks through Disentangled Representation Learning"
source: "https://proceedings.mlr.press/v235/huang24ac.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24ac/huang24ac.pdf"
categories: ['graph-neural-networks-and-topology', 'learning-with-imperfect-data-and-bias']
tags: ['graph-neural-networks', 'size-generalization', 'disentangled-representation', 'distribution-shift', 'graph-classification']
venue: "ICML 2024"
tldr: "Improves GNN size generalization by disentangling size information from graph representations via disentangled representation learning."
---

# Enhancing Size Generalization in Graph Neural Networks through Disentangled Representation Learning

**Source**: [https://proceedings.mlr.press/v235/huang24ac.html](https://proceedings.mlr.press/v235/huang24ac.html)

**TLDR**: Improves GNN size generalization by disentangling size information from graph representations via disentangled representation learning.

## Abstract

Although most graph neural networks (GNNs) can operate on graphs of any size, their classification performance often declines on graphs larger than those encountered during training. Existing methods insufficiently address the removal of size information from graph representations, resulting in sub-optimal performance and reliance on backbone models. In response, we propose DISGEN, a novel and model-agnostic framework designed to disentangle size factors from graph representations. DISGEN employs size- and task-invariant augmentations and introduces a decoupling loss that minimizes shared information in hidden representations, with theoretical guarantees for its effectiveness. Our empirical results show that DISGEN outperforms the state-of-the-art models by up to 6% on real-world datasets, underscoring its effectiveness in enhancing the size generalizability of GNNs. Our codes are available at: https://github.com/GraphmindDartmouth/DISGEN.