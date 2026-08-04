---
title: "More Benefits of Being Distributional: Second-Order Bounds for Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/wang24ba.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24ba/wang24ba.pdf"
categories: ['online-learning-and-sequential-decision-making', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['distributional-RL', 'second-order-bounds', 'online-offline-RL', 'function-approximation']
venue: "ICML 2024"
tldr: "Distributional RL is proven to yield tighter second-order instance-dependent bounds in both online and offline reinforcement learning settings."
---

# More Benefits of Being Distributional: Second-Order Bounds for Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/wang24ba.html](https://proceedings.mlr.press/v235/wang24ba.html)

**TLDR**: Distributional RL is proven to yield tighter second-order instance-dependent bounds in both online and offline reinforcement learning settings.

## Abstract

In this paper, we prove that Distributional Reinforcement Learning (DistRL), which learns the return distribution, can obtain second-order bounds in both online and offline RL in general settings with function approximation. Second-order bounds are instance-dependent bounds that scale with the variance of return, which we prove are tighter than the previously known small-loss bounds of distributional RL. To the best of our knowledge, our results are the first second-order bounds for low-rank MDPs and for offline RL. When specializing to contextual bandits (one-step RL problem), we show that a distributional learning based optimism algorithm achieves a second-order worst-case regret bound, and a second-order gap dependent bound, simultaneously. We also empirically demonstrate the benefit of DistRL in contextual bandits on real-world datasets. We highlight that our analysis with DistRL is relatively simple, follows the general framework of optimism in the face of uncertainty and does not require weighted regression. Our results suggest that DistRL is a promising framework for obtaining second-order bounds in general RL settings, thus further reinforcing the benefits of DistRL.