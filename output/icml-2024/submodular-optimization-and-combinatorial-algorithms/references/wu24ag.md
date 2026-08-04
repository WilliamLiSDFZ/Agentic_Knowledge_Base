---
title: "HGCN2SP: Hierarchical Graph Convolutional Network for Two-Stage Stochastic Programming"
source: "https://proceedings.mlr.press/v235/wu24ag.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24ag/wu24ag.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'submodular-optimization-and-combinatorial-algorithms']
tags: ['stochastic-programming', 'hierarchical-GCN', 'scenario-selection', 'two-stage', 'combinatorial-optimization']
venue: "ICML 2024"
tldr: "Proposes HGCN2SP, a hierarchical graph convolutional network for scenario selection in two-stage stochastic programming to accelerate solutions with many scenarios."
---

# HGCN2SP: Hierarchical Graph Convolutional Network for Two-Stage Stochastic Programming

**Source**: [https://proceedings.mlr.press/v235/wu24ag.html](https://proceedings.mlr.press/v235/wu24ag.html)

**TLDR**: Proposes HGCN2SP, a hierarchical graph convolutional network for scenario selection in two-stage stochastic programming to accelerate solutions with many scenarios.

## Abstract

Two-stage Stochastic Programming (2SP) is a standard framework for modeling decision-making problems under uncertainty. While numerous methods exist, solving such problems with many scenarios remains challenging. Selecting representative scenarios is a practical method for accelerating solutions. However, current approaches typically rely on clustering or Monte Carlo sampling, failing to integrate scenario information deeply and overlooking the significant impact of the scenario order on solving time. To address these issues, we develop HGCN2SP, a novel model with a hierarchical graph designed for 2SP problems, encoding each scenario and modeling their relationships hierarchically. The model is trained in a reinforcement learning paradigm to utilize the feedback of the solver. The policy network is equipped with a hierarchical graph convolutional network for feature encoding and an attention-based decoder for scenario selection in proper order. Evaluation of two classic 2SP problems demonstrates that HGCN2SP provides high-quality decisions in a short computational time. Furthermore, HGCN2SP exhibits remarkable generalization capabilities in handling large-scale instances, even with a substantial number of variables or scenarios that were unseen during the training phase.