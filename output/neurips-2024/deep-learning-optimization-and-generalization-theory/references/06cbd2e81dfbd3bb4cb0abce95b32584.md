---
title: "Optimizing Automatic Differentiation with Deep Reinforcement Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/06cbd2e81dfbd3bb4cb0abce95b32584-Abstract-Conference.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'deep-learning-optimization-and-generalization-theory']
tags: ['automatic-differentiation', 'jacobian-computation', 'deep-reinforcement-learning']
venue: "NeurIPS 2024"
tldr: "Deep reinforcement learning is used to optimize automatic differentiation schedules, reducing computational cost of Jacobian computations."
---

# Optimizing Automatic Differentiation with Deep Reinforcement Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/06cbd2e81dfbd3bb4cb0abce95b32584-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/06cbd2e81dfbd3bb4cb0abce95b32584-Abstract-Conference.html)

**TLDR**: Deep reinforcement learning is used to optimize automatic differentiation schedules, reducing computational cost of Jacobian computations.

## Abstract

Computing Jacobians with automatic differentiation is ubiquitous in many scientific domains such as machine learning, computational fluid dynamics, robotics and finance. Even small savings in the number of computations or memory usage in Jacobian computations can already incur massive savings in energy consumption and runtime. While there exist many methods that allow for such savings, they generally trade computational efficiency for approximations of the exact Jacobian.In this paper, we present a novel method to optimize the number of necessary multiplications for Jacobian computation by leveraging deep reinforcement learning (RL) and a concept called cross-country elimination while still computing the exact Jacobian. Cross-country elimination is a framework for automatic differentiation that phrases Jacobian accumulation as ordered elimination of all vertices on the computational graph where every elimination incurs a certain computational cost.Finding the optimal elimination order that minimizes the number of necessary multiplications can be seen as a single player game which in our case is played by an RL agent.We demonstrate that this method achieves up to 33% improvements over state-of-the-art methods on several relevant tasks taken from relevant domains.Furthermore, we show that these theoretical gains translate into actual runtime improvements by providing a cross-country elimination interpreter in JAX that can execute the obtained elimination orders.