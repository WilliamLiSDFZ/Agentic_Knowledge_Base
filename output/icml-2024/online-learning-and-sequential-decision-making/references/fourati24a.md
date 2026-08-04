---
title: "Stochastic Q-learning for Large Discrete Action Spaces"
source: "https://proceedings.mlr.press/v235/fourati24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fourati24a/fourati24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['Q-learning', 'large-action-spaces', 'reinforcement-learning']
venue: "ICML 2024"
tldr: "Stochastic Q-learning efficiently handles large discrete action spaces by stochastically sampling actions during value function maximization."
---

# Stochastic Q-learning for Large Discrete Action Spaces

**Source**: [https://proceedings.mlr.press/v235/fourati24a.html](https://proceedings.mlr.press/v235/fourati24a.html)

**TLDR**: Stochastic Q-learning efficiently handles large discrete action spaces by stochastically sampling actions during value function maximization.

## Abstract

In complex environments with large discrete action spaces, effective decision-making is critical in reinforcement learning (RL). Despite the widespread use of value-based RL approaches like Q-learning, they come with a computational burden, necessitating the maximization of a value function over all actions in each iteration. This burden becomes particularly challenging when addressing large-scale problems and using deep neural networks as function approximators. In this paper, we present stochastic value-based RL approaches which, in each iteration, as opposed to optimizing over the entire set of $n$ actions, only consider a variable stochastic set of a sublinear number of actions, possibly as small as $\mathcal{O}(\log(n))$. The presented stochastic value-based RL methods include, among others, Stochastic Q-learning, StochDQN, and StochDDQN, all of which integrate this stochastic approach for both value-function updates and action selection. The theoretical convergence of Stochastic Q-learning is established, while an analysis of stochastic maximization is provided. Moreover, through empirical validation, we illustrate that the various proposed approaches outperform the baseline methods across diverse environments, including different control problems, achieving near-optimal average returns in significantly reduced time.