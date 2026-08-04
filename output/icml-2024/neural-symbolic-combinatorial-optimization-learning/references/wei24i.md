---
title: "Extending Test-Time Augmentation with Metamorphic Relations for Combinatorial Problems"
source: "https://proceedings.mlr.press/v235/wei24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wei24i/wei24i.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning']
tags: ['combinatorial-optimization', 'test-time-augmentation', 'metamorphic-relations']
venue: "ICML 2024"
tldr: "MAgg uses metamorphic relations to augment ML models at inference time for improved performance on combinatorial optimization problems."
---

# Extending Test-Time Augmentation with Metamorphic Relations for Combinatorial Problems

**Source**: [https://proceedings.mlr.press/v235/wei24i.html](https://proceedings.mlr.press/v235/wei24i.html)

**TLDR**: MAgg uses metamorphic relations to augment ML models at inference time for improved performance on combinatorial optimization problems.

## Abstract

The application of machine learning methods to solve combinatorial problems has garnered considerable research interest. In this paper, we propose MAgg (Metamorphic Aggregation), a method to augment machine learning models for combinatorial problems at inference time using metamorphic relations. MAgg models metamorphic relations using directed graphs, which are then fed to a Graph Neural Network (GNN) model to improve the aggregation of predictions across transformed input instances. By incorporating metamorphic relations, MAgg essentially extends standard Test-Time Augmentation (TTA), eliminating the necessity of label-preserving transformations and expanding its applicability to a broader range of supervised learning tasks for combinatorial problems. We evaluate the proposed MAgg method on three mainstream machine learning tasks for combinatorial problems, namely Boolean Satisfiability Prediction (SAT), Decision Traveling Salesman Problem Satisfiability Prediction (Decision TSP), and Graph Edit Distance Estimation (GED). The evaluation result shows significant improvements over base models in all three tasks, corroborating the effectiveness and versatility of the proposed method.