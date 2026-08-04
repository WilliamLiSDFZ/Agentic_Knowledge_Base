---
title: "Provably Efficient Reinforcement Learning for Adversarial Restless Multi-Armed Bandits with Unknown Transitions and Bandit Feedback"
source: "https://proceedings.mlr.press/v235/xiong24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xiong24b/xiong24b.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['restless-multi-armed-bandits', 'adversarial-settings', 'reinforcement-learning']
venue: "ICML 2024"
tldr: "This paper provides provably efficient RL algorithms for adversarial restless multi-armed bandits with unknown transitions and bandit feedback."
---

# Provably Efficient Reinforcement Learning for Adversarial Restless Multi-Armed Bandits with Unknown Transitions and Bandit Feedback

**Source**: [https://proceedings.mlr.press/v235/xiong24b.html](https://proceedings.mlr.press/v235/xiong24b.html)

**TLDR**: This paper provides provably efficient RL algorithms for adversarial restless multi-armed bandits with unknown transitions and bandit feedback.

## Abstract

Restless multi-armed bandits (RMAB) play a central role in modeling sequential decision making problems under an instantaneous activation constraint that at most $B$ arms can be activated at any decision epoch. Each restless arm is endowed with a state that evolves independently according to a Markov decision process regardless of being activated or not. In this paper, we consider the task of learning in episodic RMAB with unknown transition functions, bandit feedback, and adversarial rewards, which can change arbitrarily across episodes. The goal of the decision maker is to maximize its total adversarial rewards during the learning process while the instantaneous activation constraint must be satisfied in each decision epoch. We develop a novel reinforcement learning algorithm with two key contributors: a novel biased adversarial reward estimator to deal with bandit feedback and unknown transitions, and a low-complexity index policy to satisfy the instantaneous activation constraint. We show $\tilde{\mathcal{O}}(H\sqrt{T})$ regret bound for our algorithm, where $T$ is the number of episodes and $H$ is the episode length. To our best knowledge, this is the first algorithm to ensure $\tilde{\mathcal{O}}(\sqrt{T})$ regret for adversarial RMAB in our considered challenging settings.