---
title: "On Which Nodes Does GCN Fail? Enhancing GCN From the Node Perspective"
source: "https://proceedings.mlr.press/v235/huang24t.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24t/huang24t.pdf"
categories: ['graph-neural-networks-and-topology', 'learning-with-imperfect-data-and-bias']
tags: ['graph-convolutional-networks', 'label-smoothness', 'node-classification']
venue: "ICML 2024"
tldr: "Analyzes failure modes of GCNs at the node level caused by label-smoothness violations and proposes targeted enhancements."
---

# On Which Nodes Does GCN Fail? Enhancing GCN From the Node Perspective

**Source**: [https://proceedings.mlr.press/v235/huang24t.html](https://proceedings.mlr.press/v235/huang24t.html)

**TLDR**: Analyzes failure modes of GCNs at the node level caused by label-smoothness violations and proposes targeted enhancements.

## Abstract

The label smoothness assumption is at the core of Graph Convolutional Networks (GCNs): nodes in a local region have similar labels. Thus, GCN performs local feature smoothing operation to adhere to this assumption. However, there exist some nodes whose labels obtained by feature smoothing conflict with the label smoothness assumption. We find that the label smoothness assumption and the process of feature smoothing are both problematic on these nodes, and call these nodes out of GCN’s control (OOC nodes). In this paper, first, we design the corresponding algorithm to locate the OOC nodes, then we summarize the characteristics of OOC nodes that affect their representation learning, and based on their characteristics, we present DaGCN, an efficient framework that can facilitate the OOC nodes. Extensive experiments verify the superiority of the proposed method and demonstrate that current advanced GCNs are improvements specifically on OOC nodes; the remaining nodes under GCN’s control (UC nodes) are already optimally represented by vanilla GCN on most datasets.