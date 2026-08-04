---
title: "Weisfeiler-Leman at the margin: When more expressivity matters"
source: "https://proceedings.mlr.press/v235/franks24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/franks24a/franks24a.pdf"
categories: ['graph-neural-networks-and-topology', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['Weisfeiler-Leman', 'graph-kernels', 'expressivity']
venue: "ICML 2024"
tldr: "Higher expressivity beyond 1-WL is shown to improve graph kernel performance in margin-based classification settings."
---

# Weisfeiler-Leman at the margin: When more expressivity matters

**Source**: [https://proceedings.mlr.press/v235/franks24a.html](https://proceedings.mlr.press/v235/franks24a.html)

**TLDR**: Higher expressivity beyond 1-WL is shown to improve graph kernel performance in margin-based classification settings.

## Abstract

The Weisfeiler–Leman algorithm (1-WL) is a well-studied heuristic for the graph isomorphism problem. Recently, the algorithm has played a prominent role in understanding the expressive power of message-passing graph neural networks (MPNNs) and being effective as a graph kernel. Despite its success, the 1-WL faces challenges in distinguishing non-isomorphic graphs, leading to the development of more expressive MPNN and kernel architectures. However, the relationship between enhanced expressivity and improved generalization performance remains unclear. Here, we show that an architecture’s expressivity offers limited insights into its generalization performance when viewed through graph isomorphism. Moreover, we focus on augmenting 1-WL and MPNNs with subgraph information and employ classical margin theory to investigate the conditions under which an architecture’s increased expressivity aligns with improved generalization performance. In addition, we introduce variations of expressive 1-WL-based kernel and MPNN architectures with provable generalization properties. Our empirical study confirms the validity of our theoretical findings.