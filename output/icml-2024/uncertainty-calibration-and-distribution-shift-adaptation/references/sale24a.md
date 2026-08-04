---
title: "Second-Order Uncertainty Quantification: A Distance-Based Approach"
source: "https://proceedings.mlr.press/v235/sale24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sale24a/sale24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['second-order-uncertainty', 'distributional-predictions', 'uncertainty-quantification', 'distance-based', 'classification']
venue: "ICML 2024"
tldr: "A distance-based approach to second-order uncertainty quantification is proposed for classification, providing principled representations of epistemic and aleatoric uncertainty."
---

# Second-Order Uncertainty Quantification: A Distance-Based Approach

**Source**: [https://proceedings.mlr.press/v235/sale24a.html](https://proceedings.mlr.press/v235/sale24a.html)

**TLDR**: A distance-based approach to second-order uncertainty quantification is proposed for classification, providing principled representations of epistemic and aleatoric uncertainty.

## Abstract

In the past couple of years, various approaches to representing and quantifying different types of predictive uncertainty in machine learning, notably in the setting of classification, have been proposed on the basis of second-order probability distributions, i.e., predictions in the form of distributions on probability distributions. A completely conclusive solution has not yet been found, however, as shown by recent criticisms of commonly used uncertainty measures associated with second-order distributions, identifying undesirable theoretical properties of these measures. In light of these criticisms, we propose a set of formal criteria that meaningful uncertainty measures for predictive uncertainty based on second-order distributions should obey. Moreover, we provide a general framework for developing uncertainty measures to account for these criteria, and offer an instantiation based on the Wasserstein distance, for which we prove that all criteria are satisfied.