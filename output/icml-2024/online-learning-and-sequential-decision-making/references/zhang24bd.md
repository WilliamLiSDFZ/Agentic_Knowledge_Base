---
title: "Provable Representation with Efficient Planning for Partially Observable Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/zhang24bd.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24bd/zhang24bd.pdf"
categories: ['online-learning-and-sequential-decision-making', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['POMDP', 'partial-observability', 'representation-learning', 'reinforcement-learning', 'planning']
venue: "ICML 2024"
tldr: "Provides provable representation learning with efficient planning algorithms for partially observable reinforcement learning."
---

# Provable Representation with Efficient Planning for Partially Observable Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/zhang24bd.html](https://proceedings.mlr.press/v235/zhang24bd.html)

**TLDR**: Provides provable representation learning with efficient planning algorithms for partially observable reinforcement learning.

## Abstract

In most real-world reinforcement learning applications, state information is only partially observable, which breaks the Markov decision process assumption and leads to inferior performance for algorithms that conflate observations with state. Partially Observable Markov Decision Processes (POMDPs), on the other hand, provide a general framework that allows for partial observability to be accounted for in learning, exploration and planning, but presents significant computational and statistical challenges. To address these difficulties, we develop a representation-based perspective that leads to a coherent framework and tractable algorithmic approach for practical reinforcement learning from partial observations. We provide a theoretical analysis for justifying the statistical efficiency of the proposed algorithm, and also empirically demonstrate the proposed algorithm can surpass state-of-the-art performance with partial observations across various benchmarks, advancing reliable reinforcement learning towards more practical applications.