---
title: "Deep Functional Factor Models: Forecasting High-Dimensional Functional Time Series via Bayesian Nonparametric Factorization"
source: "https://proceedings.mlr.press/v235/liu24aw.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24aw/liu24aw.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'generative-models-and-variational-inference']
tags: ['functional-time-series', 'bayesian-nonparametric', 'deep-kernel']
venue: "ICML 2024"
tldr: "A Bayesian nonparametric deep functional factor model for forecasting high-dimensional functional time series using Indian Buffet Process and deep kernels."
---

# Deep Functional Factor Models: Forecasting High-Dimensional Functional Time Series via Bayesian Nonparametric Factorization

**Source**: [https://proceedings.mlr.press/v235/liu24aw.html](https://proceedings.mlr.press/v235/liu24aw.html)

**TLDR**: A Bayesian nonparametric deep functional factor model for forecasting high-dimensional functional time series using Indian Buffet Process and deep kernels.

## Abstract

This paper introduces the Deep Functional Factor Model (DF2M), a Bayesian nonparametric model designed for analysis of high-dimensional functional time series. DF2M is built upon the Indian Buffet Process and the multi-task Gaussian Process, incorporating a deep kernel function that captures non-Markovian and nonlinear temporal dynamics. Unlike many black-box deep learning models, DF2M offers an explainable approach to utilizing neural networks by constructing a factor model and integrating deep neural networks within the kernel function. Additionally, we develop a computationally efficient variational inference algorithm to infer DF2M. Empirical results from four real-world datasets demonstrate that DF2M provides better explainability and superior predictive accuracy compared to conventional deep learning models for high-dimensional functional time series.