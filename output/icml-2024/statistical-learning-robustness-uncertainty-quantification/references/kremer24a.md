---
title: "Geometry-Aware Instrumental Variable Regression"
source: "https://proceedings.mlr.press/v235/kremer24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kremer24a/kremer24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['instrumental-variables', 'conditional-moment-restrictions', 'generalized-method-of-moments']
venue: "ICML 2024"
tldr: "A geometry-aware approach to instrumental variable regression via conditional moment restrictions and reweightings of empirical data distributions."
---

# Geometry-Aware Instrumental Variable Regression

**Source**: [https://proceedings.mlr.press/v235/kremer24a.html](https://proceedings.mlr.press/v235/kremer24a.html)

**TLDR**: A geometry-aware approach to instrumental variable regression via conditional moment restrictions and reweightings of empirical data distributions.

## Abstract

Instrumental variable (IV) regression can be approached through its formulation in terms of conditional moment restrictions (CMR). Building on variants of the generalized method of moments, most CMR estimators are implicitly based on approximating the population data distribution via reweightings of the empirical sample. While for large sample sizes, in the independent identically distributed (IID) setting, reweightings can provide sufficient flexibility, they might fail to capture the relevant information in presence of corrupted data or data prone to adversarial attacks. To address these shortcomings, we propose the Sinkhorn Method of Moments, an optimal transport-based IV estimator that takes into account the geometry of the data manifold through data-derivative information. We provide a simple plug-and-play implementation of our method that performs on par with related estimators in standard settings but improves robustness against data corruption and adversarial attacks.