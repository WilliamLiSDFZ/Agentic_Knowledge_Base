---
title: "DiffStitch: Boosting Offline Reinforcement Learning with Diffusion-based Trajectory Stitching"
source: "https://proceedings.mlr.press/v235/li24bf.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bf/li24bf.pdf"
categories: ['online-learning-and-sequential-decision-making', 'generative-models-and-variational-inference']
tags: ['offline-reinforcement-learning', 'diffusion-models', 'trajectory-stitching']
venue: "ICML 2024"
tldr: "Proposes DiffStitch, a diffusion-based trajectory stitching method to improve offline RL performance on datasets with limited optimal trajectories."
---

# DiffStitch: Boosting Offline Reinforcement Learning with Diffusion-based Trajectory Stitching

**Source**: [https://proceedings.mlr.press/v235/li24bf.html](https://proceedings.mlr.press/v235/li24bf.html)

**TLDR**: Proposes DiffStitch, a diffusion-based trajectory stitching method to improve offline RL performance on datasets with limited optimal trajectories.

## Abstract

In offline reinforcement learning (RL), the performance of the learned policy highly depends on the quality of offline datasets. However, the offline dataset contains very limited optimal trajectories in many cases. This poses a challenge for offline RL algorithms, as agents must acquire the ability to transit to high-reward regions. To address this issue, we introduce Diffusionbased Trajectory Stitching (DiffStitch), a novel diffusion-based data augmentation pipeline that systematically generates stitching transitions between trajectories. DiffStitch effectively connects low-reward trajectories with high-reward trajectories, forming globally optimal trajectories and thereby mitigating the challenges faced by offline RL algorithms in learning trajectory stitching. Empirical experiments conducted on D4RL datasets demonstrate the effectiveness of our pipeline across RL methodologies. Notably, DiffStitch demonstrates substantial enhancements in the performance of one-step methods(IQL), imitation learning methods(TD3+BC) and trajectory optimization methods(DT). Our code is publicly available at https://github.com/guangheli12/DiffStitch