---
title: "Combinatorial Multivariant Multi-Armed Bandits with Applications to Episodic Reinforcement Learning and Beyond"
source: "https://proceedings.mlr.press/v235/liu24bp.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24bp/liu24bp.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['combinatorial-bandits', 'multi-armed-bandits', 'reinforcement-learning', 'multivariate-rewards', 'triggering-arms']
venue: "ICML 2024"
tldr: "A novel combinatorial multi-armed bandit framework with multivariant probabilistically triggering arms with applications to episodic reinforcement learning."
---

# Combinatorial Multivariant Multi-Armed Bandits with Applications to Episodic Reinforcement Learning and Beyond

**Source**: [https://proceedings.mlr.press/v235/liu24bp.html](https://proceedings.mlr.press/v235/liu24bp.html)

**TLDR**: A novel combinatorial multi-armed bandit framework with multivariant probabilistically triggering arms with applications to episodic reinforcement learning.

## Abstract

We introduce a novel framework of combinatorial multi-armed bandits (CMAB) with multivariant and probabilistically triggering arms (CMAB-MT), where the outcome of each arm is a $d$-dimensional multivariant random variable and the feedback follows a general arm triggering process. Compared with existing CMAB works, CMAB-MT not only enhances the modeling power but also allows improved results by leveraging distinct statistical properties for multivariant random variables. For CMAB-MT, we propose a general 1-norm multivariant and triggering probability-modulated smoothness condition, and an optimistic CUCB-MT algorithm built upon this condition. Our framework can include many important problems as applications, such as episodic reinforcement learning (RL) and probabilistic maximum coverage for goods distribution, all of which meet the above smoothness condition and achieve matching or improved regret bounds compared to existing works. Through our new framework, we build the first connection between the episodic RL and CMAB literature, by offering a new angle to solve the episodic RL through the lens of CMAB, which may encourage more interactions between these two important directions.