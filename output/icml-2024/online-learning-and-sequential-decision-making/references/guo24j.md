---
title: "Temporal Logic Specification-Conditioned Decision Transformer for Offline Safe Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/guo24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/guo24j/guo24j.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['offline-reinforcement-learning', 'temporal-logic', 'safe-RL', 'decision-transformer', 'constraint-satisfaction']
venue: "ICML 2024"
tldr: "A decision transformer conditioned on temporal logic specifications for offline safe reinforcement learning with complex constraints."
---

# Temporal Logic Specification-Conditioned Decision Transformer for Offline Safe Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/guo24j.html](https://proceedings.mlr.press/v235/guo24j.html)

**TLDR**: A decision transformer conditioned on temporal logic specifications for offline safe reinforcement learning with complex constraints.

## Abstract

Offline safe reinforcement learning (RL) aims to train a constraint satisfaction policy from a fixed dataset. Current state-of-the-art approaches are based on supervised learning with a conditioned policy. However, these approaches fall short in real-world applications that involve complex tasks with rich temporal and logical structures. In this paper, we propose temporal logic Specification-conditioned Decision Transformer (SDT), a novel framework that harnesses the expressive power of signal temporal logic (STL) to specify complex temporal rules that an agent should follow and the sequential modeling capability of Decision Transformer (DT). Empirical evaluations on the DSRL benchmarks demonstrate the better capacity of SDT in learning safe and high-reward policies compared with existing approaches. In addition, SDT shows good alignment with respect to different desired degrees of satisfaction of the STL specification that it is conditioned on.