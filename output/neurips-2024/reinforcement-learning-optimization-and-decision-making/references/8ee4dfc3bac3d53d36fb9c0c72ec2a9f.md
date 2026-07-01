---
title: "An Accelerated Algorithm for Stochastic Bilevel Optimization under Unbounded Smoothness"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/8ee4dfc3bac3d53d36fb9c0c72ec2a9f-Abstract-Conference.html"
categories: ['stochastic-optimization-convergence-and-variance-reduction', 'reinforcement-learning-optimization-and-decision-making']
tags: ['bilevel-optimization', 'unbounded-smoothness', 'stochastic-optimization']
venue: "NeurIPS 2024"
tldr: "An accelerated algorithm for stochastic bilevel optimization with nonconvex upper-level functions exhibiting potentially unbounded smoothness."
---

# An Accelerated Algorithm for Stochastic Bilevel Optimization under Unbounded Smoothness

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/8ee4dfc3bac3d53d36fb9c0c72ec2a9f-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/8ee4dfc3bac3d53d36fb9c0c72ec2a9f-Abstract-Conference.html)

**TLDR**: An accelerated algorithm for stochastic bilevel optimization with nonconvex upper-level functions exhibiting potentially unbounded smoothness.

## Abstract

This paper investigates a class of stochastic bilevel optimization problems where the upper-level function is nonconvex with potentially unbounded smoothness and the lower-level problem is strongly convex. These problems have significant applications in sequential data learning, such as text classification using recurrent neural networks. The unbounded smoothness is characterized by the smoothness constant of the upper-level function scaling linearly with the gradient norm, lacking a uniform upper bound. Existing state-of-the-art algorithms require $\widetilde{O}(\epsilon^{-4})$ oracle calls of stochastic gradient or Hessian/Jacobian-vector product to find an $\epsilon$-stationary point. However, it remains unclear if we can further improve the convergence rate when the assumptions for the function in the population level also hold for each random realization almost surely (e.g., Lipschitzness of each realization of the stochastic gradient). To address this issue, we propose a new Accelerated Bilevel Optimization algorithm named AccBO. The algorithm updates the upper-level variable by normalized stochastic gradient descent with recursive momentum and the lower-level variable by the stochastic Nesterov accelerated gradient descent algorithm with averaging. We prove that our algorithm achieves an oracle complexity of $\widetilde{O}(\epsilon^{-3})$ to find an $\epsilon$-stationary point, when the lower-level stochastic gradient has a small variance $O(\epsilon)$. Our proof relies on a novel lemma characterizing the dynamics of stochastic Nesterov accelerated gradient descent algorithm under distribution drift with high probability for the lower-level variable, which is of independent interest and also plays a crucial role in analyzing the hypergradient estimation error over time. Experimental results on various tasks confirm that our proposed algorithm achieves the predicted theoretical acceleration and significantly outperforms baselines in bilevel optimization.