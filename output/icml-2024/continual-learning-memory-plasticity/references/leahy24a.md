---
title: "Run-Time Task Composition with Safety Semantics"
source: "https://proceedings.mlr.press/v235/leahy24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/leahy24a/leahy24a.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics', 'continual-learning-memory-plasticity']
tags: ['task-composition', 'Boolean-composition', 'reinforcement-learning', 'safety-semantics']
venue: "ICML 2024"
tldr: "A framework for Boolean composition of learned RL tasks with safety semantics enabling scalable run-time task combination."
---

# Run-Time Task Composition with Safety Semantics

**Source**: [https://proceedings.mlr.press/v235/leahy24a.html](https://proceedings.mlr.press/v235/leahy24a.html)

**TLDR**: A framework for Boolean composition of learned RL tasks with safety semantics enabling scalable run-time task combination.

## Abstract

Compositionality is a critical aspect of scalable system design. Here, we focus on Boolean composition of learned tasks as opposed to functional or sequential composition. Existing Boolean composition for Reinforcement Learning focuses on reaching a satisfying absorbing state in environments with discrete action spaces, but does not support composable safety (i.e., avoidance) constraints. We provide three contributions: i) introduce two distinct notions of compositional safety semantics; ii) show how to enforce either safety semantics, prove correctness, and analyze the trade-offs between the two safety notions; and iii) extend Boolean composition from discrete action spaces to continuous action spaces. We demonstrate these techniques using modified versions of value iteration in a grid world, Deep Q-Network (DQN) in a grid world with image observations, and Twin Delayed DDPG (TD3) in a continuous-observation and continuous-action Bullet physics environment