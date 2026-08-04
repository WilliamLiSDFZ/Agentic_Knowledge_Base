---
title: "Policy Evaluation for Variance in Average Reward Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/agrawal24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/agrawal24a/agrawal24a.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['average-reward-rl', 'variance-estimation', 'temporal-difference', 'policy-evaluation', 'risk']
venue: "ICML 2024"
tldr: "Designs a TD-type algorithm for variance policy evaluation under the average reward criterion for risk-sensitive RL."
---

# Policy Evaluation for Variance in Average Reward Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/agrawal24a.html](https://proceedings.mlr.press/v235/agrawal24a.html)

**TLDR**: Designs a TD-type algorithm for variance policy evaluation under the average reward criterion for risk-sensitive RL.

## Abstract

We consider an average reward reinforcement learning (RL) problem and work with asymptotic variance as a risk measure to model safety-critical applications. We design a temporal-difference (TD) type algorithm tailored for policy evaluation in this context. Our algorithm is based on linear stochastic approximation of an equivalent formulation of the asymptotic variance in terms of the solution of the Poisson equation. We consider both the tabular and linear function approximation settings, and establish $\tilde {O}(1/k)$ finite time convergence rate, where $k$ is the number of steps of the algorithm. Our work paves the way for developing actor-critic style algorithms for variance-constrained RL. To the best of our knowledge, our result provides the first sequential estimator for asymptotic variance of a Markov chain with provable finite sample guarantees, which is of independent interest.