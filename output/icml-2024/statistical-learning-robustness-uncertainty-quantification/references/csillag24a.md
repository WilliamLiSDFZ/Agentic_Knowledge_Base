---
title: "Generalization Bounds for Causal Regression: Insights, Guarantees and Sensitivity Analysis"
source: "https://proceedings.mlr.press/v235/csillag24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/csillag24a/csillag24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['causal-machine-learning', 'generalization-bounds', 'sensitivity-analysis']
venue: "ICML 2024"
tldr: "Proposes generalization bounds for causal regression algorithms, providing finite-sample guarantees and sensitivity analysis via a novel change-of-measure approach."
---

# Generalization Bounds for Causal Regression: Insights, Guarantees and Sensitivity Analysis

**Source**: [https://proceedings.mlr.press/v235/csillag24a.html](https://proceedings.mlr.press/v235/csillag24a.html)

**TLDR**: Proposes generalization bounds for causal regression algorithms, providing finite-sample guarantees and sensitivity analysis via a novel change-of-measure approach.

## Abstract

Many algorithms have been recently proposed for causal machine learning. Yet, there is little to no theory on their quality, especially considering finite samples. In this work, we propose a theory based on generalization bounds that provides such guarantees. By introducing a novel change-of-measure inequality, we are able to tightly bound the model loss in terms of the deviation of the treatment propensities over the population, which we show can be empirically limited. Our theory is fully rigorous and holds even in the face of hidden confounding and violations of positivity. We demonstrate our bounds on semi-synthetic and real data, showcasing their remarkable tightness and practical utility.