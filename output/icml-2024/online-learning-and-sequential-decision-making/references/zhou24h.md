---
title: "Finite-Time Convergence and Sample Complexity of Actor-Critic Multi-Objective Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/zhou24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhou24h/zhou24h.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['multi-objective-reinforcement-learning', 'actor-critic', 'finite-time-convergence']
venue: "ICML 2024"
tldr: "Proposes an actor-critic algorithm for multi-objective RL with provable finite-time convergence guarantees and sample complexity analysis."
---

# Finite-Time Convergence and Sample Complexity of Actor-Critic Multi-Objective Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/zhou24h.html](https://proceedings.mlr.press/v235/zhou24h.html)

**TLDR**: Proposes an actor-critic algorithm for multi-objective RL with provable finite-time convergence guarantees and sample complexity analysis.

## Abstract

Reinforcement learning with multiple, potentially conflicting objectives is pervasive in real-world applications, while this problem remains theoretically under-explored. This paper tackles the multi-objective reinforcement learning (MORL) problem and introduces an innovative actor-critic algorithm named MOAC which finds a policy by iteratively making trade-offs among conflicting reward signals. Notably, we provide the first analysis of finite-time Pareto-stationary convergence and corresponding sample complexity in both discounted and average reward settings. Our approach has two salient features: (a) MOAC mitigates the cumulative estimation bias resulting from finding an optimal common gradient descent direction out of stochastic samples. This enables provable convergence rate and sample complexity guarantees independent of the number of objectives; (b) With proper momentum coefficient, MOAC initializes the weights of individual policy gradients using samples from the environment, instead of manual initialization. This enhances the practicality and robustness of our algorithm. Finally, experiments conducted on a real-world dataset validate the effectiveness of our proposed method.