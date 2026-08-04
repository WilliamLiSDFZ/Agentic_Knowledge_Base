---
title: "A Contextual Combinatorial Bandit Approach to Negotiation"
source: "https://proceedings.mlr.press/v235/li24az.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24az/li24az.pdf"
categories: ['online-learning-and-sequential-decision-making', 'online-learning-matching-market-algorithms']
tags: ['contextual-bandits', 'negotiation', 'combinatorial-action-space']
venue: "ICML 2024"
tldr: "Introduces a contextual combinatorial bandit framework to learn effective negotiation strategies under exploration-exploitation tradeoffs with large action spaces."
---

# A Contextual Combinatorial Bandit Approach to Negotiation

**Source**: [https://proceedings.mlr.press/v235/li24az.html](https://proceedings.mlr.press/v235/li24az.html)

**TLDR**: Introduces a contextual combinatorial bandit framework to learn effective negotiation strategies under exploration-exploitation tradeoffs with large action spaces.

## Abstract

Learning effective negotiation strategies poses two key challenges: the exploration-exploitation dilemma and dealing with large action spaces. However, there is an absence of learning-based approaches that effectively address these challenges in negotiation. This paper introduces a comprehensive formulation to tackle various negotiation problems. Our approach leverages contextual combinatorial multi-armed bandits, with the bandits resolving the exploration-exploitation dilemma, and the combinatorial nature handles large action spaces. Building upon this formulation, we introduce NegUCB, a novel method that also handles common issues such as partial observations and complex reward functions in negotiation. NegUCB is contextual and tailored for full-bandit feedback without constraints on the reward functions. Under mild assumptions, it ensures a sub-linear regret upper bound. Experiments conducted on three negotiation tasks demonstrate the superiority of our approach.