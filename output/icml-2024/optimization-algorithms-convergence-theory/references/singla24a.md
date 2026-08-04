---
title: "SAPG: Split and Aggregate Policy Gradients"
source: "https://proceedings.mlr.press/v235/singla24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/singla24a/singla24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['policy-gradients', 'GPU-simulation', 'sample-efficiency', 'on-policy-RL']
venue: "ICML 2024"
tldr: "SAPG proposes splitting and aggregating policy gradients to improve sample efficiency of on-policy reinforcement learning at scale with GPU-driven simulation."
---

# SAPG: Split and Aggregate Policy Gradients

**Source**: [https://proceedings.mlr.press/v235/singla24a.html](https://proceedings.mlr.press/v235/singla24a.html)

**TLDR**: SAPG proposes splitting and aggregating policy gradients to improve sample efficiency of on-policy reinforcement learning at scale with GPU-driven simulation.

## Abstract

Despite extreme sample inefficiency, on-policy reinforcement learning, aka policy gradients, has become a fundamental tool in decision-making problems. With the recent advances in GPU-driven simulation, the ability to collect large amounts of data for RL training has scaled exponentially. However, we show that current RL methods, e.g. PPO, fail to ingest the benefit of parallelized environments beyond a certain point and their performance saturates. To address this, we propose a new on-policy RL algorithm that can effectively leverage large-scale environments by splitting them into chunks and fusing them back together via importance sampling. Our algorithm, termed SAPG, shows significantly higher performance across a variety of challenging environments where vanilla PPO and other strong baselines fail to achieve high performance. Webpage at https://sapg-rl.github.io/.