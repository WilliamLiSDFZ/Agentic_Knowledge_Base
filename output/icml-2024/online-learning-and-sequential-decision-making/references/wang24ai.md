---
title: "Highway Value Iteration Networks"
source: "https://proceedings.mlr.press/v235/wang24ai.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24ai/wang24ai.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'online-learning-and-sequential-decision-making']
tags: ['value-iteration-networks', 'deep-planning', 'highway-connections', 'reinforcement-learning']
venue: "ICML 2024"
tldr: "Highway connections are embedded into Value Iteration Networks to enable stable training for long-term planning tasks."
---

# Highway Value Iteration Networks

**Source**: [https://proceedings.mlr.press/v235/wang24ai.html](https://proceedings.mlr.press/v235/wang24ai.html)

**TLDR**: Highway connections are embedded into Value Iteration Networks to enable stable training for long-term planning tasks.

## Abstract

Value iteration networks (VINs) enable end-to-end learning for planning tasks by employing a differentiable "planning module" that approximates the value iteration algorithm. However, long-term planning remains a challenge because training very deep VINs is difficult. To address this problem, we embed highway value iteration—a recent algorithm designed to facilitate long-term credit assignment—into the structure of VINs. This improvement augments the "planning module" of the VIN with three additional components: 1) an "aggregate gate," which constructs skip connections to improve information flow across many layers; 2) an "exploration module," crafted to increase the diversity of information and gradient flow in spatial dimensions; 3) a "filter gate" designed to ensure safe exploration. The resulting novel highway VIN can be trained effectively with hundreds of layers using standard backpropagation. In long-term planning tasks requiring hundreds of planning steps, deep highway VINs outperform both traditional VINs and several advanced, very deep NNs.