---
title: "Automated Loss function Search for Class-imbalanced Node Classification"
source: "https://proceedings.mlr.press/v235/guo24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/guo24h/guo24h.pdf"
categories: ['graph-neural-networks-and-topology', 'llm-driven-automated-system-optimization']
tags: ['class-imbalance', 'node-classification', 'loss-function-search', 'graph-neural-networks', 'automated-ML']
venue: "ICML 2024"
tldr: "An automated loss function search framework to address class-imbalanced node classification on graphs."
---

# Automated Loss function Search for Class-imbalanced Node Classification

**Source**: [https://proceedings.mlr.press/v235/guo24h.html](https://proceedings.mlr.press/v235/guo24h.html)

**TLDR**: An automated loss function search framework to address class-imbalanced node classification on graphs.

## Abstract

Class-imbalanced node classification tasks are prevalent in real-world scenarios. Due to the uneven distribution of nodes across different classes, learning high-quality node representations remains a challenging endeavor. The engineering of loss functions has shown promising potential in addressing this issue. It involves the meticulous design of loss functions, utilizing information about the quantities of nodes in different categories and the network’s topology to learn unbiased node representations. However, the design of these loss functions heavily relies on human expert knowledge and exhibits limited adaptability to specific target tasks. In this paper, we introduce a high-performance, flexible, and generalizable automated loss function search framework to tackle this challenge. Across 15 combinations of graph neural networks and datasets, our framework achieves a significant improvement in performance compared to state-of-the-art methods. Additionally, we observe that homophily in graph-structured data significantly contributes to the transferability of the proposed framework.