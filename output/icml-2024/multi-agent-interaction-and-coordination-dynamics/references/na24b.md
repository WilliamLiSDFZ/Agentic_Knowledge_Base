---
title: "LAGMA: LAtent Goal-guided Multi-Agent Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/na24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/na24b/na24b.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics']
tags: ['multi-agent-reinforcement-learning', 'goal-conditioned', 'latent-goals']
venue: "ICML 2024"
tldr: "LAGMA uses latent goal guidance to accelerate cooperative multi-agent reinforcement learning toward semantic goals in complex tasks."
---

# LAGMA: LAtent Goal-guided Multi-Agent Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/na24b.html](https://proceedings.mlr.press/v235/na24b.html)

**TLDR**: LAGMA uses latent goal guidance to accelerate cooperative multi-agent reinforcement learning toward semantic goals in complex tasks.

## Abstract

In cooperative multi-agent reinforcement learning (MARL), agents collaborate to achieve common goals, such as defeating enemies and scoring a goal. However, learning goal-reaching paths toward such a semantic goal takes a considerable amount of time in complex tasks and the trained model often fails to find such paths. To address this, we present LAtent Goal-guided Multi-Agent reinforcement learning (LAGMA), which generates a goal-reaching trajectory in latent space and provides a latent goal-guided incentive to transitions toward this reference trajectory. LAGMA consists of three major components: (a) quantized latent space constructed via a modified VQ-VAE for efficient sample utilization, (b) goal-reaching trajectory generation via extended VQ codebook, and (c) latent goal-guided intrinsic reward generation to encourage transitions towards the sampled goal-reaching path. The proposed method is evaluated by StarCraft II with both dense and sparse reward settings and Google Research Football. Empirical results show further performance improvement over state-of-the-art baselines.