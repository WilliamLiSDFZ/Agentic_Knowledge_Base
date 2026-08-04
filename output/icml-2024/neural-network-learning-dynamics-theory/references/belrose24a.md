---
title: "Neural Networks Learn Statistics of Increasing Complexity"
source: "https://proceedings.mlr.press/v235/belrose24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/belrose24a/belrose24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['distributional-simplicity-bias', 'neural-networks', 'maximum-entropy', 'low-order-statistics', 'learning-dynamics']
venue: "ICML 2024"
tldr: "Provides new evidence that neural networks learn low-order statistical moments first before progressing to higher-order correlations."
---

# Neural Networks Learn Statistics of Increasing Complexity

**Source**: [https://proceedings.mlr.press/v235/belrose24a.html](https://proceedings.mlr.press/v235/belrose24a.html)

**TLDR**: Provides new evidence that neural networks learn low-order statistical moments first before progressing to higher-order correlations.

## Abstract

The distributional simplicity bias (DSB) posits that neural networks learn low-order moments of the data distribution first, before moving on to higher-order correlations. In this work, we present compelling new evidence for the DSB by showing that networks automatically learn to perform well on maximum-entropy distributions whose low-order statistics match those of the training set early in training, then lose this ability later. We also extend the DSB to discrete domains by proving an equivalence between token $n$-gram frequencies and the moments of embedding vectors, and by finding empirical evidence for the bias in LLMs. Finally we use optimal transport methods to surgically edit the low-order statistics of one class to match those of another, and show that early-training networks treat the edited samples as if they were drawn from the target class. Code is available at https://github.com/EleutherAI/features-across-time.