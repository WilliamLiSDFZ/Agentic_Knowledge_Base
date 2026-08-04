---
title: "$\rm E(3)$-Equivariant Actor-Critic Methods for Cooperative Multi-Agent Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/chen24az.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24az/chen24az.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['E3-equivariance', 'multi-agent-RL', 'cooperative', 'symmetry']
venue: "ICML 2024"
tldr: "Develops E(3)-equivariant actor-critic methods for cooperative multi-agent reinforcement learning in 3D physical environments."
---

# $\rm E(3)$-Equivariant Actor-Critic Methods for Cooperative Multi-Agent Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/chen24az.html](https://proceedings.mlr.press/v235/chen24az.html)

**TLDR**: Develops E(3)-equivariant actor-critic methods for cooperative multi-agent reinforcement learning in 3D physical environments.

## Abstract

Identification and analysis of symmetrical patterns in the natural world have led to significant discoveries across various scientific fields, such as the formulation of gravitational laws in physics and advancements in the study of chemical structures. In this paper, we focus on exploiting Euclidean symmetries inherent in certain cooperative multi-agent reinforcement learning (MARL) problems and prevalent in many applications. We begin by formally characterizing a subclass of Markov games with a general notion of symmetries that admits the existence of symmetric optimal values and policies. Motivated by these properties, we design neural network architectures with symmetric constraints embedded as an inductive bias for multi-agent actor-critic methods. This inductive bias results in superior performance in various cooperative MARL benchmarks and impressive generalization capabilities such as zero-shot learning and transfer learning in unseen scenarios with repeated symmetric patterns.