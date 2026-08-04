---
title: "To the Max: Reinventing Reward in Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/veviurko24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/veviurko24a/veviurko24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['reinforcement-learning', 'reward-shaping', 'max-reward', 'policy-optimization', 'learning-efficiency']
venue: "ICML 2024"
tldr: "Proposes reinventing the reward function in reinforcement learning using a max-based formulation to improve learning performance and avoid suboptimal behaviors."
---

# To the Max: Reinventing Reward in Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/veviurko24a.html](https://proceedings.mlr.press/v235/veviurko24a.html)

**TLDR**: Proposes reinventing the reward function in reinforcement learning using a max-based formulation to improve learning performance and avoid suboptimal behaviors.

## Abstract

In reinforcement learning (RL), different reward functions can define the same optimal policy but result in drastically different learning performance. For some, the agent gets stuck with a suboptimal behavior, and for others, it solves the task efficiently. Choosing a good reward function is hence an extremely important yet challenging problem. In this paper, we explore an alternative approach for using rewards for learning. We introduce max-reward RL, where an agent optimizes the maximum rather than the cumulative reward. Unlike earlier works, our approach works for deterministic and stochastic environments and can be easily combined with state-of-the-art RL algorithms. In the experiments, we study the performance of max-reward RL algorithms in two goal-reaching environments from Gymnasium-Robotics and demonstrate its benefits over standard RL. The code is available at https://github.com/veviurko/To-the-Max.