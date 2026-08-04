---
title: "Training Greedy Policy for Proposal Batch Selection in Expensive Multi-Objective Combinatorial Optimization"
source: "https://proceedings.mlr.press/v235/lee24w.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24w/lee24w.pdf"
categories: ['bayesian-optimization-and-surrogate-methods', 'submodular-optimization-and-combinatorial-algorithms']
tags: ['active-learning', 'multi-objective-optimization', 'batch-selection', 'combinatorial']
venue: "ICML 2024"
tldr: "Trains a greedy policy for batch proposal selection in expensive multi-objective combinatorial optimization via active learning."
---

# Training Greedy Policy for Proposal Batch Selection in Expensive Multi-Objective Combinatorial Optimization

**Source**: [https://proceedings.mlr.press/v235/lee24w.html](https://proceedings.mlr.press/v235/lee24w.html)

**TLDR**: Trains a greedy policy for batch proposal selection in expensive multi-objective combinatorial optimization via active learning.

## Abstract

Active learning is increasingly adopted for expensive multi-objective combinatorial optimization problems, but it involves a challenging subset selection problem, optimizing the batch acquisition score that quantifies the goodness of a batch for evaluation. Due to the excessively large search space of the subset selection problem, prior methods optimize the batch acquisition on the latent space, which has discrepancies with the actual space, or optimize individual acquisition scores without considering the dependencies among candidates in a batch instead of directly optimizing the batch acquisition. To manage the vast search space, a simple and effective approach is the greedy method, which decomposes the problem into smaller subproblems, yet it has difficulty in parallelization since each subproblem depends on the outcome from the previous ones. To this end, we introduce a novel greedy-style subset selection algorithm that optimizes batch acquisition directly on the combinatorial space by sequential greedy sampling from the greedy policy, specifically trained to address all greedy subproblems concurrently. Notably, our experiments on the red fluorescent proteins design task show that our proposed method achieves the baseline performance in 1.69x fewer queries, demonstrating its efficiency.