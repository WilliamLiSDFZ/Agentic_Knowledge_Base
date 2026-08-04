---
title: "Causal Customer Churn Analysis with Low-rank Tensor Block Hazard Model"
source: "https://proceedings.mlr.press/v235/gao24q.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gao24q/gao24q.pdf"
categories: ['causal-inference-and-discovery-methods', 'time-series-modeling-and-forecasting-methods']
tags: ['customer-churn', 'causal-inference', 'tensor-completion', 'survival-analysis']
venue: "ICML 2024"
tldr: "A tensorized latent factor block hazard model enables causal analysis of intervention effects on customer churn using tensor completion methods."
---

# Causal Customer Churn Analysis with Low-rank Tensor Block Hazard Model

**Source**: [https://proceedings.mlr.press/v235/gao24q.html](https://proceedings.mlr.press/v235/gao24q.html)

**TLDR**: A tensorized latent factor block hazard model enables causal analysis of intervention effects on customer churn using tensor completion methods.

## Abstract

This study introduces an innovative method for analyzing the impact of various interventions on customer churn, using the potential outcomes framework. We present a new causal model, the tensorized latent factor block hazard model, which incorporates tensor completion methods for a principled causal analysis of customer churn. A crucial element of our approach is the formulation of a 1-bit tensor completion for the parameter tensor. This captures hidden customer characteristics and temporal elements from churn records, effectively addressing the binary nature of churn data and its time-monotonic trends. Our model also uniquely categorizes interventions by their similar impacts, enhancing the precision and practicality of implementing customer retention strategies. For computational efficiency, we apply a projected gradient descent algorithm combined with spectral clustering. We lay down the theoretical groundwork for our model, including its non-asymptotic properties. The efficacy and superiority of our model are further validated through comprehensive experiments on both simulated and real-world applications.