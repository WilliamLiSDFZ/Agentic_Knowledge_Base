---
title: "Task-aware Orthogonal Sparse Network for Exploring Shared Knowledge in Continual Learning"
source: "https://proceedings.mlr.press/v235/hu24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hu24b/hu24b.pdf"
categories: ['continual-learning-memory-plasticity', 'neural-network-learning-dynamics-theory']
tags: ['continual-learning', 'catastrophic-forgetting', 'sparse-networks', 'lottery-ticket', 'orthogonality']
venue: "ICML 2024"
tldr: "Proposes a task-aware orthogonal sparse network that partitions parameters to preserve old task knowledge while learning new tasks in continual learning."
---

# Task-aware Orthogonal Sparse Network for Exploring Shared Knowledge in Continual Learning

**Source**: [https://proceedings.mlr.press/v235/hu24b.html](https://proceedings.mlr.press/v235/hu24b.html)

**TLDR**: Proposes a task-aware orthogonal sparse network that partitions parameters to preserve old task knowledge while learning new tasks in continual learning.

## Abstract

Continual learning (CL) aims to learn from sequentially arriving tasks without catastrophic forgetting (CF). By partitioning the network into two parts based on the Lottery Ticket Hypothesis—one for holding the knowledge of the old tasks while the other for learning the knowledge of the new task—the recent progress has achieved forget-free CL. Although addressing the CF issue well, such methods would encounter serious under-fitting in long-term CL, in which the learning process will continue for a long time and the number of new tasks involved will be much higher. To solve this problem, this paper partitions the network into three parts—with a new part for exploring the knowledge sharing between the old and new tasks. With the shared knowledge, this part of network can be learnt to simultaneously consolidate the old tasks and fit to the new task. To achieve this goal, we propose a task-aware Orthogonal Sparse Network (OSN), which contains shared knowledge induced network partition and sharpness-aware orthogonal sparse network learning. The former partitions the network to select shared parameters, while the latter guides the exploration of shared knowledge through shared parameters. Qualitative and quantitative analyses, show that the proposed OSN induces minimum to no interference with past tasks, i.e., approximately no forgetting, while greatly improves the model plasticity and capacity, and finally achieves the state-of-the-art performances.