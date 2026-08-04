---
title: "Provably Efficient Long-Horizon Exploration in Monte Carlo Tree Search through State Occupancy Regularization"
source: "https://proceedings.mlr.press/v235/schramm24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/schramm24a/schramm24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'test-time-adaptation-methods-and-evaluation']
tags: ['Monte-Carlo-tree-search', 'exploration', 'state-occupancy', 'long-horizon', 'motion-planning']
venue: "ICML 2024"
tldr: "State occupancy regularization derived from entropy-regularized MDPs improves long-horizon exploration in Monte Carlo tree search."
---

# Provably Efficient Long-Horizon Exploration in Monte Carlo Tree Search through State Occupancy Regularization

**Source**: [https://proceedings.mlr.press/v235/schramm24a.html](https://proceedings.mlr.press/v235/schramm24a.html)

**TLDR**: State occupancy regularization derived from entropy-regularized MDPs improves long-horizon exploration in Monte Carlo tree search.

## Abstract

Monte Carlo tree search (MCTS) has been successful in a variety of domains, but faces challenges with long-horizon exploration when compared to sampling-based motion planning algorithms like Rapidly-Exploring Random Trees. To address these limitations of MCTS, we derive a tree search algorithm based on policy optimization with state-occupancy measure regularization, which we call Volume-MCTS. We show that count-based exploration and sampling-based motion planning can be derived as approximate solutions to this state-occupancy measure regularized objective. We test our method on several robot navigation problems, and find that Volume-MCTS outperforms AlphaZero and displays significantly better long-horizon exploration properties.