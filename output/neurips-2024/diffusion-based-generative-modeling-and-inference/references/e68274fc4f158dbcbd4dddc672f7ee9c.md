---
title: "Bridging Model-Based Optimization and Generative Modeling via Conservative Fine-Tuning of Diffusion Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e68274fc4f158dbcbd4dddc672f7ee9c-Abstract-Conference.html"
categories: ['diffusion-based-generative-modeling-and-inference', 'machine-learning-for-molecular-biology']
tags: ['diffusion-models', 'model-based-optimization', 'conservative-fine-tuning', 'sequence-design']
venue: "NeurIPS 2024"
tldr: "Bridges generative modeling and model-based optimization by conservatively fine-tuning diffusion models for biological sequence design tasks."
---

# Bridging Model-Based Optimization and Generative Modeling via Conservative Fine-Tuning of Diffusion Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e68274fc4f158dbcbd4dddc672f7ee9c-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/e68274fc4f158dbcbd4dddc672f7ee9c-Abstract-Conference.html)

**TLDR**: Bridges generative modeling and model-based optimization by conservatively fine-tuning diffusion models for biological sequence design tasks.

## Abstract

AI-driven design problems, such as DNA/protein sequence design, are commonly tackled from two angles: generative modeling, which efficiently captures the feasible design space (e.g., natural images or biological sequences), and model-based optimization, which utilizes reward models for extrapolation. To combine the strengths of both approaches, we adopt a hybrid method that fine-tunes cutting-edge diffusion models by optimizing reward models through RL. Although prior work has explored similar avenues, they primarily focus on scenarios where accurate reward models are accessible. In contrast, we concentrate on an offline setting where a reward model is unknown, and we must learn from static offline datasets, a common scenario in scientific domains. In offline scenarios, existing approaches tend to suffer from overoptimization, as they may be misled by the reward model in out-of-distribution regions. To address this, we introduce a conservative fine-tuning approach, BRAID, by optimizing a conservative reward model, which includes additional penalization outside of offline data distributions. Through empirical and theoretical analysis, we demonstrate the capability of our approach to outperform the best designs in offline data, leveraging the extrapolation capabilities of reward models while avoiding the generation of invalid designs through pre-trained diffusion models.