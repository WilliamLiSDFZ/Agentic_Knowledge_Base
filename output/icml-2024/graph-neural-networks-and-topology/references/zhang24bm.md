---
title: "Disentangled Continual Graph Neural Architecture Search with Invariant Modular Supernet"
source: "https://proceedings.mlr.press/v235/zhang24bm.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24bm/zhang24bm.pdf"
categories: ['graph-neural-networks-and-topology', 'continual-learning-memory-plasticity']
tags: ['graph-neural-architecture-search', 'continual-learning', 'disentanglement', 'supernet', 'graph-learning']
venue: "ICML 2024"
tldr: "Proposes a disentangled continual graph neural architecture search framework with invariant modular supernet for sequential graph tasks."
---

# Disentangled Continual Graph Neural Architecture Search with Invariant Modular Supernet

**Source**: [https://proceedings.mlr.press/v235/zhang24bm.html](https://proceedings.mlr.press/v235/zhang24bm.html)

**TLDR**: Proposes a disentangled continual graph neural architecture search framework with invariant modular supernet for sequential graph tasks.

## Abstract

The existing graph neural architecture search (GNAS) methods assume that the graph tasks are static during the search process, ignoring the ubiquitous scenarios where sequential graph tasks come in a continual fashion. Moreover, existing GNAS works resort to entangled graph factors during the architecture search process, resulting in the catastrophic forgetting problems. In this paper, we study the problem of continual graph neural architecture search that is expected to continually search the architecture to learn new graph tasks without forgetting the past, which remains largely unexplored in the literature. However, this problem poses the challenge of architecture conflicts, i.e., the optimal architecture for the new graph task may have performance deterioration and thus sub-optimal for past tasks. To address the challenge, we propose a novel Disentangled Continual Graph Neural Architecture Search with Invariant Modularization (GASIM) method, which is able to continually search the optimal architectures without forgetting past knowledge. Specifically, we first design a modular graph architecture super-network incorporating multiple modules to enable searching architecture with factor expertise. Second, we propose a factor-based task-module router that discovers the latent graph factors and routes the incoming task to the best suitable architecture module to alleviate the forgetting problem induced by architecture conflicts. Finally, we propose an invariant architecture search mechanism to capture the shared knowledge among tasks. Extensive experiments on real-world datasets demonstrate that the proposed method achieves state-of-the-art performance against baselines in continual graph neural architecture search.