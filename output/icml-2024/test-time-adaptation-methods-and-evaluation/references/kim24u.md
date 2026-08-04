---
title: "Investigating Pre-Training Objectives for Generalization in Vision-Based Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/kim24u.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24u/kim24u.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'continual-learning-memory-plasticity']
tags: ['vision-based-RL', 'pre-training', 'generalization']
venue: "ICML 2024"
tldr: "Evaluates various pre-training objectives for generalization in vision-based reinforcement learning using a unified benchmark."
---

# Investigating Pre-Training Objectives for Generalization in Vision-Based Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/kim24u.html](https://proceedings.mlr.press/v235/kim24u.html)

**TLDR**: Evaluates various pre-training objectives for generalization in vision-based reinforcement learning using a unified benchmark.

## Abstract

Recently, various pre-training methods have been introduced in vision-based Reinforcement Learning (RL). However, their generalization ability remains unclear due to evaluations being limited to in-distribution environments and non-unified experimental setups. To address this, we introduce the Atari Pre-training Benchmark (Atari-PB), which pre-trains a ResNet-50 model on 10 million transitions from 50 Atari games and evaluates it across diverse environment distributions. Our experiments show that pre-training objectives focused on learning task-agnostic features (e.g., identifying objects and understanding temporal dynamics) enhance generalization across different environments. In contrast, objectives focused on learning task-specific knowledge (e.g., identifying agents and fitting reward functions) improve performance in environments similar to the pre-training dataset but not in varied ones. We publicize our codes, datasets, and model checkpoints at https://github.com/dojeon-ai/Atari-PB.