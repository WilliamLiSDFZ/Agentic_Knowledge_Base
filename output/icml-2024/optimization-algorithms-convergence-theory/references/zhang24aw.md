---
title: "A Federated Stochastic Multi-level Compositional Minimax Algorithm for Deep AUC Maximization"
source: "https://proceedings.mlr.press/v235/zhang24aw.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24aw/zhang24aw.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'optimization-algorithms-convergence-theory']
tags: ['federated-learning', 'AUC-maximization', 'minimax-optimization', 'compositional-optimization', 'imbalanced-data']
venue: "ICML 2024"
tldr: "Proposes a federated stochastic multi-level compositional minimax algorithm for deep AUC maximization to address imbalanced data classification in federated settings."
---

# A Federated Stochastic Multi-level Compositional Minimax Algorithm for Deep AUC Maximization

**Source**: [https://proceedings.mlr.press/v235/zhang24aw.html](https://proceedings.mlr.press/v235/zhang24aw.html)

**TLDR**: Proposes a federated stochastic multi-level compositional minimax algorithm for deep AUC maximization to address imbalanced data classification in federated settings.

## Abstract

AUC maximization is an effective approach to address the imbalanced data classification problem in federated learning. In the past few years, a couple of federated AUC maximization approaches have been developed based on the minimax optimization. However, directly solving a minimax optimization problem to maximize the AUC score cannot achieve satisfactory performance. To address this issue, we propose to maximize AUC via optimizing a federated multi-level compositional minimax problem. Specifically, we develop a novel federated multi-level compositional minimax algorithm with rigorous theoretical guarantees to solve this new learning paradigm in both algorithmic design and theoretical analysis. To the best of our knowledge, this is the first work studying the multi-level minimax optimization problem. Additionally, extensive empirical evaluations confirm the efficacy of our proposed approach.