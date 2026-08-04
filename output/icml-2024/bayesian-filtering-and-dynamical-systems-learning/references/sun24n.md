---
title: "Learning Latent Dynamic Robust Representations for World Models"
source: "https://proceedings.mlr.press/v235/sun24n.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sun24n/sun24n.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning']
tags: ['model-based-rl', 'world-models', 'robust-representations']
venue: "ICML 2024"
tldr: "A visual MBRL method learns latent dynamic robust representations to improve Dreamer-style agents under noisy pixel-based inputs."
---

# Learning Latent Dynamic Robust Representations for World Models

**Source**: [https://proceedings.mlr.press/v235/sun24n.html](https://proceedings.mlr.press/v235/sun24n.html)

**TLDR**: A visual MBRL method learns latent dynamic robust representations to improve Dreamer-style agents under noisy pixel-based inputs.

## Abstract

Visual Model-Based Reinforcement Learning (MBRL) promises to encapsulate agent’s knowledge about the underlying dynamics of the environment, enabling learning a world model as a useful planner. However, top MBRL agents such as Dreamer often struggle with visual pixel-based inputs in the presence of exogenous or irrelevant noise in the observation space, due to failure to capture task-specific features while filtering out irrelevant spatio-temporal details. To tackle this problem, we apply a spatio-temporal masking strategy, a bisimulation principle, combined with latent reconstruction, to capture endogenous task-specific aspects of the environment for world models, effectively eliminating non-essential information. Joint training of representations, dynamics, and policy often leads to instabilities. To further address this issue, we develop a Hybrid Recurrent State-Space Model (HRSSM) structure, enhancing state representation robustness for effective policy learning. Our empirical evaluation demonstrates significant performance improvements over existing methods in a range of visually complex control tasks such as Maniskill with exogenous distractors from the Matterport environment. Our code is avaliable at https://github.com/bit1029public/HRSSM.