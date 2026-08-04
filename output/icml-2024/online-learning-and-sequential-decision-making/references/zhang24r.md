---
title: "Model-based Reinforcement Learning for Parameterized Action Spaces"
source: "https://proceedings.mlr.press/v235/zhang24r.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24r/zhang24r.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['model-based-RL', 'parameterized-actions', 'predictive-control']
venue: "ICML 2024"
tldr: "A model-based RL algorithm for parameterized action spaces that learns dynamics models and plans with modified Model Predictive Path Integral control."
---

# Model-based Reinforcement Learning for Parameterized Action Spaces

**Source**: [https://proceedings.mlr.press/v235/zhang24r.html](https://proceedings.mlr.press/v235/zhang24r.html)

**TLDR**: A model-based RL algorithm for parameterized action spaces that learns dynamics models and plans with modified Model Predictive Path Integral control.

## Abstract

We propose a novel model-based reinforcement learning algorithm—Dynamics Learning and predictive control with Parameterized Actions (DLPA)—for Parameterized Action Markov Decision Processes (PAMDPs). The agent learns a parameterized-action-conditioned dynamics model and plans with a modified Model Predictive Path Integral control. We theoretically quantify the difference between the generated trajectory and the optimal trajectory during planning in terms of the value they achieved through the lens of Lipschitz Continuity. Our empirical results on several standard benchmarks show that our algorithm achieves superior sample efficiency and asymptotic performance than state-of-the-art PAMDP methods.