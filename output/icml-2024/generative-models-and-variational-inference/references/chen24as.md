---
title: "Diffusion Model-Augmented Behavioral Cloning"
source: "https://proceedings.mlr.press/v235/chen24as.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24as/chen24as.pdf"
categories: ['generative-models-and-variational-inference', 'online-learning-and-sequential-decision-making']
tags: ['imitation-learning', 'diffusion-models', 'behavioral-cloning', 'offline-RL']
venue: "ICML 2024"
tldr: "Augments behavioral cloning with diffusion model-based data generation to improve imitation learning without environment interaction."
---

# Diffusion Model-Augmented Behavioral Cloning

**Source**: [https://proceedings.mlr.press/v235/chen24as.html](https://proceedings.mlr.press/v235/chen24as.html)

**TLDR**: Augments behavioral cloning with diffusion model-based data generation to improve imitation learning without environment interaction.

## Abstract

Imitation learning addresses the challenge of learning by observing an expert’s demonstrations without access to reward signals from environments. Most existing imitation learning methods that do not require interacting with environments either model the expert distribution as the conditional probability p(a|s) (e.g., behavioral cloning, BC) or the joint probability p(s, a). Despite the simplicity of modeling the conditional probability with BC, it usually struggles with generalization. While modeling the joint probability can improve generalization performance, the inference procedure is often time-consuming, and the model can suffer from manifold overfitting. This work proposes an imitation learning framework that benefits from modeling both the conditional and joint probability of the expert distribution. Our proposed Diffusion Model-Augmented Behavioral Cloning (DBC) employs a diffusion model trained to model expert behaviors and learns a policy to optimize both the BC loss (conditional) and our proposed diffusion model loss (joint). DBC outperforms baselines in various continuous control tasks in navigation, robot arm manipulation, dexterous manipulation, and locomotion. We design additional experiments to verify the limitations of modeling either the conditional probability or the joint probability of the expert distribution, as well as compare different generative models. Ablation studies justify the effectiveness of our design choices.