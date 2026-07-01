---
title: "The Fragility of Fairness: Causal Sensitivity Analysis for Fair Machine Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/f7be3ebca4980b59fe3f665011115395-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['fairness-aware-machine-learning-methods', 'causal-discovery-and-inference-methods']
tags: ['fairness-metrics', 'causal-sensitivity', 'measurement-bias']
venue: "NeurIPS 2024"
tldr: "Introduces causal sensitivity analysis to assess the fragility of fairness metrics under measurement biases and violated assumptions."
---

# The Fragility of Fairness: Causal Sensitivity Analysis for Fair Machine Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/f7be3ebca4980b59fe3f665011115395-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/f7be3ebca4980b59fe3f665011115395-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces causal sensitivity analysis to assess the fragility of fairness metrics under measurement biases and violated assumptions.

## Abstract

Fairness metrics are a core tool in the fair machine learning literature (FairML),used to determine that ML models are, in some sense, “fair.” Real-world data,however, are typically plagued by various measurement biases and other violatedassumptions, which can render fairness assessments meaningless. We adapt toolsfrom causal sensitivity analysis to the FairML context, providing a general frame-work which (1) accommodates effectively any combination of fairness metric andbias that can be posed in the “oblivious setting”; (2) allows researchers to inves-tigate combinations of biases, resulting in non-linear sensitivity; and (3) enablesflexible encoding of domain-specific constraints and assumptions. Employing thisframework, we analyze the sensitivity of the most common parity metrics under 3varieties of classifier across 14 canonical fairness datasets. Our analysis reveals thestriking fragility of fairness assessments to even minor dataset biases. We show thatcausal sensitivity analysis provides a powerful and necessary toolkit for gaugingthe informativeness of parity metric evaluations. Our repository is \href{https://github.com/Jakefawkes/fragile_fair}{available here}.