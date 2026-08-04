---
title: "Zero-Sum Positional Differential Games as a Framework for Robust Reinforcement Learning: Deep Q-Learning Approach"
source: "https://proceedings.mlr.press/v235/plaksin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/plaksin24a/plaksin24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['robust-RL', 'differential-games', 'deep-Q-learning']
venue: "ICML 2024"
tldr: "Formulates robust reinforcement learning as a zero-sum positional differential game and solves it with deep Q-learning."
---

# Zero-Sum Positional Differential Games as a Framework for Robust Reinforcement Learning: Deep Q-Learning Approach

**Source**: [https://proceedings.mlr.press/v235/plaksin24a.html](https://proceedings.mlr.press/v235/plaksin24a.html)

**TLDR**: Formulates robust reinforcement learning as a zero-sum positional differential game and solves it with deep Q-learning.

## Abstract

Robust Reinforcement Learning (RRL) is a promising Reinforcement Learning (RL) paradigm aimed at training robust to uncertainty or disturbances models, making them more efficient for real-world applications. Following this paradigm, uncertainty or disturbances are interpreted as actions of a second adversarial agent, and thus, the problem is reduced to seeking the agents’ policies robust to any opponent’s actions. This paper is the first to propose considering the RRL problems within the positional differential game theory, which helps us to obtain theoretically justified intuition to develop a centralized Q-learning approach. Namely, we prove that under Isaacs’s condition (sufficiently general for real-world dynamical systems), the same Q-function can be utilized as an approximate solution of both minimax and maximin Bellman equations. Based on these results, we present the Isaacs Deep Q-Network algorithms and demonstrate their superiority compared to other baseline RRL and Multi-Agent RL algorithms in various environments.