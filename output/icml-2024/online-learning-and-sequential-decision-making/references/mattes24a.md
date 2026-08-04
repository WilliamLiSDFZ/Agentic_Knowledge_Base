---
title: "Hieros: Hierarchical Imagination on Structured State Space Sequence World Models"
source: "https://proceedings.mlr.press/v235/mattes24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mattes24a/mattes24a.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['world-models', 'hierarchical-imagination', 'structured-state-space']
venue: "ICML 2024"
tldr: "A hierarchical world model using structured state space sequences to improve sample efficiency in deep reinforcement learning."
---

# Hieros: Hierarchical Imagination on Structured State Space Sequence World Models

**Source**: [https://proceedings.mlr.press/v235/mattes24a.html](https://proceedings.mlr.press/v235/mattes24a.html)

**TLDR**: A hierarchical world model using structured state space sequences to improve sample efficiency in deep reinforcement learning.

## Abstract

One of the biggest challenges to modern deep reinforcement learning (DRL) algorithms is sample efficiency. Many approaches learn a world model in order to train an agent entirely in imagination, eliminating the need for direct environment interaction during training. However, these methods often suffer from either a lack of imagination accuracy, exploration capabilities, or runtime efficiency. We propose HIEROS, a hierarchical policy that learns time abstracted world representations and imagines trajectories at multiple time scales in latent space. HIEROS uses an S5 layer-based world model, which predicts next world states in parallel during training and iteratively during environment interaction. Due to the special properties of S5 layers, our method can train in parallel and predict next world states iteratively during imagination. This allows for more efficient training than RNN-based world models and more efficient imagination than Transformer-based world models. We show that our approach outperforms the state of the art in terms of mean and median normalized human score on the Atari 100k benchmark, and that our proposed world model is able to predict complex dynamics very accurately. We also show that HIEROS displays superior exploration capabilities compared to existing approaches.