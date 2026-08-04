---
title: "Learning Constraints from Offline Demonstrations via Superior Distribution Correction Estimation"
source: "https://proceedings.mlr.press/v235/quan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/quan24a/quan24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'llm-geometry-and-interpretability-research']
tags: ['inverse-constrained-RL', 'offline-learning', 'safety-constraints', 'distribution-correction', 'imitation']
venue: "ICML 2024"
tldr: "An offline inverse constrained RL method that learns safety constraints from demonstrations via distribution correction."
---

# Learning Constraints from Offline Demonstrations via Superior Distribution Correction Estimation

**Source**: [https://proceedings.mlr.press/v235/quan24a.html](https://proceedings.mlr.press/v235/quan24a.html)

**TLDR**: An offline inverse constrained RL method that learns safety constraints from demonstrations via distribution correction.

## Abstract

An effective approach for learning both safety constraints and control policies is Inverse Constrained Reinforcement Learning (ICRL). Previous ICRL algorithms commonly employ an online learning framework that permits unlimited sampling from an interactive environment. This setting, however, is infeasible in many realistic applications where data collection is dangerous and expensive. To address this challenge, we propose Inverse Constrained Superior Distribution Correction Estimation (ICSDICE) as an offline ICRL solver. ICSDICE extracts feasible constraints from superior distributions, thereby highlighting policies with expert-exceeding rewards maximization ability. To estimate these distributions, ICSDICE solves a regularized dual optimization problem for safe control by exploiting the observed reward signals and expert preferences. Striving for transferable constraints and unbiased estimations, ICSDICE actively encourages sparsity and incorporates a discounting effect within the learned and observed distributions. Empirical studies show that ICSDICE outperforms other baselines by accurately recovering the constraints and adapting to high-dimensional environments. The code is available at https://github.com/quangr/ICSDICE.