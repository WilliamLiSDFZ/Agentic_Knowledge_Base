---
title: "Reward Shaping for Reinforcement Learning with An Assistant Reward Agent"
source: "https://proceedings.mlr.press/v235/ma24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24l/ma24l.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['reward-shaping', 'reinforcement-learning', 'sparse-rewards', 'dual-agent']
venue: "ICML 2024"
tldr: "A dual-agent reward shaping framework uses an assistant reward agent to provide dense informative rewards for the policy agent in sparse-reward settings."
---

# Reward Shaping for Reinforcement Learning with An Assistant Reward Agent

**Source**: [https://proceedings.mlr.press/v235/ma24l.html](https://proceedings.mlr.press/v235/ma24l.html)

**TLDR**: A dual-agent reward shaping framework uses an assistant reward agent to provide dense informative rewards for the policy agent in sparse-reward settings.

## Abstract

Reward shaping is a promising approach to tackle the sparse-reward challenge of reinforcement learning by reconstructing more informative and dense rewards. This paper introduces a novel dual-agent reward shaping framework, composed of two synergistic agents: a policy agent to learn the optimal behavior and a reward agent to generate auxiliary reward signals. The proposed method operates as a self-learning approach, without reliance on expert knowledge or hand-crafted functions. By restructuring the rewards to capture future-oriented information, our framework effectively enhances the sample efficiency and convergence stability. Furthermore, the auxiliary reward signals facilitate the exploration of the environment in the early stage and the exploitation of the policy agent in the late stage, achieving a self-adaptive balance. We evaluate our framework on continuous control tasks with sparse and delayed rewards, demonstrating its robustness and superiority over existing methods.