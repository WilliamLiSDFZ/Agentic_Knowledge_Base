---
title: "BayOTIDE: Bayesian Online Multivariate Time Series Imputation with Functional Decomposition"
source: "https://proceedings.mlr.press/v235/fang24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fang24d/fang24d.pdf"
categories: ['time-series-modeling-and-forecasting-methods']
tags: ['time-series-imputation', 'bayesian-online-learning', 'functional-decomposition']
venue: "ICML 2024"
tldr: "Presents a Bayesian online framework for multivariate time series imputation via functional decomposition with uncertainty quantification."
---

# BayOTIDE: Bayesian Online Multivariate Time Series Imputation with Functional Decomposition

**Source**: [https://proceedings.mlr.press/v235/fang24d.html](https://proceedings.mlr.press/v235/fang24d.html)

**TLDR**: Presents a Bayesian online framework for multivariate time series imputation via functional decomposition with uncertainty quantification.

## Abstract

In real-world scenarios such as traffic and energy management, we frequently encounter large volumes of time-series data characterized by missing values, noise, and irregular sampling patterns. While numerous imputation methods have been proposed, the majority tend to operate within a local horizon, which involves dividing long sequences into batches of fixed-length segments for model training. This local horizon often leads to the overlooking of global trends and periodic patterns. More importantly, most methods assume the observations are sampled at regular timestamps, and fail to handle complex irregular sampled time series in various applications. Additionally, most existing methods are learned in an offline manner. Thus, it is not suitable for applications with rapidly arriving streaming data. To address these challenges, we propose BayOTIDE: Bayesian Online Multivariate Time series Imputation with functional decomposition. Our method conceptualizes multivariate time series as the weighted combination of groups of low-rank temporal factors with different patterns. We employ a suite of Gaussian Processes (GPs),each with a unique kernel, as functional priors to model these factors. For computational efficiency, we further convert the GPs into a state-space prior by constructing an equivalent stochastic differential equation (SDE), and developing a scalable algorithm for online inference. The proposed method can not only handle imputation over arbitrary timestamps, but also offer uncertainty quantification and interpretability for the downstream application. We evaluate our method on both synthetic and real-world datasets. We release the code at https://github.com/xuangu-fang/BayOTIDE.