---
title: "Near-Optimal Regret in Linear MDPs with Aggregate Bandit Feedback"
source: "https://proceedings.mlr.press/v235/cassel24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cassel24a/cassel24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['reinforcement-learning', 'aggregate-bandit-feedback', 'linear-MDPs', 'regret-bounds']
venue: "ICML 2024"
tldr: "Achieves near-optimal regret in linear MDPs where agents only receive aggregate reward feedback at the end of each episode."
---

# Near-Optimal Regret in Linear MDPs with Aggregate Bandit Feedback

**Source**: [https://proceedings.mlr.press/v235/cassel24a.html](https://proceedings.mlr.press/v235/cassel24a.html)

**TLDR**: Achieves near-optimal regret in linear MDPs where agents only receive aggregate reward feedback at the end of each episode.

## Abstract

In many real-world applications, it is hard to provide a reward signal in each step of a Reinforcement Learning (RL) process and more natural to give feedback when an episode ends. To this end, we study the recently proposed model of RL with Aggregate Bandit Feedback (RL-ABF), where the agent only observes the sum of rewards at the end of an episode instead of each reward individually. Prior work studied RL-ABF only in tabular settings, where the number of states is assumed to be small. In this paper, we extend ABF to linear function approximation and develop two efficient algorithms with near-optimal regret guarantees: a value-based optimistic algorithm built on a new randomization technique with a Q-functions ensemble, and a policy optimization algorithm that uses a novel hedging scheme over the ensemble.