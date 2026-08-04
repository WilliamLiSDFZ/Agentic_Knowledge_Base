---
title: "Reinforcement Learning and Regret Bounds for Admission Control"
source: "https://proceedings.mlr.press/v235/weber24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/weber24a/weber24a.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['reinforcement-learning', 'admission-control', 'regret-bounds']
venue: "ICML 2024"
tldr: "This paper derives reinforcement learning regret bounds for admission control problems, exploiting their specific MDP structure."
---

# Reinforcement Learning and Regret Bounds for Admission Control

**Source**: [https://proceedings.mlr.press/v235/weber24a.html](https://proceedings.mlr.press/v235/weber24a.html)

**TLDR**: This paper derives reinforcement learning regret bounds for admission control problems, exploiting their specific MDP structure.

## Abstract

The expected regret of any reinforcement learning algorithm is lower bounded by $\Omega\left(\sqrt{DXAT}\right)$ for undiscounted returns, where $D$ is the diameter of the Markov decision process, $X$ the size of the state space, $A$ the size of the action space and $T$ the number of time steps. However, this lower bound is general. A smaller regret can be obtained by taking into account some specific knowledge of the problem structure. In this article, we consider an admission control problem to an $M/M/c/S$ queue with $m$ job classes and class-dependent rewards and holding costs. Queuing systems often have a diameter that is exponential in the buffer size $S$, making the previous lower bound prohibitive for any practical use. We propose an algorithm inspired by UCRL2, and use the structure of the problem to upper bound the expected total regret by $O(S\log T + \sqrt{mT \log T})$ in the finite server case. In the infinite server case, we prove that the dependence of the regret on $S$ disappears.