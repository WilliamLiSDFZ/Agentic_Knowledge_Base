---
title: "Learning Optimal Deterministic Policies with Stochastic Policy Gradients"
source: "https://proceedings.mlr.press/v235/montenegro24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/montenegro24a/montenegro24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['policy-gradient', 'deterministic-policies', 'stochastic-optimization', 'reinforcement-learning']
venue: "ICML 2024"
tldr: "A framework is proposed to learn optimal deterministic policies by leveraging stochastic policy gradient methods while providing theoretical guarantees for convergence."
---

# Learning Optimal Deterministic Policies with Stochastic Policy Gradients

**Source**: [https://proceedings.mlr.press/v235/montenegro24a.html](https://proceedings.mlr.press/v235/montenegro24a.html)

**TLDR**: A framework is proposed to learn optimal deterministic policies by leveraging stochastic policy gradient methods while providing theoretical guarantees for convergence.

## Abstract

Policy gradient (PG) methods are successful approaches to deal with continuous reinforcement learning (RL) problems. They learn stochastic parametric (hyper)policies by either exploring in the space of actions or in the space of parameters. Stochastic controllers, however, are often undesirable from a practical perspective because of their lack of robustness, safety, and traceability. In common practice, stochastic (hyper)policies are learned only to deploy their deterministic version. In this paper, we make a step towards the theoretical understanding of this practice. After introducing a novel framework for modeling this scenario, we study the global convergence to the best deterministic policy, under (weak) gradient domination assumptions. Then, we illustrate how to tune the exploration level used for learning to optimize the trade-off between the sample complexity and the performance of the deployed deterministic policy. Finally, we quantitatively compare action-based and parameter-based exploration, giving a formal guise to intuitive results.