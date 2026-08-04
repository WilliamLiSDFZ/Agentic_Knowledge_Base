---
title: "Reservoir Computing for Short High-Dimensional Time Series: an Application to SARS-CoV-2 Hospitalization Forecast"
source: "https://proceedings.mlr.press/v235/ferte24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ferte24a/ferte24a.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['reservoir-computing', 'time-series-forecasting', 'covid-hospitalization']
venue: "ICML 2024"
tldr: "Reservoir computing is applied to forecast SARS-CoV-2 hospitalizations from high-dimensional short time series using public and EHR data."
---

# Reservoir Computing for Short High-Dimensional Time Series: an Application to SARS-CoV-2 Hospitalization Forecast

**Source**: [https://proceedings.mlr.press/v235/ferte24a.html](https://proceedings.mlr.press/v235/ferte24a.html)

**TLDR**: Reservoir computing is applied to forecast SARS-CoV-2 hospitalizations from high-dimensional short time series using public and EHR data.

## Abstract

In this work, we aimed at forecasting the number of SARS-CoV-2 hospitalized patients at 14 days to help anticipate the bed requirements of a large scale hospital using public data and electronic health records data. Previous attempts led to mitigated performance in this high-dimension setting; we introduce a novel approach to time series forecasting by providing an alternative to conventional methods to deal with high number of potential features of interest (409 predictors). We integrate Reservoir Computing (RC) with feature selection using a genetic algorithm (GA) to gather optimal non-linear combinations of inputs to improve prediction in sample-efficient context. We illustrate that the RC-GA combination exhibits excellent performance in forecasting SARS-CoV-2 hospitalizations. This approach outperformed the use of RC alone and other conventional methods: LSTM, Transformers, Elastic-Net, XGBoost. Notably, this work marks the pioneering use of RC (along with GA) in the realm of short and high-dimensional time series, positioning it as a competitive and innovative approach in comparison to standard methods.