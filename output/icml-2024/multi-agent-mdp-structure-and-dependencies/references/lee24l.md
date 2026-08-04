---
title: "Pausing Policy Learning in Non-stationary Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/lee24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24l/lee24l.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['non-stationary-RL', 'policy-learning', 'temporal-difference', 'pausing']
venue: "ICML 2024"
tldr: "Proposes strategically pausing policy updates in non-stationary reinforcement learning to improve performance under temporal distribution shifts."
---

# Pausing Policy Learning in Non-stationary Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/lee24l.html](https://proceedings.mlr.press/v235/lee24l.html)

**TLDR**: Proposes strategically pausing policy updates in non-stationary reinforcement learning to improve performance under temporal distribution shifts.

## Abstract

Real-time inference is a challenge of real-world reinforcement learning due to temporal differences in time-varying environments: the system collects data from the past, updates the decision model in the present, and deploys it in the future. We tackle a common belief that continually updating the decision is optimal to minimize the temporal gap. We propose forecasting an online reinforcement learning framework and show that strategically pausing decision updates yields better overall performance by effectively managing aleatoric uncertainty. Theoretically, we compute an optimal ratio between policy update and hold duration, and show that a non-zero policy hold duration provides a sharper upper bound on the dynamic regret. Our experimental evaluations on three different environments also reveal that a non-zero policy hold duration yields higher rewards compared to continuous decision updates.