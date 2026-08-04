---
title: "Sequence Compression Speeds Up Credit Assignment in Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/ramesh24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ramesh24b/ramesh24b.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['credit-assignment', 'reinforcement-learning', 'temporal-difference', 'sequence-compression', 'Monte-Carlo']
venue: "ICML 2024"
tldr: "Sequence compression is proposed to speed up credit assignment in RL by reducing the effective horizon while controlling variance in TD targets."
---

# Sequence Compression Speeds Up Credit Assignment in Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/ramesh24b.html](https://proceedings.mlr.press/v235/ramesh24b.html)

**TLDR**: Sequence compression is proposed to speed up credit assignment in RL by reducing the effective horizon while controlling variance in TD targets.

## Abstract

Temporal credit assignment in reinforcement learning is challenging due to delayed and stochastic outcomes. Monte Carlo targets can bridge long delays between action and consequence but lead to high-variance targets due to stochasticity. Temporal difference (TD) learning uses bootstrapping to overcome variance but introduces a bias that can only be corrected through many iterations. TD($\lambda$) provides a mechanism to navigate this bias-variance tradeoff smoothly. Appropriately selecting $\lambda$ can significantly improve performance. Here, we propose Chunked-TD, which uses predicted probabilities of transitions from a model for computing $\lambda$-return targets. Unlike other model-based solutions to credit assignment, Chunked-TD is less vulnerable to model inaccuracies. Our approach is motivated by the principle of history compression and ‘chunks’ trajectories for conventional TD learning. Chunking with learned world models compresses near-deterministic regions of the environment-policy interaction to speed up credit assignment while still bootstrapping when necessary. We propose algorithms that can be implemented online and show that they solve some problems much faster than conventional TD($\lambda$).