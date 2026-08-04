---
title: "Privacy-Preserving Data Release Leveraging Optimal Transport and Particle Gradient Descent"
source: "https://proceedings.mlr.press/v235/donhauser24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/donhauser24a/donhauser24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'generative-models-and-variational-inference']
tags: ['differential-privacy', 'data-synthesis', 'optimal-transport', 'particle-gradient-descent']
venue: "ICML 2024"
tldr: "A differentially private tabular data synthesis method using optimal transport and particle gradient descent to generate high-fidelity private datasets."
---

# Privacy-Preserving Data Release Leveraging Optimal Transport and Particle Gradient Descent

**Source**: [https://proceedings.mlr.press/v235/donhauser24a.html](https://proceedings.mlr.press/v235/donhauser24a.html)

**TLDR**: A differentially private tabular data synthesis method using optimal transport and particle gradient descent to generate high-fidelity private datasets.

## Abstract

We present a novel approach for differentially private data synthesis of protected tabular datasets, a relevant task in highly sensitive domains such as healthcare and government. Current state-of-the-art methods predominantly use marginal-based approaches, where a dataset is generated from private estimates of the marginals. In this paper, we introduce PrivPGD, a new generation method for marginal-based private data synthesis, leveraging tools from optimal transport and particle gradient descent. Our algorithm outperforms existing methods on a large range of datasets while being highly scalable and offering the flexibility to incorporate additional domain-specific constraints.