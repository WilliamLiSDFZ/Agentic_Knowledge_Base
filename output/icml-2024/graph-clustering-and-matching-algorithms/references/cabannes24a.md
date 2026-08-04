---
title: "Learning Associative Memories with Gradient Descent"
source: "https://proceedings.mlr.press/v235/cabannes24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cabannes24a/cabannes24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'graph-clustering-and-matching-algorithms']
tags: ['associative-memory', 'training-dynamics', 'token-embeddings', 'outer-products']
venue: "ICML 2024"
tldr: "Analyzes training dynamics of associative memory modules storing outer products of token embeddings via a particle interaction framework."
---

# Learning Associative Memories with Gradient Descent

**Source**: [https://proceedings.mlr.press/v235/cabannes24a.html](https://proceedings.mlr.press/v235/cabannes24a.html)

**TLDR**: Analyzes training dynamics of associative memory modules storing outer products of token embeddings via a particle interaction framework.

## Abstract

This work focuses on the training dynamics of one associative memory module storing outer products of token embeddings. We reduce this problem to the study of a system of particles, which interact according to properties of the data distribution and correlations between embeddings. Through theory and experiments, we provide several insights. In overparameterized regimes, we obtain logarithmic growth of the “classification margins.” Yet, we show that imbalance in token frequencies and memory interferences due to correlated embeddings lead to oscillatory transitory regimes. The oscillations are more pronounced with large step sizes, which can create benign loss spikes, although these learning rates speed up the dynamics and accelerate the asymptotic convergence. We also find that underparameterized regimes lead to suboptimal memorization schemes. Finally, we assess the validity of our findings on small Transformer models.