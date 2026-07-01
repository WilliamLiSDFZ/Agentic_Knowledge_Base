---
title: "Warm-up Free Policy Optimization: Improved Regret in Linear Markov Decision Processes"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/05d42b7bd130ecbc57fdf02cbdcd370e-Abstract-Conference.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'online-learning-augmented-algorithms-and-optimization']
tags: ['policy-optimization', 'linear-mdp', 'regret-bounds']
venue: "NeurIPS 2024"
tldr: "A warm-up free policy optimization algorithm achieves rate-optimal regret guarantees in linear Markov Decision Processes without requiring warm-up phases."
---

# Warm-up Free Policy Optimization: Improved Regret in Linear Markov Decision Processes

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/05d42b7bd130ecbc57fdf02cbdcd370e-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/05d42b7bd130ecbc57fdf02cbdcd370e-Abstract-Conference.html)

**TLDR**: A warm-up free policy optimization algorithm achieves rate-optimal regret guarantees in linear Markov Decision Processes without requiring warm-up phases.

## Abstract

Policy Optimization (PO) methods are among the most popular Reinforcement Learning (RL) algorithms in practice. Recently, Sherman et al. [2023a] proposed a PO-based algorithm with rate-optimal regret guarantees under the linear Markov Decision Process (MDP) model. However, their algorithm relies on a costly pure exploration warm-up phase that is hard to implement in practice. This paper eliminates this undesired warm-up phase, replacing it with a simple and efficient contraction mechanism. Our PO algorithm achieves rate-optimal regret with improved dependence on the other parameters of the problem (horizon and function approximation dimension) in two fundamental settings: adversarial losses with full-information feedback and stochastic losses with bandit feedback.