---
title: "Bridging Environments and Language with Rendering Functions and Vision-Language Models"
source: "https://proceedings.mlr.press/v235/cachet24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cachet24a/cachet24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'simulation-scaling-limits-for-robot-manipulation']
tags: ['vision-language-models', 'reinforcement-learning', 'language-conditioned-agents', 'reward-shaping']
venue: "ICML 2024"
tldr: "Bridges environments and language using rendering functions with VLMs to provide rewards for training language-conditioned RL agents."
---

# Bridging Environments and Language with Rendering Functions and Vision-Language Models

**Source**: [https://proceedings.mlr.press/v235/cachet24a.html](https://proceedings.mlr.press/v235/cachet24a.html)

**TLDR**: Bridges environments and language using rendering functions with VLMs to provide rewards for training language-conditioned RL agents.

## Abstract

Vision-language models (VLMs) have tremendous potential for grounding language, and thus enabling language-conditioned agents (LCAs) to perform diverse tasks specified with text. This has motivated the study of LCAs based on reinforcement learning (RL) with rewards given by rendering images of an environment and evaluating those images with VLMs. If single-task RL is employed, such approaches are limited by the cost and time required to train a policy for each new task. Multi-task RL (MTRL) is a natural alternative, but requires a carefully designed corpus of training tasks and does not always generalize reliably to new tasks. Therefore, this paper introduces a novel decomposition of the problem of building an LCA: first find an environment configuration that has a high VLM score for text describing a task; then use a (pretrained) goal-conditioned policy to reach that configuration. We also explore several enhancements to the speed and quality of VLM-based LCAs, notably, the use of distilled models, and the evaluation of configurations from multiple viewpoints to resolve the ambiguities inherent in a single 2D view. We demonstrate our approach on the Humanoid environment, showing that it results in LCAs that outperform MTRL baselines in zero-shot generalization, without requiring any textual task descriptions or other forms of environment-specific annotation during training.