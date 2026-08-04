---
title: "Zero-Shot Reinforcement Learning via Function Encoders"
source: "https://proceedings.mlr.press/v235/ingebrand24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ingebrand24a/ingebrand24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'learning-with-imperfect-data-and-bias']
tags: ['zero-shot', 'reinforcement-learning', 'function-encoders', 'task-representation', 'transfer-learning']
venue: "ICML 2024"
tldr: "Function encoders enable zero-shot transfer in reinforcement learning by learning compact task representations that generalize across related tasks."
---

# Zero-Shot Reinforcement Learning via Function Encoders

**Source**: [https://proceedings.mlr.press/v235/ingebrand24a.html](https://proceedings.mlr.press/v235/ingebrand24a.html)

**TLDR**: Function encoders enable zero-shot transfer in reinforcement learning by learning compact task representations that generalize across related tasks.

## Abstract

Although reinforcement learning (RL) can solve many challenging sequential decision making problems, achieving zero-shot transfer across related tasks remains a challenge. The difficulty lies in finding a good representation for the current task so that the agent understands how it relates to previously seen tasks. To achieve zero-shot transfer, we introduce the function encoder, a representation learning algorithm which represents a function as a weighted combination of learned, non-linear basis functions. By using a function encoder to represent the reward function or the transition function, the agent has information on how the current task relates to previously seen tasks via a coherent vector representation. Thus, the agent is able to achieve transfer between related tasks at run time with no additional training. We demonstrate state-of-the-art data efficiency, asymptotic performance, and training stability in three RL fields by augmenting basic RL algorithms with a function encoder task representation.