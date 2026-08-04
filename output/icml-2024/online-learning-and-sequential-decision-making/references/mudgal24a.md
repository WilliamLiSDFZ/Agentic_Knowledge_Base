---
title: "Controlled Decoding from Language Models"
source: "https://proceedings.mlr.press/v235/mudgal24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mudgal24a/mudgal24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'online-learning-and-sequential-decision-making']
tags: ['controlled-decoding', 'RLHF', 'KL-regularization', 'language-model-alignment']
venue: "ICML 2024"
tldr: "Controlled decoding is proposed as a modular prefix-scorer approach to solve a tokenwise KL-regularized RL objective for aligning language model outputs."
---

# Controlled Decoding from Language Models

**Source**: [https://proceedings.mlr.press/v235/mudgal24a.html](https://proceedings.mlr.press/v235/mudgal24a.html)

**TLDR**: Controlled decoding is proposed as a modular prefix-scorer approach to solve a tokenwise KL-regularized RL objective for aligning language model outputs.

## Abstract

KL-regularized reinforcement learning (RL) is a popular alignment framework to control the language model responses towards high reward outcomes. We pose a tokenwise RL objective and propose a modular solver for it, called controlled decoding (CD). CD exerts control through a separate prefix scorer module, which is trained to learn a value function for the reward. The prefix scorer is used at inference time to control the generation from a frozen base model, provably sampling from a solution to the RL objective. We empirically demonstrate that CD is effective as a control mechanism on popular benchmarks. We also show that prefix scorers for multiple rewards may be combined at inference time, effectively solving a multi-objective RL problem with no additional training. We show that the benefits of applying CD transfer to an unseen base model with no further tuning as well. Finally, we show that CD can be applied in a blockwise decoding fashion at inference-time, essentially bridging the gap between the popular best-of-$K$ strategy and tokenwise control through reinforcement learning. This makes CD a promising approach for alignment of language models.