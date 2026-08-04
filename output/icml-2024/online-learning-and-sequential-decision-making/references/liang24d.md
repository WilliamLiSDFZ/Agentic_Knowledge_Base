---
title: "Single-Trajectory Distributionally Robust Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/liang24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liang24d/liang24d.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['distributionally-robust-RL', 'single-trajectory', 'reinforcement-learning']
venue: "ICML 2024"
tldr: "Single-trajectory distributionally robust reinforcement learning is studied to improve policy robustness across varying environments."
---

# Single-Trajectory Distributionally Robust Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/liang24d.html](https://proceedings.mlr.press/v235/liang24d.html)

**TLDR**: Single-trajectory distributionally robust reinforcement learning is studied to improve policy robustness across varying environments.

## Abstract

To mitigate the limitation that the classical reinforcement learning (RL) framework heavily relies on identical training and test environments, Distributionally Robust RL (DRRL) has been proposed to enhance performance across a range of environments, possibly including unknown test environments. As a price for robustness gain, DRRL involves optimizing over a set of distributions, which is inherently more challenging than optimizing over a fixed distribution in the non-robust case. Existing DRRL algorithms are either model-based or fail to learn from a single sample trajectory. In this paper, we design a first fully model-free DRRL algorithm, called distributionally robust Q-learning with single trajectory (DRQ). We delicately design a multi-timescale framework to fully utilize each incrementally arriving sample and directly learn the optimal distributionally robust policy without modeling the environment, thus the algorithm can be trained along a single trajectory in a model-free fashion. Despite the algorithm’s complexity, we provide asymptotic convergence guarantees by generalizing classical stochastic approximation tools.Comprehensive experimental results demonstrate the superior robustness and sample complexity of our proposed algorithm, compared to non-robust methods and other robust RL algorithms.