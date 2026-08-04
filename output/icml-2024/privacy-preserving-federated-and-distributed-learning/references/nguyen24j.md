---
title: "Differentially private exact recovery for stochastic block models"
source: "https://proceedings.mlr.press/v235/nguyen24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nguyen24j/nguyen24j.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'graph-based-community-structure-detection']
tags: ['differential-privacy', 'stochastic-block-model', 'community-detection']
venue: "ICML 2024"
tldr: "Derives differentially private algorithms for exact recovery in stochastic block models with matching information-theoretic thresholds."
---

# Differentially private exact recovery for stochastic block models

**Source**: [https://proceedings.mlr.press/v235/nguyen24j.html](https://proceedings.mlr.press/v235/nguyen24j.html)

**TLDR**: Derives differentially private algorithms for exact recovery in stochastic block models with matching information-theoretic thresholds.

## Abstract

Stochastic block models (SBMs) are a very commonly studied network model for community detection algorithms. In the standard form of an SBM, the $n$ vertices (or nodes) of a graph are generally divided into multiple pre-determined communities (or clusters). Connections between pairs of vertices are generated randomly and independently with pre-defined probabilities, which depend on the communities containing the two nodes. A fundamental problem in SBMs is the recovery of the community structure, and sharp information-theoretic bounds are known for recoverability for many versions of SBMs. Our focus here is the recoverability problem in SBMs when the network is private. Under the edge differential privacy model, we derive conditions for exact recoverability in three different versions of SBMs, namely Asymmetric SBM (when communities have non-uniform sizes), General Structure SBM (with outliers), and Censored SBM (with edge features). Our private algorithms have polynomial running time w.r.t. the input graph’s size, and match the recovery thresholds of the non-private setting when $\epsilon\rightarrow\infty$. In contrast, the previous best results for recoverability in SBMs only hold for the symmetric case (equal size communities), and run in quasi-polynomial time, or in polynomial time with recovery thresholds being tight up to some constants from the non-private settings.