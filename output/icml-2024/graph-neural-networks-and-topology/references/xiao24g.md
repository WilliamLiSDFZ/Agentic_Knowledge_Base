---
title: "Efficient Contrastive Learning for Fast and Accurate Inference on Graphs"
source: "https://proceedings.mlr.press/v235/xiao24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xiao24g/xiao24g.pdf"
categories: ['graph-neural-networks-and-topology', 'clustering-methods-and-multi-view-learning']
tags: ['graph-contrastive-learning', 'inference-efficiency', 'message-passing']
venue: "ICML 2024"
tldr: "An efficient contrastive learning method for graphs that reduces computational overhead during inference while maintaining strong performance."
---

# Efficient Contrastive Learning for Fast and Accurate Inference on Graphs

**Source**: [https://proceedings.mlr.press/v235/xiao24g.html](https://proceedings.mlr.press/v235/xiao24g.html)

**TLDR**: An efficient contrastive learning method for graphs that reduces computational overhead during inference while maintaining strong performance.

## Abstract

Graph contrastive learning has made remarkable advances in settings where there is a scarcity of task-specific labels. Despite these advances, the significant computational overhead for representation inference incurred by existing methods that rely on intensive message passing makes them unsuitable for latency-constrained applications. In this paper, we present GraphECL, a simple and efficient contrastive learning method for fast inference on graphs. GraphECL does away with the need for expensive message passing during inference. Specifically, it introduces a novel coupling of the MLP and GNN models, where the former learns to computationally efficiently mimic the computations performed by the latter. We provide a theoretical analysis showing why MLP can capture essential structural information in neighbors well enough to match the performance of GNN in downstream tasks. The extensive experiments on widely used real-world benchmarks that show that GraphECL achieves superior performance and inference efficiency compared to state-of-the-art graph constrastive learning (GCL) methods on homophilous and heterophilous graphs.