---
title: "Q-Star Meets Scalable Posterior Sampling: Bridging Theory and Practice via HyperAgent"
source: "https://proceedings.mlr.press/v235/li24by.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24by/li24by.pdf"
categories: ['online-learning-and-sequential-decision-making', 'bayesian-optimization-and-surrogate-methods']
tags: ['reinforcement-learning', 'posterior-sampling', 'hypermodel-exploration']
venue: "ICML 2024"
tldr: "Proposes HyperAgent, an RL algorithm using hypermodels for scalable posterior sampling approximation to enable efficient exploration."
---

# Q-Star Meets Scalable Posterior Sampling: Bridging Theory and Practice via HyperAgent

**Source**: [https://proceedings.mlr.press/v235/li24by.html](https://proceedings.mlr.press/v235/li24by.html)

**TLDR**: Proposes HyperAgent, an RL algorithm using hypermodels for scalable posterior sampling approximation to enable efficient exploration.

## Abstract

We propose HyperAgent, a reinforcement learning (RL) algorithm based on the hypermodel framework for exploration in RL. HyperAgent allows for the efficient incremental approximation of posteriors associated with an optimal action-value function ($Q^\star$) without the need for conjugacy and follows the greedy policies w.r.t. these approximate posterior samples. We demonstrate that HyperAgent offers robust performance in large-scale deep RL benchmarks. It can solve Deep Sea hard exploration problems with episodes that optimally scale with problem size and exhibits significant efficiency gains in the Atari suite. Implementing HyperAgent requires minimal code addition to well-established deep RL frameworks like DQN. We theoretically prove that, under tabular assumptions, HyperAgent achieves logarithmic per-step computational complexity while attaining sublinear regret, matching the best known randomized tabular RL algorithm.