---
title: "Q-value Regularized Transformer for Offline Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/hu24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hu24c/hu24c.pdf"
categories: ['online-learning-and-sequential-decision-making', 'transformer-architecture-efficiency-and-scaling']
tags: ['offline-rl', 'transformer', 'q-value-regularization', 'sequence-modeling', 'decision-transformer']
venue: "ICML 2024"
tldr: "Proposes Q-value regularization for conditional sequence modeling transformers to improve trajectory stitching in offline reinforcement learning."
---

# Q-value Regularized Transformer for Offline Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/hu24c.html](https://proceedings.mlr.press/v235/hu24c.html)

**TLDR**: Proposes Q-value regularization for conditional sequence modeling transformers to improve trajectory stitching in offline reinforcement learning.

## Abstract

Recent advancements in offline reinforcement learning (RL) have underscored the capabilities of Conditional Sequence Modeling (CSM), a paradigm that learns the action distribution based on history trajectory and target returns for each state. However, these methods often struggle with stitching together optimal trajectories from sub-optimal ones due to the inconsistency between the sampled returns within individual trajectories and the optimal returns across multiple trajectories. Fortunately, Dynamic Programming (DP) methods offer a solution by leveraging a value function to approximate optimal future returns for each state, while these techniques are prone to unstable learning behaviors, particularly in long-horizon and sparse-reward scenarios. Building upon these insights, we propose the Q-value regularized Transformer (QT), which combines the trajectory modeling ability of the Transformer with the predictability of optimal future returns from DP methods. QT learns an action-value function and integrates a term maximizing action-values into the training loss of CSM, which aims to seek optimal actions that align closely with the behavior policy. Empirical evaluations on D4RL benchmark datasets demonstrate the superiority of QT over traditional DP and CSM methods, highlighting the potential of QT to enhance the state-of-the-art in offline RL.