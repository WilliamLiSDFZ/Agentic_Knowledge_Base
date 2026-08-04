---
title: "KernelSHAP-IQ: Weighted Least Square Optimization for Shapley Interactions"
source: "https://proceedings.mlr.press/v235/fumagalli24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fumagalli24a/fumagalli24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'algebraic-structures-in-machine-learning']
tags: ['shapley-values', 'higher-order-interactions', 'weighted-least-squares', 'interpretability']
venue: "ICML 2024"
tldr: "KernelSHAP-IQ extends KernelSHAP to efficiently estimate Shapley Interaction Indices via weighted least squares optimization."
---

# KernelSHAP-IQ: Weighted Least Square Optimization for Shapley Interactions

**Source**: [https://proceedings.mlr.press/v235/fumagalli24a.html](https://proceedings.mlr.press/v235/fumagalli24a.html)

**TLDR**: KernelSHAP-IQ extends KernelSHAP to efficiently estimate Shapley Interaction Indices via weighted least squares optimization.

## Abstract

The Shapley value (SV) is a prevalent approach of allocating credit to machine learning (ML) entities to understand black box ML models. Enriching such interpretations with higher-order interactions is inevitable for complex systems, where the Shapley Interaction Index (SII) is a direct axiomatic extension of the SV. While it is well-known that the SV yields an optimal approximation of any game via a weighted least square (WLS) objective, an extension of this result to SII has been a long-standing open problem, which even led to the proposal of an alternative index. In this work, we characterize higher-order SII as a solution to a WLS problem, which constructs an optimal approximation via SII and k-Shapley values (k-SII). We prove this representation for the SV and pairwise SII and give empirically validated conjectures for higher orders. As a result, we propose KernelSHAP-IQ, a direct extension of KernelSHAP for SII, and demonstrate state-of-the-art performance for feature interactions.