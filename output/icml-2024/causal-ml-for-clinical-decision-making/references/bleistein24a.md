---
title: "Dynamic Survival Analysis with Controlled Latent States"
source: "https://proceedings.mlr.press/v235/bleistein24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bleistein24a/bleistein24a.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'causal-ml-for-clinical-decision-making']
tags: ['survival-analysis', 'counting-processes', 'controlled-differential-equations', 'latent-states']
venue: "ICML 2024"
tldr: "This paper introduces a dynamic survival analysis model using controlled differential equations to learn individual-specific intensities from static and time-series data."
---

# Dynamic Survival Analysis with Controlled Latent States

**Source**: [https://proceedings.mlr.press/v235/bleistein24a.html](https://proceedings.mlr.press/v235/bleistein24a.html)

**TLDR**: This paper introduces a dynamic survival analysis model using controlled differential equations to learn individual-specific intensities from static and time-series data.

## Abstract

We consider the task of learning individual-specific intensities of counting processes from a set of static variables and irregularly sampled time series. We introduce a novel modelization approach in which the intensity is the solution to a controlled differential equation. We first design a neural estimator by building on neural controlled differential equations. In a second time, we show that our model can be linearized in the signature space under sufficient regularity conditions, yielding a signature-based estimator which we call CoxSig. We provide theoretical learning guarantees for both estimators, before showcasing the performance of our models on a vast array of simulated and real-world datasets from finance, predictive maintenance and food supply chain management.