---
title: "DMTG: One-Shot Differentiable Multi-Task Grouping"
source: "https://proceedings.mlr.press/v235/gao24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gao24h/gao24h.pdf"
categories: ['knowledge-distillation-methods-and-applications', 'optimization-algorithms-convergence-theory']
tags: ['multi-task-learning', 'task-grouping', 'differentiable-architecture-search', 'one-shot']
venue: "ICML 2024"
tldr: "DMTG enables one-shot differentiable multi-task grouping that jointly identifies optimal task groups and trains model weights simultaneously."
---

# DMTG: One-Shot Differentiable Multi-Task Grouping

**Source**: [https://proceedings.mlr.press/v235/gao24h.html](https://proceedings.mlr.press/v235/gao24h.html)

**TLDR**: DMTG enables one-shot differentiable multi-task grouping that jointly identifies optimal task groups and trains model weights simultaneously.

## Abstract

We aim to address Multi-Task Learning (MTL) with a large number of tasks by Multi-Task Grouping (MTG). Given $N$ tasks, we propose to simultaneously identify the best task groups from $2^N$ candidates and train the model weights simultaneously in one-shot, with the high-order task-affinity fully exploited. This is distinct from the pioneering methods which sequentially identify the groups and train the model weights, where the group identification often relies on heuristics. As a result, our method not only improves the training efficiency, but also mitigates the objective bias introduced by the sequential procedures that potentially leads to a suboptimal solution. Specifically, we formulate MTG as a fully differentiable pruning problem on an adaptive network architecture determined by an unknown Categorical distribution. To categorize $N$ tasks into $K$ groups (represented by $K$ encoder branches), we initially set up $KN$ task heads, where each branch connects to all $N$ task heads to exploit the high-order task-affinity. Then, we gradually prune the $KN$ heads down to $N$ by learning a relaxed differentiable Categorical distribution, ensuring that each task is exclusively and uniquely categorized into only one branch. Extensive experiments on CelebA and Taskonomy datasets with detailed ablations show the promising performance and efficiency of our method. The codes are available at https://github.com/ethanygao/DMTG.