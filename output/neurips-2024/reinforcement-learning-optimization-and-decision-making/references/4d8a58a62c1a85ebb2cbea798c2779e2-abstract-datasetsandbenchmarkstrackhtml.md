---
title: "XLand-MiniGrid: Scalable Meta-Reinforcement Learning Environments in JAX"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/4d8a58a62c1a85ebb2cbea798c2779e2-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'ai-benchmarking-and-evaluation-methodology']
tags: ['meta-reinforcement-learning', 'JAX', 'grid-world-environments']
venue: "NeurIPS 2024"
tldr: "XLand-MiniGrid is a scalable JAX-based suite of grid-world environments designed for meta-reinforcement learning research."
---

# XLand-MiniGrid: Scalable Meta-Reinforcement Learning Environments in JAX

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/4d8a58a62c1a85ebb2cbea798c2779e2-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/4d8a58a62c1a85ebb2cbea798c2779e2-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: XLand-MiniGrid is a scalable JAX-based suite of grid-world environments designed for meta-reinforcement learning research.

## Abstract

Inspired by the diversity and depth of XLand and the simplicity and minimalism of MiniGrid, we present XLand-MiniGrid, a suite of tools and grid-world environments for meta-reinforcement learning research. Written in JAX, XLand-MiniGrid is designed to be highly scalable and can potentially run on GPU or TPU accelerators, democratizing large-scale experimentation with limited resources. Along with the environments, XLand-MiniGrid provides pre-sampled benchmarks with millions of unique tasks of varying difficulty and easy-to-use baselines that allow users to quickly start training adaptive agents. In addition, we have conducted a preliminary analysis of scaling and generalization, showing that our baselines are capable of reaching millions of steps per second during training and validating that the proposed benchmarks are challenging. XLand-MiniGrid is open-source and available at \url{https://github.com/corl-team/xland-minigrid}.