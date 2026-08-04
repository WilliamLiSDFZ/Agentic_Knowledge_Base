---
title: "Networked Inequality: Preferential Attachment Bias in Graph Neural Network Link Prediction"
source: "https://proceedings.mlr.press/v235/subramonian24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/subramonian24a/subramonian24a.pdf"
categories: ['graph-neural-networks-and-topology', 'fairness-aware-algorithmic-decision-making']
tags: ['GNN', 'link-prediction', 'fairness', 'preferential-attachment', 'social-networks']
venue: "ICML 2024"
tldr: "Preferential attachment bias in GNN link prediction is analyzed and shown to exacerbate within-group inequality in social and citation networks."
---

# Networked Inequality: Preferential Attachment Bias in Graph Neural Network Link Prediction

**Source**: [https://proceedings.mlr.press/v235/subramonian24a.html](https://proceedings.mlr.press/v235/subramonian24a.html)

**TLDR**: Preferential attachment bias in GNN link prediction is analyzed and shown to exacerbate within-group inequality in social and citation networks.

## Abstract

Graph neural network (GNN) link prediction is increasingly deployed in citation, collaboration, and online social networks to recommend academic literature, collaborators, and friends. While prior research has investigated the dyadic fairness of GNN link prediction, the within-group (e.g., queer women) fairness and "rich get richer" dynamics of link prediction remain underexplored. However, these aspects have significant consequences for degree and power imbalances in networks. In this paper, we shed light on how degree bias in networks affects Graph Convolutional Network (GCN) link prediction. In particular, we theoretically uncover that GCNs with a symmetric normalized graph filter have a within-group preferential attachment bias. We validate our theoretical analysis on real-world citation, collaboration, and online social networks. We further bridge GCN’s preferential attachment bias with unfairness in link prediction and propose a new within-group fairness metric. This metric quantifies disparities in link prediction scores within social groups, towards combating the amplification of degree and power disparities. Finally, we propose a simple training-time strategy to alleviate within-group unfairness, and we show that it is effective on citation, social, and credit networks.