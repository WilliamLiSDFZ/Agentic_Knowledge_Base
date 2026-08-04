---
title: "Value-Evolutionary-Based Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/li24z.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24z/li24z.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['evolutionary-algorithms', 'reinforcement-learning', 'value-based-RL', 'policy-search']
venue: "ICML 2024"
tldr: "A novel framework integrates evolutionary algorithms with value-based reinforcement learning to improve policy search performance."
---

# Value-Evolutionary-Based Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/li24z.html](https://proceedings.mlr.press/v235/li24z.html)

**TLDR**: A novel framework integrates evolutionary algorithms with value-based reinforcement learning to improve policy search performance.

## Abstract

Combining Evolutionary Algorithms (EAs) and Reinforcement Learning (RL) for policy search has been proven to improve RL performance. However, previous works largely overlook value-based RL in favor of merging EAs with policy-based RL. This paper introduces Value-Evolutionary-Based Reinforcement Learning (VEB-RL) that focuses on the integration of EAs with value-based RL. The framework maintains a population of value functions instead of policies and leverages negative Temporal Difference error as the fitness metric for evolution. The metric is more sample-efficient for population evaluation than cumulative rewards and is closely associated with the accuracy of the value function approximation. Additionally, VEB-RL enables elites of the population to interact with the environment to offer high-quality samples for RL optimization, whereas the RL value function participates in the population’s evolution in each generation. Experiments on MinAtar and Atari demonstrate the superiority of VEB-RL in significantly improving DQN, Rainbow, and SPR. Our code is available on https://github.com/yeshenpy/VEB-RL.