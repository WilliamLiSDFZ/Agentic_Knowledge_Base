---
title: "Towards Robust Model-Based Reinforcement Learning Against Adversarial Corruption"
source: "https://proceedings.mlr.press/v235/ye24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ye24a/ye24a.pdf"
categories: ['adversarial-robustness-and-model-security']
tags: ['model-based-RL', 'adversarial-corruption', 'robustness', 'reinforcement-learning']
venue: "ICML 2024"
tldr: "A robust model-based reinforcement learning framework is developed to handle adversarial corruption in transition dynamics."
---

# Towards Robust Model-Based Reinforcement Learning Against Adversarial Corruption

**Source**: [https://proceedings.mlr.press/v235/ye24a.html](https://proceedings.mlr.press/v235/ye24a.html)

**TLDR**: A robust model-based reinforcement learning framework is developed to handle adversarial corruption in transition dynamics.

## Abstract

This study tackles the challenges of adversarial corruption in model-based reinforcement learning (RL), where the transition dynamics can be corrupted by an adversary. Existing studies on corruption-robust RL mostly focus on the setting of model-free RL, where robust least-square regression is often employed for value function estimation. However, these techniques cannot be directly applied to model-based RL. In this paper, we focus on model-based RL and take the maximum likelihood estimation (MLE) approach to learn transition model. Our work encompasses both online and offline settings. In the online setting, we introduce an algorithm called corruption-robust optimistic MLE (CR-OMLE), which leverages total-variation (TV)-based information ratios as uncertainty weights for MLE. We prove that CR-OMLE achieves a regret of $\tilde{\mathcal{O}}(\sqrt{T} + C)$, where $C$ denotes the cumulative corruption level after $T$ episodes. We also prove a lower bound to show that the additive dependence on $C$ is optimal. We extend our weighting technique to the offline setting, and propose an algorithm named corruption-robust pessimistic MLE (CR-PMLE). Under a uniform coverage condition, CR-PMLE exhibits suboptimality worsened by $\mathcal{O}(C/n)$, nearly matching the lower bound. To the best of our knowledge, this is the first work on corruption-robust model-based RL algorithms with provable guarantees.