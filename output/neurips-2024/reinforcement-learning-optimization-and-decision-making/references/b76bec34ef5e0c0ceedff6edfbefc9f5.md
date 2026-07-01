---
title: "Foundations of Multivariate Distributional Reinforcement Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/b76bec34ef5e0c0ceedff6edfbefc9f5-Abstract-Conference.html"
categories: ['reinforcement-learning-optimization-and-decision-making']
tags: ['multivariate-rewards', 'distributional-rl', 'multi-objective']
venue: "NeurIPS 2024"
tldr: "This paper introduces the first oracle-free, computationally tractable algorithms for provably correct multivariate distributional reinforcement learning."
---

# Foundations of Multivariate Distributional Reinforcement Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/b76bec34ef5e0c0ceedff6edfbefc9f5-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/b76bec34ef5e0c0ceedff6edfbefc9f5-Abstract-Conference.html)

**TLDR**: This paper introduces the first oracle-free, computationally tractable algorithms for provably correct multivariate distributional reinforcement learning.

## Abstract

In reinforcement learning (RL), the consideration of multivariate reward signals has led to fundamental advancements in multi-objective decision-making, transfer learning, and representation learning. This work introduces the first oracle-free and computationally-tractable algorithms for provably convergent multivariate *distributional* dynamic programming and temporal difference learning. Our convergence rates match the familiar rates in the scalar reward setting, and additionally provide new insights into the fidelity of approximate return distribution representations as a function of the reward dimension. Surprisingly, when the reward dimension is larger than $1$, we show that standard analysis of categorical TD learning fails, which we resolve with a novel projection onto the space of mass-$1$ signed measures. Finally, with the aid of our technical results and simulations, we identify tradeoffs between distribution representations that influence the performance of multivariate distributional RL in practice.