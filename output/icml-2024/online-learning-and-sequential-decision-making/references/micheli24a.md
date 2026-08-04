---
title: "Efficient World Models with Context-Aware Tokenization"
source: "https://proceedings.mlr.press/v235/micheli24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/micheli24a/micheli24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'transformer-architecture-efficiency-and-scaling']
tags: ['world-models', 'tokenization', 'model-based-reinforcement-learning']
venue: "ICML 2024"
tldr: "Proposes context-aware tokenization for transformer-based world models to improve scalability and efficiency in model-based reinforcement learning."
---

# Efficient World Models with Context-Aware Tokenization

**Source**: [https://proceedings.mlr.press/v235/micheli24a.html](https://proceedings.mlr.press/v235/micheli24a.html)

**TLDR**: Proposes context-aware tokenization for transformer-based world models to improve scalability and efficiency in model-based reinforcement learning.

## Abstract

Scaling up deep Reinforcement Learning (RL) methods presents a significant challenge. Following developments in generative modelling, model-based RL positions itself as a strong contender. Recent advances in sequence modelling have led to effective transformer-based world models, albeit at the price of heavy computations due to the long sequences of tokens required to accurately simulate environments. In this work, we propose $\Delta$-IRIS, a new agent with a world model architecture composed of a discrete autoencoder that encodes stochastic deltas between time steps and an autoregressive transformer that predicts future deltas by summarizing the current state of the world with continuous tokens. In the Crafter benchmark, $\Delta$-IRIS sets a new state of the art at multiple frame budgets, while being an order of magnitude faster to train than previous attention-based approaches. We release our code and models at https://github.com/vmicheli/delta-iris.