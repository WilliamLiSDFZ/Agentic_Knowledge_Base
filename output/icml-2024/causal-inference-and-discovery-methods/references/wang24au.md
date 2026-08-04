---
title: "A Dual-module Framework for Counterfactual Estimation over Time"
source: "https://proceedings.mlr.press/v235/wang24au.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24au/wang24au.pdf"
categories: ['causal-ml-for-clinical-decision-making', 'causal-inference-and-discovery-methods']
tags: ['counterfactual-estimation', 'time-series', 'adversarial-training', 'treatment-effects']
venue: "ICML 2024"
tldr: "ACTIN is a dual-module adversarial framework for efficient counterfactual estimation of treatment effects over time."
---

# A Dual-module Framework for Counterfactual Estimation over Time

**Source**: [https://proceedings.mlr.press/v235/wang24au.html](https://proceedings.mlr.press/v235/wang24au.html)

**TLDR**: ACTIN is a dual-module adversarial framework for efficient counterfactual estimation of treatment effects over time.

## Abstract

Efficiently and effectively estimating counterfactuals over time is crucial for optimizing treatment strategies. We present the Adversarial Counterfactual Temporal Inference Network (ACTIN), a novel framework with dual modules to enhance counterfactual estimation. The balancing module employs a distribution-based adversarial method to learn balanced representations, extending beyond the limitations of current classification-based methods to mitigate confounding bias across various treatment types. The integrating module adopts a novel Temporal Integration Predicting (TIP) strategy, which has a wider receptive field of treatments and balanced representations from the beginning to the current time for a more profound level of analysis. TIP goes beyond the established Direct Predicting (DP) strategy, which only relies on current treatments and representations, by empowering the integrating module to effectively capture long-range dependencies and temporal treatment interactions. ACTIN exceeds the confines of specific base models, and when implemented with simple base models, consistently delivers state-of-the-art performance and efficiency across both synthetic and real-world datasets.