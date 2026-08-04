---
title: "Allocation Requires Prediction Only if Inequality Is Low"
source: "https://proceedings.mlr.press/v235/shirali24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shirali24a/shirali24a.pdf"
categories: ['fairness-aware-algorithmic-decision-making']
tags: ['algorithmic-fairness', 'resource-allocation', 'prediction-based-decisions']
venue: "ICML 2024"
tldr: "Proposes a framework showing that algorithmic predictions for resource allocation are only necessary when inequality among individuals is low."
---

# Allocation Requires Prediction Only if Inequality Is Low

**Source**: [https://proceedings.mlr.press/v235/shirali24a.html](https://proceedings.mlr.press/v235/shirali24a.html)

**TLDR**: Proposes a framework showing that algorithmic predictions for resource allocation are only necessary when inequality among individuals is low.

## Abstract

Algorithmic predictions are emerging as a promising solution concept for efficiently allocating societal resources. Fueling their use is an underlying assumption that such systems are necessary to identify individuals for interventions. We propose a principled framework for assessing this assumption: Using a simple mathematical model, we evaluate the efficacy of prediction-based allocations in settings where individuals belong to larger units such as hospitals, neighborhoods, or schools. We find that prediction-based allocations outperform baseline methods using aggregate unit-level statistics only when between-unit inequality is low and the intervention budget is high. Our results hold for a wide range of settings for the price of prediction, treatment effect heterogeneity, and unit-level statistics’ learnability. Combined, we highlight the potential limits to improving the efficacy of interventions through prediction.