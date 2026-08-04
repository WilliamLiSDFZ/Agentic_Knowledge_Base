---
title: "ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL"
source: "https://proceedings.mlr.press/v235/zhou24t.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhou24t/zhou24t.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'online-learning-and-sequential-decision-making']
tags: ['language-model-agents', 'hierarchical-RL', 'multi-turn-dialogue']
venue: "ICML 2024"
tldr: "Presents ArCHer, a hierarchical multi-turn RL framework for training LLM agents to optimize long-term objectives in sequential decision-making tasks."
---

# ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL

**Source**: [https://proceedings.mlr.press/v235/zhou24t.html](https://proceedings.mlr.press/v235/zhou24t.html)

**TLDR**: Presents ArCHer, a hierarchical multi-turn RL framework for training LLM agents to optimize long-term objectives in sequential decision-making tasks.

## Abstract

Large language models (LLMs) have the potential to tackle sequential decision-making problems due to their generalist capabilities. Instead of optimizing “myopic” surrogate objectives such as human preferences within a single turn, in such problems, we wish to directly optimize long-term objectives, such as user satisfaction over an entire dialogue with an LLM or delayed success metrics in web navigation. Multi-turn reinforcement learning (RL) provides an appealing approach to directly optimize long-term objectives, but how can we design effective and efficient multi-turn RL algorithms for LLMs? In this work, we propose an algorithmic framework to multi-turn RL for LLMs that preserves the flexibility of token-by-token RL used in single-turn RL problems, while still accommodating long horizons and delayed rewards more effectively. Our framework, the Actor-Critic Framework with a Hierarchical Structure (ArCHer), combines a high-level off-policy RL algorithm that trains a value function with a low-level RL algorithm that trains a token-by-token policy. While ArCHer can be instantiated with multiple RL algorithms, a particularly convenient instantiation is to use temporal difference (TD) learning at the high level and on-policy token-level policy gradient at the low level. Empirically, we show that ArCHer significantly improves efficiency and performance of multi-turn LLM tasks, attaining sample efficiency boosts of about 100x over prior on-policy methods and converging to a much better performance than other off-policy methods.