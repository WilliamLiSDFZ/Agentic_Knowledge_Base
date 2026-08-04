---
title: "Towards Global Optimality for Practical Average Reward Reinforcement Learning without Mixing Time Oracles"
source: "https://proceedings.mlr.press/v235/patel24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/patel24b/patel24b.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['average-reward-RL', 'policy-gradient', 'global-convergence', 'mixing-time']
venue: "ICML 2024"
tldr: "Develops a globally convergent policy gradient method for average-reward RL that does not require oracle knowledge of mixing time."
---

# Towards Global Optimality for Practical Average Reward Reinforcement Learning without Mixing Time Oracles

**Source**: [https://proceedings.mlr.press/v235/patel24b.html](https://proceedings.mlr.press/v235/patel24b.html)

**TLDR**: Develops a globally convergent policy gradient method for average-reward RL that does not require oracle knowledge of mixing time.

## Abstract

In the context of average-reward reinforcement learning, the requirement for oracle knowledge of the mixing time, a measure of the duration a Markov chain under a fixed policy needs to achieve its stationary distribution, poses a significant challenge for the global convergence of policy gradient methods. This requirement is particularly problematic due to the difficulty and expense of estimating mixing time in environments with large state spaces, leading to the necessity of impractically long trajectories for effective gradient estimation in practical applications. To address this limitation, we consider the Multi-level Actor-Critic (MAC) framework, which incorporates a Multi-level Monte-Carlo (MLMC) gradient estimator. With our approach, we effectively alleviate the dependency on mixing time knowledge, a first for average-reward MDPs global convergence. Furthermore, our approach exhibits the tightest available dependence of $\mathcal{O}(\sqrt{\tau_{mix}})$ known from prior work. With a 2D grid world goal-reaching navigation experiment, we demonstrate that MAC outperforms the existing state-of-the-art policy gradient-based method for average reward settings.