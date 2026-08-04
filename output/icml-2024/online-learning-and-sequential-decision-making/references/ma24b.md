---
title: "Rethinking Decision Transformer via Hierarchical Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/ma24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24b/ma24b.pdf"
categories: ['online-learning-and-sequential-decision-making', 'transformer-architecture-efficiency-and-scaling']
tags: ['decision-transformer', 'hierarchical-reinforcement-learning', 'trajectory-stitching', 'offline-RL']
venue: "ICML 2024"
tldr: "Rethinking Decision Transformer through hierarchical RL enables trajectory stitching to overcome the limitation of relying solely on dataset recall."
---

# Rethinking Decision Transformer via Hierarchical Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/ma24b.html](https://proceedings.mlr.press/v235/ma24b.html)

**TLDR**: Rethinking Decision Transformer through hierarchical RL enables trajectory stitching to overcome the limitation of relying solely on dataset recall.

## Abstract

Decision Transformer (DT) is an innovative algorithm leveraging recent advances of the transformer architecture in reinforcement learning (RL). However, a notable limitation of DT is its reliance on recalling trajectories from datasets, losing the capability to seamlessly stitch sub-optimal trajectories together. In this work we introduce a general sequence modeling framework for studying sequential decision making through the lens of Hierarchical RL. At the time of making decisions, a high-level policy first proposes an ideal prompt for the current state, a low-level policy subsequently generates an action conditioned on the given prompt. We show DT emerges as a special case of this framework with certain choices of high-level and low-level policies, and discuss the potential failure of these choices. Inspired by these observations, we study how to jointly optimize the high-level and low-level policies to enable the stitching ability, which further leads to the development of new offline RL algorithms. Our empirical results clearly show that the proposed algorithms significantly surpass DT on several control and navigation benchmarks. We hope our contributions can inspire the integration of transformer architectures within the field of RL.