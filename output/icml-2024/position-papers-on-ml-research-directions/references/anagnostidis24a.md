---
title: "Navigating Scaling Laws: Compute Optimality in Adaptive Model Training"
source: "https://proceedings.mlr.press/v235/anagnostidis24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/anagnostidis24a/anagnostidis24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'position-papers-on-ml-research-directions']
tags: ['scaling-laws', 'compute-optimality', 'adaptive-training', 'neural-scaling']
venue: "ICML 2024"
tldr: "Analyzes compute-optimal strategies for adaptive model training under neural scaling law frameworks."
---

# Navigating Scaling Laws: Compute Optimality in Adaptive Model Training

**Source**: [https://proceedings.mlr.press/v235/anagnostidis24a.html](https://proceedings.mlr.press/v235/anagnostidis24a.html)

**TLDR**: Analyzes compute-optimal strategies for adaptive model training under neural scaling law frameworks.

## Abstract

In recent years, the state-of-the-art in deep learning has been dominated by very large models that have been pre-trained on vast amounts of data. The paradigm is very simple: investing more computational resources (optimally) leads to better performance, and even predictably so; neural scaling laws have been derived that accurately forecast the performance of a network for a desired level of compute. This leads to the notion of a ’compute-optimal’ model, i.e. a model that allocates a given level of compute during training optimally to maximize performance. In this work, we extend the concept of optimality by allowing for an ’adaptive’ model, i.e. a model that can change its shape during training. By doing so, we can design adaptive models that optimally traverse between the underlying scaling laws and outpace their ‘static’ counterparts, leading to a significant reduction in the required compute to reach a given target performance. We show that our approach generalizes across modalities and different shape parameters.