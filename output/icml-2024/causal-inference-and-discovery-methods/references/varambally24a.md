---
title: "Discovering Mixtures of Structural Causal Models from Time Series Data"
source: "https://proceedings.mlr.press/v235/varambally24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/varambally24a/varambally24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'time-series-modeling-and-forecasting-methods']
tags: ['causal-discovery', 'time-series', 'mixture-models', 'structural-causal-models', 'heterogeneous-data']
venue: "ICML 2024"
tldr: "Proposes a method to discover mixtures of structural causal models from heterogeneous time series data without assuming a single underlying causal structure."
---

# Discovering Mixtures of Structural Causal Models from Time Series Data

**Source**: [https://proceedings.mlr.press/v235/varambally24a.html](https://proceedings.mlr.press/v235/varambally24a.html)

**TLDR**: Proposes a method to discover mixtures of structural causal models from heterogeneous time series data without assuming a single underlying causal structure.

## Abstract

Discovering causal relationships from time series data is significant in fields such as finance, climate science, and neuroscience. However, contemporary techniques rely on the simplifying assumption that data originates from the same causal model, while in practice, data is heterogeneous and can stem from different causal models. In this work, we relax this assumption and perform causal discovery from time series data originating from a mixture of causal models. We propose a general variational inference-based framework called MCD to infer the underlying causal models as well as the mixing probability of each sample. Our approach employs an end-to-end training process that maximizes an evidence-lower bound for the data likelihood. We present two variants: MCD-Linear for linear relationships and independent noise, and MCD-Nonlinear for nonlinear causal relationships and history-dependent noise. We demonstrate that our method surpasses state-of-the-art benchmarks in causal discovery tasks through extensive experimentation on synthetic and real-world datasets, particularly when the data emanates from diverse underlying causal graphs. Theoretically, we prove the identifiability of such a model under some mild assumptions. Implementation is available at https://github.com/Rose-STL-Lab/MCD.