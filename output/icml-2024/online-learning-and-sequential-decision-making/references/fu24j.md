---
title: "FuRL: Visual-Language Models as Fuzzy Rewards for Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/fu24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fu24j/fu24j.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'online-learning-and-sequential-decision-making']
tags: ['visual-language-models', 'reward-shaping', 'sparse-rewards']
venue: "ICML 2024"
tldr: "VLMs are used as fuzzy reward signals for online RL, with a method to address reward misalignment in sparse-reward tasks."
---

# FuRL: Visual-Language Models as Fuzzy Rewards for Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/fu24j.html](https://proceedings.mlr.press/v235/fu24j.html)

**TLDR**: VLMs are used as fuzzy reward signals for online RL, with a method to address reward misalignment in sparse-reward tasks.

## Abstract

In this work, we investigate how to leverage pre-trained visual-language models (VLM) for online Reinforcement Learning (RL). In particular, we focus on sparse reward tasks with pre-defined textual task descriptions. We first identify the problem of reward misalignment when applying VLM as a reward in RL tasks. To address this issue, we introduce a lightweight fine-tuning method, named Fuzzy VLM reward-aided RL (FuRL), based on reward alignment and relay RL. Specifically, we enhance the performance of SAC/DrQ baseline agents on sparse reward tasks by fine-tuning VLM representations and using relay RL to avoid local minima. Extensive experiments on the Meta-world benchmark tasks demonstrate the efficacy of the proposed method. Code is available at: https://github.com/fuyw/FuRL.