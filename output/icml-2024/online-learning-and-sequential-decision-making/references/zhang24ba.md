---
title: "Online Resource Allocation with Non-Stationary Customers"
source: "https://proceedings.mlr.press/v235/zhang24ba.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ba/zhang24ba.pdf"
categories: ['online-learning-and-sequential-decision-making', 'online-learning-matching-market-algorithms']
tags: ['online-resource-allocation', 'non-stationary', 'bandit', 'click-through-rate', 'competitive-ratio']
venue: "ICML 2024"
tldr: "Presents a novel algorithm for online resource allocation with non-stationary customer arrivals and unknown click-through rates."
---

# Online Resource Allocation with Non-Stationary Customers

**Source**: [https://proceedings.mlr.press/v235/zhang24ba.html](https://proceedings.mlr.press/v235/zhang24ba.html)

**TLDR**: Presents a novel algorithm for online resource allocation with non-stationary customer arrivals and unknown click-through rates.

## Abstract

We propose a novel algorithm for online resource allocation with non-stationary customer arrivals and unknown click-through rates. We assume multiple types of customers arriving in a nonstationary stochastic fashion, with unknown arrival rates in each period. Additionally, customers’ click-through rates are assumed to be unknown and only learnable online. By leveraging results from the stochastic contextual bandit with knapsack and online matching with adversarial arrivals, we develop an online scheme to allocate the resources to nonstationary customers. We prove that under mild conditions, our scheme achieves a “best-of-both-world” result: the scheme has a sublinear regret when the customer arrivals are near-stationary, and enjoys an optimal competitive ratio under general (non-stationary) customer arrival distributions. Finally, we conduct extensive numerical experiments to show our approach generates near-optimal revenues for all different customer scenarios.