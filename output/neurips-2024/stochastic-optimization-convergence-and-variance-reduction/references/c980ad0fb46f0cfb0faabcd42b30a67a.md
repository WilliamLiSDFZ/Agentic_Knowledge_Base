---
title: "Random Function Descent"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/c980ad0fb46f0cfb0faabcd42b30a67a-Abstract-Conference.html"
categories: ['deep-learning-optimization-and-generalization-theory', 'stochastic-optimization-convergence-and-variance-reduction']
tags: ['stochastic-optimization', 'random-function', 'step-size-selection', 'convergence', 'learning-theory']
venue: "NeurIPS 2024"
tldr: "Proposes a random function framework for optimization theory that better explains machine learning success and enables principled step-size selection."
---

# Random Function Descent

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/c980ad0fb46f0cfb0faabcd42b30a67a-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/c980ad0fb46f0cfb0faabcd42b30a67a-Abstract-Conference.html)

**TLDR**: Proposes a random function framework for optimization theory that better explains machine learning success and enables principled step-size selection.

## Abstract

Classical worst-case optimization theory neither explains the success of optimization in machine learning, nor does it help with step size selection. In this paper we demonstrate the viability and advantages of replacing the classical 'convex function' framework with a 'random function' framework. With complexity $\mathcal{O}(n^3d^3)$, where $n$ is the number of steps and $d$ the number of dimensions, Bayesian optimization with gradients has not been viable in large dimension so far. By bridging the gap between Bayesian optimization (i.e. random function optimization theory) and classical optimization we establish viability. Specifically, we use a 'stochastic Taylor approximation' to rediscover gradient descent, which is scalable in high dimension due to $\mathcal{O}(nd)$ complexity. This rediscovery yields a specific step size schedule we call Random Function Descent (RFD). The advantage of this random function framework is that RFD is scale invariant and that it provides a theoretical foundation for common step size heuristics such as gradient clipping and gradual learning rate warmup.