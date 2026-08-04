---
title: "From Neurons to Neutrons: A Case Study in Interpretability"
source: "https://proceedings.mlr.press/v235/kitouni24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kitouni24a/kitouni24a.pdf"
categories: ['llm-geometry-and-interpretability-research', 'neural-network-learning-dynamics-theory']
tags: ['mechanistic-interpretability', 'neural-networks', 'arithmetic', 'algorithms']
venue: "ICML 2024"
tldr: "A case study using mechanistic interpretability to understand the diverse algorithms neural networks implement when performing simple arithmetic tasks."
---

# From Neurons to Neutrons: A Case Study in Interpretability

**Source**: [https://proceedings.mlr.press/v235/kitouni24a.html](https://proceedings.mlr.press/v235/kitouni24a.html)

**TLDR**: A case study using mechanistic interpretability to understand the diverse algorithms neural networks implement when performing simple arithmetic tasks.

## Abstract

Mechanistic Interpretability (MI) proposes a path toward fully understanding how neural networks make their predictions. Prior work demonstrates that even when trained to perform simple arithmetic, models can implement a variety of algorithms (sometimes concurrently) depending on initialization and hyperparameters. Does this mean neuron-level interpretability techniques have limited applicability? Here, we argue that high-dimensional neural networks can learn useful low-dimensional representations of the data they were trained on, going beyond simply making good predictions: Such representations can be understood with the MI lens and provide insights that are surprisingly faithful to human-derived domain knowledge. This indicates that such approaches to interpretability can be useful for deriving a new understanding of a problem from models trained to solve it. As a case study, we extract nuclear physics concepts by studying models trained to reproduce nuclear data.