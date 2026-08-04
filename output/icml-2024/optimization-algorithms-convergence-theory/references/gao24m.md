---
title: "Adaptive-Gradient Policy Optimization: Enhancing Policy Learning in Non-Smooth Differentiable Simulations"
source: "https://proceedings.mlr.press/v235/gao24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gao24m/gao24m.pdf"
categories: ['simulation-scaling-limits-for-robot-manipulation', 'optimization-algorithms-convergence-theory']
tags: ['differentiable-simulation', 'policy-optimization', 'adaptive-gradient', 'non-smooth']
venue: "ICML 2024"
tldr: "Adaptive-Gradient Policy Optimization handles non-smooth differentiable simulations to enable robust policy learning with simulation gradients."
---

# Adaptive-Gradient Policy Optimization: Enhancing Policy Learning in Non-Smooth Differentiable Simulations

**Source**: [https://proceedings.mlr.press/v235/gao24m.html](https://proceedings.mlr.press/v235/gao24m.html)

**TLDR**: Adaptive-Gradient Policy Optimization handles non-smooth differentiable simulations to enable robust policy learning with simulation gradients.

## Abstract

Recent advancements in differentiable simulators highlight the potential of policy optimization using simulation gradients. Yet, these approaches are largely contingent on the continuity and smoothness of the simulation, which precludes the use of certain simulation engines, such as Mujoco. To tackle this challenge, we introduce the adaptive analytic gradient. This method views the Q function as a surrogate for future returns, consistent with the Bellman equation. By analyzing the variance of batched gradients, our method can autonomously opt for a more resilient Q function to compute the gradient when encountering rough simulation transitions. We also put forth the Adaptive-Gradient Policy Optimization (AGPO) algorithm, which leverages our proposed method for policy learning. On the theoretical side, we demonstrate AGPO’s convergence, emphasizing its stable performance under non-smooth dynamics due to low variance. On the empirical side, our results show that AGPO effectively mitigates the challenges posed by non-smoothness in policy learning through differentiable simulation.