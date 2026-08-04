---
title: "Model Assessment and Selection under Temporal Distribution Shift"
source: "https://proceedings.mlr.press/v235/han24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/han24b/han24b.pdf"
categories: ['uncertainty-calibration-and-distribution-shift-adaptation', 'time-series-modeling-and-forecasting-methods']
tags: ['distribution-shift', 'model-selection', 'temporal-adaptation']
venue: "ICML 2024"
tldr: "An adaptive rolling window approach is proposed for model assessment and selection under temporal distribution shift by synthesizing current and historical datasets."
---

# Model Assessment and Selection under Temporal Distribution Shift

**Source**: [https://proceedings.mlr.press/v235/han24b.html](https://proceedings.mlr.press/v235/han24b.html)

**TLDR**: An adaptive rolling window approach is proposed for model assessment and selection under temporal distribution shift by synthesizing current and historical datasets.

## Abstract

We investigate model assessment and selection in a changing environment, by synthesizing datasets from both the current time period and historical epochs. To tackle unknown and potentially arbitrary temporal distribution shift, we develop an adaptive rolling window approach to estimate the generalization error of a given model. This strategy also facilitates the comparison between any two candidate models by estimating the difference of their generalization errors. We further integrate pairwise comparisons into a single-elimination tournament, achieving near-optimal model selection from a collection of candidates. Theoretical analyses and empirical experiments underscore the adaptivity of our proposed methods to the non-stationarity in data.