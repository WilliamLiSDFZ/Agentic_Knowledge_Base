---
title: "Reinforcement Learning within Tree Search for Fast Macro Placement"
source: "https://proceedings.mlr.press/v235/geng24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/geng24b/geng24b.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'simulation-scaling-limits-for-robot-manipulation']
tags: ['macro-placement', 'reinforcement-learning', 'tree-search']
venue: "ICML 2024"
tldr: "Combines reinforcement learning with tree search for sample-efficient macro placement in chip design."
---

# Reinforcement Learning within Tree Search for Fast Macro Placement

**Source**: [https://proceedings.mlr.press/v235/geng24b.html](https://proceedings.mlr.press/v235/geng24b.html)

**TLDR**: Combines reinforcement learning with tree search for sample-efficient macro placement in chip design.

## Abstract

Macro placement is a crucial step in modern chip design, and reinforcement learning (RL) has recently emerged as a promising technique for improving the placement quality. However, existing RL-based techniques are hindered by their low sample efficiency, requiring numerous online rollouts or substantial offline expert data to achieve bootstrap, which are often impractical in industrial scenarios. To address this challenge, we propose a novel sample-efficient framework, namely EfficientPlace, for fast macro placement. EfficientPlace integrates a global tree search algorithm to strategically direct the optimization process, as well as a RL agent for local policy learning to advance the tree search. Experiments on commonly used benchmarks demonstrate that EfficientPlace achieves remarkable placement quality within a short timeframe, outperforming recent state-of-the-art approaches.