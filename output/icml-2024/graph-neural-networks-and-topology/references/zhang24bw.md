---
title: "Irregular Multivariate Time Series Forecasting: A Transformable Patching Graph Neural Networks Approach"
source: "https://proceedings.mlr.press/v235/zhang24bw.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24bw/zhang24bw.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'graph-neural-networks-and-topology']
tags: ['irregular-time-series', 'graph-neural-networks', 'multivariate-forecasting', 'patching', 'transformer']
venue: "ICML 2024"
tldr: "Proposes Transformable Patching Graph Neural Networks to forecast irregular multivariate time series by capturing inter-variable correlations and temporal irregularities."
---

# Irregular Multivariate Time Series Forecasting: A Transformable Patching Graph Neural Networks Approach

**Source**: [https://proceedings.mlr.press/v235/zhang24bw.html](https://proceedings.mlr.press/v235/zhang24bw.html)

**TLDR**: Proposes Transformable Patching Graph Neural Networks to forecast irregular multivariate time series by capturing inter-variable correlations and temporal irregularities.

## Abstract

Forecasting of Irregular Multivariate Time Series (IMTS) is critical for numerous areas, such as healthcare, biomechanics, climate science, and astronomy. Despite existing research addressing irregularities in time series through ordinary differential equations, the challenge of modeling correlations between asynchronous IMTS remains underexplored. To bridge this gap, this study proposes Transformable Patching Graph Neural Networks (t-PatchGNN), which transforms each univariate irregular time series into a series of transformable patches encompassing a varying number of observations with uniform temporal resolution. It seamlessly facilitates local semantics capture and inter-time series correlation modeling while avoiding sequence length explosion in aligned IMTS. Building on the aligned patching outcomes, we then present time-adaptive graph neural networks to model dynamic intertime series correlation based on a series of learned time-varying adaptive graphs. We demonstrate the remarkable superiority of t-PatchGNN on a comprehensive IMTS forecasting benchmark we build, which contains four real-world scientific datasets covering healthcare, biomechanics and climate science, and seventeen competitive baselines adapted from relevant research fields.