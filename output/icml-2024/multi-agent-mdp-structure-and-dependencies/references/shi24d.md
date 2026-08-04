---
title: "Sample-Efficient Robust Multi-Agent Reinforcement Learning in the Face of Environmental Uncertainty"
source: "https://proceedings.mlr.press/v235/shi24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shi24d/shi24d.pdf"
categories: ['multi-agent-mdp-structure-and-dependencies', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['multi-agent-reinforcement-learning', 'robust-RL', 'environmental-uncertainty']
venue: "ICML 2024"
tldr: "This paper develops sample-efficient robust multi-agent reinforcement learning algorithms that maintain robustness against environmental uncertainties to bridge the sim-to-real gap."
---

# Sample-Efficient Robust Multi-Agent Reinforcement Learning in the Face of Environmental Uncertainty

**Source**: [https://proceedings.mlr.press/v235/shi24d.html](https://proceedings.mlr.press/v235/shi24d.html)

**TLDR**: This paper develops sample-efficient robust multi-agent reinforcement learning algorithms that maintain robustness against environmental uncertainties to bridge the sim-to-real gap.

## Abstract

To overcome the sim-to-real gap in reinforcement learning (RL), learned policies must maintain robustness against environmental uncertainties. While robust RL has been widely studied in single-agent regimes, in multi-agent environments, the problem remains understudied—despite the fact that the problems posed by environmental uncertainties are often exacerbated by strategic interactions. This work focuses on learning in distributionally robust Markov games (RMGs), a robust variant of standard Markov games, wherein each agent aims to learn a policy that maximizes its own worst-case performance when the deployed environment deviates within its own prescribed uncertainty set. This results in a set of robust equilibrium strategies for all agents that align with classic notions of game-theoretic equilibria. Assuming a non-adaptive sampling mechanism from a generative model, we propose a sample-efficient model-based algorithm (DRNVI) with finite-sample complexity guarantees for learning robust variants of various notions of game-theoretic equilibria. We also establish an information-theoretic lower bound for solving RMGs, which confirms the near-optimal sample complexity of DRNVI with respect to problem-dependent factors such as the size of the state space, the target accuracy, and the horizon length.