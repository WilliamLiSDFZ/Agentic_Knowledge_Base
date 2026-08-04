---
title: "Network Tight Community Detection"
source: "https://proceedings.mlr.press/v235/deng24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/deng24f/deng24f.pdf"
categories: ['graph-based-community-structure-detection', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['community-detection', 'tight-communities', 'scattered-nodes', 'network-analysis', 'graph-clustering']
venue: "ICML 2024"
tldr: "Proposes a community detection method that identifies tight, well-defined communities among a subset of nodes while treating remaining scattered nodes as non-informative."
---

# Network Tight Community Detection

**Source**: [https://proceedings.mlr.press/v235/deng24f.html](https://proceedings.mlr.press/v235/deng24f.html)

**TLDR**: Proposes a community detection method that identifies tight, well-defined communities among a subset of nodes while treating remaining scattered nodes as non-informative.

## Abstract

Conventional community detection methods often categorize all nodes into clusters. However, the presumed community structure of interest may only be valid for a subset of nodes (named as ‘tight nodes’), while the rest of the network may consist of noninformative “scattered nodes”. For example, a protein-protein network often contains proteins that do not belong to specific biological functional modules but are involved in more general processes, or act as bridges between different functional modules. Forcing each of these proteins into a single cluster introduces unwanted biases and obscures the underlying biological implication. To address this issue, we propose a tight community detection (TCD) method to identify tight communities excluding scattered nodes. The algorithm enjoys a strong theoretical guarantee of tight node identification accuracy and is scalable for large networks. The superiority of the proposed method is demonstrated by various synthetic and real experiments.