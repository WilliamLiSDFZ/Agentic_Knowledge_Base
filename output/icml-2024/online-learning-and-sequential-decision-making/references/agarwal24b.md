---
title: "Learning to Play Atari in a World of Tokens"
source: "https://proceedings.mlr.press/v235/agarwal24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/agarwal24b/agarwal24b.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['model-based-rl', 'transformers', 'discrete-tokens', 'world-models', 'atari']
venue: "ICML 2024"
tldr: "Presents a token-based world model using transformers for model-based RL on Atari with improved sample efficiency."
---

# Learning to Play Atari in a World of Tokens

**Source**: [https://proceedings.mlr.press/v235/agarwal24b.html](https://proceedings.mlr.press/v235/agarwal24b.html)

**TLDR**: Presents a token-based world model using transformers for model-based RL on Atari with improved sample efficiency.

## Abstract

Model-based reinforcement learning agents utilizing transformers have shown improved sample efficiency due to their ability to model extended context, resulting in more accurate world models. However, for complex reasoning and planning tasks, these methods primarily rely on continuous representations. This complicates modeling of discrete properties of the real world such as disjoint object classes between which interpolation is not plausible. In this work, we introduce discrete abstract representations for transformer-based learning (DART), a sample-efficient method utilizing discrete representations for modeling both the world and learning behavior. We incorporate a transformer-decoder for auto-regressive world modeling and a transformer-encoder for learning behavior by attending to task-relevant cues in the discrete representation of the world model. For handling partial observability, we aggregate information from past time steps as memory tokens. DART outperforms previous state-of-the-art methods that do not use look-ahead search on the Atari 100k sample efficiency benchmark with a median human-normalized score of 0.790 and beats humans in 9 out of 26 games. We release our code at https://pranaval.github.io/DART/.