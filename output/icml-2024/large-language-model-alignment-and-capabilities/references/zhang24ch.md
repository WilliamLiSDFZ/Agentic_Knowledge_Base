---
title: "Confronting Reward Overoptimization for Diffusion Models: A Perspective of Inductive and Primacy Biases"
source: "https://proceedings.mlr.press/v235/zhang24ch.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ch/zhang24ch.pdf"
categories: ['generative-models-and-variational-inference', 'large-language-model-alignment-and-capabilities']
tags: ['diffusion-models', 'reward-overoptimization', 'alignment']
venue: "ICML 2024"
tldr: "Analyzes and addresses reward overoptimization in diffusion models through the lens of inductive and primacy biases."
---

# Confronting Reward Overoptimization for Diffusion Models: A Perspective of Inductive and Primacy Biases

**Source**: [https://proceedings.mlr.press/v235/zhang24ch.html](https://proceedings.mlr.press/v235/zhang24ch.html)

**TLDR**: Analyzes and addresses reward overoptimization in diffusion models through the lens of inductive and primacy biases.

## Abstract

Bridging the gap between diffusion models and human preferences is crucial for their integration into practical generative workflows. While optimizing downstream reward models has emerged as a promising alignment strategy, concerns arise regarding the risk of excessive optimization with learned reward models, which potentially compromises ground-truth performance. In this work, we confront the reward overoptimization problem in diffusion model alignment through the lenses of both inductive and primacy biases. We first identify a mismatch between current methods and the temporal inductive bias inherent in the multi-step denoising process of diffusion models, as a potential source of reward overoptimization. Then, we surprisingly discover that dormant neurons in our critic model act as a regularization against reward overoptimization while active neurons reflect primacy bias. Motivated by these observations, we propose Temporal Diffusion Policy Optimization with critic active neuron Reset (TDPO-R), a policy gradient algorithm that exploits the temporal inductive bias of diffusion models and mitigates the primacy bias stemming from active neurons. Empirical results demonstrate the superior efficacy of our methods in mitigating reward overoptimization. Code is avaliable at https://github.com/ZiyiZhang27/tdpo.