---
title: "Global Reinforcement Learning : Beyond Linear and Convex Rewards via Submodular Semi-gradient Methods"
source: "https://proceedings.mlr.press/v235/de-santi24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/de-santi24b/de-santi24b.pdf"
categories: ['online-learning-and-sequential-decision-making', 'submodular-optimization-and-combinatorial-algorithms']
tags: ['reinforcement-learning', 'submodular-rewards', 'non-linear-objectives', 'semi-gradient', 'global-optimization']
venue: "ICML 2024"
tldr: "Extends reinforcement learning to submodular and non-linear reward objectives using submodular semi-gradient methods for global policy optimization."
---

# Global Reinforcement Learning : Beyond Linear and Convex Rewards via Submodular Semi-gradient Methods

**Source**: [https://proceedings.mlr.press/v235/de-santi24b.html](https://proceedings.mlr.press/v235/de-santi24b.html)

**TLDR**: Extends reinforcement learning to submodular and non-linear reward objectives using submodular semi-gradient methods for global policy optimization.

## Abstract

In classic Reinforcement Learning (RL), the agent maximizes an additive objective of the visited states, e.g., a value function. Unfortunately, objectives of this type cannot model many real-world applications such as experiment design, exploration, imitation learning, and risk-averse RL to name a few. This is due to the fact that additive objectives disregard interactions between states that are crucial for certain tasks. To tackle this problem, we introduce Global RL (GRL), where rewards are globally defined over trajectories instead of locally over states. Global rewards can capture negative interactions among states, e.g., in exploration, via submodularity, positive interactions, e.g., synergetic effects, via supermodularity, while mixed interactions via combinations of them. By exploiting ideas from submodular optimization, we propose a novel algorithmic scheme that converts any GRL problem to a sequence of classic RL problems and solves it efficiently with curvature-dependent approximation guarantees. We also provide hardness of approximation results and empirically demonstrate the effectiveness of our method on several GRL instances.