---
title: "Generating In-Distribution Proxy Graphs for Explaining Graph Neural Networks"
source: "https://proceedings.mlr.press/v235/chen24bd.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24bd/chen24bd.pdf"
categories: ['graph-neural-networks-and-topology', 'ai-explainability-uncertainty-human-decision-making']
tags: ['GNN-explainability', 'proxy-graphs', 'in-distribution-explanations']
venue: "ICML 2024"
tldr: "A method generates in-distribution proxy graphs to improve explainability of Graph Neural Networks in high-stakes applications."
---

# Generating In-Distribution Proxy Graphs for Explaining Graph Neural Networks

**Source**: [https://proceedings.mlr.press/v235/chen24bd.html](https://proceedings.mlr.press/v235/chen24bd.html)

**TLDR**: A method generates in-distribution proxy graphs to improve explainability of Graph Neural Networks in high-stakes applications.

## Abstract

Graph Neural Networks (GNNs) have become a building block in graph data processing, with wide applications in critical domains. The growing needs to deploy GNNs in high-stakes applications necessitate explainability for users in the decision-making processes. A popular paradigm for the explainability of GNNs is to identify explainable subgraphs by comparing their labels with the ones of original graphs. This task is challenging due to the substantial distributional shift from the original graphs in the training set to the set of explainable subgraphs, which prevents accurate prediction of labels with the subgraphs. To address it, in this paper, we propose a novel method that generates proxy graphs for explainable subgraphs that are in the distribution of training data. We introduce a parametric method that employs graph generators to produce proxy graphs. A new training objective based on information theory is designed to ensure that proxy graphs not only adhere to the distribution of training data but also preserve explanatory factors. Such generated proxy graphs can be reliably used to approximate the predictions of the labels of explainable subgraphs. Empirical evaluations across various datasets demonstrate our method achieves more accurate explanations for GNNs.