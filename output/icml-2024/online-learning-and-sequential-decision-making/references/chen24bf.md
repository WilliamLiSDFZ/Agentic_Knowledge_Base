---
title: "Provable Risk-Sensitive Distributional Reinforcement Learning with General Function Approximation"
source: "https://proceedings.mlr.press/v235/chen24bf.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24bf/chen24bf.pdf"
categories: ['online-learning-and-sequential-decision-making', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['risk-sensitive-RL', 'distributional-reinforcement-learning', 'function-approximation']
venue: "ICML 2024"
tldr: "A general framework for risk-sensitive distributional reinforcement learning with provable guarantees under general function approximation."
---

# Provable Risk-Sensitive Distributional Reinforcement Learning with General Function Approximation

**Source**: [https://proceedings.mlr.press/v235/chen24bf.html](https://proceedings.mlr.press/v235/chen24bf.html)

**TLDR**: A general framework for risk-sensitive distributional reinforcement learning with provable guarantees under general function approximation.

## Abstract

In the realm of reinforcement learning (RL), accounting for risk is crucial for making decisions under uncertainty, particularly in applications where safety and reliability are paramount. In this paper, we introduce a general framework on Risk-Sensitive Distributional Reinforcement Learning (RS-DisRL), with static Lipschitz Risk Measures (LRM) and general function approximation. Our framework covers a broad class of risk-sensitive RL, and facilitates analysis of the impact of estimation functions on the effectiveness of RSRL strategies and evaluation of their sample complexity. We design two innovative meta-algorithms: RS-DisRL-M, a model-based strategy for model-based function approximation, and RS-DisRL-V, a model-free approach for general value function approximation. With our novel estimation techniques via Least Squares Regression (LSR) and Maximum Likelihood Estimation (MLE) in distributional RL with augmented Markov Decision Process (MDP), we derive the first $\widetilde{\mathcal{O}}(\sqrt{K})$ dependency of the regret upper bound for RSRL with static LRM, marking a pioneering contribution towards statistically efficient algorithms in this domain.