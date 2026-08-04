---
title: "ODIN: Disentangled Reward Mitigates Hacking in RLHF"
source: "https://proceedings.mlr.press/v235/chen24bn.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24bn/chen24bn.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'fairness-aware-algorithmic-decision-making']
tags: ['RLHF', 'reward-hacking', 'length-bias']
venue: "ICML 2024"
tldr: "ODIN disentangles reward signals to mitigate length-based reward hacking in reinforcement learning from human feedback."
---

# ODIN: Disentangled Reward Mitigates Hacking in RLHF

**Source**: [https://proceedings.mlr.press/v235/chen24bn.html](https://proceedings.mlr.press/v235/chen24bn.html)

**TLDR**: ODIN disentangles reward signals to mitigate length-based reward hacking in reinforcement learning from human feedback.

## Abstract

In this work, we study the issue of reward hacking on the response length, a challenge emerging in Reinforcement Learning from Human Feedback (RLHF) on LLMs. A well-formatted, verbose but less helpful response from the LLMs can often deceive LLMs or even human evaluators and achieve high scores. The same issue also holds for some reward models in RL. To address the challenges in both training and evaluation, we establish a more reliable evaluation protocol for comparing different training configurations, which inspects the trade-off between LLM evaluation score and response length obtained by varying training hyperparameters. Based on this evaluation, we conduct large-scale studies, where the results shed insights into the efficacy of hyperparameters and tricks used in RL on mitigating length bias. We further propose to improve the reward model by jointly training two linear heads to predict the preference, one trained to correlate with length and the other trained to decorrelate with length and therefore focusing more on the actual content. We then discard the length head in RL to ignore the spurious length reward. Experiments demonstrate that our approach eliminates the reward correlation with length, and improves the obtained policy by a significant margin.