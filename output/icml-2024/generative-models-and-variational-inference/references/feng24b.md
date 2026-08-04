---
title: "Resisting Stochastic Risks in Diffusion Planners with the Trajectory Aggregation Tree"
source: "https://proceedings.mlr.press/v235/feng24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/feng24b/feng24b.pdf"
categories: ['generative-models-and-variational-inference']
tags: ['diffusion-planners', 'trajectory-aggregation', 'stochastic-risk']
venue: "ICML 2024"
tldr: "Introduces a trajectory aggregation tree to mitigate stochastic risks in diffusion-based planning for long-horizon tasks."
---

# Resisting Stochastic Risks in Diffusion Planners with the Trajectory Aggregation Tree

**Source**: [https://proceedings.mlr.press/v235/feng24b.html](https://proceedings.mlr.press/v235/feng24b.html)

**TLDR**: Introduces a trajectory aggregation tree to mitigate stochastic risks in diffusion-based planning for long-horizon tasks.

## Abstract

Diffusion planners have shown promise in handling long-horizon and sparse-reward tasks due to the non-autoregressive plan generation. However, their inherent stochastic risk of generating infeasible trajectories presents significant challenges to their reliability and stability. We introduce a novel approach, the Trajectory Aggregation Tree (TAT), to address this issue in diffusion planners. Compared to prior methods that rely solely on raw trajectory predictions, TAT aggregates information from both historical and current trajectories, forming a dynamic tree-like structure. Each trajectory is conceptualized as a branch and individual states as nodes. As the structure evolves with the integration of new trajectories, unreliable states are marginalized, and the most impactful nodes are prioritized for decision-making. TAT can be deployed without modifying the original training and sampling pipelines of diffusion planners, making it a training-free, ready-to-deploy solution. We provide both theoretical analysis and empirical evidence to support TAT’s effectiveness. Our results highlight its remarkable ability to resist the risk from unreliable trajectories, guarantee the performance boosting of diffusion planners in 100% of tasks, and exhibit an appreciable tolerance margin for sample quality, thereby enabling planning with a more than $3\times$ acceleration.