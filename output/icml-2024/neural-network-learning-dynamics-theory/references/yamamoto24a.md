---
title: "Mean Field Langevin Actor-Critic: Faster Convergence and Global Optimality beyond Lazy Learning"
source: "https://proceedings.mlr.press/v235/yamamoto24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yamamoto24a/yamamoto24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'neural-network-learning-dynamics-theory']
tags: ['mean-field-theory', 'actor-critic', 'neural-network-optimization']
venue: "ICML 2024"
tldr: "Analyzes feature learning in over-parameterized neural actor-critic via mean-field Langevin dynamics, proving faster convergence and global optimality."
---

# Mean Field Langevin Actor-Critic: Faster Convergence and Global Optimality beyond Lazy Learning

**Source**: [https://proceedings.mlr.press/v235/yamamoto24a.html](https://proceedings.mlr.press/v235/yamamoto24a.html)

**TLDR**: Analyzes feature learning in over-parameterized neural actor-critic via mean-field Langevin dynamics, proving faster convergence and global optimality.

## Abstract

This work explores the feature learning capabilities of deep reinforcement learning algorithms in the pursuit of optimal policy determination. We particularly examine an over-parameterized neural actor-critic framework within the mean-field regime, where both actor and critic components undergo updates via policy gradient and temporal-difference (TD) learning, respectively. We introduce the mean-field Langevin TD learning (MFLTD) method, enhancing mean-field Langevin dynamics with proximal TD updates for critic policy evaluation, and assess its performance against conventional approaches through numerical analysis. Additionally, for actor policy updates, we present the mean-field Langevin policy gradient (MFLPG), employing policy gradient techniques augmented by Wasserstein gradient flows for parameter space exploration. Our findings demonstrate that MFLTD accurately identifies the true value function, while MFLPG ensures linear convergence of actor sequences towards the globally optimal policy, considering a Kullback-Leibler divergence regularized framework. Through both time particle and discretized analysis, we substantiate the linear convergence guarantees of our neural actor-critic algorithms, representing a notable contribution to neural reinforcement learning focusing on global optimality and feature learning, extending the existing understanding beyond the conventional scope of lazy training.