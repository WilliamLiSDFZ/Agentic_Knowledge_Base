---
title: "Boosting Reinforcement Learning with Strongly Delayed Feedback Through Auxiliary Short Delays"
source: "https://proceedings.mlr.press/v235/wu24af.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24af/wu24af.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['reinforcement-learning', 'delayed-feedback', 'state-augmentation', 'auxiliary-delays', 'stochastic-environments']
venue: "ICML 2024"
tldr: "Addresses strongly delayed feedback in reinforcement learning using auxiliary short delays to boost performance while avoiding state space explosion."
---

# Boosting Reinforcement Learning with Strongly Delayed Feedback Through Auxiliary Short Delays

**Source**: [https://proceedings.mlr.press/v235/wu24af.html](https://proceedings.mlr.press/v235/wu24af.html)

**TLDR**: Addresses strongly delayed feedback in reinforcement learning using auxiliary short delays to boost performance while avoiding state space explosion.

## Abstract

Reinforcement learning (RL) is challenging in the common case of delays between events and their sensory perceptions. State-of-the-art (SOTA) state augmentation techniques either suffer from state space explosion or performance degeneration in stochastic environments. To address these challenges, we present a novel Auxiliary-Delayed Reinforcement Learning (AD-RL) method that leverages auxiliary tasks involving short delays to accelerate RL with long delays, without compromising performance in stochastic environments. Specifically, AD-RL learns a value function for short delays and uses bootstrapping and policy improvement techniques to adjust it for long delays. We theoretically show that this can greatly reduce the sample complexity. On deterministic and stochastic benchmarks, our method significantly outperforms the SOTAs in both sample efficiency and policy performance. Code is available at https://github.com/QingyuanWuNothing/AD-RL.