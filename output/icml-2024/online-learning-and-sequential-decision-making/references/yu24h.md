---
title: "Enabling Few-Shot Learning with PID Control: A Layer Adaptive Optimizer"
source: "https://proceedings.mlr.press/v235/yu24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yu24h/yu24h.pdf"
categories: ['optimization-algorithms-convergence-theory', 'online-learning-and-sequential-decision-making']
tags: ['meta-learning', 'MAML', 'PID-control', 'layer-adaptive-optimizer']
venue: "ICML 2024"
tldr: "A PID-control-inspired layer-adaptive optimizer to improve MAML-based few-shot learning convergence and stability."
---

# Enabling Few-Shot Learning with PID Control: A Layer Adaptive Optimizer

**Source**: [https://proceedings.mlr.press/v235/yu24h.html](https://proceedings.mlr.press/v235/yu24h.html)

**TLDR**: A PID-control-inspired layer-adaptive optimizer to improve MAML-based few-shot learning convergence and stability.

## Abstract

Model-Agnostic Meta-Learning (MAML) and its variants have shown remarkable performance in scenarios characterized by a scarcity of labeled data during the training phase of machine learning models. Despite these successes, MAMLbased approaches encounter significant challenges when there is a substantial discrepancy in the distribution of training and testing tasks, resulting in inefficient learning and limited generalization across domains. Inspired by classical proportional-integral-derivative (PID) control theory, this study introduces a Layer-Adaptive PID (LA-PID) Optimizer, a MAML-based optimizer that employs efficient parameter optimization methods to dynamically adjust task-specific PID control gains at each layer of the network, conducting a first-principles analysis of optimal convergence conditions. A series of experiments conducted on four standard benchmark datasets demonstrate the efficacy of the LA-PID optimizer, indicating that LA-PID achieves state-oftheart performance in few-shot classification and cross-domain tasks, accomplishing these objectives with fewer training steps. Code is available on https://github.com/yuguopin/LA-PID.