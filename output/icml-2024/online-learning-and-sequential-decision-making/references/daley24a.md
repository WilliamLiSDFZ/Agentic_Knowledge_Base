---
title: "Averaging $n$-step Returns Reduces Variance in Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/daley24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/daley24a/daley24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['multistep-returns', 'variance-reduction', 'reinforcement-learning', 'n-step-returns', 'lambda-returns']
venue: "ICML 2024"
tldr: "Shows that averaging n-step returns reduces variance compared to individual n-step returns, improving sample efficiency in reinforcement learning."
---

# Averaging $n$-step Returns Reduces Variance in Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/daley24a.html](https://proceedings.mlr.press/v235/daley24a.html)

**TLDR**: Shows that averaging n-step returns reduces variance compared to individual n-step returns, improving sample efficiency in reinforcement learning.

## Abstract

Multistep returns, such as $n$-step returns and $\lambda$-returns, are commonly used to improve the sample efficiency of reinforcement learning (RL) methods. The variance of the multistep returns becomes the limiting factor in their length; looking too far into the future increases variance and reverses the benefits of multistep learning. In our work, we demonstrate the ability of compound returns—weighted averages of $n$-step returns—to reduce variance. We prove for the first time that any compound return with the same contraction modulus as a given $n$-step return has strictly lower variance. We additionally prove that this variance-reduction property improves the finite-sample complexity of temporal-difference learning under linear function approximation. Because general compound returns can be expensive to implement, we introduce two-bootstrap returns which reduce variance while remaining efficient, even when using minibatched experience replay. We conduct experiments showing that compound returns often increase the sample efficiency of $n$-step deep RL agents like DQN and PPO.