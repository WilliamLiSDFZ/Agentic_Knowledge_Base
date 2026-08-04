---
title: "Feasibility Consistent Representation Learning for Safe Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/cen24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cen24b/cen24b.pdf"
categories: ['online-learning-and-sequential-decision-making', 'neural-network-learning-dynamics-theory']
tags: ['safe-reinforcement-learning', 'feasibility', 'representation-learning', 'constraint-satisfaction']
venue: "ICML 2024"
tldr: "Introduces feasibility-consistent representation learning to better estimate safety constraints in safe reinforcement learning."
---

# Feasibility Consistent Representation Learning for Safe Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/cen24b.html](https://proceedings.mlr.press/v235/cen24b.html)

**TLDR**: Introduces feasibility-consistent representation learning to better estimate safety constraints in safe reinforcement learning.

## Abstract

In the field of safe reinforcement learning (RL), finding a balance between satisfying safety constraints and optimizing reward performance presents a significant challenge. A key obstacle in this endeavor is the estimation of safety constraints, which is typically more difficult than estimating a reward metric due to the sparse nature of the constraint signals. To address this issue, we introduce a novel framework named Feasibility Consistent Safe Reinforcement Learning (FCSRL). This framework combines representation learning with feasibility-oriented objectives to identify and extract safety-related information from the raw state for safe RL. Leveraging self-supervised learning techniques and a more learnable safety metric, our approach enhances the policy learning and constraint estimation. Empirical evaluations across a range of vector-state and image-based tasks demonstrate that our method is capable of learning a better safety-aware embedding and achieving superior performance than previous representation learning baselines.