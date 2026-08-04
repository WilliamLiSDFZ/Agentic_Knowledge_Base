---
title: "Multi-View Clustering by Inter-cluster Connectivity Guided Reward"
source: "https://proceedings.mlr.press/v235/dai24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dai24b/dai24b.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'graph-neural-networks-and-topology']
tags: ['multi-view-clustering', 'inter-cluster-connectivity', 'reward']
venue: "ICML 2024"
tldr: "Proposes a multi-view clustering method guided by inter-cluster connectivity rewards, reducing reliance on strong prior information."
---

# Multi-View Clustering by Inter-cluster Connectivity Guided Reward

**Source**: [https://proceedings.mlr.press/v235/dai24b.html](https://proceedings.mlr.press/v235/dai24b.html)

**TLDR**: Proposes a multi-view clustering method guided by inter-cluster connectivity rewards, reducing reliance on strong prior information.

## Abstract

Multi-view clustering has been widely explored for its effectiveness in harmonizing heterogeneity along with consistency in different views of data. Despite the significant progress made by recent works, the performance of most existing methods is heavily reliant on strong priori information regarding the true cluster number $\textit{K}$, which is rarely feasible in real-world scenarios. In this paper, we propose a novel graph-based multi-view clustering algorithm to infer unknown $\textit{K}$ through a graph consistency reward mechanism. To be specific, we evaluate the cluster indicator matrix during each iteration with respect to diverse $\textit{K}$. We formulate the inference process of unknown $\textit{K}$ as a parsimonious reinforcement learning paradigm, where the reward is measured by inter-cluster connectivity. As a result, our approach is capable of independently producing the final clustering result, free from the input of a predefined cluster number. Experimental results on multiple benchmark datasets demonstrate the effectiveness of our proposed approach in comparison to existing state-of-the-art methods.