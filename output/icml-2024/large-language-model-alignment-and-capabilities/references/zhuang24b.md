---
title: "Reinformer: Max-Return Sequence Modeling for Offline RL"
source: "https://proceedings.mlr.press/v235/zhuang24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhuang24b/zhuang24b.pdf"
categories: ['online-learning-and-sequential-decision-making', 'large-language-model-alignment-and-capabilities']
tags: ['offline-RL', 'sequence-modeling', 'transformers', 'return-maximization', 'decision-making']
venue: "ICML 2024"
tldr: "Reinformer reformulates offline reinforcement learning as max-return sequence modeling to better align the supervised training objective with RL's return-maximization goal."
---

# Reinformer: Max-Return Sequence Modeling for Offline RL

**Source**: [https://proceedings.mlr.press/v235/zhuang24b.html](https://proceedings.mlr.press/v235/zhuang24b.html)

**TLDR**: Reinformer reformulates offline reinforcement learning as max-return sequence modeling to better align the supervised training objective with RL's return-maximization goal.

## Abstract

As a data-driven paradigm, offline reinforcement learning (RL) has been formulated as sequence modeling that conditions on the hindsight information including returns, goal or future trajectory. Although promising, this supervised paradigm overlooks the core objective of RL that maximizes the return. This overlook directly leads to the lack of trajectory stitching capability that affects the sequence model learning from sub-optimal data. In this work, we introduce the concept of max-return sequence modeling which integrates the goal of maximizing returns into existing sequence models. We propose Reinforced Transformer (Reinformer), indicating the sequence model is reinforced by the RL objective. Reinformer additionally incorporates the objective of maximizing returns in the training phase, aiming to predict the maximum future return within the distribution. During inference, this in-distribution maximum return will guide the selection of optimal actions. Empirically, Reinformer is competitive with classical RL methods on the D4RL benchmark and outperforms state-of-the-art sequence model particularly in trajectory stitching ability. Code is public at https://github.com/Dragon-Zhuang/Reinformer.