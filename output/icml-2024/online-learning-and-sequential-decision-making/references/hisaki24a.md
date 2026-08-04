---
title: "RVI-SAC: Average Reward Off-Policy Deep Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/hisaki24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hisaki24a/hisaki24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['average-reward', 'off-policy', 'deep-reinforcement-learning', 'RVI']
venue: "ICML 2024"
tldr: "Proposes RVI-SAC, an off-policy deep RL algorithm using the average reward criterion better suited for continuous control tasks."
---

# RVI-SAC: Average Reward Off-Policy Deep Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/hisaki24a.html](https://proceedings.mlr.press/v235/hisaki24a.html)

**TLDR**: Proposes RVI-SAC, an off-policy deep RL algorithm using the average reward criterion better suited for continuous control tasks.

## Abstract

In this paper, we propose an off-policy deep reinforcement learning (DRL) method utilizing the average reward criterion. While most existing DRL methods employ the discounted reward criterion, this can potentially lead to a discrepancy between the training objective and performance metrics in continuing tasks, making the average reward criterion a recommended alternative. We introduce RVI-SAC, an extension of the state-of-the-art off-policy DRL method, Soft Actor-Critic (SAC), to the average reward criterion. Our proposal consists of (1) Critic updates based on RVI Q-learning, (2) Actor updates introduced by the average reward soft policy improvement theorem, and (3) automatic adjustment of Reset Cost enabling the average reward reinforcement learning to be applied to tasks with termination. We apply our method to the Gymnasium’s Mujoco tasks, a subset of locomotion tasks, and demonstrate that RVI-SAC shows competitive performance compared to existing methods.