---
title: "Langevin Policy for Safe Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/lei24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lei24a/lei24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['safe-reinforcement-learning', 'Langevin-dynamics', 'sampling', 'constrained-policy', 'safety']
venue: "ICML 2024"
tldr: "Proposes a Langevin-based sampling approach to safe reinforcement learning, demonstrating that sampling methods can achieve desirable performance under safety constraints."
---

# Langevin Policy for Safe Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/lei24a.html](https://proceedings.mlr.press/v235/lei24a.html)

**TLDR**: Proposes a Langevin-based sampling approach to safe reinforcement learning, demonstrating that sampling methods can achieve desirable performance under safety constraints.

## Abstract

Optimization and sampling based algorithms are two branches of methods in machine learning, while existing safe reinforcement learning (RL) algorithms are mainly based on optimization, it is still unclear whether sampling based methods can lead to desirable performance with safe policy. This paper formulates the Langevin policy for safe RL, and proposes Langevin Actor-Critic (LAC) to accelerate the process of policy inference. Concretely, instead of parametric policy, the proposed Langevin policy provides a stochastic process that directly infers actions, which is the numerical solver to the Langevin dynamic of actions on the continuous time. Furthermore, to make Langevin policy practical on RL tasks, the proposed LAC accumulates the transitions induced by Langevin policy and reproduces them with a generator. Finally, extensive empirical results show the effectiveness and superiority of LAC on the MuJoCo-based and Safety Gym tasks.