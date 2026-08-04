---
title: "Towards a Self-contained Data-driven Global Weather Forecasting Framework"
source: "https://proceedings.mlr.press/v235/xiao24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xiao24a/xiao24a.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['weather-forecasting', 'data-assimilation', '4DVar']
venue: "ICML 2024"
tldr: "A self-contained data-driven global weather forecasting framework that integrates data assimilation with deep learning to replace traditional pipelines."
---

# Towards a Self-contained Data-driven Global Weather Forecasting Framework

**Source**: [https://proceedings.mlr.press/v235/xiao24a.html](https://proceedings.mlr.press/v235/xiao24a.html)

**TLDR**: A self-contained data-driven global weather forecasting framework that integrates data assimilation with deep learning to replace traditional pipelines.

## Abstract

Data-driven weather forecasting models are advancing rapidly, yet they rely on initial states (i.e., analysis states) typically produced by traditional data assimilation algorithms. Four-dimensional variational assimilation (4DVar) is one of the most widely adopted data assimilation algorithms in numerical weather prediction centers; it is accurate but computationally expensive. In this paper, we aim to couple the AI forecasting model, FengWu, with 4DVar to build a self-contained data-driven global weather forecasting framework, FengWu-4DVar. To achieve this, we propose an AI-embedded 4DVar algorithm that includes three components: (1) a 4DVar objective function embedded with the FengWu forecasting model and its error representation to enhance efficiency and accuracy; (2) a spherical-harmonic-transform-based (SHT-based) approximation strategy for capturing the horizontal correlation of background error; and (3) an auto-differentiation (AD) scheme for determining the optimal analysis fields. Experimental results show that under the ERA5 simulated observational data with varying proportions and noise levels, FengWu-4DVar can generate accurate analysis fields; remarkably, it has achieved stable self-contained global weather forecasts for an entire year for the first time, demonstrating its potential for real-world applications. Additionally, our framework is approximately 100 times faster than the traditional 4DVar algorithm under similar experimental conditions, highlighting its significant computational efficiency.