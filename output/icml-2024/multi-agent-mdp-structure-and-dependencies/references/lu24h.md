---
title: "Rethinking Transformers in Solving POMDPs"
source: "https://proceedings.mlr.press/v235/lu24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lu24h/lu24h.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['transformers', 'POMDP', 'partial-observability', 'reinforcement-learning', 'sequential-decision-making']
venue: "ICML 2024"
tldr: "Re-examines transformer architectures for solving POMDPs, analyzing their effectiveness under partial observability in sequential decision-making."
---

# Rethinking Transformers in Solving POMDPs

**Source**: [https://proceedings.mlr.press/v235/lu24h.html](https://proceedings.mlr.press/v235/lu24h.html)

**TLDR**: Re-examines transformer architectures for solving POMDPs, analyzing their effectiveness under partial observability in sequential decision-making.

## Abstract

Sequential decision-making algorithms such as reinforcement learning (RL) in real-world scenarios inevitably face environments with partial observability. This paper scrutinizes the effectiveness of a popular architecture, namely Transformers, in Partially Observable Markov Decision Processes (POMDPs) and reveals its theoretical limitations. We establish that regular languages, which Transformers struggle to model, are reducible to POMDPs. This poses a significant challenge for Transformers in learning POMDP-specific inductive biases, due to their lack of inherent recurrence found in other models like RNNs. This paper casts doubt on the prevalent belief in Transformers as sequence models for RL and proposes to introduce a point-wise recurrent structure. The Deep Linear Recurrent Unit (LRU) emerges as a well-suited alternative for Partially Observable RL, with empirical results highlighting the sub-optimal performance of the Transformer and considerable strength of LRU.