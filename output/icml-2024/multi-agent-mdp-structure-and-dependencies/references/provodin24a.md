---
title: "Efficient Exploration in Average-Reward Constrained Reinforcement Learning: Achieving Near-Optimal Regret With Posterior Sampling"
source: "https://proceedings.mlr.press/v235/provodin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/provodin24a/provodin24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['constrained-MDP', 'posterior-sampling', 'regret-bounds']
venue: "ICML 2024"
tldr: "A posterior sampling algorithm for constrained MDPs achieving near-optimal regret in the infinite-horizon undiscounted setting."
---

# Efficient Exploration in Average-Reward Constrained Reinforcement Learning: Achieving Near-Optimal Regret With Posterior Sampling

**Source**: [https://proceedings.mlr.press/v235/provodin24a.html](https://proceedings.mlr.press/v235/provodin24a.html)

**TLDR**: A posterior sampling algorithm for constrained MDPs achieving near-optimal regret in the infinite-horizon undiscounted setting.

## Abstract

We present a new algorithm based on posterior sampling for learning in Constrained Markov Decision Processes (CMDP) in the infinite-horizon undiscounted setting. The algorithm achieves near-optimal regret bounds while being advantageous empirically compared to the existing algorithms. Our main theoretical result is a Bayesian regret bound for each cost component of $\tilde{O} (DS\sqrt{AT})$ for any communicating CMDP with $S$ states, $A$ actions, and diameter $D$. This regret bound matches the lower bound in order of time horizon $T$ and is the best-known regret bound for communicating CMDPs achieved by a computationally tractable algorithm. Empirical results show that our posterior sampling algorithm outperforms the existing algorithms for constrained reinforcement learning.