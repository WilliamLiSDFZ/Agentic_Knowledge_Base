---
title: "An Analysis of Linear Time Series Forecasting Models"
source: "https://proceedings.mlr.press/v235/toner24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/toner24a/toner24a.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'neural-network-learning-dynamics-theory']
tags: ['linear-models', 'time-series-forecasting', 'normalization']
venue: "ICML 2024"
tldr: "An analysis of linear time series forecasting models reveals that feature normalization is a key driver of their strong generalization performance across benchmarks."
---

# An Analysis of Linear Time Series Forecasting Models

**Source**: [https://proceedings.mlr.press/v235/toner24a.html](https://proceedings.mlr.press/v235/toner24a.html)

**TLDR**: An analysis of linear time series forecasting models reveals that feature normalization is a key driver of their strong generalization performance across benchmarks.

## Abstract

Despite their simplicity, linear models perform well at time series forecasting, even when pitted against deeper and more expensive models. A number of variations to the linear model have been proposed, often including some form of feature normalisation that improves model generalisation. In this paper we analyse the sets of functions expressible using these linear model architectures. In so doing we show that several popular variants of linear models for time series forecasting are equivalent and functionally indistinguishable from standard, unconstrained linear regression. We characterise the model classes for each linear variant. We demonstrate that each model can be reinterpreted as unconstrained linear regression over a suitably augmented feature set, and therefore admit closed-form solutions when using a mean-squared loss function. We provide experimental evidence that the models under inspection learn nearly identical solutions, and finally demonstrate that the simpler closed form solutions are superior forecasters across 72% dataset-horizon settings.