---
title: "Agnostic Learning of Mixed Linear Regressions with EM and AM Algorithms"
source: "https://proceedings.mlr.press/v235/ghosh24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ghosh24b/ghosh24b.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'neural-symbolic-combinatorial-optimization-learning']
tags: ['mixed-linear-regression', 'EM-algorithm', 'agnostic-learning']
venue: "ICML 2024"
tldr: "Analyzes EM and AM algorithms for agnostic learning of mixed linear regressions without distributional label assumptions."
---

# Agnostic Learning of Mixed Linear Regressions with EM and AM Algorithms

**Source**: [https://proceedings.mlr.press/v235/ghosh24b.html](https://proceedings.mlr.press/v235/ghosh24b.html)

**TLDR**: Analyzes EM and AM algorithms for agnostic learning of mixed linear regressions without distributional label assumptions.

## Abstract

Mixed linear regression is a well-studied problem in parametric statistics and machine learning. Given a set of samples, tuples of covariates and labels, the task of mixed linear regression is to find a small list of linear relationships that best fit the samples. Usually it is assumed that the label is generated stochastically by randomly selecting one of two or more linear functions, applying this chosen function to the covariates, and potentially introducing noise to the result. In that situation, the objective is to estimate the ground-truth linear functions up to some parameter error. The popular expectation maximization (EM) and alternating minimization (AM) algorithms have been previously analyzed for this. In this paper, we consider the more general problem of agnostic learning of mixed linear regression from samples, without such generative models. In particular, we show that the AM and EM algorithms, under standard conditions of separability and good initialization, lead to agnostic learning in mixed linear regression by converging to the population loss minimizers, for suitably defined loss functions. In some sense, this shows the strength of AM and EM algorithms that converges to “optimal solutions” even in the absence of realizable generative models.