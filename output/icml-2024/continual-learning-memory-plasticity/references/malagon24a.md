---
title: "Self-Composing Policies for Scalable Continual Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/malagon24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/malagon24a/malagon24a.pdf"
categories: ['continual-learning-memory-plasticity', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['continual-reinforcement-learning', 'modular-networks', 'catastrophic-forgetting']
venue: "ICML 2024"
tldr: "A growable modular neural network architecture for continual RL that avoids catastrophic forgetting by selectively composing previous policies."
---

# Self-Composing Policies for Scalable Continual Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/malagon24a.html](https://proceedings.mlr.press/v235/malagon24a.html)

**TLDR**: A growable modular neural network architecture for continual RL that avoids catastrophic forgetting by selectively composing previous policies.

## Abstract

This work introduces a growable and modular neural network architecture that naturally avoids catastrophic forgetting and interference in continual reinforcement learning. The structure of each module allows the selective combination of previous policies along with its internal policy accelerating the learning process on the current task. Unlike previous growing neural network approaches, we show that the number of parameters of the proposed approach grows linearly with respect to the number of tasks, and does not sacrifice plasticity to scale. Experiments conducted in benchmark continuous control and visual problems reveal that the proposed approach achieves greater knowledge transfer and performance than alternative methods.