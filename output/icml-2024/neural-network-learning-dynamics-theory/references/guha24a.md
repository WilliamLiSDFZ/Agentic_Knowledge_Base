---
title: "On the Diminishing Returns of Width for Continual Learning"
source: "https://proceedings.mlr.press/v235/guha24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/guha24a/guha24a.pdf"
categories: ['continual-learning-memory-plasticity', 'neural-network-learning-dynamics-theory']
tags: ['continual-learning', 'catastrophic-forgetting', 'network-width', 'diminishing-returns', 'overparameterization']
venue: "ICML 2024"
tldr: "Theoretically and empirically shows that increasing neural network width yields diminishing returns for mitigating catastrophic forgetting in continual learning."
---

# On the Diminishing Returns of Width for Continual Learning

**Source**: [https://proceedings.mlr.press/v235/guha24a.html](https://proceedings.mlr.press/v235/guha24a.html)

**TLDR**: Theoretically and empirically shows that increasing neural network width yields diminishing returns for mitigating catastrophic forgetting in continual learning.

## Abstract

While deep neural networks have demonstrated groundbreaking performance in various settings, these models often suffer from catastrophic forgetting when trained on new tasks in sequence. Several works have empirically demonstrated that increasing the width of a neural network leads to a decrease in catastrophic forgetting but have yet to characterize the exact relationship between width and continual learning. We design one of the first frameworks to analyze Continual Learning Theory and prove that width is directly related to forgetting in Feed-Forward Networks (FFN), demonstrating that the diminishing returns of increasing widths to reduce forgetting. We empirically verify our claims at widths hitherto unexplored in prior studies where the diminishing returns are clearly observed as predicted by our theory.