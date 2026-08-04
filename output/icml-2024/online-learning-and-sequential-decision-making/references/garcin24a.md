---
title: "DRED: Zero-Shot Transfer in Reinforcement Learning via Data-Regularised Environment Design"
source: "https://proceedings.mlr.press/v235/garcin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/garcin24a/garcin24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'continual-learning-memory-plasticity']
tags: ['reinforcement-learning', 'zero-shot-generalization', 'environment-design']
venue: "ICML 2024"
tldr: "Introduces data-regularized environment design to improve zero-shot transfer in deep reinforcement learning agents."
---

# DRED: Zero-Shot Transfer in Reinforcement Learning via Data-Regularised Environment Design

**Source**: [https://proceedings.mlr.press/v235/garcin24a.html](https://proceedings.mlr.press/v235/garcin24a.html)

**TLDR**: Introduces data-regularized environment design to improve zero-shot transfer in deep reinforcement learning agents.

## Abstract

Autonomous agents trained using deep reinforcement learning (RL) often lack the ability to successfully generalise to new environments, even when these environments share characteristics with the ones they have encountered during training. In this work, we investigate how the sampling of individual environment instances, or levels, affects the zero-shot generalisation (ZSG) ability of RL agents. We discover that, for deep actor-critic architectures sharing their base layers, prioritising levels according to their value loss minimises the mutual information between the agent’s internal representation and the set of training levels in the generated training data. This provides a novel theoretical justification for the regularisation achieved by certain adaptive sampling strategies. We then turn our attention to unsupervised environment design (UED) methods, which assume control over level generation. We find that existing UED methods can significantly shift the training distribution, which translates to low ZSG performance. To prevent both overfitting and distributional shift, we introduce data-regularised environment design (DRED). DRED generates levels using a generative model trained to approximate the ground truth distribution of an initial set of level parameters. Through its grounding, DRED achieves significant improvements in ZSG over adaptive level sampling strategies and UED methods.