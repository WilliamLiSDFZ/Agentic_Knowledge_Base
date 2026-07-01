---
title: "Proving Olympiad Algebraic Inequalities without Human Demonstrations"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/96f8c5e879c339dae55e6c2188b02a33-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['neural-networks-for-formal-reasoning-and-verification', 'llm-training-and-optimization-techniques']
tags: ['olympiad-inequalities', 'automated-theorem-proving', 'algebraic-reasoning', 'formal-verification', 'mathematical-AI']
venue: "NeurIPS 2024"
tldr: "Develops a machine learning approach to prove Olympiad-level algebraic inequalities without human demonstrations by generating synthetic proof data."
---

# Proving Olympiad Algebraic Inequalities without Human Demonstrations

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/96f8c5e879c339dae55e6c2188b02a33-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/96f8c5e879c339dae55e6c2188b02a33-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Develops a machine learning approach to prove Olympiad-level algebraic inequalities without human demonstrations by generating synthetic proof data.

## Abstract

Solving Olympiad-level mathematical problems represents a significant advancement in machine intelligence and automated reasoning. Current machine learning methods, however, struggle to solve Olympiad-level problems beyond Euclidean plane geometry due to a lack of large-scale, high-quality datasets. The challenge is even greater in algebraic systems, which involve infinite reasoning spaces within finite conditions. To address these issues, we propose AIPS, an Algebraic Inequality Proving System capable of autonomously generating complex inequality theorems and effectively solving Olympiad-level inequality problems without requiring human demonstrations. During proof search in a mixed reasoning manner, a value curriculum learning strategy on generated datasets is implemented to improve proving performance, demonstrating strong mathematical intuitions. On a test set of 20 International Mathematical Olympiad-level inequality problems, AIPS successfully solved 10, outperforming state-of-the-art methods. Furthermore, AIPS automatically generated a vast array of non-trivial theorems without human intervention, some of which have been evaluated by professional contestants and deemed to reach the level of the International Mathematical Olympiad. Notably, one theorem was selected as a competition problem in a major city's 2024 Mathematical Olympiad.All the materials are available at  sites.google.com/view/aips2