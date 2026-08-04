---
title: "RL-CFR: Improving Action Abstraction for Imperfect Information Extensive-Form Games with Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/li24t.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24t/li24t.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['imperfect-information-games', 'action-abstraction', 'counterfactual-regret-minimization', 'reinforcement-learning', 'game-theory']
venue: "ICML 2024"
tldr: "Combines reinforcement learning with counterfactual regret minimization to learn adaptive action abstractions in large imperfect information extensive-form games."
---

# RL-CFR: Improving Action Abstraction for Imperfect Information Extensive-Form Games with Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/li24t.html](https://proceedings.mlr.press/v235/li24t.html)

**TLDR**: Combines reinforcement learning with counterfactual regret minimization to learn adaptive action abstractions in large imperfect information extensive-form games.

## Abstract

Effective action abstraction is crucial in tackling challenges associated with large action spaces in Imperfect Information Extensive-Form Games (IIEFGs). However, due to the vast state space and computational complexity in IIEFGs, existing methods often rely on fixed abstractions, resulting in sub-optimal performance. In response, we introduce RL-CFR, a novel reinforcement learning (RL) approach for dynamic action abstraction. RL-CFR builds upon our innovative Markov Decision Process (MDP) formulation, with states corresponding to public information and actions represented as feature vectors indicating specific action abstractions. The reward is defined as the expected payoff difference between the selected and default action abstractions. RL-CFR constructs a game tree with RL-guided action abstractions and utilizes counterfactual regret minimization (CFR) for strategy derivation. Impressively, it can be trained from scratch, achieving higher expected payoff without increased CFR solving time. In experiments on Heads-up No-limit Texas Hold’em, RL-CFR outperforms ReBeL’s replication and Slumbot, demonstrating significant win-rate margins of $64\pm 11$ and $84\pm 17$ mbb/hand, respectively.