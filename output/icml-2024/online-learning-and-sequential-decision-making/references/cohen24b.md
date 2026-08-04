---
title: "Improving Token-Based World Models with Parallel Observation Prediction"
source: "https://proceedings.mlr.press/v235/cohen24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cohen24b/cohen24b.pdf"
categories: ['online-learning-and-sequential-decision-making', 'transformer-architecture-efficiency-and-scaling']
tags: ['world-models', 'reinforcement-learning', 'transformers']
venue: "ICML 2024"
tldr: "Improves token-based world models by introducing parallel observation prediction to enhance sample efficiency in model-based reinforcement learning."
---

# Improving Token-Based World Models with Parallel Observation Prediction

**Source**: [https://proceedings.mlr.press/v235/cohen24b.html](https://proceedings.mlr.press/v235/cohen24b.html)

**TLDR**: Improves token-based world models by introducing parallel observation prediction to enhance sample efficiency in model-based reinforcement learning.

## Abstract

Motivated by the success of Transformers when applied to sequences of discrete symbols, token-based world models (TBWMs) were recently proposed as sample-efficient methods. In TBWMs, the world model consumes agent experience as a language-like sequence of tokens, where each observation constitutes a sub-sequence. However, during imagination, the sequential token-by-token generation of next observations results in a severe bottleneck, leading to long training times, poor GPU utilization, and limited representations. To resolve this bottleneck, we devise a novel Parallel Observation Prediction (POP) mechanism. POP augments a Retentive Network (RetNet) with a novel forward mode tailored to our reinforcement learning setting. We incorporate POP in a novel TBWM agent named REM (Retentive Environment Model), showcasing a 15.4x faster imagination compared to prior TBWMs. REM attains superhuman performance on 12 out of 26 games of the Atari 100K benchmark, while training in less than 12 hours. Our code is available at https://github.com/leor-c/REM