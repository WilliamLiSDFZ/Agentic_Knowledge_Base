---
title: "Encodings for Prediction-based Neural Architecture Search"
source: "https://proceedings.mlr.press/v235/akhauri24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/akhauri24a/akhauri24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'bayesian-optimization-and-surrogate-methods']
tags: ['neural-architecture-search', 'architecture-encodings', 'predictor-based-NAS']
venue: "ICML 2024"
tldr: "This paper studies and compares encoding methods for neural architectures used in predictor-based NAS to improve search efficiency."
---

# Encodings for Prediction-based Neural Architecture Search

**Source**: [https://proceedings.mlr.press/v235/akhauri24a.html](https://proceedings.mlr.press/v235/akhauri24a.html)

**TLDR**: This paper studies and compares encoding methods for neural architectures used in predictor-based NAS to improve search efficiency.

## Abstract

Predictor-based methods have substantially enhanced Neural Architecture Search (NAS) optimization. The efficacy of these predictors is largely influenced by the method of encoding neural network architectures. While traditional encodings used an adjacency matrix describing the graph structure of a neural network, novel encodings embrace a variety of approaches from unsupervised pretraining of latent representations to vectors of zero-cost proxies. In this paper, we categorize and investigate neural encodings from three main types: structural, learned, and score-based. Furthermore, we extend these encodings and introduce unified encodings, that extend NAS predictors to multiple search spaces. Our analysis draws from experiments conducted on over 1.5 million neural network architectures on NAS spaces such as NASBench-101 (NB101), NB201, NB301, Network Design Spaces (NDS), and TransNASBench-101. Building on our study, we present our predictor FLAN: Flow Attention for NAS. FLAN integrates critical insights on predictor design, transfer learning, and unified encodings to enable more than an order of magnitude cost reduction for training NAS accuracy predictors. Our implementation and encodings for all neural networks are open-sourced at https://github.com/abdelfattah-lab/flan_nas.