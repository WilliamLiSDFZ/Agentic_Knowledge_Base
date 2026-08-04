---
title: "Neural-Kernel Conditional Mean Embeddings"
source: "https://proceedings.mlr.press/v235/shimizu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shimizu24a/shimizu24a.pdf"
categories: ['generative-models-and-variational-inference', 'neural-network-learning-dynamics-theory']
tags: ['kernel-methods', 'conditional-mean-embeddings', 'deep-learning']
venue: "ICML 2024"
tldr: "Proposes a method combining deep learning with kernel conditional mean embeddings to improve scalability and expressiveness for representing conditional distributions."
---

# Neural-Kernel Conditional Mean Embeddings

**Source**: [https://proceedings.mlr.press/v235/shimizu24a.html](https://proceedings.mlr.press/v235/shimizu24a.html)

**TLDR**: Proposes a method combining deep learning with kernel conditional mean embeddings to improve scalability and expressiveness for representing conditional distributions.

## Abstract

Kernel conditional mean embeddings (CMEs) offer a powerful framework for representing conditional distributions, but they often face scalability and expressiveness challenges. In this work, we propose a new method that effectively combines the strengths of deep learning with CMEs in order to address these challenges. Specifically, our approach leverages the end-to-end neural network (NN) optimization framework using a kernel-based objective. This design circumvents the computationally expensive Gram matrix inversion required by current CME methods. To further enhance performance, we provide efficient strategies to optimize the remaining kernel hyperparameters. In conditional density estimation tasks, our NN-CME hybrid achieves competitive performance and often surpasses existing deep learning-based methods. Lastly, we showcase its remarkable versatility by seamlessly integrating it into reinforcement learning (RL) contexts. Building on Q-learning, our approach naturally leads to a new variant of distributional RL methods, which demonstrates consistent effectiveness across different environments.