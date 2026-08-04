---
title: "SF-DQN: Provable Knowledge Transfer using Successor Feature for Deep Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/zhang24q.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24q/zhang24q.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['successor-features', 'transfer-learning', 'reward-decomposition']
venue: "ICML 2024"
tldr: "Provably efficient knowledge transfer across tasks with different reward functions using successor feature decomposition in deep RL."
---

# SF-DQN: Provable Knowledge Transfer using Successor Feature for Deep Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/zhang24q.html](https://proceedings.mlr.press/v235/zhang24q.html)

**TLDR**: Provably efficient knowledge transfer across tasks with different reward functions using successor feature decomposition in deep RL.

## Abstract

This paper studies the transfer reinforcement learning (RL) problem where multiple RL problems have different reward functions but share the same underlying transition dynamics. In this setting, the Q-function of each RL problem (task) can be decomposed into a successor feature (SF) and a reward mapping: the former characterizes the transition dynamics, and the latter characterizes the task-specific reward function. This Q-function decomposition, coupled with a policy improvement operator known as generalized policy improvement (GPI), reduces the sample complexity of finding the optimal Q-function, and thus the SF & GPI framework exhibits promising empirical performance compared to traditional RL methods like Q-learning. However, its theoretical foundations remain largely unestablished, especially when learning the successor features using deep neural networks (SF-DQN). This paper studies the provable knowledge transfer using SFs-DQN in transfer RL problems. We establish the first convergence analysis with provable generalization guarantees for SF-DQN with GPI. The theory reveals that SF-DQN with GPI outperforms conventional RL approaches, such as deep Q-network, in terms of both faster convergence rate and better generalization. Numerical experiments on real and synthetic RL tasks support the superior performance of SF-DQN & GPI, aligning with our theoretical findings.