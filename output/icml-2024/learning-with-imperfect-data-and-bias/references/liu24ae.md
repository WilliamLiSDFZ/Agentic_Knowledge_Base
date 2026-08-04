---
title: "Time-Series Forecasting for Out-of-Distribution Generalization Using Invariant Learning"
source: "https://proceedings.mlr.press/v235/liu24ae.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24ae/liu24ae.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'learning-with-imperfect-data-and-bias']
tags: ['time-series-forecasting', 'out-of-distribution', 'invariant-learning']
venue: "ICML 2024"
tldr: "An invariant learning framework for time-series forecasting that improves out-of-distribution generalization across temporal distribution shifts."
---

# Time-Series Forecasting for Out-of-Distribution Generalization Using Invariant Learning

**Source**: [https://proceedings.mlr.press/v235/liu24ae.html](https://proceedings.mlr.press/v235/liu24ae.html)

**TLDR**: An invariant learning framework for time-series forecasting that improves out-of-distribution generalization across temporal distribution shifts.

## Abstract

Time-series forecasting (TSF) finds broad applications in real-world scenarios. Due to the dynamic nature of time-series data, it is crucial for TSF models to preserve out-of-distribution (OOD) generalization abilities, as training and test sets represent historical and future data respectively. In this paper, we aim to alleviate the inherent OOD problem in TSF via invariant learning. We identify fundamental challenges of invariant learning for TSF. First, the target variables in TSF may not be sufficiently determined by the input due to unobserved core variables in TSF, breaking the fundamental assumption of invariant learning. Second, time-series datasets lack adequate environment labels, while existing environmental inference methods are not suitable for TSF. To address these challenges, we propose FOIL, a model-agnostic framework that endows time-series forecasting for out-of-distribution generalization via invariant learning. Specifically, FOIL employs a novel surrogate loss to mitigate the impact of unobserved variables. Further, FOIL implements joint optimization by alternately inferring environments effectively with a multi-head network while preserving the temporal adjacency structure and learning invariant representations across inferred environments for OOD generalized TSF. Extensive experiments demonstrate that the proposed FOIL significantly and consistently improves the performance of various TSF models, achieving gains of up to 85%.