---
title: "Probabilistic Constrained Reinforcement Learning with Formal Interpretability"
source: "https://proceedings.mlr.press/v235/wang24bf.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24bf/wang24bf.pdf"
categories: ['probabilistic-generating-circuits-research', 'multi-agent-mdp-structure-and-dependencies']
tags: ['constrained-reinforcement-learning', 'probabilistic-circuits', 'interpretability', 'policy-representation']
venue: "ICML 2024"
tldr: "Introduces a probabilistic constrained RL framework using formal probabilistic models to improve interpretability of reward functions and optimal policies."
---

# Probabilistic Constrained Reinforcement Learning with Formal Interpretability

**Source**: [https://proceedings.mlr.press/v235/wang24bf.html](https://proceedings.mlr.press/v235/wang24bf.html)

**TLDR**: Introduces a probabilistic constrained RL framework using formal probabilistic models to improve interpretability of reward functions and optimal policies.

## Abstract

Reinforcement learning can provide effective reasoning for sequential decision-making problems with variable dynamics. Such reasoning in practical implementation, however, poses a persistent challenge in interpreting the reward function and the corresponding optimal policy. Consequently, representing sequential decision-making problems as probabilistic inference can have considerable value, as, in principle, the inference offers diverse and powerful mathematical tools to infer the stochastic dynamics whilst suggesting a probabilistic interpretation of policy optimization. In this study, we propose a novel Adaptive Wasserstein Variational Optimization, namely AWaVO, to tackle these interpretability challenges. Our approach uses formal methods to achieve the interpretability: convergence guarantee, training transparency, and intrinsic decision-interpretation. To demonstrate its practicality, we showcase guaranteed interpretability including a global convergence rate $\Theta(1/\sqrt{T})$ not only in simulation but also in real-world quadrotor tasks. In comparison with state-of-the-art benchmarks, including TRPO-IPO, PCPO, and CRPO, we empirically verify that AWaVO offers a reasonable trade-off between high performance and sufficient interpretability.