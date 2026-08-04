---
title: "Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/nauman24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nauman24a/nauman24a.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['actor-critic', 'overestimation', 'plasticity']
venue: "ICML 2024"
tldr: "Off-policy RL improvements from regularization are shown to suffer from overestimation, overfitting, and plasticity loss in broader benchmarks."
---

# Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/nauman24a.html](https://proceedings.mlr.press/v235/nauman24a.html)

**TLDR**: Off-policy RL improvements from regularization are shown to suffer from overestimation, overfitting, and plasticity loss in broader benchmarks.

## Abstract

Recent advancements in off-policy Reinforcement Learning (RL) have significantly improved sample efficiency, primarily due to the incorporation of various forms of regularization that enable more gradient update steps than traditional agents. However, many of these techniques have been tested in limited settings, often on tasks from single simulation benchmarks and against well-known algorithms rather than a range of regularization approaches. This limits our understanding of the specific mechanisms driving RL improvements. To address this, we implemented over 60 different off-policy agents, each integrating established regularization techniques from recent state-of-the-art algorithms. We tested these agents across 14 diverse tasks from 2 simulation benchmarks, measuring training metrics related to overestimation, overfitting, and plasticity loss — issues that motivate the examined regularization techniques. Our findings reveal that while the effectiveness of a specific regularization setup varies with the task, certain combinations consistently demonstrate robust and superior performance. Notably, a simple Soft Actor-Critic agent, appropriately regularized, reliably finds a better-performing policy within the training regime, which previously was achieved mainly through model-based approaches.