---
title: "Operator World Models for Reinforcement Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/c9da56addea9c977cf4ba873e1da979d-Abstract-Conference.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'physics-informed-neural-operators-and-simulations']
tags: ['reinforcement-learning', 'policy-mirror-descent', 'world-models', 'operator-learning', 'action-value-functions']
venue: "NeurIPS 2024"
tldr: "Introduces operator world models to enable Policy Mirror Descent in reinforcement learning settings where explicit action-value functions are inaccessible."
---

# Operator World Models for Reinforcement Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/c9da56addea9c977cf4ba873e1da979d-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/c9da56addea9c977cf4ba873e1da979d-Abstract-Conference.html)

**TLDR**: Introduces operator world models to enable Policy Mirror Descent in reinforcement learning settings where explicit action-value functions are inaccessible.

## Abstract

Policy Mirror Descent (PMD) is a powerful and theoretically sound methodology for sequential decision-making. However, it is not directly applicable to Reinforcement Learning (RL) due to the inaccessibility of explicit action-value functions. We address this challenge by introducing a novel approach based on learning a world model of the environment using conditional mean embeddings. Leveraging tools from operator theory we derive a closed-form expression of the action-value function in terms of the world model via simple matrix operations. Combining these estimators with PMD leads to POWR, a new RL algorithm for which we prove convergence rates to the global optimum. Preliminary experiments in finite and infinite state settings support the effectiveness of our method.