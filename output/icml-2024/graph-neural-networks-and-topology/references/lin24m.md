---
title: "HGAP: Boosting Permutation Invariant and Permutation Equivariant in Multi-Agent Reinforcement Learning via Graph Attention Network"
source: "https://proceedings.mlr.press/v235/lin24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24m/lin24m.pdf"
categories: ['multi-agent-mdp-structure-and-dependencies', 'graph-neural-networks-and-topology']
tags: ['multi-agent-reinforcement-learning', 'graph-attention-network', 'permutation-equivariance']
venue: "ICML 2024"
tldr: "A graph attention network approach boosting permutation invariance and equivariance in multi-agent reinforcement learning."
---

# HGAP: Boosting Permutation Invariant and Permutation Equivariant in Multi-Agent Reinforcement Learning via Graph Attention Network

**Source**: [https://proceedings.mlr.press/v235/lin24m.html](https://proceedings.mlr.press/v235/lin24m.html)

**TLDR**: A graph attention network approach boosting permutation invariance and equivariance in multi-agent reinforcement learning.

## Abstract

Graph representation has gained widespread application across various machine learning domains, attributed to its ability to discern correlations among input nodes. In the realm of Multi- agent Reinforcement Learning (MARL), agents are tasked with observing other entities within their environment to determine their behavior. Conventional MARL methodologies often suffer from training difficulties if Permutation Invariant (PI) and Permutation Equivariant (PE) properties are not considered during training. The adoption of graph representation offers a solution to these challenges by conceptualizing observed entities as a graph. In this context, we introduce the Hyper Graphical Attention Policy (HGAP) Network, which employs a graph attention mechanism to fulfill the PI and PE properties, while also understanding inter-entity interactions for decision-making. HGAP is assessed across various MARL benchmarks to confirm its effectiveness and efficiency. In addition, a series of ablation studies are provided to demonstrate its adaptability, transferability, and the capability to alleviate the complexities introduced by the POMDP constraint.