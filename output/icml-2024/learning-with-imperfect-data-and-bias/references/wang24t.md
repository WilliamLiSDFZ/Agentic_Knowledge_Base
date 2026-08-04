---
title: "Identification and Estimation for Nonignorable Missing Data: A Data Fusion Approach"
source: "https://proceedings.mlr.press/v235/wang24t.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24t/wang24t.pdf"
categories: ['causal-inference-and-discovery-methods', 'learning-with-imperfect-data-and-bias']
tags: ['missing-not-at-random', 'data-fusion', 'identification', 'nonignorable-missingness', 'semiparametric']
venue: "ICML 2024"
tldr: "A data fusion approach achieves identification and estimation of parameters under missing-not-at-random data without strong assumptions on the missingness model."
---

# Identification and Estimation for Nonignorable Missing Data: A Data Fusion Approach

**Source**: [https://proceedings.mlr.press/v235/wang24t.html](https://proceedings.mlr.press/v235/wang24t.html)

**TLDR**: A data fusion approach achieves identification and estimation of parameters under missing-not-at-random data without strong assumptions on the missingness model.

## Abstract

We consider the task of identifying and estimating a parameter of interest in settings where data is missing not at random (MNAR). In general, such parameters are not identified without strong assumptions on the missing data model. In this paper, we take an alternative approach and introduce a method inspired by data fusion, where information in the MNAR dataset is augmented by information in an auxiliary dataset subject to missingness at random (MAR). We show that even if the parameter of interest cannot be identified given either dataset alone, it can be identified given pooled data, under two complementary sets of assumptions. We derive inverse probability weighted (IPW) estimators for identified parameters under both sets of assumptions, and evaluate the performance of our estimation strategies via simulation studies, and a data application.