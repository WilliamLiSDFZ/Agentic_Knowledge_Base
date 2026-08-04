---
title: "Learning Decision Policies with Instrumental Variables through Double Machine Learning"
source: "https://proceedings.mlr.press/v235/shao24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shao24d/shao24d.pdf"
categories: ['causal-inference-and-discovery-methods', 'causal-ml-for-clinical-decision-making']
tags: ['instrumental-variables', 'double-machine-learning', 'causal-policy-learning']
venue: "ICML 2024"
tldr: "A framework is proposed for learning decision-making policies from observational data with hidden confounders using instrumental variable regression combined with double machine learning."
---

# Learning Decision Policies with Instrumental Variables through Double Machine Learning

**Source**: [https://proceedings.mlr.press/v235/shao24d.html](https://proceedings.mlr.press/v235/shao24d.html)

**TLDR**: A framework is proposed for learning decision-making policies from observational data with hidden confounders using instrumental variable regression combined with double machine learning.

## Abstract

A common issue in learning decision-making policies in data-rich settings is spurious correlations in the offline dataset, which can be caused by hidden confounders. Instrumental variable (IV) regression, which utilises a key uncounfounded variable called the instrument, is a standard technique for learning causal relationships between confounded action, outcome and context variables. Most recent IV regression algorithms use a two-stage approach, where a deep neural network (DNN) estimator learnt in the first stage is directly plugged into the second stage, in which another DNN is used to estimate the causal effect. Naively plugging the estimator can cause heavy bias in the second stage, especially when regularisation bias is present in the first stage estimator. We propose DML-IV, a non-linear IV regression method that reduces the bias in two-stage IV regressions and effectively learns high-performing policies. We derive a novel learning objective to reduce bias and design the DML-IV algorithm following the double/debiased machine learning (DML) framework. The learnt DML-IV estimator has strong convergence rate and $O(N^{-1/2})$ suboptimality guarantees that match those when the dataset is unconfounded. DML-IV outperforms state-of-the-art IV regression methods on IV regression benchmarks and learns high-performing policies in the presence of instruments.