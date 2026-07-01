---
title: "The Sample-Communication Complexity Trade-off in Federated Q-Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/45fc4a0da7e7f6fbabaabe2d20a441d1-Abstract-Conference.html"
categories: ['privacy-preserving-federated-distributed-learning']
tags: ['federated-q-learning', 'sample-complexity', 'communication-complexity']
venue: "NeurIPS 2024"
tldr: "This paper characterizes the fundamental sample-communication complexity trade-off in federated Q-learning for collaborative reinforcement learning across multiple agents."
---

# The Sample-Communication Complexity Trade-off in Federated Q-Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/45fc4a0da7e7f6fbabaabe2d20a441d1-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/45fc4a0da7e7f6fbabaabe2d20a441d1-Abstract-Conference.html)

**TLDR**: This paper characterizes the fundamental sample-communication complexity trade-off in federated Q-learning for collaborative reinforcement learning across multiple agents.

## Abstract

We consider the problem of Federated Q-learning, where $M$ agents aim to collaboratively learn the optimal Q-function of an unknown infinite horizon Markov Decision Process with finite state and action spaces. We investigate the trade-off between sample and communication complexity for the widely used class of intermittent communication algorithms. We first establish the converse result, where we show that any Federated Q-learning that offers a linear speedup with respect to number of agents in sample complexity needs to incur a communication cost of at least $\Omega(\frac{1}{1-\gamma})$, where $\gamma$ is the discount factor. We also propose a new Federated Q-learning algorithm, called Fed-DVR-Q, which is the first Federated Q-learning algorithm to simultaneously achieve order-optimal sample and communication complexities. Thus, together these results provide a complete characterization of the sample-communication complexity trade-off in Federated Q-learning.