---
title: "Model-based Reinforcement Learning for Confounded POMDPs"
source: "https://proceedings.mlr.press/v235/hong24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hong24d/hong24d.pdf"
categories: ['online-learning-and-sequential-decision-making', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['offline-rl', 'pomdp', 'confounding', 'function-approximation', 'model-based']
venue: "ICML 2024"
tldr: "Proposes a provably efficient model-based offline RL algorithm for confounded POMDPs using general function approximations with partial data coverage."
---

# Model-based Reinforcement Learning for Confounded POMDPs

**Source**: [https://proceedings.mlr.press/v235/hong24d.html](https://proceedings.mlr.press/v235/hong24d.html)

**TLDR**: Proposes a provably efficient model-based offline RL algorithm for confounded POMDPs using general function approximations with partial data coverage.

## Abstract

We propose a model-based offline reinforcement learning (RL) algorithm for confounded partially observable Markov decision processes (POMDPs) under general function approximations and show it is provably efficient under some technical conditions such as the partial coverage imposed on the offline data distribution. Specifically, we first establish a novel model-based identification result for learning the effect of any action on the reward and future transitions in the confounded POMDP. Using this identification result, we then design a nonparametric two-stage estimation procedure to construct an estimator for off-policy evaluation (OPE), which permits general function approximations. Finally, we learn the optimal policy by performing a conservative policy optimization within the confidence regions based on the proposed estimation procedure for OPE. Under some mild conditions, we establish a finite-sample upper bound on the suboptimality of the learned policy in finding the optimal one, which depends on the sample size and the length of horizons polynomially.