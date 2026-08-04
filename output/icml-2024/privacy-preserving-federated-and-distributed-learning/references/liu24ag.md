---
title: "Multi-Source Conformal Inference Under Distribution Shift"
source: "https://proceedings.mlr.press/v235/liu24ag.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24ag/liu24ag.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'privacy-preserving-federated-and-distributed-learning']
tags: ['conformal-inference', 'distribution-shift', 'multi-source-data']
venue: "ICML 2024"
tldr: "A multi-source conformal inference framework that provides valid uncertainty quantification under distribution shifts across data sources without sharing individual-level data."
---

# Multi-Source Conformal Inference Under Distribution Shift

**Source**: [https://proceedings.mlr.press/v235/liu24ag.html](https://proceedings.mlr.press/v235/liu24ag.html)

**TLDR**: A multi-source conformal inference framework that provides valid uncertainty quantification under distribution shifts across data sources without sharing individual-level data.

## Abstract

Recent years have experienced increasing utilization of complex machine learning models across multiple sources of data to inform more generalizable decision-making. However, distribution shifts across data sources and privacy concerns related to sharing individual-level data, coupled with a lack of uncertainty quantification from machine learning predictions, make it challenging to achieve valid inferences in multi-source environments. In this paper, we consider the problem of obtaining distribution-free prediction intervals for a target population, leveraging multiple potentially biased data sources. We derive the efficient influence functions for the quantiles of unobserved outcomes in the target and source populations, and show that one can incorporate machine learning prediction algorithms in the estimation of nuisance functions while still achieving parametric rates of convergence to nominal coverage probabilities. Moreover, when conditional outcome invariance is violated, we propose a data-adaptive strategy to upweight informative data sources for efficiency gain and downweight non-informative data sources for bias reduction. We highlight the robustness and efficiency of our proposals for a variety of conformal scores and data-generating mechanisms via extensive synthetic experiments. Hospital length of stay prediction intervals for pediatric patients undergoing a high-risk cardiac surgical procedure between 2016-2022 in the U.S. illustrate the utility of our methodology.