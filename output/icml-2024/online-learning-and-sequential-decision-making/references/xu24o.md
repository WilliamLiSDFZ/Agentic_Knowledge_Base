---
title: "Meta-Reinforcement Learning Robust to Distributional Shift Via Performing Lifelong In-Context Learning"
source: "https://proceedings.mlr.press/v235/xu24o.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24o/xu24o.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['meta-reinforcement-learning', 'in-context-learning', 'distributional-shift']
venue: "ICML 2024"
tldr: "A posterior sampling Bayesian lifelong in-context RL method is proposed to improve meta-RL robustness under task distribution shift."
---

# Meta-Reinforcement Learning Robust to Distributional Shift Via Performing Lifelong In-Context Learning

**Source**: [https://proceedings.mlr.press/v235/xu24o.html](https://proceedings.mlr.press/v235/xu24o.html)

**TLDR**: A posterior sampling Bayesian lifelong in-context RL method is proposed to improve meta-RL robustness under task distribution shift.

## Abstract

A key challenge in Meta-Reinforcement Learning (meta-RL) is the task distribution shift, since the generalization ability of most current meta-RL methods is limited to tasks sampled from the training distribution. In this paper, we propose Posterior Sampling Bayesian Lifelong In-Context Reinforcement Learning (PSBL), which is robust to task distribution shift. PSBL meta-trains a variant of transformer to directly perform amortized inference about the Predictive Posterior Distribution (PPD) of the optimal policy. Once trained, the network can infer the PPD online with frozen parameters. The agent then samples actions from the approximate PPD to perform online exploration, which progressively reduces uncertainty and enhances performance in the interaction with the environment. This property is known as in-context learning. Experimental results demonstrate that PSBL significantly outperforms standard Meta RL methods both in tasks with sparse rewards and dense rewards when the test task distribution is strictly shifted from the training distribution.