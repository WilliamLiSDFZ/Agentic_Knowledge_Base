---
title: "SiT: Symmetry-invariant Transformers for Generalisation in Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/weissenbacher24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/weissenbacher24a/weissenbacher24a.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'online-learning-and-sequential-decision-making']
tags: ['symmetry-invariance', 'vision-transformer', 'reinforcement-learning-generalization']
venue: "ICML 2024"
tldr: "SiT is a symmetry-invariant vision transformer that improves generalization of RL policies across semantically similar but visually different environments."
---

# SiT: Symmetry-invariant Transformers for Generalisation in Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/weissenbacher24a.html](https://proceedings.mlr.press/v235/weissenbacher24a.html)

**TLDR**: SiT is a symmetry-invariant vision transformer that improves generalization of RL policies across semantically similar but visually different environments.

## Abstract

An open challenge in reinforcement learning (RL) is the effective deployment of a trained policy to new or slightly different situations as well as semantically-similar environments. We introduce Symmetry-Invariant Transformer (SiT), a scalable vision transformer (ViT) that leverages both local and global data patterns in a self-supervised manner to improve generalisation. Central to our approach is Graph Symmetric Attention, which refines the traditional self-attention mechanism to preserve graph symmetries, resulting in invariant and equivariant latent representations. We showcase SiT’s superior generalization over ViTs on MiniGrid and Procgen RL benchmarks, and its sample efficiency on Atari 100k and CIFAR10.