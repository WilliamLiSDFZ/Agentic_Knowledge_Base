---
title: "In-Context Reinforcement Learning for Variable Action Spaces"
source: "https://proceedings.mlr.press/v235/sinii24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sinii24a/sinii24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'large-language-model-alignment-and-capabilities']
tags: ['in-context-learning', 'transformers', 'variable-action-spaces', 'meta-RL']
venue: "ICML 2024"
tldr: "A transformer-based in-context RL method is proposed that generalizes to new tasks with variable and previously unseen action space sizes and structures."
---

# In-Context Reinforcement Learning for Variable Action Spaces

**Source**: [https://proceedings.mlr.press/v235/sinii24a.html](https://proceedings.mlr.press/v235/sinii24a.html)

**TLDR**: A transformer-based in-context RL method is proposed that generalizes to new tasks with variable and previously unseen action space sizes and structures.

## Abstract

Recently, it has been shown that transformers pre-trained on diverse datasets with multi-episode contexts can generalize to new reinforcement learning tasks in-context. A key limitation of previously proposed models is their reliance on a predefined action space size and structure. The introduction of a new action space often requires data re-collection and model re-training, which can be costly for some applications. In our work, we show that it is possible to mitigate this issue by proposing the Headless-AD model that, despite being trained only once, is capable of generalizing to discrete action spaces of variable size, semantic content and order. By experimenting with Bernoulli and contextual bandits, as well as a gridworld environment, we show that Headless-AD exhibits significant capability to generalize to action spaces it has never encountered, even outperforming specialized models trained for a specific set of actions on several environment configurations.