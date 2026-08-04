---
title: "HarmonyDream: Task Harmonization Inside World Models"
source: "https://proceedings.mlr.press/v235/ma24o.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24o/ma24o.pdf"
categories: ['multi-agent-mdp-structure-and-dependencies', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['model-based-rl', 'world-models', 'task-harmonization']
venue: "ICML 2024"
tldr: "An empirical study revealing task imbalance in world models and a harmonization approach to balance observation and reward modeling for improved sample efficiency."
---

# HarmonyDream: Task Harmonization Inside World Models

**Source**: [https://proceedings.mlr.press/v235/ma24o.html](https://proceedings.mlr.press/v235/ma24o.html)

**TLDR**: An empirical study revealing task imbalance in world models and a harmonization approach to balance observation and reward modeling for improved sample efficiency.

## Abstract

Model-based reinforcement learning (MBRL) holds the promise of sample-efficient learning by utilizing a world model, which models how the environment works and typically encompasses components for two tasks: observation modeling and reward modeling. In this paper, through a dedicated empirical investigation, we gain a deeper understanding of the role each task plays in world models and uncover the overlooked potential of sample-efficient MBRL by mitigating the domination of either observation or reward modeling. Our key insight is that while prevalent approaches of explicit MBRL attempt to restore abundant details of the environment via observation models, it is difficult due to the environment’s complexity and limited model capacity. On the other hand, reward models, while dominating implicit MBRL and adept at learning compact task-centric dynamics, are inadequate for sample-efficient learning without richer learning signals. Motivated by these insights and discoveries, we propose a simple yet effective approach, HarmonyDream, which automatically adjusts loss coefficients to maintain task harmonization, i.e. a dynamic equilibrium between the two tasks in world model learning. Our experiments show that the base MBRL method equipped with HarmonyDream gains 10%-69% absolute performance boosts on visual robotic tasks and sets a new state-of-the-art result on the Atari 100K benchmark. Code is available at https://github.com/thuml/HarmonyDream.