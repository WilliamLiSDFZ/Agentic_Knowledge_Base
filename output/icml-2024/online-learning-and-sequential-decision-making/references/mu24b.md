---
title: "On the Second-Order Convergence of Biased Policy Gradient Algorithms"
source: "https://proceedings.mlr.press/v235/mu24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mu24b/mu24b.pdf"
categories: ['optimization-algorithms-convergence-theory', 'online-learning-and-sequential-decision-making']
tags: ['policy-gradient', 'second-order-convergence', 'saddle-points', 'biased-estimators']
venue: "ICML 2024"
tldr: "Second-order convergence guarantees for biased policy gradient algorithms are established, showing escape from saddle points to second-order stationary points."
---

# On the Second-Order Convergence of Biased Policy Gradient Algorithms

**Source**: [https://proceedings.mlr.press/v235/mu24b.html](https://proceedings.mlr.press/v235/mu24b.html)

**TLDR**: Second-order convergence guarantees for biased policy gradient algorithms are established, showing escape from saddle points to second-order stationary points.

## Abstract

Since the objective functions of reinforcement learning problems are typically highly nonconvex, it is desirable that policy gradient, the most popular algorithm, escapes saddle points and arrives at second-order stationary points. Existing results only consider vanilla policy gradient algorithms with unbiased gradient estimators, but practical implementations under the infinite-horizon discounted reward setting are biased due to finite-horizon sampling. Moreover, actor-critic methods, whose second-order convergence has not yet been established, are also biased due to the critic approximation of the value function. We provide a novel second-order analysis of biased policy gradient methods, including the vanilla gradient estimator computed from Monte-Carlo sampling of trajectories as well as the double-loop actor-critic algorithm, where in the inner loop the critic improves the approximation of the value function via TD(0) learning. Separately, we also establish the convergence of TD(0) on Markov chains irrespective of initial state distribution.