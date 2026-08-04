---
title: "Graphon Mean Field Games with a Representative Player: Analysis and Learning Algorithm"
source: "https://proceedings.mlr.press/v235/zhou24u.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhou24u/zhou24u.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics', 'multi-agent-mdp-structure-and-dependencies']
tags: ['graphon-games', 'mean-field-games', 'heterogeneous-agents']
venue: "ICML 2024"
tldr: "Proposes a discrete-time graphon mean field game formulation with a representative player for stochastic games with heterogeneous agent interactions, along with a learning algorithm."
---

# Graphon Mean Field Games with a Representative Player: Analysis and Learning Algorithm

**Source**: [https://proceedings.mlr.press/v235/zhou24u.html](https://proceedings.mlr.press/v235/zhou24u.html)

**TLDR**: Proposes a discrete-time graphon mean field game formulation with a representative player for stochastic games with heterogeneous agent interactions, along with a learning algorithm.

## Abstract

We propose a discrete time graphon game formulation on continuous state and action spaces using a representative player to study stochastic games with heterogeneous interaction among agents. This formulation admits both conceptual and mathematical advantages, compared to a widely adopted formulation using a continuum of players. We prove the existence and uniqueness of the graphon equilibrium with mild assumptions, and show that this equilibrium can be used to construct an approximate solution for the finite player game, which is challenging to analyze and solve due to curse of dimensionality. An online oracle-free learning algorithm is developed to solve the equilibrium numerically, and sample complexity analysis is provided for its convergence.