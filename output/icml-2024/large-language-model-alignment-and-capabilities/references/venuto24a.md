---
title: "Code as Reward: Empowering Reinforcement Learning with VLMs"
source: "https://proceedings.mlr.press/v235/venuto24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/venuto24a/venuto24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'large-language-model-alignment-and-capabilities']
tags: ['reinforcement-learning', 'vision-language-models', 'reward-generation', 'code-as-reward', 'VLM']
venue: "ICML 2024"
tldr: "Leverages Vision-Language Models to generate code-based reward functions for training reinforcement learning agents on complex visual tasks."
---

# Code as Reward: Empowering Reinforcement Learning with VLMs

**Source**: [https://proceedings.mlr.press/v235/venuto24a.html](https://proceedings.mlr.press/v235/venuto24a.html)

**TLDR**: Leverages Vision-Language Models to generate code-based reward functions for training reinforcement learning agents on complex visual tasks.

## Abstract

Pre-trained Vision-Language Models (VLMs) are able to understand visual concepts, describe and decompose complex tasks into sub-tasks, and provide feedback on task completion. In this paper, we aim to leverage these capabilities to support the training of reinforcement learning (RL) agents. In principle, VLMs are well suited for this purpose, as they can naturally analyze image-based observations and provide feedback (reward) on learning progress. However, inference in VLMs is computationally expensive, so querying them frequently to compute rewards would significantly slowdown the training of an RL agent. To address this challenge, we propose a framework named Code as Reward (VLM-CaR). VLM-CaR produces dense reward functions from VLMs through code generation, thereby significantly reducing the computational burden of querying the VLM directly. We show that the dense rewards generated through our approach are very accurate across a diverse set of discrete and continuous environments, and can be more effective in training RL policies than the original sparse environment rewards.