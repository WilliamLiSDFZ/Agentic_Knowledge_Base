---
title: "Slow and Steady Wins the Race: Maintaining Plasticity with Hare and Tortoise Networks"
source: "https://proceedings.mlr.press/v235/lee24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24d/lee24d.pdf"
categories: ['continual-learning-memory-plasticity', 'neural-network-learning-dynamics-theory']
tags: ['plasticity', 'continual-learning', 'warm-starting', 'generalization', 'neural-networks']
venue: "ICML 2024"
tldr: "Empirically investigates plasticity loss in neural networks and proposes a dual-network Hare and Tortoise approach to maintain generalization ability."
---

# Slow and Steady Wins the Race: Maintaining Plasticity with Hare and Tortoise Networks

**Source**: [https://proceedings.mlr.press/v235/lee24d.html](https://proceedings.mlr.press/v235/lee24d.html)

**TLDR**: Empirically investigates plasticity loss in neural networks and proposes a dual-network Hare and Tortoise approach to maintain generalization ability.

## Abstract

This study investigates the loss of generalization ability in neural networks, revisiting warm-starting experiments from Ash & Adams. Our empirical analysis reveals that common methods designed to enhance plasticity by maintaining trainability provide limited benefits to generalization. While reinitializing the network can be effective, it also risks losing valuable prior knowledge. To this end, we introduce the Hare & Tortoise, inspired by the brain’s complementary learning system. Hare & Tortoise consists of two components: the Hare network, which rapidly adapts to new information analogously to the hippocampus, and the Tortoise network, which gradually integrates knowledge akin to the neocortex. By periodically reinitializing the Hare network to the Tortoise’s weights, our method preserves plasticity while retaining general knowledge. Hare & Tortoise can effectively maintain the network’s ability to generalize, which improves advanced reinforcement learning algorithms on the Atari-100k benchmark. The code is available at https://github.com/dojeon-ai/hare-tortoise.