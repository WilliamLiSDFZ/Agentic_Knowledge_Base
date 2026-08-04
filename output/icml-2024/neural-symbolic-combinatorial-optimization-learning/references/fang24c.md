---
title: "INViT: A Generalizable Routing Problem Solver with Invariant Nested View Transformer"
source: "https://proceedings.mlr.press/v235/fang24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fang24c/fang24c.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning']
tags: ['routing-problems', 'deep-reinforcement-learning', 'invariant-transformers']
venue: "ICML 2024"
tldr: "Proposes an Invariant Nested View Transformer for generalizable deep RL-based routing problem solving across distributions and scales."
---

# INViT: A Generalizable Routing Problem Solver with Invariant Nested View Transformer

**Source**: [https://proceedings.mlr.press/v235/fang24c.html](https://proceedings.mlr.press/v235/fang24c.html)

**TLDR**: Proposes an Invariant Nested View Transformer for generalizable deep RL-based routing problem solving across distributions and scales.

## Abstract

Recently, deep reinforcement learning has shown promising results for learning fast heuristics to solve routing problems. Meanwhile, most of the solvers suffer from generalizing to an unseen distribution or distributions with different scales. To address this issue, we propose a novel architecture, called Invariant Nested View Transformer (INViT), which is designed to enforce a nested design together with invariant views inside the encoders to promote the generalizability of the learned solver. It applies a modified policy gradient algorithm enhanced with data augmentations. We demonstrate that the proposed INViT achieves a dominant generalization performance on both TSP and CVRP problems with various distributions and different problem scales. Our source code and datasets are available in supplementary materials.