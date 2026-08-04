---
title: "Offline Imitation from Observation via Primal Wasserstein State Occupancy Matching"
source: "https://proceedings.mlr.press/v235/yan24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yan24e/yan24e.pdf"
categories: ['online-learning-and-sequential-decision-making', 'causal-inference-and-discovery-methods']
tags: ['offline-imitation-learning', 'observation-only', 'Wasserstein-distance']
venue: "ICML 2024"
tldr: "Proposes offline learning from observations via primal Wasserstein state occupancy matching without requiring expert action labels."
---

# Offline Imitation from Observation via Primal Wasserstein State Occupancy Matching

**Source**: [https://proceedings.mlr.press/v235/yan24e.html](https://proceedings.mlr.press/v235/yan24e.html)

**TLDR**: Proposes offline learning from observations via primal Wasserstein state occupancy matching without requiring expert action labels.

## Abstract

In real-world scenarios, arbitrary interactions with the environment can often be costly, and actions of expert demonstrations are not always available. To reduce the need for both, offline Learning from Observations (LfO) is extensively studied: the agent learns to solve a task given only expert states and task-agnostic non-expert state-action pairs. The state-of-the-art DIstribution Correction Estimation (DICE) methods, as exemplified by SMODICE, minimize the state occupancy divergence between the learner’s and empirical expert policies. However, such methods are limited to either $f$-divergences (KL and $\chi^2$) or Wasserstein distance with Rubinstein duality, the latter of which constrains the underlying distance metric crucial to the performance of Wasserstein-based solutions. To enable more flexible distance metrics, we propose Primal Wasserstein DICE (PW-DICE). It minimizes the primal Wasserstein distance between the learner and expert state occupancies and leverages a contrastively learned distance metric. Theoretically, our framework is a generalization of SMODICE, and is the first work that unifies $f$-divergence and Wasserstein minimization. Empirically, we find that PW-DICE improves upon several state-of-the-art methods. The code is available at https://github.com/KaiYan289/PW-DICE.