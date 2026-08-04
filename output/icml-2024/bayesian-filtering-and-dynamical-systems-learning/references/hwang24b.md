---
title: "Fine-Grained Causal Dynamics Learning with Quantization for Improving Robustness in Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/hwang24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hwang24b/hwang24b.pdf"
categories: ['causal-inference-and-discovery-methods', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['causal-dynamics', 'reinforcement-learning', 'robustness', 'quantization', 'causal-discovery']
venue: "ICML 2024"
tldr: "Proposes fine-grained causal dynamics learning with quantization to improve robustness in reinforcement learning agents."
---

# Fine-Grained Causal Dynamics Learning with Quantization for Improving Robustness in Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/hwang24b.html](https://proceedings.mlr.press/v235/hwang24b.html)

**TLDR**: Proposes fine-grained causal dynamics learning with quantization to improve robustness in reinforcement learning agents.

## Abstract

Causal dynamics learning has recently emerged as a promising approach to enhancing robustness in reinforcement learning (RL). Typically, the goal is to build a dynamics model that makes predictions based on the causal relationships among the entities. Despite the fact that causal connections often manifest only under certain contexts, existing approaches overlook such fine-grained relationships and lack a detailed understanding of the dynamics. In this work, we propose a novel dynamics model that infers fine-grained causal structures and employs them for prediction, leading to improved robustness in RL. The key idea is to jointly learn the dynamics model with a discrete latent variable that quantizes the state-action space into subgroups. This leads to recognizing meaningful context that displays sparse dependencies, where causal structures are learned for each subgroup throughout the training. Experimental results demonstrate the robustness of our method to unseen states and locally spurious correlations in downstream tasks where fine-grained causal reasoning is crucial. We further illustrate the effectiveness of our subgroup-based approach with quantization in discovering fine-grained causal relationships compared to prior methods.