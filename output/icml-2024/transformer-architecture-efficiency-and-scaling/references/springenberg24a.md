---
title: "Offline Actor-Critic Reinforcement Learning Scales to Large Models"
source: "https://proceedings.mlr.press/v235/springenberg24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/springenberg24a/springenberg24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'transformer-architecture-efficiency-and-scaling']
tags: ['offline-RL', 'actor-critic', 'scaling-laws', 'transformers']
venue: "ICML 2024"
tldr: "Offline actor-critic RL is shown to scale to large transformer models following similar scaling laws as supervised learning, outperforming behavioral cloning baselines."
---

# Offline Actor-Critic Reinforcement Learning Scales to Large Models

**Source**: [https://proceedings.mlr.press/v235/springenberg24a.html](https://proceedings.mlr.press/v235/springenberg24a.html)

**TLDR**: Offline actor-critic RL is shown to scale to large transformer models following similar scaling laws as supervised learning, outperforming behavioral cloning baselines.

## Abstract

We show that offline actor-critic reinforcement learning can scale to large models - such as transformers - and follows similar scaling laws as supervised learning. We find that offline actor-critic algorithms can outperform strong, supervised, behavioral cloning baselines for multi-task training on a large dataset; containing both sub-optimal and expert behavior on 132 continuous control tasks. We introduce a Perceiver-based actor-critic model and elucidate the key features needed to make offline RL work with self- and cross-attention modules. Overall, we find that: i) simple offline actor critic algorithms are a natural choice for gradually moving away from the currently predominant paradigm of behavioral cloning, and ii) via offline RL it is possible to learn multi-task policies that master many domains simultaneously, including real robotics tasks, from sub-optimal demonstrations or self-generated data.