---
title: "Transformers Provably Learn Sparse Token Selection While Fully-Connected Nets Cannot"
source: "https://proceedings.mlr.press/v235/wang24ca.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24ca/wang24ca.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'neural-network-learning-dynamics-theory']
tags: ['transformers', 'sparse-token-selection', 'expressivity', 'theoretical-analysis']
venue: "ICML 2024"
tldr: "Proves that transformers can provably learn sparse token selection tasks that fully-connected networks cannot, explaining a key architectural advantage."
---

# Transformers Provably Learn Sparse Token Selection While Fully-Connected Nets Cannot

**Source**: [https://proceedings.mlr.press/v235/wang24ca.html](https://proceedings.mlr.press/v235/wang24ca.html)

**TLDR**: Proves that transformers can provably learn sparse token selection tasks that fully-connected networks cannot, explaining a key architectural advantage.

## Abstract

The transformer architecture has prevailed in various deep learning settings due to its exceptional capabilities to select and compose structural information. Motivated by these capabilities, Sanford et al. (2023) proposed the sparse token selection task, in which transformers excel while fully-connected networks (FCNs) fail in the worst case. Building upon that, we strengthen the FCN lower bound to an average-case setting and establish an algorithmic separation of transformers over FCNs. Specifically, a one-layer transformer trained with gradient descent provably learns the sparse token selection task and, surprisingly, exhibits strong out-of-distribution length generalization. We provide empirical simulations to justify our theoretical findings.