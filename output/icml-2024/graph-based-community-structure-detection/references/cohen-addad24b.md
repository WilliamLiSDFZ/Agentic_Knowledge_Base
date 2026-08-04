---
title: "Multi-View Stochastic Block Models"
source: "https://proceedings.mlr.press/v235/cohen-addad24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cohen-addad24b/cohen-addad24b.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'graph-based-community-structure-detection']
tags: ['multi-view-clustering', 'stochastic-block-models', 'graph-clustering']
venue: "ICML 2024"
tldr: "Formalizes multi-view stochastic block models for graph clustering leveraging multiple data sources to improve community detection."
---

# Multi-View Stochastic Block Models

**Source**: [https://proceedings.mlr.press/v235/cohen-addad24b.html](https://proceedings.mlr.press/v235/cohen-addad24b.html)

**TLDR**: Formalizes multi-view stochastic block models for graph clustering leveraging multiple data sources to improve community detection.

## Abstract

Graph clustering is a central topic in unsupervised learning with a multitude of practical applications. In recent years, multi-view graph clustering has gained a lot of attention for its applicability to real-world instances where one often has access to multiple data sources. In this paper we formalize a new family of models, called multi-view stochastic block models that capture this setting. For this model, we first study efficient algorithms that naively work on the union of multiple graphs. Then, we introduce a new efficient algorithm that provably outperforms previous approaches by analyzing the structure of each graph separately. Finally, we complement our results with an information-theoretic lower bound studying the limits of what can be done in this model.