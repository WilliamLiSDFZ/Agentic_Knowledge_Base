---
title: "Constrained Reinforcement Learning Under Model Mismatch"
source: "https://proceedings.mlr.press/v235/sun24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sun24d/sun24d.pdf"
categories: ['multi-agent-mdp-structure-and-dependencies', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['constrained-RL', 'model-mismatch', 'robustness', 'safe-RL', 'sim-to-real']
venue: "ICML 2024"
tldr: "A robust constrained RL framework is proposed to maintain constraint satisfaction under model mismatch between training and deployment environments."
---

# Constrained Reinforcement Learning Under Model Mismatch

**Source**: [https://proceedings.mlr.press/v235/sun24d.html](https://proceedings.mlr.press/v235/sun24d.html)

**TLDR**: A robust constrained RL framework is proposed to maintain constraint satisfaction under model mismatch between training and deployment environments.

## Abstract

Existing studies on constrained reinforcement learning (RL) may obtain a well-performing policy in the training environment. However, when deployed in a real environment, it may easily violate constraints that were originally satisfied during training because there might be model mismatch between the training and real environments. To address this challenge, we formulate the problem as constrained RL under model uncertainty, where the goal is to learn a policy that optimizes the reward and at the same time satisfies the constraint under model mismatch. We develop a Robust Constrained Policy Optimization (RCPO) algorithm, which is the first algorithm that applies to large/continuous state space and has theoretical guarantees on worst-case reward improvement and constraint violation at each iteration during the training. We show the effectiveness of our algorithm on a set of RL tasks with constraints.