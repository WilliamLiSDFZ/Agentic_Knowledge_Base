---
title: "ReLU to the Rescue: Improve Your On-Policy Actor-Critic with Positive Advantages"
source: "https://proceedings.mlr.press/v235/jesson24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jesson24a/jesson24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['actor-critic', 'Bayesian-inference', 'advantage-estimation', 'ReLU', 'spectral-normalization']
venue: "ICML 2024"
tldr: "Applying ReLU to advantage estimates and spectral normalization in A3C moves on-policy actor-critic toward approximate Bayesian inference and improves performance."
---

# ReLU to the Rescue: Improve Your On-Policy Actor-Critic with Positive Advantages

**Source**: [https://proceedings.mlr.press/v235/jesson24a.html](https://proceedings.mlr.press/v235/jesson24a.html)

**TLDR**: Applying ReLU to advantage estimates and spectral normalization in A3C moves on-policy actor-critic toward approximate Bayesian inference and improves performance.

## Abstract

This paper proposes a step toward approximate Bayesian inference in on-policy actor-critic deep reinforcement learning. It is implemented through three changes to the Asynchronous Advantage Actor-Critic (A3C) algorithm: (1) applying a ReLU function to advantage estimates, (2) spectral normalization of actor-critic weights, and (3) incorporating dropout as a Bayesian approximation. We prove under standard assumptions that restricting policy updates to positive advantages optimizes for value by maximizing a lower bound on the value function plus an additive term. We show that the additive term is bounded proportional to the Lipschitz constant of the value function, which offers theoretical grounding for spectral normalization of critic weights. Finally, our application of dropout corresponds to approximate Bayesian inference over both the actor and critic parameters, which enables adaptive state-aware exploration around the modes of the actor via Thompson sampling. We demonstrate significant improvements for median and interquartile mean metrics over A3C, PPO, SAC, and TD3 on the MuJoCo continuous control benchmark and improvement over PPO in the challenging ProcGen generalization benchmark.