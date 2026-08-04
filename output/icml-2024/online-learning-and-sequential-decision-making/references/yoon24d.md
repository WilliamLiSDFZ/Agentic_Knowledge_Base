---
title: "Breadth-First Exploration on Adaptive Grid for Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/yoon24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yoon24d/yoon24d.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['reinforcement-learning', 'goal-conditioned', 'graph-planner', 'adaptive-grid']
venue: "ICML 2024"
tldr: "A breadth-first exploration strategy on an adaptive grid is proposed to improve goal-conditioned reinforcement learning planning."
---

# Breadth-First Exploration on Adaptive Grid for Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/yoon24d.html](https://proceedings.mlr.press/v235/yoon24d.html)

**TLDR**: A breadth-first exploration strategy on an adaptive grid is proposed to improve goal-conditioned reinforcement learning planning.

## Abstract

Graph-based planners have gained significant attention for goal-conditioned reinforcement learning (RL), where they construct a graph consisting of confident transitions between subgoals as edges and run shortest path algorithms to exploit the confident edges. Meanwhile, identifying and avoiding unattainable transitions are also crucial yet overlooked by the previous graph-based planners, leading to wasting an excessive number of attempts at unattainable subgoals. To address this oversight, we propose a graph construction method that efficiently manages all the achieved and unattained subgoals on a grid graph adaptively discretizing the goal space. This enables a breadth-first exploration strategy, grounded in the local adaptive grid refinement, that prioritizes broad probing of subgoals on a coarse grid over meticulous one on a dense grid. We conducted a theoretical analysis and demonstrated the effectiveness of our approach through empirical evidence, showing that only BEAG succeeds in complex environments under the proposed fixed-goal setting.