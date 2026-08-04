---
title: "Stationarity without mean reversion in improper Gaussian processes"
source: "https://proceedings.mlr.press/v235/ambrogioni24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ambrogioni24a/ambrogioni24a.pdf"
categories: ['bayesian-optimization-and-surrogate-methods', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['Gaussian-processes', 'stationarity', 'improper-priors']
venue: "ICML 2024"
tldr: "This paper introduces improper Gaussian processes that are stationary without mean reversion, addressing pathological behavior in long-range regression settings."
---

# Stationarity without mean reversion in improper Gaussian processes

**Source**: [https://proceedings.mlr.press/v235/ambrogioni24a.html](https://proceedings.mlr.press/v235/ambrogioni24a.html)

**TLDR**: This paper introduces improper Gaussian processes that are stationary without mean reversion, addressing pathological behavior in long-range regression settings.

## Abstract

The behavior of a GP regression depends on the choice of covariance function. Stationary covariance functions are preferred in machine learning applications. However, (non-periodic) stationary covariance functions are always mean reverting and can therefore exhibit pathological behavior when applied to data that does not relax to a fixed global mean value. In this paper we show that it is possible to use improper GP priors with infinite variance to define processes that are stationary but not mean reverting. To this aim, we use of non-positive kernels that can only be defined in this limit regime. The resulting posterior distributions can be computed analytically and it involves a simple correction of the usual formulas. The main contribution of the paper is the introduction of a large family of smooth non-reverting covariance functions that closely resemble the kernels commonly used in the GP literature (e.g. squared exponential and Matérn class). By analyzing both synthetic and real data, we demonstrate that these non-positive kernels solve some known pathologies of mean reverting GP regression while retaining most of the favorable properties of ordinary smooth stationary kernels.