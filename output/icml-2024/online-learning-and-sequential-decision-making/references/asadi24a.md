---
title: "Learning the Target Network in Function Space"
source: "https://proceedings.mlr.press/v235/asadi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/asadi24a/asadi24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['reinforcement-learning', 'value-function', 'target-network', 'function-space', 'lookahead']
venue: "ICML 2024"
tldr: "Proposes Lookahead-Replicate, a new value-function learning method targeting network updates in function space for RL."
---

# Learning the Target Network in Function Space

**Source**: [https://proceedings.mlr.press/v235/asadi24a.html](https://proceedings.mlr.press/v235/asadi24a.html)

**TLDR**: Proposes Lookahead-Replicate, a new value-function learning method targeting network updates in function space for RL.

## Abstract

We focus on the task of learning the value function in the reinforcement learning (RL) setting. This task is often solved by updating a pair of online and target networks while ensuring that the parameters of these two networks are equivalent. We propose Lookahead-Replicate (LR), a new value-function approximation algorithm that is agnostic to this parameter-space equivalence. Instead, the LR algorithm is designed to maintain an equivalence between the two networks in the function space. This value-based equivalence is obtained by employing a new target-network update. We show that LR leads to a convergent behavior in learning the value function. We also present empirical results demonstrating that LR-based target-network updates significantly improve deep RL on the Atari benchmark.