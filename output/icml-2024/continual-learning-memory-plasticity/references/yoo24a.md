---
title: "Layerwise Proximal Replay: A Proximal Point Method for Online Continual Learning"
source: "https://proceedings.mlr.press/v235/yoo24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yoo24a/yoo24a.pdf"
categories: ['continual-learning-memory-plasticity']
tags: ['continual-learning', 'experience-replay', 'proximal-point', 'catastrophic-forgetting']
venue: "ICML 2024"
tldr: "Layerwise proximal replay is proposed as a proximal point method to mitigate catastrophic forgetting in online continual learning."
---

# Layerwise Proximal Replay: A Proximal Point Method for Online Continual Learning

**Source**: [https://proceedings.mlr.press/v235/yoo24a.html](https://proceedings.mlr.press/v235/yoo24a.html)

**TLDR**: Layerwise proximal replay is proposed as a proximal point method to mitigate catastrophic forgetting in online continual learning.

## Abstract

In online continual learning, a neural network incrementally learns from a non-i.i.d. data stream. Nearly all online continual learning methods employ experience replay to simultaneously prevent catastrophic forgetting and underfitting on past data. Our work demonstrates a limitation of this approach: neural networks trained with experience replay tend to have unstable optimization trajectories, impeding their overall accuracy. Surprisingly, these instabilities persist even when the replay buffer stores all previous training examples, suggesting that this issue is orthogonal to catastrophic forgetting. We minimize these instabilities through a simple modification of the optimization geometry. Our solution, Layerwise Proximal Replay (LPR), balances learning from new and replay data while only allowing for gradual changes in the hidden activation of past data. We demonstrate that LPR consistently improves replay-based online continual learning across multiple problem settings, regardless of the amount of available replay memory.