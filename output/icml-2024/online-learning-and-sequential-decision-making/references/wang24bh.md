---
title: "LLM-Empowered State Representation for Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/wang24bh.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24bh/wang24bh.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'online-learning-and-sequential-decision-making']
tags: ['reinforcement-learning', 'state-representation', 'large-language-models', 'reward-shaping']
venue: "ICML 2024"
tldr: "Leverages LLMs to enrich state representations in reinforcement learning, improving value network accuracy and sample efficiency."
---

# LLM-Empowered State Representation for Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/wang24bh.html](https://proceedings.mlr.press/v235/wang24bh.html)

**TLDR**: Leverages LLMs to enrich state representations in reinforcement learning, improving value network accuracy and sample efficiency.

## Abstract

Conventional state representations in reinforcement learning often omit critical task-related details, presenting a significant challenge for value networks in establishing accurate mappings from states to task rewards. Traditional methods typically depend on extensive sample learning to enrich state representations with task-specific information, which leads to low sample efficiency and high time costs. Recently, surging knowledgeable large language models (LLM) have provided promising substitutes for prior injection with minimal human intervention. Motivated by this, we propose LLM-Empowered State Representation (LESR), a novel approach that utilizes LLM to autonomously generate task-related state representation codes which help to enhance the continuity of network mappings and facilitate efficient training. Experimental results demonstrate LESR exhibits high sample efficiency and outperforms state-of-the-art baselines by an average of 29% in accumulated reward in Mujoco tasks and 30% in success rates in Gym-Robotics tasks. Codes of LESR are accessible at https://github.com/thu-rllab/LESR.