---
title: "Do Transformer World Models Give Better Policy Gradients?"
source: "https://proceedings.mlr.press/v235/ma24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24i/ma24i.pdf"
categories: ['online-learning-and-sequential-decision-making', 'transformer-architecture-efficiency-and-scaling']
tags: ['world-models', 'transformer', 'policy-gradients', 'model-based-RL']
venue: "ICML 2024"
tldr: "This paper investigates whether transformer-based world models provide better policy gradients than standard world models for reinforcement learning."
---

# Do Transformer World Models Give Better Policy Gradients?

**Source**: [https://proceedings.mlr.press/v235/ma24i.html](https://proceedings.mlr.press/v235/ma24i.html)

**TLDR**: This paper investigates whether transformer-based world models provide better policy gradients than standard world models for reinforcement learning.

## Abstract

A natural approach for reinforcement learning is to predict future rewards by unrolling a neural network world model, and to backpropagate through the resulting computational graph to learn a control policy. However, this method often becomes impractical for long horizons, since typical world models induce hard-to-optimize loss landscapes. Transformers are known to efficiently propagate gradients over long horizons: could they be the solution to this problem? Surprisingly, we show that commonly-used transformer world models produce circuitous gradient paths, which can be detrimental to long-range policy gradients. To tackle this challenge, we propose a class of world models called Action-conditioned World Models (AWMs), designed to provide more direct routes for gradient propagation. We integrate such AWMs into a policy gradient framework that underscores the relationship between network architectures and the policy gradient updates they inherently represent. We demonstrate that AWMs can generate optimization landscapes that are easier to navigate even when compared to those from the simulator itself. This property allows transformer AWMs to produce better policies than competitive baselines in realistic long-horizon tasks.