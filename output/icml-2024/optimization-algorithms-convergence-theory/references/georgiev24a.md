---
title: "Adaptive Horizon Actor-Critic for Policy Learning in Contact-Rich Differentiable Simulation"
source: "https://proceedings.mlr.press/v235/georgiev24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/georgiev24a/georgiev24a.pdf"
categories: ['simulation-scaling-limits-for-robot-manipulation', 'optimization-algorithms-convergence-theory']
tags: ['differentiable-simulation', 'actor-critic', 'contact-rich-control']
venue: "ICML 2024"
tldr: "Proposes an adaptive horizon actor-critic method combining model-free and model-based gradients for contact-rich differentiable simulation."
---

# Adaptive Horizon Actor-Critic for Policy Learning in Contact-Rich Differentiable Simulation

**Source**: [https://proceedings.mlr.press/v235/georgiev24a.html](https://proceedings.mlr.press/v235/georgiev24a.html)

**TLDR**: Proposes an adaptive horizon actor-critic method combining model-free and model-based gradients for contact-rich differentiable simulation.

## Abstract

Model-Free Reinforcement Learning (MFRL), leveraging the policy gradient theorem, has demonstrated considerable success in continuous control tasks. However, these approaches are plagued by high gradient variance due to zeroth-order gradient estimation, resulting in suboptimal policies. Conversely, First-Order Model-Based Reinforcement Learning (FO-MBRL) methods employing differentiable simulation provide gradients with reduced variance but are susceptible to sampling error in scenarios involving stiff dynamics, such as physical contact. This paper investigates the source of this error and introduces Adaptive Horizon Actor-Critic (AHAC), an FO-MBRL algorithm that reduces gradient error by adapting the model-based horizon to avoid stiff dynamics. Empirical findings reveal that AHAC outperforms MFRL baselines, attaining 40% more reward across a set of locomotion tasks and efficiently scaling to high-dimensional control environments with improved wall-clock-time efficiency. adaptive-horizon-actor-critic.github.io